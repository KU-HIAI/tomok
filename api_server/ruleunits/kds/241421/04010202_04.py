import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010202_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.2 전단보강철근이 없는 부재
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계전단강도];
    B["KDS 24 14 21 4.1.2.2 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 설계전단강도/];
		VarOut2[/출력변수: 최소설계전단강도/];
		VarOut3[/출력변수: 절대건조밀도에 따른 전단강도 보정계수/];
		VarIn1[/입력변수: 콘크리트의 재료계수/];
		VarIn2[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn3[/입력변수: 주인장 철근비/];
		VarIn4[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
		VarIn5[/입력변수: 축응력/];
		VarIn6[/입력변수: 단면의 복부폭/];
		VarIn7[/입력변수: 단면의 유효깊이/];
		VarIn8[/입력변수: 콘크리트 하위 0.05분위 기준인장강도/];
		VarIn9[/입력변수: 절대건조 밀도/];

		VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6 ~~~ VarIn7 & VarIn8 & VarIn9

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.2 (4)"])
		C --> Variable_def

		Variable_def--->E--->D
		Variable_def--->F
		E["<img src='https://latex.codecogs.com/svg.image?\eta&space;_{1}=0.4&plus;0.6\gamma&space;_{g}/2200'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?V_{cd,min}=(0.35\eta&space;_{1}\phi&space;_{c}f_{ctk}&plus;0.15f_{n})b_{w}d'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?V_{cd}=[0.7\eta&space;_{1}\phi&space;_{c}\kappa(\rho&space;f_{ck})^{1/3}&plus;0.15f_{n}]b_{w}d'>---------------------------------"]

		D & F--->G
		G(["설계전단강도"])
    """

    @rule_method
    def design_shear_strength(fIphic,fIk,fIrho,fIfck,fIfn,fIbw,fId,fIfctk,fIgammag) -> RuleUnitResult:
        """설계전단강도

        Args:
            fIphic (float): 콘크리트의 재료계수
            fIk (float): 유효깊이 변화에 따른 전단강도 보정계수
            fIrho (float): 주인장 철근비
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도
            fIfn (float): 축응력
            fIbw (float): 단면의 복부폭
            fId (float): 단면의 유효깊이
            fIfctk (float): 콘크리트 하위 0.05분위 기준인장강도
            fIgammag (float): 절대건조 밀도


        Returns:
            fOVcd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (4)의 값 1
            fOVcdmin (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (4)의 값 2
            fOetal (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (4)의 값 3
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.2 전단보강철근이 없는 부재 (4)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIk, float)
        assert isinstance(fIrho, float)
        assert fIrho > 0
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIfn, float)
        assert isinstance(fIbw, float)
        assert isinstance(fId, float)
        assert isinstance(fIfctk, float)
        assert isinstance(fIgammag, float)

        fOetal = 0.4 + 0.6 * fIgammag / 2200
        fOVcdmin = (0.35 * fOetal * fIphic * fIfctk + 0.15 * fIfn) * fIbw * fId
        fOVcd = (0.7 * fOetal * fIphic * fIk * (fIrho * fIfck)**(1/3) + 0.15 * fIfn) * fIbw * fId

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
                  "pass_fail": False,
              }
          )