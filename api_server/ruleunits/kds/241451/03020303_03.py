import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03020303_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '기초의 활동저항'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.3 활동 파괴
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기초의 활동저항];
    B["KDS 24 14 51 3.2.3.3 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 점성토의 점착력/];
		VarIn2[/입력변수: 기초와 흙사이 경계면상 수직응력/];

		VarIn1 ~~~ VarIn2

    end
    Python_Class ~~~ E(["KDS 24 14 51 3.2.3.1 (5)"])
		E --> Variable_def;

		C[점성토에 설치된 기초의 활동저항]
		D["min(점성토의 점착력,150mm이상 다져진 사질토위에 놓이는 경우의 기초와 흙사이의 경계면상 수직응력의 1/2)"]


		Variable_def ---> C ---> D
		D ---> G([점성토에 설치된 기초의 활동저항])
    """

    @rule_method
    def Foundation_Resistance(fIAdhvis,fIVersoi) -> RuleUnitResult:
        """기초의 활동저항

        Args:
            fIAdhvis (float): 점성토의 점착력
            fIVersoi (float): 기초와 흙사이 경계면상 수직응력

        Returns:
            fOActrotf (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 활동 파괴 (3)의 값
        """

        assert isinstance(fIAdhvis, float)
        assert isinstance(fIVersoi, float)

        fOActrotf = min(fIAdhvis, fIVersoi * 0.5)
        return RuleUnitResult(
            result_variables = {
                "fOActrotf": fOActrotf,
                }
            )