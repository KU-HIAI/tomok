import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '철근 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 단면적];
    B["KDS 24 14 21 4.6.2.1 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:인장철근 단면적/];
		VarIn2[/입력변수: 콘크리트 단면적/];
		VarIn3[/입력변수: 압축철근 단면적/];

		VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (4)"])
		C --> Variable_def

		Variable_def--->F & G

		F{"인장철근 단면적<콘크리트 단면적X0.04"}
		G{"압축철근 단면적<콘크리트 단면적X0.04"}
		F & G---->J
		J(["Pass or Fail"])
    """

    @rule_method
    def Cross_sectional_area_of_rebar(fIcrosat,fIconcse,fIcompba) -> RuleUnitResult:
        """철근 단면적

        Args:
            fIcrosat (float): 인장철근 단면적
            fIconcse (float): 콘크리트 단면적
            fIcompba (float): 압축철근 단면적


        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.1 주철근 (4)의 판단 결과
        """

        assert isinstance(fIcrosat, float)
        assert isinstance(fIconcse, float)
        assert isinstance(fIcompba, float)

        if fIcrosat != 0 and fIcompba == 0 :
          if fIcrosat <= fIconcse * 0.04 :
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

        if fIcrosat == 0 and fIcompba != 0 :
          if fIcompba <= fIconcse * 0.04 :
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

        if fIcrosat != 0 and fIcompba != 0 :
          if fIcompba <= fIconcse * 0.04 and fIcrosat <= fIconcse * 0.04 :
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