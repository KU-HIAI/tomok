import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010403_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '기둥 기초판의 설계뚫림전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기둥 기초판의 설계뚫림전단강도];
    B["KDS 24 14 21 4.1.4.3 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 재료계수/];
		VarIn2[/입력변수: k/];
		VarIn3[/입력변수: 인장철근비/];
		VarIn4[/입력변수: 콘크리트 기준압축강도/];
		VarIn5[/입력변수: 단면의 유효깊이/];
		VarIn6[/입력변수: 기둥면에서부터 검토하는 위험단면까지의 거리/];
		VarIn7[/입력변수: 콘크리트 인장강도/];
		VarOut1[/출력변수: 기둥 기초판의 설계뚫림전단강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.3 (2)"])
		C --> Variable_def

		Variable_def--->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?v&space;_{d}=0.85\phi&space;_c\kappa(100\rho&space;_lf_ck)^{1/3}\frac{2d}{\alpha}\geq&space;0.4\phi&space;_cf_{ctk}\frac{2d}{a};'>---------------------------------"]
		E(["기둥 기초판의 설계뚫림전단강도"])
    """

    @rule_method
    def Design_penetration_shear_strength_of_column_base_plate(fIphic,fIk,fIrhol,fIfck,fId,fIa,fIfctk) -> RuleUnitResult:
        """기둥 기초판의 설계뚫림전단강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIk (float): 단면 유효깊이에 의해 결정되는 계수
            fIrhol (float): 인장철근비
            fIfck (float): 콘크리트 기준압축강도
            fId (float): 단면의 유효깊이
            fIa (float): 기둥면에서부터 검토하는 위험단면까지의 거리
            fIfctk (float): 콘크리트 인장강도

        Returns:
            fOvd (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (2)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (2)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIk, float)
        assert isinstance(fIrhol, float)
        assert isinstance(fIfck, float)
        assert isinstance(fId, float)
        assert isinstance(fIa, float)
        assert isinstance(fIfctk, float)

        fOvd = 0.85 * fIphic * fIk * (100 * fIrhol * fIfck)**(1/3) * 2 * fId / fIa

        if fOvd >= 0.4 * fIphic * fIfctk * 2 * fId / fIa :
          return RuleUnitResult(
              result_variables = {
                  "fOvd": fOvd,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOvd": fOvd,
                  "pass_fail": False,
              }
          )