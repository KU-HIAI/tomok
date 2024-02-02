import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060305_06(RuleUnit): # KDS241711_04060305_06

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.3.5 (6)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '수평간격과 보강띠철근 간의 수평간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.5 심부구속 횡방향철근상세
    (6)
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
	A([심부구속 횡방향철근상세])
	B["KDS 24 17 11 4.6.3.5(6)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarIn[/입력변수: 수평간격과 보강띠철근 간의 수평간격/]
	end

	Python_Class ~~~ Variable_def --> D --> E
	D["후프띠철근과 보강띠철근의 수평간격, 보강띠철근간의수평간격 ≤ 350mm"]
	E(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def horizontal_spacing(fIhosphore,fIhosprere) -> bool:
        """수평간격과 보강띠철근 간의 수평간격

        Args:
            fIhosphore (float): 후프띠철근과 보강띠철간의 수평간격
            fIhosprere (float): 보강띠철근 간의 수평간격

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.3.5 심부구속 횡방향철근상세 (6)의 통과 여부
        """

        if fIhosphore <= 350 and fIhosprere <= 350:
          return "Pass"
        else:
          return "Fail"