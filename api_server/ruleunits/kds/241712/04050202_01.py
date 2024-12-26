import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04050202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.5.2.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '축력을 고려한 교각의 항복강성'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.2 주탑 및 교각의 휨강성
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 축력을 고려한 교각의 항복강성];
    B["KDS 24 17 12 4.5.2.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 축력을 고려한 교각의 항복강성/];
    VarIn1[/입력변수: 축력을 고려한 교각의 항복모멘트/];
		VarIn2[/입력변수: 축력을 고려한 교각의 항복곡률/];

		VarOut1~~~~ VarIn1 & VarIn2

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.5.2.2 (1)"])
		C --> Variable_def


		D["<img src='https://latex.codecogs.com/svg.image?EI_{y}=\frac{M_{y}}{\phi&space;_{y}}'>--------------------------------------------------------"];

	  Variable_def--->D---> E

		E(["축력을 고려한 교각의 항복강성"]);
    """

    @rule_method
    def Flexural_Strength_of_Pylon_and_Piers(fIMy,fIphiy) -> RuleUnitResult:
        """축력을 고려한 교각의 항복강성

        Args:
            fIMy (float): 축력을 고려한 교각의 항복모멘트
            fIphiy (float): 축력을 고려한 교각의 항복곡률

        Returns:
            fOEIy (bool): 교량내진설계기준(한계상태설계법) 4.5.2.2 주탑 및 교각의 휨강성 (1)의 값
        """

        assert isinstance(fIMy, float)
        assert isinstance(fIphiy, float)

        fOEIy = fIMy / fIphiy
        return RuleUnitResult(
              result_variables = {
                  "fOEIy": fOEIy,
                  }
              )