import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경사 전단철근이 배치된 부재의 설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (3)
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
    A["경사 전단철근이 배치된 부재의 설계전단강도"];
    B["KDS 24 14 21 4.1.2.3 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 경사 전단철근이 배치된 부재의 설계전단강도/];
		VarIn1[/입력변수: 축력이 작용하지 않는 경우의 최대설계전단강도/];
		VarIn2[/입력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
		VarIn3[/입력변수: 철근의 재료저항계수/];
		VarIn4[/입력변수: 전단철근의 항복강도/];
		VarIn5[/입력변수: 전단 철근량/];
		VarIn6[/입력변수: 단면 내부 팔길이/];
		VarIn7[/입력변수: 전단철근 간격/];
		VarIn8[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
		VarIn9[/입력변수: 경사전단철근과 주인장철근 사이의 경사각/];
		VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn11[/입력변수: 콘크리트의 재료저항계수/];
		VarIn12[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn13[/입력변수: 단면의 복부폭/];
		VarIn14[/입력변수: 철근의 기준항복강도/];
		VarIn15[/입력변수: 최대 허용 전단철근량/];

		VarOut1 ~~~ VarIn1 & VarIn2
    VarIn2 ~~~ VarIn3 & VarIn4 & VarIn5
    VarIn4 ~~~ VarIn6 & VarIn7 & VarIn8
		VarIn7~~~ VarIn9 & VarIn10 & VarIn11
		VarIn10~~~VarIn11 & VarIn12 & VarIn13
		VarIn12~~~VarIn14 & VarIn15





		end
		Python_Class ~~~ Variable_def;
		Variable_def--축력이 작용하지 않을때 -->C--->D--->E
		Variable_def--축방향 압축력--->F
		Variable_def--최대 허용전단철근량---> G
		E & F & G--->K
		C["<img src='https://latex.codecogs.com/svg.image?V_{sd}=\frac{\phi&space;_sf_{vy}A_vz}{s}(cot\theta&plus;cot\alpha)sin\alpha&space;'>---------------------------------"]
		D["<img src='https://quicklatex.com/cache3/f8/ql_01fc4d56ac44d78014cb3d5ef63cd4f8_l3.png'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?V_{sd}\leq&space;V_{d,max}'>------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?V_{sd}\leq&space;V_{d,max,com}'>---------------------------------"]
		G["<img src='https://quicklatex.com/cache3/35/ql_8100bf766d4a61d696d37394f37bfe35_l3.png'>---------------------------------"]


		K(["경사 전단철근이 배치된 부재의 설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength_of_members_with_inclined_shear_bars(fOVsd,fIVdmax,fIVdmaxcom,fIphis,fIfvy,fIAv,fIz,fIs,fItheta,fIalpha,fInu,fIphic,fIfck,fIbw,fIfy,fIAvmax,fIuserdefined) -> bool:
        """경사 전단철근이 배치된 부재의 설계전단강도

        Args:
             fOVsd (float): 경사 전단철근이 배치된 부재의 설계전단강도
             fIVdmax (float): 축력이 작용하지 않는 경우의 최대설계전단강도
             fIVdmaxcom (float): 축방향 압축력이 작용하는 경우의 최대설계전단강도
             fIphis (float): 철근의 재료저항계수
             fIfvy (float): 전단철근의 항복강도
             fIAv (float): 전단 철근량
             fIz (float): 단면 내부 팔길이
             fIs (float): 전단철근 간격
             fItheta (float): 부재 복부에 형성된 스트럿의 경사각
             fIalpha (float): 경사전단철근과 주인장철근 사이의 경사각
             fInu (float): 콘크리트 압축강도 유효계수
             fIphic (float): 콘크리트의 재료저항계수
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도
             fIbw (float): 단면의 복부폭
             fIfy (float): 철근의 기준항복강도
             fIAvmax (float): 최대 허용 전단철근량
             fIuserdefined (float): 사용자 선택



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (3)의 통과 여부
        """

        import math
        fOVsd = fIphis * fIfvy * fIAv * fIz / fIs * ( 1/math.tan(math.radians(fItheta)) + 1/math.tan(math.radians(fIalpha)) ) * math.sin(math.radians(fIalpha))
        fIVdmax = fInu * fIphic * fIfck * fIbw * fIz * ( 1/math.tan(math.radians(fItheta)) + 1/math.tan(math.radians(fIalpha))) / (1+(1/math.tan(math.radians(fItheta)))**2)

        #축력이 작용하지 않는 경우: fIuserdefined = 1
        #프리스트레스를 포함하 축방향 압축력이 작용하는 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          if fOVsd <= fIVdmax and fIphis * fIfy * fIAvmax / ( fIbw * fIs) <= 0.5 * fInu * fIphic * fIfck * math.sin(math.radians(fIalpha)) / ( 1- math.cos(math.radians(fIalpha))) :
            return fOVsd, "Pass"
          else:
            return fOVsd, "Fail"
        elif fIuserdefined == 2:
          if fOVsd <= fIVdmaxcom and fIphis * fIfy * fIAvmax / ( fIbw * fIs) <= 0.5 * fInu * fIphic * fIfck * math.sin(math.radians(fIalpha)) / ( 1- math.cos(math.radians(fIalpha))):
            return fOVsd, "Pass"
          else:
            return fOVsd, "Fail"


# 

