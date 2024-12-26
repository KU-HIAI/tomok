import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_0302_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 부록 3.2 (2)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '그라우트의 두께'

    description = """
    철근공사
    부록
    3. 시공
    3.2 그라우트에 관한 요구 사항
    (2)
    """
    content = """
    #### 3.2 그라우트에 관한 요구 사항
    (2) 그라우트의 두께는 40mm~50mm로 하여야 한다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그라우트의 두께];
    B["KCS 14 20 11 부록 3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 부록 3.2 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 그라우트의 두께/];
    VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"40 ≤ 그라우트의 두께 ≤ 50"}
    C --> D(["Pass or Fail"])
    """

    @rule_method
    def grout_thickness(fIGroThi)-> RuleUnitResult:
        """
        Args:
            fIGroThi (float): 그라우트의 두께

        Returns:
            pass_fail (bool): 철근공사 부록 3.2 그라우트에 관한 요구 사항 (2)의 판단 결과
        """
        assert isinstance(fIGroThi, float)

        if fIGroThi >= 40 and fIGroThi <= 50:
            return RuleUnitResult(
                result_variables = {
                "pass_fail": True,
                })
        else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                    })