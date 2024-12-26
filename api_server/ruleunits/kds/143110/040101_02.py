import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040101_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '모든 인장부재의 세장비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.1 세장비 제한
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[세장비 제한] ;
		B["KDS 14 31 10 4.1.1 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 교번응력을 받는 주부재의 세장비/]
    VarIn2[/입력변수: 교번응력을 받지 않는 주부재의 세장비/]
    VarIn3[/입력변수: 2차 부재의 세장비/]
		end

		Python_Class ~~~ Variable_def
	  C["교번응력을 받는 주부재"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;140'>--------------------"])
	  E["교번응력을 받지 않는 주부재"] ;
    F(["<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;200'>--------------------"])
    G["2차 부재"] ;
    H(["<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;240'>--------------------"])
    Variable_def --> C-->D --> I([PASS or Fail]);
    Variable_def --> E-->F --> J([PASS or Fail]);
    Variable_def --> G-->H --> K([PASS or Fail]);
    """

    @rule_method
    def slender_ratio_of_all_tension_members(fIslesub,fIslenot,fIslesec) -> RuleUnitResult:
        """모든 인장부재의 세장비

        Args:
            fIslesub (float): 교번응력을 받는 주부재의 세장비
            fIslenot (float): 교번응력을 받지 않는 주부재의 세장비
            fIslesec (float): 2차 부재의 세장비

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.1.1 세장비 제한 (2)의 판단 결과
        """

        assert isinstance(fIslesub, float)
        assert isinstance(fIslenot, float)
        assert isinstance(fIslesec, float)

        if fIslesub <= 140 and fIslenot <= 200 and fIslesec <= 240:
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