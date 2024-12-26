import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030105_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.1.5 (4)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '횡방향 재하위치'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.5 주거더를 설계하는 경우의 설계차량활하중
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표준트럭하중 최외측 차륜중심의 횡방향 재하위치];
    B["KDS 24 12 21 4.3.1.5 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 횡방향 재하위치/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.1.5 (4)"])
		C --> Variable_def --> D

    D["횡방향 재하위치 = 차도부분의 단부로부터 600mm"]
    """

    @rule_method
    def width_of_a_loading_lane(fOlatpos) -> RuleUnitResult:
        """횡방향 재하위치

        Args:
            fOlatpos (float): 차도부분의 단부로부터 횡방향 재하거리

        Returns:
            fOlatpos (float): 강교 설계기준(한계상태설계법)  4.3.1.5 주거더를 설계하는 경우의 설계차량활하중 (4)의 값
        """

        fOlatpos = 600

        return RuleUnitResult(
            result_variables = {
                "fOlatpos": fOlatpos,
            }
        )