import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115040_020514_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 40 2.5.14 (1)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-18'
    title = '횡방향 재하시험 재하장치'

    description = """
    말뚝재하시험
    2. 시험
    2.5 횡방향재하시험
    2.5.14 가력장치
    (1)
    """
    content = """
    #### 2.5.14 가력장치
    (1) 재하장치는 계획최대시험하중의 120% 이상의 가력능력을 가져야 하며, 예상되는 시험말뚝 등의 변형에 충분히 따를 수 있는 것으로 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 재하시험 재하장치];
    B["KCS 11 50 40 2.5.14 (1)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 40 2.5.14 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 가력능력/];
    VarIn2[/입력변수: 계획최대시험하중/];
    VarIn3[/입력변수: 예상되는 시험말뚝 등의 변형 수용/];
    VarIn1 & VarIn2  ~~~ VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"가력능력 ≥ 계획최대시험하중*1.2 \n & 예상되는 시험말뚝 등의 변형 수용"}
    C --> End([Pass or Fail])
    """

    @rule_method
    def loading_device(fILoaCap,fIDesLoa,bIDefPil)-> RuleUnitResult:
        """
        Args:
            fILoaCap (float): 가력능력
            fIDesLoa (float): 계획최대시험하중
            bIDefPil (bool): 예상되는 시험말뚝 등의 변형 수용

        Returns:
            pass_fail (bool): 말뚝재하시험 2.5.14 가력장치 (1)의 판단 결과
        """
        assert isinstance(fILoaCap, float)
        assert isinstance(fIDesLoa, float)
        assert isinstance(bIDefPil, bool)

        if fILoaCap >= fIDesLoa*1.2:
            if bIDefPil == True:
                pass_fail = True
            else:
                pass_fail = False
        else:
            pass_fail = False
        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })