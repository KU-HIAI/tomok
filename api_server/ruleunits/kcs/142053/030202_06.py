import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_030202_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 3.2.2 (6)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-21'
    title = '거푸집 내 긴장재의 배치오차'


    description = """
    프리스트레스트 콘크리트
    3. 시공
    3.2 긴장재의 배치
    3.2.2 덕트, 보호관 및 긴장재의 배치
    (6)
    """
    content = """
    #### 3.2.2 덕트, 보호관 및 긴장재의 배치
    (6) 거푸집 내에서 허용되는 긴장재의 배치오차는 도심 위치 변동의 경우 부재치수가 1m 미만일 때에는 5 mm를 넘지 않아야 하며,
    또 1 m 이상인 경우에는 부재치수의 1/200 이하로서 10 mm를 넘지 않도록 하여야 한다. 어떠한 경우라도 10 mm를 넘는 경우에는 이것을 수정하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 거푸집 내 긴장재의 배치오차];
    B["KCS 14 20 53 3.2.2 (6)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 3.2.2 (6)"])

    subgraph Variable_def
    VarOut[/출력변수: 거푸집 내 긴장재의 배치오차/];
    VarIn1[/입력변수: 도심 위치 변동/];
    VarIn2[/입력변수: 부재치수/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"도심 위치 변동"}
    C --> |False|D[거푸집 내 긴장재의 배치오차 = 10 mm]
    C --> |True| F{부재치수}
    F --> |"부재치수 < 1m"|G[거푸집 내 긴장재의 배치오차 = 5 mm]
    F --> |"부재치수 >= 1m"|H["거푸집 내 긴장재의 배치오차 = min(부재치수/200, 10 mm)"]
    D & G & H --> I(["거푸집 내 긴장재의 배치오차"])
    """

    @rule_method

    def arrange_tolerance(bICenFlu ,fIEleSiz) -> RuleUnitResult:
        """
        Args:
            bICenFlu (bool): 도심 위치 변동
            fIEleSiz (float): 부재치수

        Returns:
            fOTolTen (float): 거푸집 내 긴장재의 배치오차
        """
        assert isinstance(bICenFlu, bool)
        assert isinstance(fIEleSiz, float)
        assert fIEleSiz > 1

        if bICenFlu:
            if fIEleSiz < 1000:
                fOTolTen = 5
            else:
                fOTolTen = min(fIEleSiz/200, 10)
        else:
            fOTolTen = 10

        return RuleUnitResult(
            result_variables = {
                "fOTolTen": fOTolTen,
                })