import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020302_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '최소 철근 감소량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.2 최소철근량
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소 철근 감소량];
    B["KDS 24 14 21 4.2.3.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 프리스트레스 긴장재의 단면적/];
		VarIn2[/입력변수: 철근과 긴장재의 부착특성 및 지름의 차이에 따른 영향을 반영하기 위한 계수/];
		VarIn3[/입력변수: 철근과 프리스트레싱 강재의 부착강도 비/];
		VarIn4[/입력변수: 철근 지름/];
		VarIn5[/입력변수: 프리스트레싱 강재의 등가지름/];
		VarIn6[/입력변수: 프리스트레싱 강재의 면적/];
		VarIn7[/입력변수: 연선의 지름/];
		VarOut1[/출력변수: 최소 철근 감소량/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5  & VarIn6 & VarIn7
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.2 (3)"])
		C --> Variable_def

		Variable_def--->D
		Variable_def--철근은 사용되지 않고 프리스트레싱 강재만 사용된 경우--->L
		L["<img src='https://quicklatex.com/cache3/3d/ql_f541c74dbd6864a2ccfb0dc283bc653d_l3.png'>---------------------------------"]
		D--다발 프리스트레싱 강재--->F
		D{"<img src='https://latex.codecogs.com/svg.image?d_{p,eq}'>---------------------------------"}
		D--7연선 1가닥--->G
		D--3연선 1가닥--->H
		F["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.6\sqrt{A_p}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.75d_{wire}'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?d_{p,eq}=1.2d_{wire}'>---------------------------------"]
		I["<img src='https://quicklatex.com/cache3/f3/ql_0a2a6ee5d956bcd187cb8bfdf13a07f3_l3.png'>---------------------------------"]
		F & G & H--->I
		I~~~|table 24 14 21 4.2-3|I
		L--->J
		I--->J--->K
		J["<img src='https://quicklatex.com/cache3/25/ql_40f741d3c69c715f84195efa89b00625_l3.png'>---------------------------------"]
		K(["최소 철근 감소량"])
    """

    @rule_method
    def Minimum_reinforcement_reduction(fIdpeqA,fIdpeqB,fIdpeqC,fIAp,fIxi,fIdb,fIdwire) -> RuleUnitResult:
        """최소 철근 감소량

        Args:
            fIdpeqA (float): 프리스트레싱 강재의 등가지름 (다발 프시스트레싱 강재)
            fIdpeqB (float): 프리스트레싱 강재의 등가지름 (7연선 1가닥)
            fIdpeqC (float): 프리스트레싱 강재의 등가지름 (3연선 1가닥)
            fIAp (float): 프리스트레스 긴장재의 단면적
            fIxi (float): 철근과 프리스트레싱 강재의 부착강도 비
            fIdb (float): 철근 지름
            fIdwire (float): 연선의 지름

        Returns:
            fOmirere (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (3)의 값 1
            fOxi1 (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (3)의 값 2
            fOdpeq (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.2 최소철근량 (3)의 값 3
        """

        assert isinstance(fIAp, float)
        assert fIAp > 0
        assert isinstance(fIxi, float)
        assert fIxi > 0
        assert isinstance(fIdb, float)
        assert fIdb > 0
        assert isinstance(fIdwire, float)
        assert fIdwire > 0

        if fIdb != 0 :
          if fIdpeqA != 0 and fIdpeqB == 0 and fIdpeqC == 0 :
            fOdpeq = 1.6 * (fIAp**0.5)
            fOxi1 = (fIxi * fIdb / fOdpeq)**0.5

          if fIdpeqA == 0 and fIdpeqB != 0 and fIdpeqC == 0 :
            fOdpeq = 1.75 * fIdwire
            fOxi1 = (fIxi * fIdb / fOdpeq)**0.5

          else:
            fOdpeq = 1.20 * fIdwire
            fOxi1 = (fIxi * fIdb / fOdpeq)**0.5

          fOmirere = fOxi1 * fIAp

          return RuleUnitResult(
              result_variables = {
                  "fOmirere": fOmirere,
              }
          )

        else:

          fOxi1 = fIxi**0.5
          fOmirere = fOxi1 * fIAp

          return RuleUnitResult(
             result_variables = {
                  "fOmirere": fOmirere,
              }
          )