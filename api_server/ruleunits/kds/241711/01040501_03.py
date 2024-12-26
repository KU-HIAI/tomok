import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_01040501_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 1.4.5.1 (3)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-19'
    title = '지진의 재현주기'

    description = """
    교량내진설계기준(한계상태설계법)
    1. 일반사항
    1.4 내진설계의 기본방침
    1.4.5 철도 중요구조물의 내진설계 검토사항
    1.4.5.1 열차 주행의 안전성 검증
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지진의 재현주기] ;
		B["KDS 24 17 11 1.4.5.1 (3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 지진의 재현주기/] ;
		end

		Python_Class ~~~ C(["KDS 24 12 21 4.3.1.1 (1)"])
		C --> Variable_def

		E["지진의 재현주기"] ;

		D([100년])

		Variable_def --> E --> D
    """

    @rule_method
    def earthquake_cycle(fOEarcyc) -> RuleUnitResult:
        """지진의 재현주기

        Args:
            fOEarcyc (float): 지진의 재현주기

        Returns:
            fOEarcyc (float): 교량내진설계기준(한계상태설계법) 1.4.5.1 열차 주행의 안전성 검증 (3)의 값
        """

        fOEarcyc = 100
        return RuleUnitResult(
            result_variables = {
                "fOEarcyc": fOEarcyc,
            }
        )