import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060205_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.2.5 (3)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-15'
    title = '기초의 설계지진력'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.5 교각의 최대 소성힌지력
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 기초의 설계지진력]
	  B["KDS 24 17 11 4.6.2.5 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 기초의 설계지진력/]
	  VarIn1[/입력변수: 교각의 최대 소성 힌지력/]
	  VarIn2[/입력변수: 응답수정계수를 적용하지 않은 탄성지지력/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.2.5 (3)"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["확대기초, 말뚝머리 및 말뚝을 포함하는 기초의 설계 지진력 = min(교각의 최대소성 힌지력, 응답계수를 적용하지않은 탄성지진력)"]
	  E([기초의 설계 지진력])
    """

    @rule_method
    def design_seismic_force_foundation(fImaphfp,fIebcwoR) -> RuleUnitResult:
        """기초의 설계지진력

        Args:
            fImaphfp (float): 교각의 최대 소성힌지력
            fIebcwoR (float): 응답수정계수를 적용하지 않은 탄성지지력

        Returns:
            fOdesfof (float): 교량내진설계기준(한계상태설계법) 4.6.2.5 교각의 최대 소성힌지력 (3)의 값
        """

        assert isinstance(fImaphfp, float)
        assert isinstance(fIebcwoR, float)

        fOdesfof = min(fImaphfp,fIebcwoR)

        return RuleUnitResult(
            result_variables = {
                "fOdesfof": fOdesfof,
                }
            )