import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010113_02_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.1.13 (2) ①'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = 'H형강 부재의 단면제한'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.1 휨강도
    4.3.2.1.1.13 휨부재의 단면산정
    (2)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: H형강 부재의 단면제한]
	  B["KDS 14 31 10 4.3.2.1.1.13 (2) ①"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: y축에 대한 압축플랜지의 단면2차모멘트 또는 복곡률의 경우 압축플랜지중 작은플랜지의 단면2차모멘트/]
	  VarIn2[/입력변수: y축에 대한 단면2차모멘트/]
	  VarIn3[/입력변수: 수직보강재의 순간격/]
	  VarIn4[/입력변수: 웨브의 높이/]
	  VarIn5[/입력변수: 웨브의 두께/]
	  VarIn6[/입력변수: 강재의 탄성계수/]
	  VarIn7[/입력변수: 항복강도/]
	  VarIn8[/입력변수: 웨브의 면적/]
	  VarIn9[/입력변수: 압축플랜지면적/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  VarIn6 ~~~ VarIn8 & VarIn9
	  end
	  Python_Class ~~~ C1(["KDS 14 31 10 4.3.2.1.1.13 (2) ①"]) --> Variable_def --> C
	  C --> L -->  D
	  D --> E
	  E--> H
	  C["H형강 부재의 단면제한"]
	  D{"<img src='https://latex.codecogs.com/svg.image?\frac{a}{h}\leq&space;1.5'>-------------"}
	  E["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}=11.7\sqrt{\frac{E}{F_y}}'>------------------------"]
	  H(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}'>---------------"])
	  L{"<img src='https://latex.codecogs.com/svg.image?0.1\leq\frac{I_{yc}}{I_y}\leq&space;0.9'>----------------------"}

    """

    @rule_method
    def Restriction_of_section_of_H_steel(fIIyc,fIIy,fIa,fIhA,fIhB,fItw,fIE,fIFy,fIAw,fIAfc,fIh) -> RuleUnitResult:
        """H형강 부재의 단면제한

        Args:
            fIIyc (float): y축에 대한 압축플랜지의 단면2차모멘트 또는 복곡률의 경우 압축플랜지 중 작은플랜지의 단면2차모멘트
            fIIy (float): y축에 대한 단면2차모멘트
            fIa (float): 수직보강재의 순간격
            fIhA (float): 웨브의 높이 (보강재가 없는 보)
            fIhB (float): 웨브의 높이 (보강재가 있는 보)
            fItw (float): 웨브의 두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 항복강도
            fIAw (float): 웨브의 면적
            fIAfc (float): 압축플랜지면적
            fIh (float): 웨브의 높이

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.13 휨부재의 단면산정 (2) ①의 판단 결과 1
            sOnone (string): 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.13 휨부재의 단면산정 (2) ①의 판단 결과 2
        """

        assert isinstance(fIIyc, float)
        assert isinstance(fIIy, float)
        assert isinstance(fIa, float)
        assert isinstance(fIhA, float)
        assert isinstance(fIhB, float)
        assert isinstance(fItw, float)
        assert isinstance(fIE, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIAw, float)
        assert isinstance(fIAfc, float)
        assert isinstance(fIh, float)

        if fIhA != 0:
            if 0.1 <= fIIyc / fIIy <= 0.9:
                if fIa / fIh <= 1.5:
                  11.7 * (fIE / fIFy) ** 0.5 >= fIh / fItw
                  return  RuleUnitResult(
                   result_variables = {
                    "pass_fail": True,
                    }
                  )
                else:
                  return  RuleUnitResult(
                   result_variables = {
                    "pass_fail": False,
                    }
                  )
            else:
                return  RuleUnitResult(
                 result_variables = {
                  "pass_fail": False,
                  }
                )
        else:
            if 0.1 <= fIIyc / fIIy <= 0.9 and fIh / fItw <= 260 and fIAw <= fIAfc * 10:
                if fIa / fIh <= 1.5:
                  11.7 * (fIE / fIFy) ** 0.5 >= fIh / fItw
                  return  RuleUnitResult(
                   result_variables = {
                    "pass_fail": True,
                    }
                  )
                else:
                  return  RuleUnitResult(
                   result_variables = {
                    "pass_fail": False,
                    }
                  )
            else:
                return  RuleUnitResult(
                 result_variables = {
                  "pass_fail": False,
                  }
                )