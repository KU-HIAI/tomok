import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS115020_030703_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 50 20 3.7.3 (2)'
    ref_date = '2021-05-12'
    doc_date = '2023-09-15'
    title = '콘크리트 널말뚝의 허용오차'

    description = """
    널말뚝
    3. 시공
    3.7 콘크리트 널말뚝
    3.7.3 검사 및 허용오차
    (2)
    """
    content = """
    ####3.7.3 검사 및 허용오차
    (2) 허용오차에 대하여는 3.4.2(17)의 요건에 따르며 널말뚝 마루높이에 대한 허용오차는 (±)50mm로 한다
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 널말뚝의 허용오차];
    B["KCS 11 50 20 3.7.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 50 20 3.7.3 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 널말뚝 마루높이의 설계값/];
    VarIn2[/입력변수: 널말뚝 마루높이의 시공값/]
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"|널말뚝 마루높이의 설계값-널말뚝 마루높이의 시공값| ≤ 50"}
    D --> End([Pass or Fail])
    """

    @rule_method
    def tolerance_pile(fIDesHei, fIConHei)-> RuleUnitResult:
        """
        Args:
            fIDesHei (float): 널말뚝 마루높이의 설계값
            fIConHei (float): 널말뚝 마루높이의 시공값

        Returns:
            pass_fail (bool): 널말뚝 3.7.3 검사 및 허용오차 (2)의 판단 결과
        """
        assert isinstance(fIDesHei, float)
        assert isinstance(fIConHei, float)


        if abs(fIDesHei - fIConHei) <= 50:
            return RuleUnitResult(
                    result_variables = {
                        "pass_fail": True,
                    }
                )
        else:
            return RuleUnitResult(
                    result_variables = {
                        "pass_fail": False,
                    }
                )