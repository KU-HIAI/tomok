import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0403030402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.4.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '다이아프램이나 수직가새의 높이'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.4 다이아프램 및 수직가새
    4.3.3.4.2 플레이트거더 단면
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 다이아프램이나 수직가새의 높이] ;
		B["KDS 14 31 10 4.3.3.4.2 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 다이아프램이나 수직가새의 높이/] ;
      VarIn2[/입력변수: 거더 높이/] ;
			end

		Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.4.2 (1)"]) --> Variable_def

		C["다이아프램이나 수직가새의 높이 &ge; 거더높이x1/2"]

		Variable_def --> C -->D(["PASS or Fail"])
    """

    @rule_method
    def Height_of_a_diaphragm_or_vertical_brace(fIhedivb,fIgirhei) -> RuleUnitResult:
        """다이아프램이나 수직가새의 높이

        Args:
            fIhedivb (float): 다이아프램이나 수직가새의 높이
            fIgirhei (float): 거더 높이

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.4.2 플레이트거더 단면 (1)의 통과여부
        """

        assert isinstance(fIhedivb, float)
        assert isinstance(fIgirhei, float)


        if fIhedivb >= fIgirhei * 1 / 2:
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