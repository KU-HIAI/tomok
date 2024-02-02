import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04011001 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.10.1' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플랜지에 수직으로 용접된 판에 작용된 인장력에 의해 국부휨을 받는 플랜지의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.1 플랜지 국부휨강도
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
  	A([플랜지 국부휨강도])
  	B["KDS 14 31 25 4.1.10.1"]
  	A ~~~ B
  	end

	  subgraph Variable_def
    VarOut[/출력변수: 플랜지의 설계강도/]
  	VarIn1[/입력변수: 공칭지압강도/]
  	VarIn2[/입력변수: 저항계수/]
  	VarIn3[/입력변수: 플랜지의 항복강도/]
  	VarIn4[/입력변수: 하중을 받는 플랜지의 두께/]
  	VarIn5[/입력변수: 하중구간의 길이/]
  	VarIn6[/입력변수: 플랜지 부재의 폭/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
  	end

  	Python_Class ~~~ Variable_def --> C --> D --Pass--> E
  	D --Fail--> F --> G --> H --Pass--> I
  	H --Fail --> J

  	C["하중구간의 길이 <<img src='https://latex.codecogs.com/svg.image?&space;0.15b_f'>"]
  	D["Pass or Fail"]
  	E["검토 x"]
  	F["<img src='https://latex.codecogs.com/svg.image?R_n=6.25t_f^2F_{yf}'>------------------------------"]
  	G["부재단부로부터 집중하중에 저항하는 거리 <<img src='https://latex.codecogs.com/svg.image?10t_f'>"]
  	H["Pass or Fail"]
	  I(["<img src='https://latex.codecogs.com/svg.image?R_n'> x 0.5"])
	  J(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength_of_flanges_subjected_to_local_bending_by_tensile_force_applied_to_plates_welded_perpendicular_to_the_flanges(fOphiRn,fIRn,fIPhi,fIFyf,fItf,fIlelose,fIbf) -> bool:
        """플랜지에 수직으로 용접된 판에 작용된 인장력에 의해 국부휨을 받는 플랜지의 설계강도
        Args:
            fOphiRn (float): 플랜지의 설계강도
            fIRn (float): 공칭지압강도
            fIPhi (float): 저항계수
            fIFyf (float): 플랜지의 항복강도
            fItf (float): 하중을 받는 플랜지의 두께
            fIlelose (float): 하중구간의 길이
            fIbf (float): 플랜지 부재의 폭

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.1 플랜지에 수직으로 용접된 판에 작용된 인장력에 의해 국부휨을 받는 플랜지의 설계강도의 값
        """

        fIRn = (6.25)*(fItf*fItf)*fIFyf
        if fIlelose < (0.15)*fIbf :
          fOphiRn = fIPhi * fIRn
        if fIlelose < (10)*fItf :
          fOphiRn = fIPhi * fIRn * 0.5

        return fOphiRn


# 

