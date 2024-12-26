import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_04_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (4) ③'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (4)
    ③
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균인장강도];
    B["KDS 24 14 21 3.1.2.1 (4) ③"];
    A ~~~ B
    end
	  subgraph Variable_def;

		VarIn1[/입력변수: 콘크리트의 평균압축강도/];

 	  VarOut1[/출력변수: 평균인장강도/];

		VarOut1~~~VarIn1

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (4) ③"])
		C --> Variable_def

		Variable_def---->G--->F
		G["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.3(f_{cm})^{2/3}'>--------------------------------------------------------"]
		F(["평균인장강도"]);
    """

    @rule_method
    def Concrete_tensile_strength(fIfcm) -> RuleUnitResult:
        """평균인장강도

        Args:
            fIfcm (float): 콘크리트의 평균압축강도


        Returns:
            fOfctm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4) ③의 값
        """

        assert isinstance(fIfcm, float)


        fOfctm = 0.3 * (fIfcm)**(2/3)

        return RuleUnitResult(
            result_variables = {
                "fOfctm": fOfctm,
          }
        )