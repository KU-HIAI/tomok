import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_02_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '최대 소요 변위연성도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
		(5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 최대 소요 변위연성도]
	  B["KDS 24 17 10 부록 2 (5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:고려하는 방향으로의 단면 최대두께/];
		VarIn2[/입력변수:기둥형상비의 기준이 되는 기둥길이/];

		VarOut1[/출력변수:소요 변위연성도의 최대값/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 2 (5)"])
		C --> Variable_def

	  Variable_def--->D---> E

		E([Pass or Fail])
		D{"<img src='https://latex.codecogs.com/svg.image?\mu_{\Delta,max}=2(L_{s}/h)\leq&space;5.0'>---------------------------------"}
    """

    @rule_method
    def maximum_value_of_required_response_displacement_ductility(fIh,fIls) -> RuleUnitResult:
        """최대 소요 변위연성도

        Args:
            fIh (float): 고려하는 방향으로의 단면 최대두께
            fIls (float): 기둥 형상비의 기준이 되는 기둥길이

        Returns:
            fOmudelm (float): 교량 내진설계기준(일반설계법) 부록  2. 소요연성도 (5)의 값
            pass_fail (bool): 교량 내진설계기준(일반설계법) 부록  2. 소요연성도 (5)의 판단 결과
        """

        assert isinstance(fIh, float)
        assert fIh != 0
        assert isinstance(fIls, float)

        fOmudelm = (fIls / fIh) * 2
        if (fIls / fIh) * 2 <= 5.0 :
          return RuleUnitResult(
              result_variables = {
                  "fOmudelm": fOmudelm,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )