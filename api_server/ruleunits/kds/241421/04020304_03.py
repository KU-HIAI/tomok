import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020304_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '최종 균열의 최대 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최종 균열의 최대 간격];
    B["KDS 24 14 21 4.2.3.4 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 강재의 중심 간격/];
		VarIn2[/입력변수: 최외단 인장철근이나 긴장재의 표면과 콘크리트 표면 사이의 최소피복두께/];
		VarIn3[/입력변수: 부착강도에 따른 계수/];
		VarIn4[/입력변수: 부재의 하중작용에 따른 계수/];
		VarIn5[/입력변수: 콘크리트의 유효인장면적을 기준으로 한 강재비/];
		VarIn6[/입력변수: 철근콘크리트나 긴장재와 철근이 같이 사용된 프리스트레스트 콘크리트의 경우에는 가장 큰 인장철근의 지름을, 긴장재만 사용된 프리스트레스트콘크리트의 경우에는 프리스트레싱강재의 등가지름 d_{p,eq}/];
		VarIn7[/입력변수: 단면의 깊이/];
		VarIn8[/입력변수: 중립축 깊이/];
		VarOut1[/출력변수: 최종 균열의 최대 간격/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5 ~~~ VarIn6
		VarIn7~~~VarIn8
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.4 (3)"])
		C --> Variable_def

		Variable_def--->F
		F{"강재의 중심간격 ≤<img src='https://latex.codecogs.com/svg.image?\leq&space;5(c_c&plus;d_b/2)'>---------------------------------"}
		D["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=3.4c_c&plus;\frac{0.425k_1k_2d_b}{\rho&space;_e}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=1.3(h-c)'>---------------------------------"]
		F--yes-->D
		F--No-->E
		D & E--->G
		G(["최종 균열의 최대 간격"])
    """

    @rule_method
    def maximum_spacing_of_final_cracks(fIcensst,fIcc,fIk1,fIk2,fIrhoe,fIdb,fIh,fIc) -> RuleUnitResult:
        """최종 균열의 최대 간격

        Args:
            fIcensst (float): 강재의 중심 간격
            fIcc (float): 최외단 인장철근이나 긴장재의 표면과 콘크리트 표면 사이의 최소피복두께
            fIk1 (float): 부착강도에 따른 계수
            fIk2 (float): 부재의 하중작용에 따른 계수
            fIrhoe (float): 콘크리트의 유효인장면적을 기준으로 한 강재비
            fIdb (float): 철근콘크리트나 긴장재와 철근이 같이 사용된 프리스트레스트 콘크리트의 경우에는 가장 큰 인장철근의 지름을, 긴장재만 사용된 프리스트레스트콘크리트의 경우에는 프리스트레싱강재의 등가지름 d_{p,eq}
            fIh (float): 단면의 깊이
            fIc (float): 중립축 깊이

        Returns:
            fOmaxspc (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (3)의 값
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (3)의 판단 결과
        """

        assert isinstance(fIcensst, float)
        assert isinstance(fIcc, float)
        assert isinstance(fIk1, float)
        assert isinstance(fIk2, float)
        assert isinstance(fIrhoe, float)
        assert isinstance(fIdb, float)
        assert isinstance(fIh, float)
        assert isinstance(fIc, float)

        if fIk1 == (0.8 or 1.6) and fIk2 == (0.5 or 1.0) :
          if fIcensst <= 5 * (fIcc + fIdb / 2):
           fOmaxspc = 3.4 * fIcc + 0.425 * fIk1 * fIk2 * fIdb / fIrhoe
          else:
           fOmaxspc = 1.3 * (fIh - fIc)

          return RuleUnitResult(
              result_variables = {
                  "fOmaxspc": fOmaxspc,
                  "pass_fail": True
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False
              }
          )