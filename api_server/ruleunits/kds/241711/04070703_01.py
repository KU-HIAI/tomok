import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070703_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.3 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-13'
    title = '등가정적 지진하중의 단위길이 당 하중강도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.3 단일모드스펙트럼해석법
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 등가정적 지진하중의 단위길이 당 하중강도];
	  B["KDS 24 17 11 4.7.7.3(1)"];
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 등가정적 지진하중의 단위길이당 하중강도/];
	  VarIn1[/입력변수: 상부구조의 단위길이당 고정하중/];
	  VarIn2[/입력변수: 탄성지진응답계수/];
	  VarOut ~~~ VarIn1 & VarIn2
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.3(1)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?p_e(x)=w(x)C_s'>-----------------------------------------"];

	  E(["<img src='https://latex.codecogs.com/svg.image?p_e(x)'>"]);

	  Variable_def --> D --> E
    """

    @rule_method
    def Load_intensity_per_unit_length_of_equivlent_static_seismic_load(fIwx,fICs) -> RuleUnitResult:
        """등가정적 지진하중의 단위길이 당 하중강도

        Args:
            fIwx (float): 상부구조의 단위길이 당 고정하중
            fICs (float): 탄성지진응답계수

        Returns:
            fOpex (float): 교량내진설계기준(한계상태설계법) 4.7.7.3 단일모드스펙트럼해석법 (1)의 값
        """

        assert isinstance(fIwx, float)
        assert isinstance(fICs, float)

        fOpex = fIwx * fICs
        return RuleUnitResult(
            result_variables = {
                "fOpex": fOpex,
            }
        )