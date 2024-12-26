import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020103_15(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.3 (14)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '덕트의 내부 단면적'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (15)
    """
    content = """
    #### 2.1.3 프리스트레스트 콘크리트용 그라우트
    (15) 그라우트되는 다수의 강선, 강연선 또는 강봉을 배치하기 위한 덕트는 내부 단면적이 긴장재 단면적의 2.5배 이상이어야 한다. 단, 30 m 이하의 짧은 텐던에서는 2배 이상이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 덕트의 내부 단면적];
    B["KCS 14 20 53 2.1.4 (15)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.4 (15)"])

    subgraph Variable_def
    VarIn1[/입력변수: 텐던 길이/];
    VarIn2[/입력변수: 덕트의 내부 단면적/];
    VarIn3[/입력변수: 긴장재 단면적/];
    VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"텐던길이"}
    C --> |<=30m|D{덕트의 최소 내부 단면적 \n / 긴장재 단면적 >= 2.0}
    C --> |>30m|E{덕트의 최소 내부 단면적 \n / 긴장재 단면적 >= 2.5}
    D & E --> End([Pass or Fail])
    """

    @rule_method

    def internal_cross_section_duct(fITenLen,fICroTen, fICroDuc) -> RuleUnitResult:
        """
        Args:
            fITenLen (float): 텐던 길이
            fICroTen (float): 긴장재 단면적
            fICroDuc (float): 덕트의 내부 단면적

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.3 프리스트레스트 콘크리트용 그라우트 (15)의 판단 결과
        """
        assert isinstance(fITenLen, float)
        assert isinstance(fICroTen, float)
        assert fICroTen > 0
        assert isinstance(fICroDuc, float)

        if fITenLen<=30:
            if fICroDuc/fICroTen >=2:
                pass_fail = True
            else:
                pass_fail = False
        else:
            if fICroDuc/fICroTen >=2.5:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })