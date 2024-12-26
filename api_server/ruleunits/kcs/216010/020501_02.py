import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_020501_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 2.5.1.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-26'
    title = '재사용 달기체인의 상태'

    description = """
    비계
    2. 자재
    2.5 기타 비계
    2.5.1 달비계
    (2)
    """

    content = """
    #### 2.5.1 달비계
    (2) 재사용하는 달기체인은 다음에 해당되는 것을 사용하지 않아야 한다.
    ① 체인의 길이가 제조되었을 때보다 5％를 초과한 것
    ② 링 단면의 직경이 10％를 초과하여 감소한 것
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 재사용 달기체인의 상태];
    B["KCS 21 60 10 2.5.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 2.5.1 (2)"])

    subgraph Variable_def
    VarIn1[/입력변수: 체인의 길이/];
    VarIn2[/입력변수: 제조되었을 때의 체인의 길이/];
    VarIn3[/입력변수: 링 단명의 직경/];
    VarIn4[/입력변수: 제조되었을 때의 링 단명의 직경/];
		end
		VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"제조되었을 때의 체인의 길이 * 1 <= 체인의 길이 </br> <= 제조되었을 때의 체인의 길이 * 1.05"}
    Variable_def --> C2{"제조되었을 때의 링 단면의 직경 * 0.9 <= 링 단면의 직경 </br> <= 제조되었을 때의 링 단면의 직경 * 1"}
    C1 & C2 --> D([Pass or Fail])
    """

    @rule_method
    def Chain_Length(fIChaLen, fIOriCha, fIRinDia, fIOriRin) -> bool:
        """ 재사용 달기체인의 상태
        Args:
            fIChaLen (float): 체인의 길이
            fIOriCha (float): 제조되었을 때의 체인의 길이
            fIRinDia (float): 링 단면의 직경
            fIOriRin (float): 제조되었을 때의 링 단면의 직경

        Returns:
            pass_fail_1 (bool): 비계 2.5.1 달비계 (2) ①의 판단결과
            pass_fail_2 (bool): 비계 2.5.1 달비계 (2) ②의 판단결과
        """
        assert isinstance(fIChaLen, float)
        assert isinstance(fIOriCha, float)
        assert isinstance(fIRinDia, float)
        assert isinstance(fIOriRin, float)

        if fIOriCha * 1 <= fIChaLen <= fIOriCha * 1.05:
          pass_fail_1 = True
        else:
          pass_fail_1 = False

        if fIOriRin * 0.9 <= fIRinDia <= fIOriRin * 1:
          pass_fail_2 = True
        else:
          pass_fail_2 = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail_1": pass_fail_1,
                    "pass_fail_2": pass_fail_2,
                }
            )