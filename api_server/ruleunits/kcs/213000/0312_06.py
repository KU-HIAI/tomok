import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_0312_06(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.12. (6)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '타이로드에 가하는 하중'

    description = """
    가설흙막이 공사
    3. 시공
    3.12 타이 로드와 케이블
    (6)
    """

    content = """
    #### 3.12. 타이 로드와 케이블
    (6) 설치된 타이로드는 설계도면에 명시된 시험하중까지 가하여야 하며, 하중의 5％ 이상 손실되지 않아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 타이로드에 가하는 하중];
    B["KCS 21 30 00 3.12 (6)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.12 (6)"])

    subgraph Variable_def
    VarIn1[/입력변수: 타이로드의 하중/];
    VarIn2[/입력변수: 시험하중/];
    VarIn3[/입력변수: 하중의 손실/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"타이로드의 하중 >= 시험하중"}
    Variable_def --> C2{"하중의 손실 <= 타이로드의 하중 * 0.05"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Load_on_Tie_Rods(fILoaTie, fITesLoa, fILoaLos) -> bool:
        """ 타이로드에 가하는 하중
        Args:
            fILoaTie (float): 타이로드의 하중
            fITesLoa (float): 시험하중
            fILoaLos (float): 하중의 손실

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.12 타이 로드와 케이블 (6)의 판단 결과
        """
        assert isinstance(fILoaTie, float)
        assert isinstance(fITesLoa, float)
        assert isinstance(fILoaLos, float)

        if fILoaTie >= fITesLoa:
          if fILoaLos <= 0.05*fILoaTie:
            pass_fail = True
          else:
            pass_fail = False
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )