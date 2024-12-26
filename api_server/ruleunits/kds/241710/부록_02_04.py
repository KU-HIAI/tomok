import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_02_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '소요 변위연성도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
		(4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 소요 변위연성도]
	  B["KDS 24 17 10 부록 2 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:교량의 주축방향 1차모드 주기/];
		VarIn2[/입력변수:통제주기/];
		VarIn3[/입력변수:소요 응답수정계수/];

		VarOut1[/출력변수:소위 변위연성도/];
		VarOut2[/출력변수:변위연성도-응답수정계수 상관계수/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 2 (4)"])
		C --> Variable_def

	  Variable_def ---> F
		F -- Yes ---> E ---> D
		F -- No ---> G ---> D ---> H

		H([소요 변위연성도])
		D["<img src='https://latex.codecogs.com/svg.image?\mu_{\Delta}=\lambda_{DR}R_{req}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\lambda_{DR}=(1-\frac{1}{R_{req}}\frac{1.25T_{s}}{T}&plus;\frac{1}{R_{req}})'>---------------------------------"]
		F{T ≤ 1.25T_s}
		G["<img src='https://latex.codecogs.com/svg.image?\lambda_{DR}=1'>---------------------------------"]
    """

    @rule_method
    def required_response_displacement_ductility(fIT,fITs,fIRreq) -> RuleUnitResult:
        """소요 변위연성도

        Args:
            fIT (float): 교량의 주축방향 1차모드 주기
            fITs (float): 통제주기
            fIRreq (float): 소요 응답수정계수

        Returns:
            fOmudelt (float): 교량 내진설계기준(일반설계법) 부록  2. 소요연성도 (4)의 값 1
            fOlambDR (float): 교량 내진설계기준(일반설계법) 부록  2. 소요연성도 (4)의 값 2
        """

        assert isinstance(fIT, float)
        assert fIT != 0
        assert isinstance(fITs, float)
        assert isinstance(fIRreq, float)
        assert fIRreq != 0

        if fIT < fITs * 1.25:
          fOlambDR = (1 - 1 / fIRreq) * 1.25 * fITs / fIT + 1 / fIRreq
          fOmudelt = fOlambDR * fIRreq
          return RuleUnitResult(
              result_variables = {
                  "fOmudelt": fOmudelt,
              }
          )
        else:
          fOlambDR = 1.0
          fOmudelt = fOlambDR * fIRreq
          return RuleUnitResult(
              result_variables = {
                  "fOmudelt": fOmudelt,
              }
          )