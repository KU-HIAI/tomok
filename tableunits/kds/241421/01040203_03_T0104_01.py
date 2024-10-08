import sys
import os

from tomok import TableUnit, table_function, RuleUnitResult

import math
from typing import List


class KDS241421_01040203_03_T0104_01(TableUnit):
    priority = 1
    table_able = True
    author = "국가건설기준센터"
    ref_code = "KDS 24 14 21 1.4.2.3 (3)"
    ref_date = "2021-04-12"
    doc_date = "2024-10-08"
    title = "재료 계수"

    description = """
    """
    content = """
    """

    @table_function
    def Material_Factor(fILoadC) -> float:
        """가동받침의 이동량

        Args:
            fILoadC (str): 하중조합

        Returns:
            fOPie (float): 콘크리트 pi_e
            fOPis (float): 철근 또는 프리스트래싱 강재 pi_s
        """

        fOPie = -9999
        fOPis = -9999

        assert isinstance(fILoadC, str)

        if fILoadC == "극한하중조합-I, -II, -III, -IV, -V":
            fOPie = 0.65
            fOPis = 0.90
        elif fILoadC == "극단상황하중조합-I, -II":
            fOPie = 1.0
            fOPis = 1.0
        elif fILoadC == "사용하중조합-I, -III, -IV, -V":
            fOPie = 1.0
            fOPis = 1.0
        elif fILoadC == "피로하중조합":
            fOPie = 1.0
            fOPis = 1.0

        return RuleUnitResult(
            result_variables={
                "fOPie": fOPie,
                "fOPis": fOPis,
            }
        )
