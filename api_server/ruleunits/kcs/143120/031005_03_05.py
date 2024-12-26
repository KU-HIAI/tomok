import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031005_03_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.5 (3) ⑤'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '스터드의 필릿용접'

    description = """
    용접
    3. 시공
    3.10 스터드의 용접
    3.10.5 스터드필릿용접
    """

    content = """
    #### 3.10.5 스터드필릿용접
    (3) 스터드의 필릿용접은 다음 규정에 준하여 시행한다.
    ⑤ 스터드의 기울기는 5° 이내 이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 스터드의 필릿용접"];
    B["KCS 14 31 20 3.10.5 (3) ⑤"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.5 (3) ⑤"])

    subgraph Variable_def
    VarIn3[/입력변수: 스터드의 기울기/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"스터드의 기울기 < 5°"}
		C  --> End([Pass or Fail])
    """

    @rule_method
    def Stud_Fillet_Welding(fISloStu) -> RuleUnitResult:
        """ 스터드의 필릿용접
        Args:
        fISloStu (float): 스터드의 기울기

        Returns:
        pass_fail (bool): 용접 3.10.5 스터드필릿용접 (3) ⑤의 판단 결과
        """
        assert isinstance(fISloStu, float)

        if fISloStu <= 5:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )