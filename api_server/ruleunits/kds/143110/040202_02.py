import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040202_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '압축부재 세장비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.2 유효좌굴길이와 세장비 제한
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 압축부재 세장비] ;
		B["KDS 14 31 10 4.2.2 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 모든 인장부재의 세장비/]
    VarIn2[/입력변수: 교번응력을 받는 주부재의 세장비/]
    VarIn3[/입력변수: 교번응력을 받지 않는 주부재의 세장비/]
    VarIn4[/입력변수: 2차 부재의 세장비/]
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.2 (2)"])
		C --> Variable_def

	  L["교번응력을 받는 주부재"] ;
    D{"<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;140'>--------------------"}
	  E["교번응력을 받지 않는 주부재"] ;
    F{"<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;200'>--------------------"}
    G["2차 부재"] ;
    H{"<img src='https://latex.codecogs.com/svg.image?L/r\leq&space;240'>--------------------"}
    Variable_def --> L-->D --> I([PASS or Fail]);
    Variable_def --> E-->F --> J([PASS or Fail]);
    Variable_def --> G-->H --> K([PASS or Fail]);
    """

    @rule_method
    def slenderness_ratio_of_compression_member(fIslramm,fIslrabr,fIL,fIr,fIK) -> RuleUnitResult:
        """압축부재 세장비

        Args:
            fIslramm (float): 주부재의 세장비
            fIslrabr (float): 가새의 세장비
            fIL (float): 횡좌굴에 대한 비지지길이
            fIr (float): 단면2차반경
            fIK (float): 유효좌굴길이계수

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.2.2 유효좌굴길이와 세장비 제한 (2)의 판단 결과
        """

        assert isinstance(fIslramm, float)
        assert isinstance(fIslrabr, float)
        assert isinstance(fIL, float)
        assert isinstance(fIr, float)
        assert fIr > 0
        assert isinstance(fIK, float)

        if fIslramm != 0 and fIslrabr == 0 :
          if fIL * fIK / fIr <= 120 :
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

        elif fIslramm == 0 and fIslrabr != 0 :
          if fIL * fIK / fIr <= 140 :
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

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )