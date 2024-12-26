import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_020501_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 2.5.1.(4)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '와이어로프의 상태'

    description = """
    비계
    2. 자재
    2.5 기타 비계
    2.5.1 달비계
    (4)
    """

    content = """
    #### 2.5.1 달비계
    (4) 와이어 로프는 다음에 해당되는 것을 사용하지 않아야 한다.
    ② 와이어로프의 한 꼬임에서 끊어진 소선의 수가 10％ 이상인 것
    ③ 지름의 감소가 공칭지름의 7％를 초과하는 것
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 와이어로프의 상태];
    B["KCS 21 60 10 2.5.1 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 2.5.1 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 와이어로프의 소선의 수/];
    VarIn2[/입력변수: 와이어로프의 끊어진 소선의 수/];
    VarIn3[/입력변수: 와이어로프의 지름/];
    VarIn4[/입력변수: 와이어로프의 공칭지름/];
		end
		VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"와이어로프의 끊어진 소선의 수 <= 와이어로프의 소선의 수 * 0.1"}
    Variable_def --> C2{"와이어로프의 지름 >= 와이어로프의 공칭지름 + 0.93"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Number_of_Strands_in_Wire_Rope(nINumStr, nIBroStr, fIWirDia, fIWirNom) -> bool:
        """ 와이어로프의 상태
        Args:
            nINumStr (int): 와이어로프의 소선의 수
            nIBroStr (int): 와이어로프의 끊어진 소선의 수
            fIWirDia (float): 와이어로프의 지름
            fIWirNom (float): 와이어로프의 공칭지름

        Returns:
            pass_fail_1 (bool): 비계 2.5.1 달비계 (4) ②의 판단 결과
            pass_fail_2 (bool): 비계 2.5.1 달비계 (4) ③의 판단 결과
        """
        assert isinstance(nINumStr, int)
        assert isinstance(nIBroStr, int)
        assert isinstance(fIWirDia, float)
        assert isinstance(fIWirNom, float)

        if nIBroStr <= nINumStr * 0.1:
          pass_fail_1 = True
        else:
          pass_fail_1 = False

        if fIWirDia >= fIWirNom * 0.93:
          pass_fail_2 = True
        else:
          pass_fail_2 = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail_1": pass_fail_1,
                    "pass_fail_2": pass_fail_2,
                }
            )