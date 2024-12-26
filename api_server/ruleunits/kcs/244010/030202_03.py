import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_030202_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 3.2.2 (8)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '신축이음 봉함재의 현장이음'
    description = """
    신축이음
    3. 시공
    3.2 조립
    3.2.2 조립 시 주의사항
    (3)
    """

    content = """
    #### 3.2.2 조립 시 주의사항
    (3) 길이 18 m 이하로 조립된 신축이음 봉함재는 중간에 현장이음이 없이 반입되어야 한다.
"""

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 신축이음 봉함재의 현장이음];
    B["KCS 24 40 10 3.2.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 3.2.2 (3)"])

    subgraph Variable_def
    VarOut[/출력변수: 신축이음 조립 시 주의사항/];
    VarIn1[/입력변수: 조립된 신축이음 봉합재의 길이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{조립된 신축이음 봉합재의 길이 <=18}

    C --> |True|D["중간에 현장이음이 없이 반입되어야 한다."]
		D --> F([신축이음 조립 시 주의사항])


    """

    @rule_method
    def on_site_joint_sealant(fILenSea) -> str :
        """신축이음 봉함재의 현장이음

        Args:
            fILenSea (float): 조립된 신축이음 봉함재의 길이

        Returns:
            sOPreJoi (str) : 신축이음 조립 시 주의사항
        """
        assert isinstance(fILenSea, float)

        if fILenSea <= 18:
            sOJoiSea = "중간에 현장이음이 없이 반입되어야 한다."
        else:
            sOPreJoi = "중간에 현장이음 여부와 상관없이 반입할 수 있다."

        return RuleUnitResult(
                result_variables = {
                    "sOPreJoi": sOPreJoi,
                }
            )