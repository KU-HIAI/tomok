import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216010_030202_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 10 3.2.2.(2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '수평재의 설치 높이'

    description = """
    비계
    3. 시공
    3.2. 시스템 비계
    3.2.2. 수평재
    (2)
    """

    content = """
    #### 3.2.2. 수평재
    (2) 안전난간의 용도로 사용되는 상부수평재의 설치높이는 작업발판면으로부터 수평재 윗면까지 0.9m 이상이어야 하며,
    중간수평재는 설치높이의 중앙부에 설치(설치높이가 1.2m를 넘는 경우에는 2단 이상의 중간수평재를 설치하여 각각의 사이 간격이 0.6m 이하가 되도록 설치)하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수평재의 설치 높이];
    B["KCS 21 60 10 3.2.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 10 3.2.2 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 중간수평재의 설치높이/];
    VarOut2[/출력변수: 중간수평재의 설치개수/];
    VarOut3[/출력변수: 중간수평재의 설치간격/];
    VarIn1[/입력변수: 상부수평재의 설치높이/];
    end
    VarOut1 & VarOut2 ~~~ VarOut3

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"상부수평재의 설치높이 >= 0.9m"}
    Variable_def --> C2{"상부수평재의 설치높이 > 1.2m"}
    C2 --> |No|D2{"중간수평재의 설치높이 =
상부수평재의 설치높이 * 0.5"}
    C2 --> |YES|D1{"중간수평재의 설치개수 >= 2개
and 중간수평재의 설치간격 <= 0.9m"}
    D1 --> E2["중간수평재의 설치개수"] & E3["중간수평재의 설치간격"]
    D2 --> E4["중간수평재의 설치높이"]
    C1 --> F([Pass or Fail])
    E2 --> F2(["중간수평재의 설치개수"])
    E3 --> F3(["중간수평재의 설치간격"])
    """

    @rule_method
    def Installation_Height_of_the_Top_Horizontal_Member(fIHeiTop) -> RuleUnitResult:
        """ 수평재의 설치 높이
        Args:
            fIHeiTop (float): 상부수평재의 설치높이

        Returns:
            pass_fail (bool): 비계 3.2.2. 수평재 (2)의 판단 결과
            fOHeiInt (float): 중간수평재의 설치높이
            nONumInt (int): 중간수평재의 설치개수
            fOSpaInt (float): 중간수평재의 설치간격
        """
        assert isinstance(fIHeiTop, float)


        if 0.9 <= fIHeiTop < 1.2:
          pass_fail = True
          fOHeiInt = 0.5 * fIHeiTop
          nONumInt = 1
          fOSpaInt = None
        elif fIHeiTop >= 1.2:
          pass_fail = True
          fOHeiInt = None
          nONumInt = int(fIHeiTop / 0.6)
          fOSpaInt = fIHeiTop / (nONumInt+1)
        else:
          pass_fail = False
          fOHeiInt = None
          nONumInt = None
          fOSpaInt = None

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "fOHeiInt": fOHeiInt,
                    "nONumInt": nONumInt,
                    "fOSpaInt": fOSpaInt,
                }
            )