import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS112025_030302_25(RuleUnit):

   # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 11 20 25 3.3.2 (25)' # 건설기준문서
    ref_date = '2020-12-03'  # 고시일
    doc_date = '2024-02-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '되메우기 및 뒤채움'    # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    되메우기 및 뒤채움
    3. 시공
    3.3 시공기준
    3.3.2 되메우기, 흙쌓기 및 땅고르기
    (25)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.2 되메우기, 흙쌓기 및 땅고르기
    (25) 자갈 다지기
    ① 자갈의 크기는 45 mm 이내의 자갈 또는 부순 돌로 한다.

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 자갈 다지기];
    B["KCS 11 20 25 3.3.2 (25)"];
    B ~~~ A
    end

    KCS(["KCS 11 20 25 3.3.2 (25)"])

    subgraph Variable_def
    VarIn1[/입력변수: 자갈의 크기/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{자갈의 크기 <= 45 mm}

		C --> D([PASS or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def gravel_size(fIGraSiz) -> RuleUnitResult:
        """자갈 다지기의 자갈 크기

        Args:
            fIGraSiz (float): 자갈의 크기

        Returns:
            pass_fail (bool): 되메우기 및 뒤채움 3.3.2 되메우기, 흙쌓기 및 땅고르기 (25)의 판단 결과
        """
        assert isinstance(fIGraSiz, float)

        if fIGraSiz < 45:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False
                }
            )