import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.2.2 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '항복유효 단면2차모멘트'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.2 교각의 휨강성
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 항복유효 단면2차모멘트]
	  B["KDS 24 17 11 4.6.2.2 (2)"]
	  A ~~~ B
	  end
	  subgraph Variable_def
	  VarOut[/출력변수: 항복유효 단면2차모멘트/]
	  VarIn1[/입력변수: 교각의 총단면적/]
	  VarIn2[/입력변수: 콘크리트의 설계기준압축강도/]
	  VarIn3[/입력변수: 철근을 무시한 교각 전체 단면의 중심축에 대한 단면2차모멘트/]
	  VarIn4[/입력변수: 계수 축력/]
	  VarIn5[/입력변수: 교각의 축방향철근비/]
	  VarOut ~~~ VarIn1 & VarIn3
	  VarIn1 & VarIn3 ~~~ VarIn2 & VarIn4 & VarIn5
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.2.2 (2)"])
		C --> Variable_def --> D & F

	  F--> E --> H
	  D --> G
	  D["<img src='https://latex.codecogs.com/svg.image?I_{y,eff}=(0.16&plus;12\rho&space;_l&plus;0.3\sqrt{\frac{P_u}{f_{ck}A_g}})I_g';width='30'/>--------------------------------------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?EI_y=\frac{M_u}{\psi&space;_u}'------------------------------------>"]
	  F["교각의 축방향철근이 항복할것으로 예상되는 경우"]
	  G(["<img src='https://latex.codecogs.com/svg.image?I_{y,eff}'--------------->"])
	  H(["<img src='https://latex.codecogs.com/svg.image?EI_y'>"])
    """

    @rule_method
    def yield_effective_area_moment_of_inertia(fIAg,fIfck,fIIg,fIPu,fIrhol) -> RuleUnitResult:
        """항복유효 단면2차모멘트

        Args:
            fIAg (float): 교각의 총단면적
            fIfck (float): 콘크리트의 설계기준압축강도
            fIIg (float): 철근을 무시한 교각 전체 단면의 중심축에 대한 단면2차모멘트
            fIPu (float): 계수 축력
            fIrhol (float): 교각의 축방향철근비

        Returns:
            fOIyeff (float): 교량내진설계기준(한계상태설계법) 4.6.2.2 교각의 휨강성 (2)의 값
        """

        assert isinstance(fIAg, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIIg, float)
        assert isinstance(fIPu, float)
        assert isinstance(fIrhol, float)
        assert fIfck > 0
        assert fIAg > 0

        fOIyeff = (0.16 + 12 * fIrhol + 0.3 * ((fIPu / (fIfck * fIAg)) ** 0.5)) * fIIg

        return RuleUnitResult(
            result_variables = {
                "fOIyeff": fOIyeff,
            }
        )