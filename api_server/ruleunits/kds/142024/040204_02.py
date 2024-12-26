import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040204_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.2.4 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '종방향으로 보강된 스트럿의 강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.2 스트럿의 축강도
    4.2.4 철근 효과
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향으로 보강된 스트럿의 강도];
    B["KDS 14 20 24 4.2.4 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut[/출력변수 : 종방향으로 보강된 스트럿의 강도/];
		VarIn1[/입력변수 : 절점영역의 콘크리트 유효압축강도/];
		VarIn2[/입력변수 : 스트럿의 유효단면적/];
		VarIn3[/입력변수 : 철근스트럿의 단면적/];
		VarIn4[/입력변수 : 압축철근의 응력/];
		VarOut ~~~VarIn1~~~VarIn3
		VarOut ~~~VarIn2~~~VarIn4
    end

		Python_Class ~~~ C(["KDS 14 20 24 4.2.4 (2)"])
		C --> Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?f^{,}_{s}'>"];
		E{"설계기준항복강도 ≤500MPa"}--->G["<img src='https://latex.codecogs.com/svg.image?f^{,}_{s}'>=설계기준항복강도"];
		F{"압축철근의 응력으로 스트럿이 압축파괴 될 경우"}--->H["스트럿 변형률로부터 계산"];

		Variable_def--->D
		D--->E
		D--->F

		I["<img src='https://latex.codecogs.com/svg.image?F_{ns}=f_{ce}A_{c}&plus;1.13A^{,}_{s}f^{,}_{s}'>-----------------------------------"];
		G--->I
		H--->I
		I--->J(["종방향으로 보강된 스트럿의 강도"])
    """

    @rule_method
    def strength_of_longitudinally_reinforcedstruts(fIfprims,fIAprims,fIAc,fIfce) -> RuleUnitResult:
        """종방향으로 보강된 스트럿의 강도

        Args:
            fIfprims (float): 압축철근의 응력
            fIAprims (float): 철근스트럿의 단면적
            fIAc (float): 스트럿의 유효단면적
            fIfce (float): 스트럿 또는 절점영역의 콘크리트 유효압축강도

        Returns:
            fOFns (float): 콘크리트구조 스트럿-타이모델 기준  4.2.4 철근 효과 (2)의 값
        """

        assert isinstance(fIfprims, float)
        assert isinstance(fIAprims, float)
        assert isinstance(fIAc, float)
        assert isinstance(fIfce, float)

        fOFns = fIfce * fIAc + 1.13 * fIAprims * fIfprims

        return RuleUnitResult(
              result_variables = {
                  "fOFns": fOFns,
              }
          )