import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04060301_04(RuleUnit): # KDS241712_04060301_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.6.3.1 (4)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-10'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '압력지반운동 시간이력 수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.3 응답(시간)이력해석법
    4.6.3.1 해석방법
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
    A[해석방법];
    B["KDS 24 17 12 4.6.3.1 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 입력지반운동 시간이력 수/];




	 VarIn1

		end
		Python_Class ~~~ Variable_def--->E




		E["4세트≤입력지반운동 시간이력 수"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def interpretation_method(fInumpgm) -> bool:
        """압력지반운동 시간이력 수

        Args:
            fInumpgm (float): 압력지반운동 시간이력 수

        Returns:
            bool: 교량내진 설계기준(케이블교량) 4.6.3.1 (4) 의 통과여부
        """
        if fInumpgm >= 4:
          return("Pass")
        else:
          return("Fail")


