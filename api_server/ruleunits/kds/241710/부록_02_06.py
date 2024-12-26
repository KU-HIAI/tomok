import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_02_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 2 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '소요 곡룔연성도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
		(6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 소요 곡룔연성도]
	  B["KDS 24 17 10 부록 2 (6)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:고려하는 방향으로의 단면 최대두께/];
		VarIn2[/입력변수:기둥 형상비의 기준이 되는 기둥길이/];

		VarOut1[/출력변수:소위 변위연성도의 최댓값/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 2 (6)"])
		C --> Variable_def

	  Variable_def--->D---> C

		C([소위 변위연성도의 최대값])
		D["<img src='https://latex.codecogs.com/svg.image?\mu_{\Delta}=\frac{\mu_{\Delta}(0.7&plus;0.75(\frac{h}{L_{s}}))}{0.13(1.1&plus;\frac{h}{L_{s}})}'>---------------------------------"]
    """

    @rule_method
    def required_response_curvature_ductility(fOmuphi,fImudelt,fIh,fIls) -> RuleUnitResult:
        """소요 곡룔연성도

        Args:
            fImudelt (float): 소위 변위연성도
            fIh (float): 고려하는 방향으로의 단면 최대두께
            fIls (float): 기둥 형상비의 기준이 되는 기둥길이

        Returns:
            fOmuphi (float): 교량 내진설계기준(일반설계법) 부록  2. 소요연성도 (6)의 값
        """

        assert isinstance(fImudelt, float)
        assert isinstance(fIh, float)
        assert isinstance(fIls, float)
        assert fIls != 0

        fOmuphi = (fImudelt - 0.5 * (0.7 + 0.75 * (fIh / fIls))) / (0.13 * (1.1 + fIh / fIls))

        return RuleUnitResult(
            result_variables = {
                "fOmuphi": fOmuphi,
            }
        )