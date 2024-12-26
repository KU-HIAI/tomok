import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균압축강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균압축강도];
    B["KDS 24 14 21 3.1.2.1 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 쪼갬 인장강도의 평균값/];
		VarIn2[/입력변수: 휨인장강도의 평균값/];
		VarIn3[/입력변수: 콘크리트의 평균압축강도/];
		VarIn4[/입력변수: 강도 보정 계수/];
		VarIn5[/입력변수: α/];
		VarIn6[/재령 28일 평균인장강도/];
		VarIn7[/평균인장강도/];
 	  VarOut1[/출력변수: 평균인장강도/];
		VarOut2[/출력변수: 기준인장강도/];
		VarOut3[/출력변수: 재령에서의 콘크리트 인장강도/];

	  VarOut1 ~~~VarIn1
		VarOut1 ~~~VarIn2
		VarOut1~~~VarIn3
	  VarOut2~~~VarIn7
  	VarOut3~~~VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (4)"])
		C --> Variable_def

		Variable_def---->D--->F
		Variable_def---->E--->F
		Variable_def---->G--->F
		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.9f_{spm'>--------------------------------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.5f_{rm'>--------------------------------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.3(f_{cm})^{3/2'>--------------------------------------------------------"]
		F(["평균인장강도"]);
		I(["콘크리트의 기준인장강도"]);
		H["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctk}=0.7f_{ctm}'>--------------------------------------------------------"]
		Variable_def---->H--->I
		J["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}(t)=[\beta_{cc}(t)]^{\alpha}f_{ctm}'>--------------------------------------------------------"]
		Variable_def---->J--->K
		K(["재령에서의 콘크리트 인장강도"])
    """

    @rule_method
    def Concrete_tensile_strength(fIfctmA,fIfctmB,fIfctmC,fIfspm,fIfrm,fIfcm,fIbetacc,fIt,fIalpha,fIfctm) -> RuleUnitResult:
        """평균인장강도

        Args:
            fIfctmA (float): 평균인장강도 (쪼갬 인장강도의 평균값으로 인장강도를 결정할 경우)
            fIfctmB (float): 평균인장강도 (휨인장강도의 평균값으로 인장강도를 결정할 경우)
            fIfctmC (float): 평균인장강도 (콘크리트의 인장시험 결과가 없는 경우)
            fIfspm (float): 쪼갬 인장강도의 평균값
            fIfrm (float): 휨인장강도의 평균
            fIfcm (float): 콘크리트의 평균압축강도
            fIbetacc (float): 강도 보정 계수
            fIt (float): 콘크리트의 재령
            fIalpha (float): t가 28일 미만이면 1, t가 28일 이상이면 2/3
            fIfctm (float): 재령 28일 평균인장강도

        Returns:
            fOfctm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4)의 값 1
            fOfctk (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4)의 값 2
            fOfctmt (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4)의 값 3
        """

        assert isinstance(fIfspm, float)
        assert isinstance(fIfrm, float)
        assert isinstance(fIfcm, float)
        assert isinstance(fIbetacc, float)
        assert isinstance(fIt, float)
        assert isinstance(fIalpha, float)
        assert isinstance(fIfctm, float)

        if fIfctmA != 0 and fIfctmB == 0 and fIfctmC == 0 :
          fOfctm = 0.9 * fIfspm
          fOfctk = 0.7 * fOfctm
          fOfctmt = (fIbetacc**fIalpha) * fOfctm
          return RuleUnitResult(
              result_variables = {
                  "fOfctm": fOfctm,
                  "fOfctk": fOfctk,
                  "fOfctmt": fOfctmt,
              }
          )

        if fIfctmA == 0 and fIfctmB != 0 and fIfctmC == 0 :
          fOfctm = 0.9 * fIfspm
          fOfctk = 0.7 * fOfctm
          fOfctmt = (fIbetacc**fIalpha) * fOfctm
          return RuleUnitResult(
              result_variables = {
                  "fOfctm": fOfctm,
                  "fOfctk": fOfctk,
                  "fOfctmt": fOfctmt,
              }
          )

        if fIfctmA == 0 and fIfctmB == 0 and fIfctmC != 0 :
          fOfctm = 0.9 * fIfspm
          fOfctk = 0.7 * fOfctm
          fOfctmt = (fIbetacc**fIalpha) * fOfctm
          return RuleUnitResult(
              result_variables = {
                  "fOfctm": fOfctm,
                  "fOfctk": fOfctk,
                  "fOfctmt": fOfctmt,
              }
          )