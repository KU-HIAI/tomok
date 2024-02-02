import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010401_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.4.1' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '접합부재의 인장파단에 대하여 설계인장강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.1 설계인장강도
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
	  A([설계인장강도])
	  B["KDS 14 31 25 4.1.4.1(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계인장강도/]
	  VarIn1[/입력변수: 저항계수/]
	  VarIn2[/입력변수: 피접합체의 공칭인장강도/]
	  VarIn3[/입력변수: 유효단면적/]
  	VarOut ~~~ VarIn2 & VarIn3
  	end

  	Python_Class ~~~ Variable_def --> D --> E
  	D["<img src='https://latex.codecogs.com/svg.image?R_n=F_uA_e'>-------------------------------"]
  	E(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>--------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_tensile_strength_for_tensile_failure_of_the_joint(fOphiRn,fIphi,fIFu,fIAe) -> bool:
        """접합부재의 인장파단에 대하여 설계인장강도

        Args:
            fOphiRn (float): 설계인장강도
            fIphi (float): 저항계수
            fIFu (float): 피접합재의 공칭인장강도
            fIAe (float): 유효단면적

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.1 접합부재의 인장파단에 대한 설계인장강도 (2)의 값
        """
        fOphiRn = fIphi*fIFu*fIAe
        return fOphiRn


# 

