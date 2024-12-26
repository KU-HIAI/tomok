import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030502_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.5.2 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '그루브용접 루트 패스의 최대 두께'

    description = """
    용접
    3. 시공
    3.5 피복아크용접(SMAW)
    3.5.2 용접절차
    """

    content = """
    #### 3.5.2 용접절차
    (3) 그루브용접 루트패스의 최대 두께는 6 mm로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 그루브용접 루트 패스의 최대 두께"];
    B["KCS 14 31 20 3.5.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.5.2 (3)"])

    subgraph Variable_def
    VarIn[/입력변수: 그루브용접 루트 패스의 두께/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"그루브용접 루트 패스의 두께 > 6 mm"}
    C --> D([Fail or Fail])
    """

    @rule_method
    def Thickness_of_Root_Pass_in_Groove_Weld(fIThiRoo) -> bool:
        """ 그루브용접 루트 패스의 최대 두께
        Args:
        fIThiRoo (float): 그루브용접 루트 패스의 두께

        Returns:
        pass_fail (bool): 용접 3.5.2 용접절차 (3)의 판단 결과
        """
        assert isinstance(fIThiRoo, float)

        if fIThiRoo <= 6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )