import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040402(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '휨과 축력을 받는 비대칭 단면 부재 및 기타 부재'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.2 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재] ;
		B["KDS 14 31 10 4.4.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 부재 단면의 특정 위치에서 하중조합으로 구한 소요축방향응력/] ;
      VarIn2[/입력변수: 설계축방향응력/] ;
      VarIn3[/입력변수: 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력/] ;
      VarIn4[/입력변수: 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력/] ;
      VarIn5[/입력변수: 설계휨응력/] ;
      VarIn6[/입력변수: 설계휨응력/] ;
			end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

		Python_Class ~~~ C1(["KDS 14 31 10 4.4.2"]) --> Variable_def

		C["<img src=https://latex.codecogs.com/svg.image?\left|\frac{f_{ua}}{F_{ra}}&plus;\frac{f_{ubw}}{F_{rbw}}&plus;\frac{f_{ubz}}{F_{rbz}}\right|\leq&space;1.0>---------------------------------------------------"]

		Variable_def--> C --> D(["PASS or Fail"])
    """

    @rule_method
    def Asymmetric_cross_sectional_members_and_other_members_subjected_to_bending_and_axial_forces(fIfua,fIFra,fIfubw,fIfubz,fIFrbw,fIFrbz) -> RuleUnitResult:
        """휨과 축력을 받는 비대칭 단면 부재 및 기타 부재

        Args:
            fIfua (float): 부재 단면의 특정 위치에서 하중조합으로 구한 소요축방향응력
            fIFra (float): 설계축방향응력
            fIfubw (float): 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력
            fIfubz (float): 부재 단면의 특정위치에서 하중조합으로 구한 소요휨응력
            fIFrbw (float): 설계휨응력
            fIFrbz (float): 설계휨응력


        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.4.2 휨과 축력을 받는 비대칭 단면 부재 및 기타 부재의 통과여부
        """

        assert isinstance(fIfua, float)
        assert isinstance(fIFra, float)
        assert fIFra !=0
        assert isinstance(fIfubw, float)
        assert isinstance(fIfubz, float)
        assert isinstance(fIFrbw, float)
        assert fIFrbw !=0
        assert isinstance(fIFrbz, float)
        assert fIFrbz !=0

        if abs(fIfua / fIFra + fIfubw / fIFrbw + fIfubz / fIFrbz) <= 1.0:
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