import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_01040501_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 1.4.5.1 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '하중조합'

    description = """
    교량내진설계기준(한계상태설계법)
    1. 일반사항
    1.4 내진설계의 기본방침
    1.4.5 철도 중요구조물의 내진설계 검토사항
    1.4.5.1 열차 주행의 안전성 검증
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 하중조합];
		B["KDS 24 17 11 1.4.5.1 (4)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 전단지연에 의한 감소계수/];
		VarIn1[/입력변수: 고정하중/];
		VarIn2[/입력변수: 단선활하중/];
		VarIn3[/입력변수: 수평토압/];
		VarIn4[/입력변수: 정수압과 유수압/];
		VarIn5[/입력변수: 부력 또는 양압력/];
		VarIn6[/입력변수: 기초의 설계지진력/];

		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		VarOut ~~~ VarIn3
		VarIn2 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn2 ~~~ VarIn6
		end

		Python_Class ~~~ C(["KDS 24 17 11 1.4.5.1 (4)"])
		C --> Variable_def

		E["<img src='https://latex.codecogs.com/svg.image?U=1.0(DW&plus;L/2&plus;EH&plus;(WA&plus;BP)&plus;EQ)'>--------------------------------------------------------------------------------"];

		D(["<img src='https://latex.codecogs.com/svg.image?U'>"])

		Variable_def --> E --> D
    """

    @rule_method
    def load_combination(fIDW,fILover2,fIEH,fIWA,fIBP,fIEQ) -> RuleUnitResult:
        """하중조합

        Args:
            fIDW (float): 고정하중
            fILover2 (float): 단선활하중
            fIEH (float): 수평토압
            fIWA (float): 정수압과 유수압
            fIBP (float): 부력 또는 양압력
            fIEQ (float): 기초의 설계지진력


        Returns:
            fOU (float): 교량내진설계기준(한계상태설계법) 1.4.5.1 열차 주행의 안전성 검증 (4)의 값
        """

        fOU = 1.0 * (fIDW + fILover2 + fIEH + (fIWA + fIBP) + fIEQ)
        return RuleUnitResult(
            result_variables = {
                "fOU": fOU,
            }
        )