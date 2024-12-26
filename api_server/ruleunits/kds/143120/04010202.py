import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143120_04010202(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 20 4.1.2.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '하중유발피로를 고려하는 경우 구조상세'

    description = """
    강구조 피로 및 파단 설계기준(하중저항계수설계법)
    4. 설계(피로 및 파단)
    4.1 피로
    4.1.2 하중유발피로
    4.1.2.2 설계기준
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A([Title: 하중유발피로를 고려하는 경우 구조상세]);
    B["KDS 14 31 20 4.1.2.2"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 하중조합 규정에 명시된 하중계수/];
    VarIn2[/입력변수: 하중효과/];
    VarIn3[/입력변수: 4.1.2.5에 규정된 공칭피로강도/];

    end

    Python_Class ~~~ C(["KDS 14 31 20 4.1.2.2"])
		C --> Variable_def

		Variable_def --> H

    E([PASS or Fail])

		H{"<img src='https://latex.codecogs.com/svg.image?\gamma(\Delta&space;f)\leq(\Delta&space;F)_{n}';\gamma (\Delta f)\leq (\Delta F)_{n}>-----------------------------"};
	  H-->E
    """

    @rule_method
    def Structural_details_when_considering_load_induced_fatigue(fIgamma,fIdeltaf,fIdeltaFn) -> RuleUnitResult:
        """하중유발피로를 고려하는 경우 구조상세

        Args:
            fIgamma (float): 하중조합 규정에 명시된 하중계수
            fIdeltaf (float): 하중효과
            fIdeltaFn (float): 4.1.2.5에 규정된 공칭피로강도

        Returns:
            pass_fail (bool): 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.2 설계기준의 판단 결과
        """

        assert isinstance(fIgamma, float)
        assert isinstance(fIdeltaf, float)
        assert isinstance(fIdeltaFn, float)

        if fIgamma * fIdeltaf <= fIdeltaFn :
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