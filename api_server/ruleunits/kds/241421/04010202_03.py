import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010202_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 최대설계전단강도/];
		VarIn2[/입력변수: 도콘크리트의 재료계수/];
		VarIn3[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn4[/입력변수: 주인장 철근비/];
		VarIn5[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn6[/입력변수: 단면의 유효깊이/];
		VarIn7[/입력변수: 받침점 내면으로부터의 거리/];
		VarIn8[/입력변수: 축응력/];
		VarIn9[/입력변수: 단면의 복부폭/];
		VarIn10[/입력변수: 콘크리트 압축강도 유효계수/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.2 (3)"])
		C --> Variable_def

		Variable_def--->H--->D
		Variable_def--->E

		H["<img src='https://quicklatex.com/cache3/ab/ql_b4f38ae0068e05c894b6e710c36223ab_l3.png'>---------------------------------"]

		D["<img src='https://quicklatex.com/cache3/4e/ql_b1289fbc8cf4f8a9bd2110158381674e_l3.png'>---------------------------------"]

		E["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.85\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}(\frac{2d}{x})&plus;0.15f_{n}]b_{w}d'>---------------------------------"]
		F{"<img src='https://latex.codecogs.com/svg.image?V_{cd}\leq&space;V_{cd,max}'>---------------------------------"}

		E & D--->F--->G
		G(["설계전단강도"])
    """

    @rule_method
    def design_shear_strength(fIphic,fIk,fIfck,fIrho,fId,fIx,fIfn,fIbw) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIphic (float): 콘크리트의 재료계수
            fIk (float): 유효깊이 변화에 따른 전단강도 보정계수
            fIfck (float): 주인장 철근비
            fIrho (float): 28일 콘크리트 공시체의 기준압축강도
            fId (float): 단면의 유효깊이
            fIx (float): 받침점 내면으로부터의 거리
            fIfn (float): 축응력
            fIbw (float): 단면의 복부폭


        Returns:
            fOVcd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (3)의 값 1
            fOnu (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (3)의 값 2
            fOVcdmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (3)의 값 3
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (3)의 판단 결과 1
            desc (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (3)의 판단 결과 2
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIk, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIrho, float)
        assert fIrho > 0
        assert isinstance(fId, float)
        assert isinstance(fIx, float)
        assert fIx != 0
        assert isinstance(fIfn, float)
        assert isinstance(fIbw, float)

        fOnu = 0.6 * (1 - fIfck / 250)

        if 0.5 * fId <= fIx < 2 * fId :
          fOVcd = ((0.85 * fIphic * fIk * (fIrho * fIfck)**(1/3)) * (2 * fId / fIx) + 0.15 * fIfn) * fIbw * fId
          fOVcdmax = 0.5 * fIphic * fOnu * fIfck * fIbw * fId
          if fOVcd <= fOVcdmax :
            return RuleUnitResult(
                result_variables = {
                    "fOVcd": fOVcd,
                    "fOnu": fOnu,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "fOVcdmax": fOVcdmax,
                    "fOnu": fOnu,
                    "pass_fail": False,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOnu": fOnu,
                  "desc": "전단강도 검토조건에 해당하지 않으므로 콘크리트 압축강도 유효계수만 계산되었음",
              }
          )