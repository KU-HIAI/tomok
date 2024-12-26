import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_10(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (10)'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '이동식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (10)
    """

    content = """
    #### 3.4 사다리
    (10) 이동식 사다리는 다음 항에 적합하여야 한다.
    ① 이동식 사다리의 길이는 6m 이내이어야 한다.
    ② 이동식 사다리의 경사는 수평면으로부터 75°이하로 하는 것을 원칙으로 한다.
    ③ 사다리 폭은 300mm 이상이어야 하며, 발 받침대 간격은 250mm ∼ 350mm 이내로 하여야 한다.
    ④ 벽면 상부로부터 0.6m 이상의 여장길이가 있어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 이동식 사다리의 설치];
    B["KCS 21 60 15 3.4 (10)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (10)"])

    subgraph Variable_def
    VarIn1[/입력변수: 이동식 사다리의 길이/];
    VarIn2[/입력변수: 이동식 사다리의 경사/];
    VarIn3[/입력변수: 사다리 폭/];
    VarIn4[/입력변수: 발 받침대 간격/];
    VarIn5[/입력변수: 여장길이/];
    end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"이동식 사다리의 길이 <= 6m"}
    Variable_def --> C2{"이동식 사다리의 경사 <= 75°"}
    Variable_def --> C3{"사다리 폭 >= 300mm"}
    Variable_def --> C4{"250mm <= 발 받침대 간격 <= 350mm"}
    Variable_def --> C5{"여장길이 >= 0.6m"}

    C1 & C2 & C3 & C4 & C5 --> D([Pass or Fail])
    """

    @rule_method
    def Length_of_Portable_Ladder(fILenPor, fISloPor, fIWidLad, fISpaFoo, fICleLen) -> bool:
        """ 이동식 사다리의 설치
        Args:
        fILenPor (float): 이동식 사다리 길이
        fISloPor (float): 이동식 사다리 경사
        fIWidLad (float): 사다리 폭
        fISpaFoo (float): 발 받침대 간격
        fICleLen (float): 여장길이

        Returns:
        pass_fail (bool): 작업발판 및 통로 3.4 사다리 (10)의 판단 결과
        """
        assert isinstance(fILenPor, float)
        assert isinstance(fISloPor, float)
        assert isinstance(fIWidLad, float)
        assert isinstance(fISpaFoo, float)
        assert isinstance(fICleLen, float)

        if fILenPor <= 6 and fISloPor <= 75 and fIWidLad >= 300 and 250 <= fISpaFoo <= 350 and fICleLen >= 0.6:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )