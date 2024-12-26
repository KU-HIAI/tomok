import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115015_030105_06(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 11 50 15 3.1.5 (6)' # 건설기준문서
    ref_date = '2021-05-12'  # 고시일
    doc_date = '2024-02-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기성말뚝'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    기성말뚝
    3. 시공
    3.1 일반사항
    3.1.5 시험시공말뚝
    (6)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.5 시험시공말뚝
    (6) 시험시공말뚝은 설계서에 명시된 말뚝규격으로 선정하고 말뚝길이는 소요길이보다 2m 이상 긴 말뚝으로 시공하여야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 시험시공말뚝 시공 조건"];
    B["KCS 11 50 15 3.1.5 (6)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 15 3.1.5 (6)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 말뚝길이"/];
		VarIn2[/"입력변수: 소요길이"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> F{말뚝길이 => 소요길이 + 2 m }
		F --> G([PASS or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def construction_conditions_for_test_piles(fIPilLen, fIReqLen) -> RuleUnitResult:
        """시험시공말뚝 시공 조건

        Args:
            fIPilLen (float): 말뚝길이
            fIReqLen (float): 소요길이

        Returns:
            pass_fail (bool): 기성말뚝 3.1.5 시험시공말뚝 (6)의 판단 결과
        """
        assert isinstance(fIPilLen, float)
        assert isinstance(fIReqLen, float)

        if fIPilLen >= fIReqLen + 2:
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