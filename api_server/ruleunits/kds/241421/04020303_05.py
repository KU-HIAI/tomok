import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020303_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.3 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '2축 응력 상태의 거더 복부의 유효인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.3 간접 균열 제어
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 2축 응력 상태의 거더 복부의 유효인장강도];
    B["KDS 24 14 21 4.2.3.3 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 주압축응력/];
		VarIn2[/입력변수: 콘크리트의 기준압축강도/];
		VarIn3[/입력변수: 콘크리트 하위 0.5 분위 기준인장강도/];
		VarOut1[/출력변수: 거더 복부의 유효인장강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.3 (5)"])
		C --> Variable_def

		Variable_def--->D--->E--->F
		D["<img src='https://latex.codecogs.com/svg.image?f_{2}\leq&space;0.6f_{ck}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?f_{cte}=(1-0.8\frac{f_2}{f_{ck}})f_{ctk}'>---------------------------------"]

		F(["거더 복부의 유효인장강도"])
    """

    @rule_method
    def Effective_tensile_strength_of_girders_abdominal_under_biaxial_stress(fIfone,fIftwo,fIfck,fIfctk) -> RuleUnitResult:
        """2축 응력 상태의 거더 복부의 유효인장강도

        Args:
            fIfone (float): 주인장응력
            fIftwo (float): 주압축응력
            fIfck (float): 콘크리트의 기준압축강도
            fIfctk (float): 콘크리트 하위 0.5 분위 기준인장강도

        Returns:
            fOfcte (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (5)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (5)의 판단 결과 1
            sOfcteA (string): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (5)의 판단 결과 2
            sOfcteB (string): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (5)의 판단 결과 3
        """

        assert isinstance(fIfone, float)
        assert isinstance(fIftwo, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIfctk, float)

        if fIftwo <= 0.6*fIfck :
          fOfcte = (1 - 0.8 * fIftwo / fIfck) * fIfctk
          if fIfone < fOfcte :
            return RuleUnitResult(
                result_variables = {
                    "fOfcte": fOfcte,
                    "sOfcteA": "비균열 상태",
                    "pass_fail": True,
                }
            )
          elif fIfone > fOfcte :
            return RuleUnitResult(
                result_variables = {
                    "fOfcte": fOfcte,
                    "sOfcteB": "복부 균열이 발생한 상태",
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )