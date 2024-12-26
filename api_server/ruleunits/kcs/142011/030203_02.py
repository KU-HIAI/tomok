import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_030203_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.2.3 (2)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '손상된 에폭시 도막'

    description = """
    철근공사
    3. 시공
    3.2 에폭시 도막철근
    3.1.3 철근의 이음
    3.2.3 손상된 에폭시 도막 보수
    (2)
    """
    content = """
    #### 3.2.3 손상된 에폭시 도막 보수
    (2) 에폭시 도막이 손상된 경우, 300mm 길이 당 보수해야 할 표면적이 2%를 넘지 않아야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 손상된 에폭시 도막];
    B["KCS 14 20 11 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.2.3 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 에폭시 도막의 손상/];
    VarIn2[/입력변수: 300mm 길이 당 보수해야 할 표면적 비율/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"에폭시 도막의 손상 & \n 300mm 길이 당 보수해야 할 표면적 비율 < 2%"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def damaged_epoxy_paint(bIDamEpo,fIRatSur)-> RuleUnitResult:
        """
        Args:
            bIDamEpo (bool): 에폭시 도막의 손상
            fIRatSur (float): 300mm 길이 당 보수해야 할 표면적 비율

        Returns:
            pass_fail (bool): 철근공사 3.2.3 손상된 에폭시 도막 보수 (2)의 판단 결과

        """
        assert isinstance(bIDamEpo, bool)
        assert isinstance(fIRatSur, float)
        assert 0< fIRatSur < 100

        if bIDamEpo:
            if fIRatSur <= 2:
                pass_fail = True
            else:
                pass_fail = False
        else:
            pass_fail = True
        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })