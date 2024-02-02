import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04030104 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.4' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '판재의 항복강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.4 강관폭의 중심에 종방향으로 분포된 종방향 집중하중
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
	  A[강관폭의 중심에 종방향으로 분포된 종방향 집중하중]
	  B["KDS 14 31 25 4.3.1.4"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 판재의 항복강도/]
	  VarIn2[/입력변수: 판재의 두께/]
	  VarIn3[/입력변수: 강재의 최소인장강도/]
	  VarIn4[/입력변수: 주강관의 두께/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  end
	  Python_Class ~~~ Variable_def --> C --> D(["PASS or Fail"])
	  C["<img src='https://latex.codecogs.com/svg.image?F_{yp}t_p\leq&space;F_yt'>--------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def yield_strength_of_plate(fIFyp, fItp, fIFu, fIt) -> bool:
        """판재의 항복강도

        Args:
            fIFyp (float): 판재의 항복강도
            fItp (float): 판재의 두께
            fIFu (float): 강재의 최소인장강도
            fIt (float): 주강관의 두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.4 강관폭의 중심에 종방향으로 분포된 종방향 집중하중의 통과여부
        """

        if fIFyp * fItp <= fIFu * fIt:
          return "Pass"
        else:
          return "Fail"


# 

