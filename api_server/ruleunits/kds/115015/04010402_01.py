import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.4.2 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '기성콘크리트말뚝의 허용압축응력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.4 말뚝재료의 허용응력
    4.1.4.2 기성콘크리트말뚝
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기성콘크리트말뚝 허용압축응력];
    B["KDS 11 50 15 4.1.4.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 기성콘크리트말뚝 장기 허용압축응력/];
		VarOut2[/출력변수: 기성콘크리트말뚝 단기 허용압축응력/];
    VarIn1[/입력변수: 콘크리트 설계기준강도/] ;
    VarIn2[/입력변수: 장기 허용압축응력/];

		VarOut~~~VarIn1
		VarOut2~~~VarIn2

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.4.2 (1)"])
		C --> Variable_def;

		Variable_def-->D
		D["35Mpa ≤ 콘크리트설계기기준강도"];
    E(["장기 허용압축응력=콘크리트설계기준강도X0.25"]);
    F(["단기 허용압축응력=장기 허용압축응력X1.5"]);
    D--->E
		D--->F
    """

    @rule_method
    def allowable_compressive_stress_of_precast_concrete_pile(fIfck) -> RuleUnitResult:
        """기성콘크리트말뚝의 허용압축응력

        Args:
            fIfck (float): 설계기준 압축강도

        Returns:
            fOlacspc (float): 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (1)의 값 1
            fOsacspc (float): 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (1)의 값 2
        """

        assert isinstance(fIfck, float)

        fOlacspc = fIfck * 0.25
        fOsacspc = fOlacspc * 1.5

        return RuleUnitResult(
            result_variables = {
                "fOlacspc": fOlacspc,
                "fOsacspc": fOsacspc,
            }
        )