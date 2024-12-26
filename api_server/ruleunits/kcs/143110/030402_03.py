import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030402_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.4.2 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '볼트구멍의 허용오차'

    description = """
    제작
    3. 시공
    3.4 구멍뚫기
    3.4.2 볼트 구멍의 치수 및 정밀도
    (3)
    """

    content = """
    #### 3.4.2 볼트 구멍의 치수 및 정밀도
    (3) 제작 시 구멍중심선 축에서 구멍의 어긋남은 ±1 mm 이하로 하며, 볼트그룹에서 처음 볼트와 마지막 볼트의 최대연단 거리의 오차는 ±2 mm 이하로 한다. 다만 볼트구멍 간 허용오차는 ±0.5 mm 이하로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트구멍의 허용오차];
    B["KCS 14 31 10 3.4.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.4.2 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 구멍의 어긋남/];
    VarIn2[/입력변수: 최대연단 거리의 오차/];
    VarIn3[/입력변수: 볼트구멍간 허용오차/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"-1 ≤구멍의 어긋남 ≤ 1 \n  -2 ≤최대연단 거리의 오차 ≤ 2 \n  -0.5 ≤볼트구멍 간 허용오차 ≤ 0.5 \n."}
		C --> D([Pass or Fail])
    """

    @rule_method
    def Slip_of_Hole(fISliHol, fITolMax, fITolBet) -> bool:
        """ 볼트구멍의 허용오차
        Args:
        fISliHol (float): 구멍의 어긋남
        fITolMax (float): 최대연단 거리의 오차
        fITolBet (float): 볼트구멍간 허용오차

        Returns:
        pass_fail (bool): 제작 3.4.2 볼트 구멍의 치수 및 정밀도 (3)의 판단 결과
        """
        assert isinstance(fISliHol, float)
        assert isinstance(fITolMax, float)
        assert isinstance(fITolBet, float)

        if -1 <= fISliHol <= 1 and -2 <= fITolMax <= 2 and -0.5 <= fITolBet <= 0.5:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )