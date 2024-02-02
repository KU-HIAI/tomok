import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010304_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.4 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-10-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트의 설계전단응력'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.4 지압접합에서 인장과 전단의 조합
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
	  A([지압접합에서 인장과 전단의 조합])
	  B["KDS 14 31 25 4.1.3.4(2)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarIn1[/입력변수: 저항계수/]
    VarIn2[/입력변수: 공칭인장강도/]
  	end

	  Python_Class ~~~ Variable_def --> D --> E


	  D["볼트의 설계전단응력 ≥ fv"]
	  E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fIdeshst,fIfv) -> bool:
        """볼트의 설계전단응력

        Args:
            fIdeshst (float): 설계전단응력
            fIfv (float): 전단소요응력

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (2)의 통과 여부
        """

        if fIdeshst >= fIfv :
          return "Pass"
        else :
          return "Fail"


# 

