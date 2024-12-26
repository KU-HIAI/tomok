import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030401_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.4.1.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '주틀의 높이와 간격'

    description = """
    비계
    3. 시공
    3.4 강관틀 비계
    3.4.1 주틀
    (1)
    """

    content = """
    #### 3.4.1 주틀
    (1) 전체 높이는 원칙적으로 40m를 초과할 수 없으며, 높이가 20m를 초과하는 경우 또는 중량작업을 하는 경우에는 내력상 중요한 틀의 높이를 2m 이하로 하고 주틀의 간격을 1.8m 이하로 하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 주틀의 높이와 간격];
    B["KCS 21 60 10 3.4.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.4.1 (1)"])

    subgraph Variable_def
		VarIn1[/입력변수: 주틀의 전체 높이/];
    VarIn2[/입력변수: 중량작업을 하는 경우/];
    VarIn3[/입력변수: 내력상 중요한 틀의 높이/];
    VarIn4[/입력변수: 주틀의 전체 높이/];
    end
    VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"주틀의 전체높이 < 40m"}
    C1 --> |YES|C2{"주틀의 전체 높이 > 20m </br> or 중량작업을 하는경우"}
    C2 --> |YES|C3{"내력상 중요한 틀의 높이 <= 2m </br> and 주틀의 간격 <= 1.8m"}
    C1 --> |No|D([Pass or Fail])
    C3 --> D([Pass or Fail])
    """

    @rule_method
    def Overall_Height_of_the_Main_Frame(fIHeiFra, bICasHea, fIHeiCri, fISpaFra) -> bool:
        """ 주틀의 높이와 간격
        Args:
            fIHeiFra (float): 주틀의 전체 높이
            bICasHea (bool): 중량작업을 하는 경우
            fIHeiCri (float): 내력상 중요한 틀의 높이
            fISpaFra (float): 주틀의 간격

        Returns:
            pass_fail (bool): 비계 3.4.1 주틀 (1)의 판단 결과
        """
        assert isinstance(fIHeiFra, float)
        assert isinstance(bICasHea, bool)
        assert isinstance(fIHeiCri, float)
        assert isinstance(fISpaFra, float)

        if 20 < fIHeiFra <= 40 or bICasHea == True:
          if fIHeiCri <= 2 and fISpaFra <= 1.8:
            pass_fail = True
          else:
            pass_fail = False
        elif fIHeiFra <= 20:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )