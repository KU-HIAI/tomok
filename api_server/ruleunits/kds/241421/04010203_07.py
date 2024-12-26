import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010203_07(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.3 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '추가 인장력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 추가 인장력];
    B["KDS 24 14 21 4.1.2.3 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 추가 인장력/];
		VarIn1[/입력변수: 작용하는계수하중에의한단면전단력/];
		VarIn2[/입력변수: 부재 복부에 형성된 스트럿의 경사각/];
		VarIn3[/입력변수: 경사전단철근과 주인장철근 사이의 경사각/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.3 (7)"])
		C --> Variable_def

		Variable_def--->L--->K

		L["<img src='https://latex.codecogs.com/svg.image?\Delta&space;T=0.5V_u(cot\theta-cot\alpha)'>---------------------------------"]

		K(["추가 인장력"])
    """

    @rule_method
    def additional_tensile_force(fIVu,fItheta,fIalpha) -> RuleUnitResult:
        """추가 인장력

        Args:
            fIVu (float): 작용하는 계수하중에 의한 단면전단력
            fItheta (float): 부재 복부에 형성된 스트럿의 경사각
            fIalpha (float): 경사전단철근과 주인장철근 사이의 경사각

        Returns:
            fOdeltaT (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.3 전단보강철근이 배치된 부재 (7)의 값
        """

        assert isinstance(fIVu, float)
        assert isinstance(fItheta, float)
        assert fItheta != 0
        assert isinstance(fIalpha, float)
        assert fIalpha != 0

        import math

        fOdeltaT = 0.5 * fIVu * ( 1/math.tan(math.radians(fItheta)) - 1/math.tan(math.radians(fIalpha)))

        return RuleUnitResult(
            result_variables = {
                "fOdeltaT": fOdeltaT,
            }
        )