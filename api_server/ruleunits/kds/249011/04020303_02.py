import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '내부보강판의 최소두께'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.3 재료
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 내부보강판의 최소두께];
    B["KDS 24 90 11 4.2.3.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 내부보강판의 최소두께/];

		end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.3 (2)"])
		C --> Variable_def;

		Variable_def--->D
		D["내부보강판의 최소두께=2mm"]
		D~~~ |"KDS 24 90 11  4.2.3.11"| D
    """

    @rule_method
    def Minimum_Thickness_Of_Inner_Reinforcement (fOmintir) -> RuleUnitResult:
        """내부보강판의 최소두께

        Args:
            fOmintir (float): 내부보강판의 최소두께

        Returns:
            fOmintir (float): 교량 기타시설설계기준 (한계상태설계법)  4.2.3.3 재료 (2)의 값
        """

        fOmintir = 2
        return RuleUnitResult(
            result_variables = {
                "fOmintir": fOmintir,
            }
        )