import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031005_03_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.5 (3) ④'
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
    ④ 스터드의 마무리 높이는 설계 치수에 대해 ±2 mm 이내 이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 스터드의 필릿용접"];
    B["KCS 14 31 20 3.10.5 (3) ④"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.5 (3) ④"])

    subgraph Variable_def
    VarIn1[/입력변수: 스터드의 마무리 높이/];
    VarIn2[/입력변수: 설계치수/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"설계치수-2mm < \n 스터드의 마무리 높이 \n< 설계치수+2mm"}
		C  --> End([Pass or Fail])
    """

    @rule_method
    def Stud_Fillet_Welding(fIFinHei, fIDesSiz) -> RuleUnitResult:
        """ 스터드의 필릿용접
        Args:
        fIFinHei (float): 스터드의 마무리 높이
        fIDesSiz (float): 설계치수

        Returns:
        pass_fail (bool): 용접 3.10.5 스터드필릿용접 (3) ④의 판단 결과
        """
        assert isinstance(fIFinHei, float)
        assert isinstance(fIDesSiz, float)

        if fIDesSiz - 2 <= fIFinHei <= fIDesSiz + 2:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                }
            )