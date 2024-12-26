import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04090201_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.9.2.1 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '종방향 항력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.9 정수압, 유수압, 부력, 파압: WA, BP, WP
    4.9.2 유수압
    4.9.2.1 종방향
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 항력];
    B["KDS 24 12 21 4.9.2.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 종방향 항력/];
    VarIn1[/입력변수 : 종방향 동수압/];
    VarIn2[/입력변수 : 흐름에 노출된 투영면적/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.9.2.1 (2)"])
		C --> Variable_def

    D["종방향 항력 = 종방향 동수압 X 흐름에 노출된 투영면적"];
    E(["종방향 항력"]);
    Variable_def --->D--->E
    """

    @rule_method
    def Longitudinal_pressure(fIPdylon,fIAexflo) -> RuleUnitResult:
        """ 종방향 압력

        Args:
            fIPdylon (float): 종방향 동수압
            fIAexflo (float): 흐름에 노출된 투영면적

        Returns:
            fOlonrea (float): 강교 설계기준(한계상태설계법)  4.9.2.1 종방향 (2)의 값
        """

        assert isinstance(fIPdylon, float)
        assert isinstance(fIAexflo, float)

        fOlonrea = fIPdylon * fIAexflo / 1000000

        return RuleUnitResult(
            result_variables = {
                "fOlonrea": fOlonrea,
            }
        )