import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060201_02(RuleUnit): # KDS241711_04060201_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.2.1 (2)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '설계기준항복강도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.1 일반사항
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
	  A([철근 콘크리트 교각의 철근])
	  B["KDS 24 17 11 4.6.2.1(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 설계기준항복강도/]
	  VarIn2[/입력변수: 인장강도/]
	  VarIn3[/입력변수: 항복강도/]
	  VarIn1 & VarIn2
	  end
	  Python_Class ~~~ Variable_def --> D & E
	  D --> G --> H --> I
	  E --> F --> I
	  D{"축방향 철근"}
	  E{"횡방향 철근"}
	  F["설계기준항복강도 ≤ 500Mpa"]
	  G["설계기준항복강도 ≤ 500Mpa"]
  	H["인장강도 ≥ 항복강도 x 1.25"]
	  I([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def pier_rebar_strengh_consideration(fIspyist,fItenstr,fIyiestr,fluserdefined) -> bool:
        """설계기준항복강도

        Args:
            fIspyist (float): 설계기준항복강도
            fItenstr (float): 인장강도
            fIyiestr (float): 항복강도
            fluserdefined (float): 사용자 선택

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.4.2.1 일반사항 (2)의 통과 여부
        """
        if fluserdefined == 1: #축방향 철근
          if fIspyist <= 500 and fItenstr >= 1.25:
           return "Pass"
          else:
           return "Fail"
        elif fluserdefined == 2: #횡방향 철근
          if fIspyist <= 500:
           return "Pass"
          else:
           return "Fail"