import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_09_01(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (9) ①'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '고정식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (9)
    ①
    """

    content = """
    #### 3.4 사다리
    (9) 고정식 사다리는 다음 항에 적합하여야 한다.
    ① 고정식 사다리의 기울기는 90°이하로 하고, 그 높이가 7m 이상인 경우에는 바닥으로부터 높이가 2.5m 되는 지점부터 등받이울을 설치하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고정식 사다리의 설치];
    B["KCS 21 60 15 3.4 (9) ①"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (9) ①"])

    subgraph Variable_def
    VarOut[/출력변수: 등받이울의 설치/];
    VarIn1[/입력변수: 고정식 사다리 높이/];
    VarIn2[/입력변수: 고정식 사다리의 기울기/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"고정식 사다리의 기울기 <= 90°"}
    C1 --> C2{"고정식 사다리 높이 >= 7m"}
    C2 --> D1(["바닥으로 2.5m가 되는 지점부터 등받이울을 설치한다."])
    C2 --> D2(["등받이울을 설치하지 않아도 된다."])

    C1--> E1([Pass or Fail])
    """

    @rule_method
    def Height_of_Fixed_Ladder(fIIncFix, fIHeiFix) -> RuleUnitResult:
        """ 고정식 사다리의 설치
        Args:
        fIIncFix (float): 고정식 사다리의 기울기
        fIHeiFix (float): 고정식 사다리 높이

        Returns:
        pass_fail (bool): 작업 발판 및 통로 3.4 (9) ①의 판단 결과
        sOInsBac (str): 등받이울의 설치
        """
        assert isinstance(fIIncFix, float)
        assert isinstance(fIHeiFix, float)

        if fIIncFix <= 90:
          pass_fail = True
          if fIHeiFix >= 7:
            sOInsBac = "바닥으로부터 높이가 2.5m 되는 지점부터 등받이울을 설치하여야 한다."
          else:
            sOInsBac = "등받이울을 설치하지 않아도 된다"
        else:
          pass_fail = False
          sOInsBac = None

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "sOInsBac": sOInsBac,
                }
            )