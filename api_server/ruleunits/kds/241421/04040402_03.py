import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04040402_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.4.4.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '최소피복두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.2 최소피복두께
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소피복두께];
    B["KDS 24 14 21 4.4.4.2 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 최소피복두께/];
		VarIn2[/입력변수: 부착에 대한 요구사항을 만족하는 최소피복두께/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.4.4.2 (3)"])
		C --> Variable_def

		Variable_def--->D--->F
		D{"최소피복두께><img src='https://latex.codecogs.com/svg.image?t_{c,min,b}'>---------------------------------"}
		D~~~|KDS 24 14 21 table 4.4-3|D
		F(["Pass or fail"])
    """

    @rule_method
    def minimum_cover_thickness(fImincth,fItcminb) -> RuleUnitResult:
        """최소피복두께

        Args:
            fImincth (float): 최소피복두께
            fItcminb (float): 부착에 대한 요구사항을 만족하는 최소피복두께

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.4.4.2 일반 사항 (3)의 판단 결과
        """

        assert isinstance(fImincth, float)
        assert isinstance(fItcminb, float)

        if fImincth > fItcminb:
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