import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_030203_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.2.3 (3)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '에폭시 도막철근의 보수'

    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.2.3 손상된 에폭시 도막 보수
    (3)
    """
    content = """
    #### 3.2.3 손상된 에폭시 도막 보수
    (3) 300mm 길이 당 보수해야 할 표면적이 2%를 초과하는 에폭시 도막철근은 사용할 수 없다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 에폭시 도막철근의 보수];
    B["KCS 14 20 11 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (3)"])

    subgraph Variable_def
    VarIn2[/입력변수: 300mm 길이 당 보수해야 할 표면적 비율/];
    VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"300mm 길이 당 보수해야 할 표면적 비율 <= 2%"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def maintenance_epoxy(fIRatSur)-> RuleUnitResult:
        """
        Args:
            fIRatSur (float): 300mm 길이 당 보수해야 할 표면적 비율

        Returns:
            pass_fail (bool): 철근공사 3.2.3 손상된 에폭시 도막 보수 (3)의 판단 결과

        """
        assert isinstance(fIRatSur, float)
        assert 0< fIRatSur < 100

        if fIRatSur > 2:
            pass_fail = False
        elif fIRatSur <= 2:
            pass_fail = True
        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })