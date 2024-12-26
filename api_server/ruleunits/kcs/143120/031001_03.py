import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031001_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.1 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '스터드 용접'

    description = """
    용접
    3. 시공
    3.10 스터드의 용접
    3.10.1 스터드의 용접에 관한 일반사항
    """

    content = """
    #### 3.10.1 스터드의 용접에 관한 일반사항
    (3) 직경 8 mm 이상의 스터드를 용접하는 경우에는 탈산화와 아크안정을 위한 플럭스가 갖추어져야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 스터드 용접"];
    B["KCS 14 31 20 3.10.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.1 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 스터드 용접"/];
    VarIn1[/입력변수: 스터드의 직경/];
		VarOut1 ~~~ VarIn1
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"스터드의 직경 ≥ 8 mm"}
    C --> |"True"|D[탈산화와 아크안정을 위한 플럭스가 갖추어져야 한다.]
		D  --> End([스터드 용접])
    """

    @rule_method
    def Diameter_Of_Stud(fIDiaStu) -> RuleUnitResult:
        """ 스터드 용접
        Args:
        fIDiaStu (float): 스터드의 직경

        Returns:
        sOStuWel (str): 스터드의 용접
        """
        assert isinstance(fIDiaStu, float)

        if fIDiaStu >= 8:
          sOStuWel = "탈산화와 아크안정을 위한 플럭스가 갖추어져야 한다."
        else:
          sOStuWel = "탈산화와 아크안정을 위한 플럭스가 갖추어져있지 않아도 된다."

        return RuleUnitResult(
                result_variables = {
                    "sOStuWel": sOStuWel
                }
            )