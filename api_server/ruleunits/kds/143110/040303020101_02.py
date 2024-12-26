import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303020101_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.1.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '플랜지의 계수비틀림 전단강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2.1 일반사항
    4.3.3.2.1.1 응력계산
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 플랜지의 계수비틀림 전단강도] ;
		B["KDS 14 31 10 4.3.3.2.1.1 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 플랜지의 계수비틀림 전단강도/] ;
    VarIn1[/입력변수: 박스플랜지의 순수비틀림 전단응력/] ;
    VarIn2[/입력변수: 전단에 대한 강도저항/] ;
    VarIn3[/입력변수: 플랜지의 최소항복강도/] ;
		end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		Python_Class ~~~ C1(["KDS 14 31 10 4.3.3.2.1.1 (2)"]) -->Variable_def

		C["<img src=https://latex.codecogs.com/svg.image?&space;F_{vr}=0.75\phi&space;_{v}\frac{F_{yf}}{\sqrt{3}}>------------------------"]
		D(["<img src=https://latex.codecogs.com/svg.image?&space;F_{vr}>---------"])
		Variable_def --> C --> D --> E(["플랜지의 계수비틀림 전단강도"])
    """

    @rule_method
    def Modulus_torsional_shear_strength_of_flange(fIptssbf,fIphiv,fIFyf) -> RuleUnitResult:
        """플랜지의 계수비틀림 전단강도

        Args:
            fIptssbf (float): 박스플랜지의 순수비틀림 전단응력
            fIphiv (float): 전단에 대한 강도저항
            fIFyf (float): 플랜지의 최소항복강도

        Returns:
            fOFvr (float): 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.1 일반사항 (2)의 값
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.1 일반사항 (2)의 통과여부
        """

        assert isinstance(fIptssbf, float)
        assert isinstance(fIphiv, float)
        assert isinstance(fIFyf, float)

        fOFvr = 0.75 * fIphiv * fIFyf / (3 ** 0.5)


        if fIptssbf <= fOFvr:
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