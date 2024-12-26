import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010402_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.4.2 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '기성콘크리트말뚝의 허용하중'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.4 말뚝재료의 허용응력
    4.1.4.2 기성콘크리트말뚝
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기성콘크리트 말뚝의 허용하중];
    B["KDS 11 50 15 4.1.4.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 기성콘크리트말뚝의 허용하중/];
    VarIn1[/입력변수: 말뚝 최소단면/] ;
    VarIn2[/입력변수: 설계기준강도/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.4.2 (2)"])
		C --> Variable_def;
		Variable_def-->D
		D["기성콘크리트 말뚝의 허용하중= 말뚝 최소단면X설계기준강도"];
    E(["기성콘크리트 말뚝의 허용하중"]);

    D--->E
    """

    @rule_method
    def allowable_load_of_precast_concrete_pile(fIfck,fIminsep) -> RuleUnitResult:
        """기성콘크리트말뚝의 허용하중

        Args:
            fIfck (float): 설계기준 압축강도
            fIminsep (float): 말뚝의 최소단면

        Returns:
            fOallopc (float): 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (2)의 값
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (2)의 판단 결과
        """

        assert isinstance(fIfck, float)
        assert isinstance(fIminsep, float)

        fOallopc = fIminsep * fIfck

        if fIfck >= 35:
          return RuleUnitResult(
                result_variables = {
                    "fOallopc": fOallopc,
                    "pass_fail": True,
                }
            )
        else:
            return RuleUnitResult(
                result_variables = {
                    "fOallopc": fOallopc,
                    "pass_fail": False,
                }
            )