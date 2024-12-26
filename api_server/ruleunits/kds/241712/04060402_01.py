import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241712_04060402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 12 4.6.4.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-16'
    title = '지진해석에 의한 단면의 전단력'

    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.4 주탑 및 교각의 내진성능검증
    4.6.4.2 전단성능 검증
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지진해석에 의한 단면의 전단력];
    B["KDS 24 17 12 4.6.4.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지진해석에 의한 단면의 전단력/];
		VarIn2[/입력변수: 전단강도/];

	  VarIn1

		end
		Python_Class ~~~ C(["KDS 24 17 12 4.6.4.2 (1)"])
		C --> Variable_def--->E

		E{"지진해석에 의한 단면의 전단력≤전단강도"}
    E ---> F(["Pass or Fail"])
    """

    @rule_method
    def Verification_of_shear_performance(fIsecsfs,fIshestr) -> RuleUnitResult:
        """지진해석에 의한 단면의 전단력

        Args:
            fIsecsfs (float): 지진해석에 의한 단면의 전단력
            fIshestr (float): 전단강도

        Returns:
            pass_fail (bool): 교량내진 설계기준(케이블교량) 4.6.4.2 (1)의 판단 결과
        """

        assert isinstance(fIsecsfs, float)
        assert isinstance(fIshestr, float)

        if fIsecsfs <= fIshestr :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )