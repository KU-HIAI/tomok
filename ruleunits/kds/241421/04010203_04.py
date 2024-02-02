import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수직 스터럽 또는 경사 스터럽이 배치된 부재의 설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (4)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["계산한 최대 설계전단강도"];
    B["KDS 24 14 21 4.1.2.3 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
		VarIn1[/입력변수: 수직 스터럽 또는 경사 스터럽이 배치된 부재의설계전단강도/];
		VarIn2[/입력변수: 축력이 작용하지 않을 경우의 최대설계전단강도/];
		VarIn3[/입력변수: 계수하중에 의해 단면에 유발된 평균압축응력/];
		VarIn4[/입력변수: 콘크리트의 재료저항계수/];
		VarIn5[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn6[/입력변수: αcw/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6


		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->F
		Variable_def--->D--->G
		Variable_def--->E--->H
		F & G & H--->I--->J--->K
		C{"<img src='https://latex.codecogs.com/svg.image?&space;0<f_{n}\leq&space;0.25\phi&space;_cf_{ck};'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?0.25\phi&space;_cf_{ck}<f_n\leq&space;0.5\phi&space;_{c}f_{ck}'>---------------------------------"}
		E{"<img src='https://latex.codecogs.com/svg.image?0.5\phi&space;_{c}f_{ck}<f_{n}\leq&space;1.0\phi&space;_cf_{ck}'>------------------------------"}
		F["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=(1&plus;f_n/\phi&space;_cf_{ck})'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=1.25'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?\alpha_{cw}=2.5(1-f_n/\phi&space;_cf_{ck})'>---------------------------------"]
		I["<img src='https://latex.codecogs.com/svg.image?V_{d,max,com}=\alpha&space;_{cw}V_{d,max}'>---------------------------------"]
		J["<img src='https://latex.codecogs.com/svg.image?V_{sd}\leq&space;V_{d,max,com}'>---------------------------------"]
		K(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength_of_members_with_vertical_stirrups_or_inclined_stirrups(fIVsd,fOVdmaxcom,fIalphacw,fIVdmax,fIfn,fIphic,fIfck) -> bool:
        """수직 스터럽 또는 경사 스터럽이 배치된 부재의 설계전단강도

        Args:
             fIVsd (float): 수직 스터럽 또는 경사 스터럽이 배치된 부재의 설계전단강도
             fOVdmaxcom (float): 축방향 압축력이 작용할 경우의 최대설계전단강도
             fIalphacw (float): 축방향 압축력에 의한 강도계수
             fIVdmax (float): 축력이 작용하지 않을 경우의 최대설계전단강도
             fIfn (float):  계수하중에 의해 단면에 유발된 평균압축응력
             fIphic (float): 콘크리트의 재료저항계수
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (4)의 통과 여부
        """

        if 0 < fIfn <= 0.25 * fIphic * fIfck:
          fIalphacw = 1 + fIfn / ( fIphic * fIfck )
        elif 0.25 * fIphic * fIfck < fIfn <= 0.5 * fIphic * fIfck:
          fIalphacw = 1.25
        elif 0.5 * fIphic * fIfck < fIfn <= 1.0 * fIphic * fIfck:
          fIalphacw = 2.5 * ( 1- fIfn/( fIphic * fIfck ) )

        fOVdmaxcom = fIalphacw * fIVdmax
        if fIVsd <= fOVdmaxcom:
          return fOVdmaxcom, "Pass"
        else:
          return fOVdmaxcom, "Fail"


# 

