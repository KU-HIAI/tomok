import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050602_08(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.6.2 (8)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '휨강성'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.6 장주 효과
    1.5.6.2 모멘트 확대계수법의 적용
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 휨강성];
    B["KDS 24 14 21 1.5.6.2 (8)"];
    A ~~~ B
    end
	  subgraph Variable_def
	  VarOut1[/출력변수 : 휨강성/];
	  VarIn1[/입력변수 : 콘크리트의 탄성계수/];
	  VarIn2[/입력변수 : 도심축에 대한 콘크리트 총단면의 단면2차모멘트/];
	  VarIn3[/입력변수 : 종방향 철근의 탄성계수/];
	  VarIn4[/입력변수 : 도심축에 대한 종방향 철근의 단면2차모멘트/];
	  VarIn5[/입력변수 : 횡구속 골조에서 최대 계수축력에 대한 최대계수지속축력의 비/];

	  VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5

	  end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.6.2 (8)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/png.image?max\left ( EI=\frac{\left ( 0.2E_{c}I{g} + E_{s}I{s} \right ))}{1+\ beta _{d}}, EI=\frac{0.4E_{c}I{g}}{1+\beta _{d}} \right )'>-------------------"];
	  Variable_def --> D --> E["휨강성"]
    """

    @rule_method
    def flexural_stiffness(fIEc,fIIg,fIEs,fIls,fIbetad) -> RuleUnitResult:
        """휨강성

        Args:
            fIEc (float) : 콘크리트의 탄성계수
            fIIg (float) : 도심축에 대한 콘크리트 총단면의 단면2차모멘트
            fIEs (float) : 종방향 철근의 탄성계수
            fIls (float) : 도심축에 대한 종방향 철근의 단면2차모멘트
            fIbetad (float) : 횡구속 골조에서 최대 계수축력에 대한 최대계수지속축력의 비

        Returns:
            fOEI (float): 콘크리트교 설계기준 (한계상태설계법) 1.5.6.2 모멘트 확대계수법의 적용 (8)의 값
        """

        assert isinstance(fIEc, float)
        assert isinstance(fIIg, float)
        assert isinstance(fIEs, float)
        assert isinstance(fIls, float)
        assert isinstance(fIbetad, float)
        assert fIbetad > 0

        fOEI = max((0.2 * fIEc * fIIg + fIEs * fIls) / (1 + fIbetad), 0.4 * fIEc * fIIg / (1 + fIbetad))
        return RuleUnitResult(
            result_variables = {
                "fOEI": fOEI,
                }
            )