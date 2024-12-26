import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060304_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.3.4 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '횡방향철근의 총단면적'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.3 기둥
    4.6.3.4 소성힌지구역에서의 심부구속 횡방향철근량
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 횡방향철근의 총단면적]
	  B["KDS 24 17 11 4.6.3.4 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 횡방향철근의 총단면적/]
	  VarIn1[/입력변수: 띠철근의 수직간격/]
	  VarIn2[/입력변수: 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 신부의 단면 치수/]
	  VarIn3[/입력변수: 나선철근 외측표면을 기준으로 한 기둥 심부의 면적/]
	  VarIn4[/입력변수: 기둥의 총단면적/]
	  VarIn5[/입력변수: 콘크리트의 설계기준 압축강도/]
	  VarIn6[/입력변수: 횡방향철근의 설계기준 항복강도/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5 & VarIn6
	  end
	  Python_Class ~~~ C(["KDS 24 17 11 4.6.3.4 (4)"])
		C --> Variable_def---> H ---> G
	  G(["<img src='https://latex.codecogs.com/svg.image?&space;A_{sh}'>"])
	  H["Ash=<img src='https://latex.codecogs.com/svg.image?MAX(0.30ah_c\frac{f_{ck}}{f_{yh}}(\frac{A_h}{A_c}-1),0.12ah_c\frac{f_{ck}}{f_{yh}})'>-----------------------------------------------------------"]
    """

    @rule_method
    def gross_cross_sectional_area_transverse_rebar(fIa,fIhc,fIAc,fIAg,fIfck,fIfyh) -> RuleUnitResult:
        """횡방향철근의 총단면적

        Args:
            fIa (float): 띠철근의 수직간격
            fIhc (float): 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 신부의 단면 치수
            fIAc (float): 나선철근 외측표면을 기준으로 한 기둥 심부의 면적
            fIAg (float): 기둥의 총단면적
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도

        Returns:
            fOAsh (float): 교량내진설계기준(한계상태설계법) 4.6.3.4 소성힌지구역에서의 심부구속 횡방향철근량 (4)의 값
        """

        assert isinstance(fIa, float)
        assert isinstance(fIhc, float)
        assert isinstance(fIAc, float)
        assert isinstance(fIAg, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIfyh, float)

        fOAsh = max(0.30 * fIa * fIhc * fIfck / fIfyh * (fIAg / fIAc - 1), 0.12 * fIa * fIhc * fIfck / fIfyh)
        return RuleUnitResult(
            result_variables = {
                "fOAsh": fOAsh,
            }
        )