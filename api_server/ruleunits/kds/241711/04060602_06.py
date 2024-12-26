import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060602_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.2 (6)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '소요 곡률연성도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소요 곡률연성도];
    B["KDS 24 17 11 4.6.6.2 (6)"];
    A ~~~ B
    end

    subgraph Variable_def
	  VarOut[/출력변수: 소요 곡률연성도/]
	  VarIn1[/입력변수: 고려하는 방향으로의 단면 최대두께/]
	  VarIn2[/입력변수: 기둥 형상비의 기준이 되는 기둥길이/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.6.2 (6)"])
		C --> Variable_def

    Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?\mu_\phi=\frac{u_\Delta-0.5\left\{0.7&plus;0.75\left(\frac{h}{L_s}\right)\right\}}{0.13\left(1.1&plus;\frac{h}{L_s}\right)}'>------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?\mu_\phi'>"])
    """

    @rule_method
    def required_curvature_ductility(fImudelt,fIh,fILs) -> RuleUnitResult:
        """소요 곡률연성도

        Args:
            fImudelt (float): 소요 변위연성도
            fIh (float): 고려하는 방향으로의 단면 최대 두께
            fILs (float): 기둥 형상비의 기준이 되는 기둥길이

        Returns:
            fOmuphi (float): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (6)의 값
        """

        assert isinstance(fImudelt, float)
        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fILs, float)
        assert fILs > 0

        fOmuphi = (fImudelt - 0.5 * (0.7 + 0.75 * fIh / fILs))/(0.13 * (1.1 + fIh / fILs))

        return RuleUnitResult(
            result_variables = {
                "fOmuphi": fOmuphi,
            }
        )