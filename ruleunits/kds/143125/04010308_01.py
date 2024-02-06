import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010308_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.8' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '휨모멘트를 받는 핀의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.8 핀접합
    (1)
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
	  A([핀의 설계강도])
	  B["KDS 14 31 25 4.1.3.8(1)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 설계강도/]
    VarIn1[/입력변수: 저항계수/]
    VarIn2[/입력변수: 핀의 항복강도/]
    VarIn3[/입력변수: 핀의 소성단면계수/]
    VarOut & VarIn1 ~~~ VarIn2 & VarIn3
  	end

	  Python_Class ~~~ Variable_def --> D --> E

	  D["<img src='https://latex.codecogs.com/svg.image?M_n=1.00F_yZ'>-------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_n'>-------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength_of_pins_subjected_to_bending_moments(fOphiMn,fIphi,fIFy,fIZ) -> bool:
        """휨모멘트를 받는 핀의 설계강도

        Args:
            fOphiMn (float): 설계강도
            fIphi (float): 저항계수
            fIFy (float): 핀의 항복강도
            fIZ (float): 핀의 소성단면계수

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.8 휨모멘트를 받는 핀의 설계강도 (1)의 값
        """
        fOphiMn = fIphi * 1.00 * fIFy * fIZ
        return fOphiMn


# 
