import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060205_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.2.5 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-15'
    title = '설계전단력'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.5 교각의 최대 소성힌지력
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계전단력]
	  B["KDS 24 17 11 4.6.2.5(2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 설계전단력/]
	  VarIn1[/입력변수: 응답수정계수/]
	  VarIn2[/입력변수: 탄성전단력/]
	  VarIn3[/입력변수: 교각의 최대 소성 힌지력/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.2.5(2)"])
		C --> Variable_def

	  Variable_def --> E --> F --> D --> G

	  D["설계전단력= min(탄성전단력, 교각의 최대 소성 힌지력)"]
	  E{"응답수정계수 1.0"}
	  F["탄성전단력"]
	  G(["설계전단력"])
    """

    @rule_method
    def design_shear_force(fOdeshfo,fIelshfo,fImphfop) -> RuleUnitResult:
        """설계전단력

        Args:
            fOdeshfo (float): 설계전단력
            fIelshfo (float): 탄성전단력
            fImphfop (float): 교각의 최대 소성힌지력

        Returns:
            fOdeshfo (float): 교량내진설계기준(한계상태설계법) 4.6.2.5 교각의 최대 소성힌지력 (2)의 값
        """

        assert isinstance(fIelshfo, float)
        assert isinstance(fImphfop, float)

        fOdeshfo = min(fIelshfo,fImphfop)

        return RuleUnitResult(
            result_variables = {
                "fOdeshfo": fOdeshfo,
                }
            )