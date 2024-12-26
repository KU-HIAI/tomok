import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.2.5 (1)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '트러스의 솟음'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.2 트러스교
    4.11.2.5 솟음
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 트러스의 솟음];
    B["KDS 24 14 31 4.11.2.5 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
		VarIn1[/입력변수: 트러스의 솟음/] ;
		VarIn2[/입력변수: 고정하중에 의한 처짐/] ;
    end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.2.5 (1)"])
		C --> Variable_def

		Variable_def -->D
    D{"트러스의 솟음 &ge; 고정하중에 의한 처짐"};
    D --> H([PASS or Fail]);
    """

    @rule_method
    def Camber_of_truss(fIcamtru,fIcamddl) -> RuleUnitResult:
        """트러스의 솟음

        Args:
            fIcamtru (float): 트러스의 솟음
            fIcamddl (float): 고정하중에 의한 처짐

        Returns:
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.11.2.5 솟음 (1)의 판단 결과
        """

        assert isinstance(fIcamtru, float)
        assert isinstance(fIcamddl, float)

        if fIcamtru >= fIcamddl:
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