import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_030203_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.2.3 (4)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '손상된 에폭시 도막에 덧댄 보수재의 면적'

    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.2.3 손상된 에폭시 도막 보수
    (4)
    """
    content = """
    #### 3.2.3 손상된 에폭시 도막 보수
    (4) 손상된 에폭시 도막에 덧댄 보수재의 면적은 300mm 길이 당 5%를 넘지 않아야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 손상된 에폭시 도막에 덧댄 보수재의 면적];
    B["KCS 14 20 11 3.2.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (4)"])

    subgraph Variable_def
    VarIn2[/입력변수: 300mm 길이 당 보수재 면적의 비율/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"300mm 길이 당 보수재 면적의 비율 < 5%"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def repair_material_epoxy(fIRatRep)-> RuleUnitResult:
        """
        Args:
            fIRatRep (float): 300mm 길이 당 보수재 면적의 비율

        Returns:
            pass_fail (bool): 철근공사 3.2.3 손상된 에폭시 도막 보수 (4)의 판단 결과

        """
        assert isinstance(fIRatRep, float)
        assert 0< fIRatRep < 100

        if fIRatRep <= 5:
            pass_fail = True
        else:
            pass_fail = False
        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })