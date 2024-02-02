import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010307 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.7' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-10-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장과 전단 조합 시 마찰접합의 감소계수'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.7 마찰접합에서 인장과 전단의 조합
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
	  A([마찰접합에서 인장과 전단의 조합])
	  B["KDS 14 31 25 4.1.3.7"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut1[/출력변수: 인장과 전단조합시 마찰접합의 감소계수/]
    VarOut2[/출력변수: 소요인장력/]
    VarIn1[/입력변수: 설계볼트장력/]
    VarIn2[/입력변수: 인장력을 받는 볼트의 수/]
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
  	end

	  Python_Class ~~~ Variable_def --> D --> E

	  D["<img src='https://latex.codecogs.com/svg.image?K_s=1-\frac{T_u}{T_oN_b}'>-------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?K_s'>----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fOKs,fITu,fITo,fINb) -> bool:
        """인장과 전단 조합 시 마찰접합의 감소계수

        Args:
            fOKs (float): 인장과 전단 조합 시 마찰접합의 감소계수
            fITu (float): 소요인장력
            fITo (float): 설계볼트장력
            fINb (float): 인장력을 받는 볼트의 수

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.7 인장과 전단 조합 시 마찰접합의 감소계수의 값
        """
        fOKs = 1-fITu/(fITo*fINb)
        return fOKs


# 

