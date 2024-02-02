import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-09'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수직 스터럽이 배치된 부재의 설계전단강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (2)
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
    A[전단보강철근이 배치된 부재];
    B["KDS 24 14 21 4.1.2.3 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수: 수직 스트럽이 배치된 부재의 설계전단강도/];
      VarIn1[/입력변수: 축력이 작용하지 않는 경우의 최대설계전단강도/];
      VarIn2[/입력변수: 축방향 압축력이 작용하는 경우의 최대설계전단강도/];
      VarIn3[/입력변수: 복부 철근의 항복을 기준으로 한 설계전단강도/];
      VarIn4[/입력변수: 철근의 재료저항계수/];
      VarIn5[/입력변수: 전단철근의 항복강도/];
      VarIn6[/입력변수: 전단 철근량/];
      VarIn7[/입력변수: 단면 내부 팔길이/];
			VarIn8[/입력변수: 전단철근 간격/];
			VarIn9[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
			VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];
			VarIn11[/입력변수: 콘크리트의 재료저항계수/];
			VarIn12[/입력변수: 단면의 복부폭/];
			VarIn13[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
			VarIn14[/입력변수: 철근의 기준항복강도/];
			VarIn15[/입력변수: 최대 허용 전단철근량/];

			VarOut1~~~
			VarIn1 & VarIn2  & VarIn3 & VarIn4 & VarIn5 ~~~
      VarIn6 & VarIn7 & VarIn8  & VarIn9 & VarIn10 ~~~
			VarIn11 & VarIn12 & VarIn13 & VarIn14 & VarIn15

			end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://quicklatex.com/cache3/97/ql_73e3665047dffc9b774216b46a1be897_l3.png'>---------------------------------"]
			D{프리스트레스 포함하여 축방향 압축력이 작용}
			E["<img src='https://latex.codecogs.com/svg.image?V_{sd} \leq V_{d,max,com}'>---------------------------------"]
			F["<img src='https://latex.codecogs.com/svg.image?V_{sd}=\frac{\phi&space;_{s}f_{vy}A_{v}z}{s}(cot\theta)'>---------------------------------"]
			G{축력작용}
			I["<img src='https://quicklatex.com/cache3/5c/ql_b1652b4c6b21a5518810995d66b3ec5c_l3.png'>---------------------------------"]
			J([Pass or Fail])
			M([Pass or Fail])
			N([Pass or Fail])



			Variable_def ---> C ---> J
			Variable_def ---> D ---> E ---> M
			Variable_def ---> G --No ---> I ---> N
			G -- yes ---> F ---> N
			E~~~ |"KDS 24 14 21 4.1.2.3 (4)"| E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_shear_strength_off_members_with_vertical_stirrups(fOVd,fIVsd,fIVdmax,fIVdmaxcom,fIphis,fIphic,fIfvy,fIAv,fIz,fIs,fItheta,fInu,fIfy,fIfck,fIbw,fIAvmax,fIuserdefined) -> bool:
        """수직 스터럽이 배치된 부재의 설계전단강도

        Args:
             fOVd (float): 수직 스터럽이 배치된 부재의 설계전단강도
             fIVsd (float): 복부 철근의 항복을 기준으로 한 설계전단강도
             fIVdmax (float): 축력이 작용하지 않는 경우의 최대설계전단강도
             fIVdmaxcom (float): 축방향 압축력이 작용하는 경우의 최대설계전단강도
             fIphis (float): 철근의 재료저항계수
             fIphic (float): 콘크리트의 재료저항계수
             fIfvy (float): 전단철근의 항복강도
             fIAv (float): 전단 철근량
             fIz (float): 단면 내부 팔길이
             fIs (float): 전단철근 간격
             fItheta (float): 부재 복부에 형성된 스트럿의 경사각
             fInu (float): 콘크리트 압축강도 유효계수
             fIfy (float): 철근의 기준항복강도
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도
             fIbw (float): 단면의 복부폭
             fIAvmax (float): 최대 허용 전단철근량
             fIuserdefined (float): 사용자 선택



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (2)의 통과 여부
        """

        import math
        fIVsd = fIphis * fIfvy * fIAv * fIz / ( fIs * math.tan(math.radians(fItheta)))
        fOVd = fIVsd
        fIVdmax = fInu * fIphic * fIfck * fIbw * fIz / ( 1/math.tan(math.radians(fItheta)) + math.tan(math.radians(fItheta)))

        #축력이 작용하지 않는 경우: fIuserdefined = 1
        #프리스트레스를 포함하 축방향 압축력이 작용하는 경우: fIuserdefined = 2

        if fIphis * fIfy * fIAvmax / ( fIbw * fIs) <= 0.5 * fInu * fIphic * fIfck:
          if fIuserdefined == 1:
            if fOVd <= fIVdmax :
              return fOVd, "Pass"
            else:
              return fOVd, "Fail"
          elif fIuserdefined == 2:
            if fOVd <= fIVdmaxcom :
              return fOVd, "Pass"
            else:
              return fOVd, "Fail"
          return "Pass"
        else:
          return "Fail"


# 

