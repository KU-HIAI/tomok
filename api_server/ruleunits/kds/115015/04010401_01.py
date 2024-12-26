import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010401_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.4.1 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '나무말뚝의 허용압축응력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.4 말뚝재료의 허용응력
    4.1.4.1 나무말뚝
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 나무말뚝의 허용압축응력];
    B["KDS 11 50 15 4.1.4.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 나무말뚝의 허용압축응력/];
    VarIn1[/입력변수: 상시 습윤상태에서의 허용압축응력/] ;

		VarOut~~~VarIn1

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.4.1 (1)"])
		C --> Variable_def;
		Variable_def---->D
		D{"소나무, 낙엽송, 미송의 경우"}
		G["5 MPa"]
		E["min(상시습윤상태에서의 허용압축응력, 5Mpa)"]
		F(["나무말뚝의 허용압축응력"])

		D--YES---->G
		D--NO---->E
		G & E----->F
    """

    @rule_method
    def allowable_compressive_stress_of_timber_pile(fIalcswc) -> RuleUnitResult:
        """나무말뚝의 허용압축응력

        Args:
            fIalcswc (float): 상시 습윤상태에서의 허용압축응력

        Returns:
            fOalcstp (float): 깊은기초 설계기준(일반설계법)  4.1.4.1 나무말뚝 (1)의 값 1
            fOalcsop (float): 깊은기초 설계기준(일반설계법)  4.1.4.1 나무말뚝 (1)의 값 2
        """

        assert isinstance(fIalcswc, float)

        fOalcstp = 5
        fOalcsop = min(fIalcswc, 5)

        return RuleUnitResult(
            result_variables = {
                "fOalcstp": fOalcstp,
                "fOalcsop": fOalcsop,
            }
        )