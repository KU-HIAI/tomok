import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_020201_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 2.2.1 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '일반구조용 압연강재 강판의 두께'

    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.1 강판
    (1)
    """
    content = """
    #### 2.2.1 강판
    (1) 일반구조용 압연강재: KS D 3503
    \begin{table}[]
    \begin{tabular}{llll}
    규격        & 종류    & 기호 & 두께 t(㎜)     \\
    KS D 3503 & SS400 & -  & 8 ≤ t ≤ 100
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반구조용 압연강재 강판의 두께];
    B["KCS 24 30 00 2.2.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.1 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 강판의 두께/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"일반구조용 압연강재"}
    C --> |True|D{"8 ≤ 강판의 두께 ≤ 100"}
    D --> End([Pass or Fail])
    """

    @rule_method

    def thickness_steel_plate(bIRolGen, fIThiSte) -> RuleUnitResult:
        """
        Args:
            bIRolGen (bool): 일반구조용 압연강재
            fIThiSte (float): 강판의 두께

        Returns:
            pass_fail (bool): 강교량공사 2.2.1 강판 (1)의 판단 결과
        """
        assert isinstance(bIRolGen, bool)
        assert isinstance(fIThiSte, float)
        assert bIRolGen == True

        if bIRolGen:
            if fIThiSte >=8 and fIThiSte <=100:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })