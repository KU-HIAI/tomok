import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020203_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.2.3 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '바닥판의 내민부'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.2 단면비 요구조건
    4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 바닥판의 내민부] ;
		B["KDS 14 31 10 4.3.3.2.2.3 (4)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarIn1[/입력변수: 바닥판의 내민부/] ;
		VarIn2[/입력변수: 상부 강재플랜지의 평균 중심간격/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.2.3 (4)"])
		C --> Variable_def

		D{"(0.6a or 1800mm) &ge; 바닥판의 내민부"}

		Variable_def --> D --> F(["PASS or Fail"])
    """

    @rule_method
    def inner_part_of_bottom_plate(fIipbopl,fIa) -> RuleUnitResult:
        """바닥판의 내민부

        Args:
            fIipbopl (float): 바닥판의 내민부
            fIa (float): 상부 강재플랜지의 평균 중심간격

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.2.3 다중 박스단면의 활하중 분배계수 적용 특별제한 (4)의 통과여부
        """

        assert isinstance(fIipbopl, float)
        assert isinstance(fIa, float)


        if fIipbopl <= fIa * 0.6 and fIipbopl <= 1800:
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