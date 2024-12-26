import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_0314_02_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.14 (2) ②'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '응력제거 열처리'

    description = """
    용접
    3. 시공
    3.14 응력제거 열처리
    """

    content = """
    #### 3.14 응력제거 열처리
    (2) 응력제거 열처리는 다음 조건에 준하여 실시해야 한다.
    ② 315℃ 이상에서의 가열비(℃/hr)는 가장 두꺼운 부재를 기준으로 25 mm당 1시간에 220 ℃를 초과해서는 안 된다.
    또한 어떠한 경우도 단위 시간당의 가열온도가 220℃를 초과해서는 안 된다. 가열 중에 가열시키는 부재의 전 부위의 온도편차는 5 m 길이 이내에서 140 ℃ 이하가 되도록 해야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 응력제거 열처리"];
    B["KCS 14 31 20 3.14 (2) ②"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.14 (2) ②"])

    subgraph Variable_def
    VarIn1[/입력변수: 내부 온도/];
    VarIn2[/입력변수: 가장 두꺼운 부재의 25mm 당 가열비/];
    VarIn3[/입력변수: 단위 시간당 가열온도/];
    VarIn4[/입력변수: 가열 부재 전부위의 5m 길이 내 온도편차/];
		end
		VarIn1 & VarIn2 ~~~ VarIn3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{내부 온도 >= 315}
    C --> |True|D{가장 두꺼운 부재의 25mm 당 가열비 <= 220 \n and 단위 시간당 가열온도 <= 220 \n and 가열 부재 전부위의 5m 길이 내 온도편차 <= 140}
    D --> End([Pass or Fail])
    """

    @rule_method
    def Stress_Relief_Heat_Treatment(fIInnTem, fIHeaRat, fIHeaTem, fITemDev) -> RuleUnitResult:
        """ 응력제거 열처리
        Args:
        fIInnTem (float): 내부 온도
        fIHeaRat (float): 가장 두꺼운 부재의 25mm 당 가열비
        fIHeaTem (float): 단위 시간당 가열온도
        fITemDev (float): 가열 부재 전부위의 5m 길이 내 온도편차

        Returns:
        pass_fail (bool): 용접 3.14 응력제거 열처리 (2) ②의 판단 결과
        """
        assert isinstance(fIInnTem, float)
        fIInnTem >= 350
        assert isinstance(fIHeaRat, float)
        assert isinstance(fIHeaTem, float)
        assert isinstance(fITemDev, float)

        if fIInnTem >= 350:
          if fIHeaRat <= 220 and fIHeaTem <= 220 and fITemDev <= 140:
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