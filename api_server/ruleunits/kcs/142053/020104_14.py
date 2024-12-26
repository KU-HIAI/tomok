import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020104_14(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.4 (14)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '덕트의 최소 내면 지름'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.4 프리스트레스트 콘크리트 부속 재료
    (14)
    """
    content = """
    #### 2.1.4 프리스트레스트 콘크리트 부속 재료
    (14) 그라우트되는 단독 강선, 강연선 또는 강봉을 배치하기 위한 덕트는 내면 지름이 긴장재 지름보다 6 mm 이상 커야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 덕트의 최소 내면 지름];
    B["KCS 14 20 53 2.1.4 (14)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.4 (14)"])

    subgraph Variable_def
    VarIn1[/입력변수: 긴장재 지름/];
    VarIn2[/입력변수: 덕트 내면 지름/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"덕트의 최소 내면 지름 \n - 긴장재 지름 >= 6mm"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def internal_diameter_duct(fIIntDia,fITenDia) -> RuleUnitResult:
        """
        Args:
            fIIntDia (float): 덕트의 내면 지름
            fITenDia (float): 긴장재 지름

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.3 프리스트레스트 콘크리트용 그라우트 (14)의 판단 결과
        """
        assert isinstance(fIIntDia, float)
        assert isinstance(fITenDia, float)

        if (fIIntDia-fITenDia)>=6:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })