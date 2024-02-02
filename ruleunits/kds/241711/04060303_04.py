import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060303_04(RuleUnit): # KDS241711_04060303_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.3 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '겹침이음'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.3 축방향철근과 횡방향철근
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
	A([축방향철근과 횡방향철근])
	B["KDS 24 17 11 4.6.3.3 (4)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarIn1[/입력변수: 겹침이음/]
	VarIn2[/입력변수: 겹침이음 사이의 거리/]
	end

	Python_Class ~~~ Variable_def--> D --> E & F --> G

	D["소성힌지구역 이외의 구역"]
	E["전체 축방향철근x1/2 > 겹침이음"]
	F["겹침이음 사이의 거리 ≥  600mm"]
  G([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def lap_joint(fIlapjoi,fIdilajo,fItozxre) -> bool:
        """겹침이음

        Args:
            fIlapjoi (float): 겹침이음.
            fIdilajo (float): 겹침이음 사이의 거리.
            fItoaxre (float): 전체 축방향철근.

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.3 축방향철근과 횡방향철근 (4)의 통과 여부
        """

        if fIlapjoi <= 0.5 * fItozxre and fIdilajo >= 600:
          return "Pass"
        else:
          return "Fail"