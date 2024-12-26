import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010202_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarIn1[/입력변수: 최소설계전단강도/];
		VarIn2[/입력변수: 콘크리트 재료계수/];
		VarIn3[/입력변수: 콘크리트 기준압축강도/];
		VarIn4[/입력변수: 콘크리트 인장강도/];
		VarIn5[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn6[/입력변수: 단면유효깊이/];
		VarIn7[/입력변수: 철근비/];
		VarIn8[/입력변수: 단면의 복부폭/];
		VarIn9[/입력변수: 주인장 철근량/];
		VarIn10[/입력변수: 축응력/];
		VarIn11[/입력변수: 축력/];
		VarIn12[/입력변수: 철근비/];
		VarIn13[/입력변수: 단면적/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.2 (1)"])
		C --> Variable_def

		Variable_def--->E--->D

		E["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.85\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}&plus;0.15f_{n}]b_{w}d'>---------------------------------"]
		D(["설계전단강도"])
    """

    @rule_method
    def design_shear_strength_shearing_free_member(fIphic,fIfck,fIfctk,fId,fIAs,fIbw,fINu,fIAc) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIfck (float): 콘크리트 기준압축강도
            fIfctk (float): 콘크리트 인장강도
            fId (float): 단면유효깊이
            fIAs (float): 주인장 철근량
            fIbw (float): 단면의 복부폭
            fINu (float): 축력
            fIAc (float): 단면적

        Returns:
            fOVcd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 값 1
            fOk (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 값 2
            fOrho (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 값 3
            fOfn (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 값 4
            fOVcdmin (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 값 5
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (1)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIfctk, float)
        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIAs, float)
        assert fIAs > 0
        assert isinstance(fIbw, float)
        assert fIbw > 0
        assert isinstance(fINu, float)
        assert isinstance(fIAc, float)
        assert fIAc != 0

        fOk = 1 + (200 / fId)**0.5
        fOrho = fIAs / (fIbw * fId)
        fOfn = fINu / fIAc

        fOVcdmin = (0.4 * fIphic * fIfctk + 0.15 * fOfn) * fIbw * fId / 1000
        fOVcd = (0.85 * fIphic * fOk * (fOrho * fIfck)**(1/3) + 0.15 * fOfn) * fIbw * fId / 1000

        if fOk <= 0.02 and fOrho <= 0.02 and fOfn <= 0.2 * fIphic * fIfck :
          if fOVcd >= fOVcdmin :
            return RuleUnitResult(
                result_variables = {
                    "fOVcd": fOVcd,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "fOVcdmin": fOVcdmin,
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )