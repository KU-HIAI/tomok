import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010113_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.1.13 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '세장한 자유돌출판의 저감계수'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    4.2.7.1 세장한 자유돌출판
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[휨부재의 단면산정]
	  B["KDS 14 31 10 4.3.2.1.1.13(2)"]
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
	  Python_Class ~~~ C1(["KDS 14 31 10 4.3.2.1.1.13(2)"]) --> Variable_def --> C & I
	  C --> L -->  D & F
	  D --> E
	  F --> G
	  E & G --> H
	  I --> J & K
	  C["H형강 부재의 단면제한"]
	  D["<img src='https://latex.codecogs.com/svg.image?\frac{a}{h}\leq&space;1.5'>-------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}=11.7\sqrt{\frac{E}{F_y}}'>------------------------"]
	  F["<img src='https://latex.codecogs.com/svg.image?\frac{a}{h}>1.5'>-------------"]
	  G["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}=\frac{0.42E}{F_y}'>--------------------"]
	  H(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}'>---------------"])
	  I["보강재가 없는 보"]
	  J(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{h}{t_w}\right)_{max}<260'>--------------------------"])
	  K(["웨브의 면적 < 압축플랜지면적 x10"])
	  L["<img src='https://latex.codecogs.com/svg.image?0.1\leq\frac{I_{yc}}{I_y}\leq&space;0.9'>----------------------"]

    """

    @rule_method
    def Moment_of_inertia_of_the_compression_flange_about_the_y_axis_or_moment_of_inertia_of_the_smaller_of_the_compression_flanges_in_case_of_back(fIIyc,fIIy,fIa,fIhA,fIhB,fItw,fIE,fIFy,fIAw,fIAfc) -> RuleUnitResult:
        """단일 ㄱ형강 항복강도

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

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.13 (1)의 통과여부
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

        if fIhA != 0:
            if 0.1 <= fIIyc / fIIy <= 0.9:
                if fIa / fIh <= 1.5:
                  11.7 * (fIE / fIFy) ** 0.5 >= fIh / fItw
                  return  RuleUnitResult(
                   result_variables = {
                    "pass_fail": True,
                    }
                  )
                elif fIa / fIh >= 1.5:
                  0.42 * fIE / fIFy >= fIh / fItw
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
                elif fIa / fIh >= 1.5:
                  0.42 * fIE / fIFy >= fIh / fItw
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