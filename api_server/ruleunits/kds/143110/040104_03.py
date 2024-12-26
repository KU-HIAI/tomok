import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040104_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.4 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '조립인장재'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[조립 인장부재] ;
		B["KDS 14 31 10 4.1.4(3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 띠판의 재축방향 길이/]
    VarIn2[/입력변수: 용접/]
    VarIn3[/입력변수: 연결재 사이거리/]
    VarIn4[/입력변수: 띠판 두께/]
    VarIn5[/입력변수: 열 사이거리/]
    VarIn6[/입력변수: 단순용접/]
    VarIn7[/입력변수: 연결재의 재축방향 간격/]
    VarIn8[/입력변수: 조립부재 개별부재의 세장비/]
    VarIn1 ~~~ VarIn5
    VarIn2  ~~~ VarIn6
    VarIn3 & VarIn4 ~~~ VarIn7 & VarIn8
		end

		Python_Class ~~~ Variable_def
  	C["띠판의 재축방향 길이"]
  	D(["띠판의 재축방향 길이 ≥ 용접 or 연결재사이거리의 2/3"])
    E["띠판 두께"]
    F(["띠판 두께 ≥ 열 사이거리의 1/50"])
    G["단순용접 or 연결재의 재축방향 간격"]
    H(["단순용접 or 연결재의 재축방향 간격 ≤ 150mm"])
    I["조립부재 개별부재의 세장비"]
    J(["가급적 세장비 ≤ 300"])
    Variable_def --> C-->D
    Variable_def --> E-->F
    Variable_def --> G-->H
    Variable_def --> I-->J
    """

    @rule_method
    def  the_length_of_the_strip_in_the_axial_direction(fIlestad,fIweldin,fIdibeco,fIbanthi,fIdibero,fIinwedw,fIspaxdc,fIamsrim) -> RuleUnitResult:
        """띠판의 재축방향 길이

        Args:
            fIlestad (float): 띠판의 재축방향 길이
            fIweldin (float): 용접
            fIdibeco (float): 연결재 사이거리
            fIbanthi (float): 띠판 두께
            fIdibero (float): 열 사이거리
            fIinwedw (float): 단속용접
            fIspaxdc (float): 연결재의 재축방향 간격
            fIamsrim (float): 조립부재 개별부재의 세장비

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.1.4 조립 인장부재 (3)의 통과여부
        """

        assert isinstance(fIlestad, float)
        assert isinstance(fIweldin, float)
        assert isinstance(fIdibeco, float)
        assert isinstance(fIbanthi, float)
        assert isinstance(fIdibero, float)
        assert isinstance(fIinwedw, float)
        assert isinstance(fIspaxdc, float)
        assert isinstance(fIamsrim, float)

        if fIlestad >= 2/3*max(fIweldin,fIdibeco) and fIbanthi >= fIdibero/50 and (fIinwedw<=150 or fIspaxdc<=150) and fIamsrim <=300:
          return RuleUnitResult(
              result_variables = {
                "pass_fail": True,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                "pass_fail": False,
              }
          )