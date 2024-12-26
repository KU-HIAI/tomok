import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_030103_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '극한한계상태'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.1 한계상태와 저항계수
    3.1.3 극한한계상태
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 극한한계상태];
    B["KDS 24 14 51 3.2.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 저항계수/];
		VarIn2[/입력변수: 지지력/];
		VarIn3[/입력변수: 하중계수/];
		VarIn4[/입력변수: 하중/];

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.2.3 (2)"])
		C --> Variable_def;

		Variable_def---->E--->F
		E{"저항계수X지지력 ≥ 하중계수X하중"};
    F(["Pass or Fail"]);
    E~~~ |"KDS 24 12 11"| E
    """

    @rule_method
    def ultimate_limit_state(fIresfac,fIbeacap,fIloafac,fIload) -> RuleUnitResult:
        """극한한계상태

        Args:
            fIresfac (float): 저항계수
            fIbeacap (float): 지지력
            fIloafac (float): 하중계수
            fIload (float): 하중

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법)  3.1.3 극한한계상태 (2)의 판단 결과
        """

        assert isinstance(fIresfac, float)
        assert isinstance(fIbeacap, float)
        assert isinstance(fIloafac, float)
        assert isinstance(fIload, float)

        if fIresfac * fIbeacap >= fIloafac * fIload :
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