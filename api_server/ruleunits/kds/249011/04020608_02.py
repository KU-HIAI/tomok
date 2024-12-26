import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020608_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.8 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '받침판 변형'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.8 지지판(backing plate) 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침판의 변형];
    B["KDS 24 90 11 4.2.6.8 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지지판의 전체 변형/];
		VarIn2[/입력변수: 높이/];
		VarIn3[/입력변수: 지지판길이/];

		VarIn1 & VarIn2 & VarIn3


		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.6.8 (2)"])
		C --> Variable_def;
		Variable_def--->K


		K{"<img src='https://latex.codecogs.com/svg.image?\bigtriangleup&space;w_{1}&plus;\bigtriangleup&space;w_{2}\leq&space;h(0.45-2\sqrt{h/L})'>--------------------------------------------------------"};
		K --->M
		M(["Pass or Fail"])
    """

    @rule_method
    def Total_Deformation_Of_The_Support_Plate(fIDelwot,fIh,fIL) -> RuleUnitResult:
        """받침판 변형
        Args:
            fIDelwot (float): 지지판의 전체 변형
            fIh (float): 높이
            fIL (float): 지지판길이

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.6.8 지지판(backing plate) 설계 (2)의 판단 결과
        """

        assert isinstance(fIDelwot, float)
        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fIL, float)
        assert fIL > 0

        if fIDelwot <= fIh * (0.45 - 2 * (fIh / fIL) ** 0.5) :
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