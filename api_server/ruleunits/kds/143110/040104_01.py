import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040104_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.1.4 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '조립 인장부재의 재축방향 긴결간격'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.4 조립 인장부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 조립 인장부재의 재축방향 긴결간격] ;
		B["KDS 14 31 10 4.1.4(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarIn1[/입력변수: 조립 인장부재의 재축방향 긴결간격/]
    VarIn2[/입력변수: 얇은 판 두께/]

		end

		Python_Class ~~~ Variable_def
  	C["도장된 부재 또는 부식의 우려가 없어 도장되지 않는 부재의 경우"]
  	D["대기 중 부식에 노출된 도장되지 않는 내후성강의 경우"]
    E(["조립 인장부재의 재축방향 긴결간격 ≤ 얇은 판 두께의 24배 or 300mm"])
    F(["조립 인장부재의 재축방향 긴결간격 ≤ 얇은 판 두께의 14배 or 180mm"])
	  Variable_def --> C & D
    C-->E-->G([PASS or Fail]);
    D-->F-->H([PASS or Fail]);
    """

    @rule_method
    def Tightening_interval_in_the_reaxial_direction_of_the_assembly_tension_member(fItirdtm,fIthplthA,fIthplthB) -> RuleUnitResult:
        """조립 인장부재의 재축방향 긴결간격

        Args:
            fItirdtm (float): 조립 인장부재의 재축방향 긴결간격
            fIthplthA (float): 얇은 판 두께 (도장된 부재 또는 도장되지 않은 부재)
            fIthplthB (float): 얇은 판 두께 (내후성강의 경우)

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.1.4 조립 인장부재 (1)의 통과여부
        """

        assert isinstance(fItirdtm, float)
        assert isinstance(fIthplthA, float)
        assert isinstance(fIthplthB, float)

        if fIthplthA !=0 and fIthplthB ==0 :
           if fItirdtm <= min(fIthplthA*24,300):
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

        elif fIthplthB !=0 and fIthplthA ==0:
           if fItirdtm <= min(fIthplthA*14,180):
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

        else :
          return RuleUnitResult(
              result_variables = {
                "pass_fail": False,
              }
          )