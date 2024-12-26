import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0304_09(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.4 (9)'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '고정식 사다리의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.4 사다리
    (9)
    """

    content = """
    #### 3.4 사다리
    (9) 고정식 사다리는 다음 항에 적합하여야 한다.
    ① 고정식 사다리의 기울기는 90°이하로 하고, 그 높이가 7m 이상인 경우에는 바닥으로부터 높이가 2.5m 되는 지점부터 등받이울을 설치하여야 한다.
    ② 사다리 폭은 300mm 이상이어야 하며, 발 받침대 간격은 250mm ∼ 350mm 이내로 하여야 한다.
    ③ 벽면 상부로부터 0.6m 이상의 여장길이가 있어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고정식 사다리의 설치];
    B["KCS 21 60 15 3.4 (9)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.4 (9)"])

    subgraph Variable_def
    VarOut[/출력변수: 등받이울의 설치/];
    VarIn1[/입력변수: 고정식 사다리 높이/];
    VarIn2[/입력변수: 고정식 사다리의 기울기/];
    VarIn3[/입력변수: 사다리 폭/];
    VarIn4[/입력변수: 발 받침대 간격/];
    VarIn5[/입력변수: 여장길이/];
    end
		VarOut & VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"고정식 사다리의 기울기 <= 90°"}
    C1 --> C2{"고정식 사다리 높이 >= 7m"}
    Variable_def --> C3{"사다리 폭 >= 300mm"}
    Variable_def --> C4{"250mm <= 발 받침대 간격 <= 350mm"}
    Variable_def --> C5{"여장길이 >= 0.6m"}
    C2 --> D["바닥으로 2.5m가 되는 지점부터 등받이울 설치"]

    C1 & C3 & C4 & C5 --> E1([Pass or Fail])
    D --> E2(["등받이울의 설치"])
    """

    @rule_method
    def Height_of_Fixed_Ladder(fIIncFix, fIHeiFix, fIWidLad, fISpaFoo, fICleLen) -> RuleUnitResult:
        """ 고정식 사다리의 설치
        Args:
        fIIncFix (float): 고정식 사다리의 기울기
        fIHeiFix (float): 고정식 사다리 높이
        fIWidLad (float): 사다리 폭
        fISpaFoo (float): 발 받침대 간격
        fICleLen (float): 여장길이

        Returns:
        pass_fail (bool): 작업 발판 및 통로 3.4 (9)의 판단 결과
        sOInsBac (str): 등받이울의 설치
        """
        assert isinstance(fIIncFix, float)
        assert isinstance(fIHeiFix, float)
        assert isinstance(fIWidLad, float)
        assert isinstance(fISpaFoo, float)
        assert isinstance(fICleLen, float)

        if fIIncFix <= 90 and fIWidLad >= 300 and 250 <= fISpaFoo <= 350 and fICleLen >= 0.6:
          pass_fail = True
          if fIHeiFix >= 7:
            sOInsBac = "바닥으로부터 높이가 2.5m 되는 지점부터 등받이울을 설치하여야 한다"
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