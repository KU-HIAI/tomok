import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_04_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '설계전단력'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 설계전단력]
	  B["KDS 24 17 10 부록 4 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:교각의 최대 소성힌지력/];
		VarIn2[/입력변수: 탄성전단력/];

		VarOut1[/출력변수: 설계전단력/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 4 (2)"])
		C --> Variable_def

	  Variable_def--->E--->F

		E["설계전단력=Min(탄성전단력, 교각의 최대 소성힌지력) "]
		E~~~ |"KDS 24 17 10 2.1(4)"| E

		F(["설계전단력"])
    """

    @rule_method
    def Design_shear_force(fImaxpla,fIelshro) -> RuleUnitResult:
        """설계전단력

        Args:
            fImaxpla (float): 교각의 최대 소성힌지력
            fIelshro (float): 탄성전단력

        Returns:
            fOshforc (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (2)의 값
        """

        assert isinstance(fImaxpla, float)
        assert isinstance(fIelshro, float)

        fOshforc = min(fImaxpla,fIelshro)

        return RuleUnitResult(
            result_variables = {
                "fOshforc": fOshforc,
            }
        )