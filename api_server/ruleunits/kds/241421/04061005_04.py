import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04061005_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.10.5 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '현장 타설 말뚝의 축방향 철근'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.10 기초판
    4.6.10.5 현장 타설 말뚝
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 현장 타설 말뚝의 축방향 철근];
    B["KDS 24 14 21 4.6.10.5 (4)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:축방향 철근의 최소 지름/];
		VarIn2[/입력변수:축방향 철근 개수/];
		VarIn3[/입력변수:철근 사이의 순간격/];

		VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.10.5 (4)"])
		C --> Variable_def

		Variable_def--->D & E & F --->G

		E["축방향 철근의 최소 지름 ≥ 16mm"]
		D["축방향 철근 개수 ≥ 6개"]
		F["철근 사이의 순간격 ≤ 200mm"]
		G(["Pass or Fail"])
    """

    @rule_method
    def Axial_reinforcement_of_cast_in_place_concrete_pile(fImindaxr,fIaxireb,fIinsgbr) -> RuleUnitResult:
        """현장 타설 말뚝의 축방향 철근

        Args:
            fImindaxr (float): 축방향 철근의 최소 지름
            fIaxireb (float): 축방향 철근 개수
            fIinsgbr (float): 철근 사이의 순간격

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.10.5 현장 타설 말뚝 (4)의 판단 결과
        """

        assert isinstance(fImindaxr, float)
        assert isinstance(fIaxireb, float)
        assert isinstance(fIinsgbr, float)

        if fImindaxr>=16 and fIaxireb>=6 and fIinsgbr<=200 :
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