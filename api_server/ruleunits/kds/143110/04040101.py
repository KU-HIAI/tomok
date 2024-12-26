import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04040101(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    title = '하중조합으로 구한 소요압축강도'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '하중조합으로 구한 소요압축강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.1 휨과 축력이 작용하는 1축 및 2축 대칭단면 부재
    4.4.1.1 압축력과 휨을 받는 1축 및 2축 대칭단면 부재
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 압축력과 휨을 받는 1축 및 2축 대칭단면 부재] ;
		B["KDS 14 31 10 4.4.1.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 하중조합으로 구한 소요압축강도/] ;
      VarIn2[/입력변수: 설계압축강도/] ;
      VarIn3[/입력변수: 압축에 대한 강도 저항계수/] ;
      VarIn4[/입력변수: 하중조합으로 구한 소요휨강도/] ;
      VarIn5[/입력변수: 설계휨강도/] ;
      VarIn6[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn7[/입력변수: 강축 휨을 나타내는 아래첨자/] ;
      VarIn8[/입력변수: 약축 휨을 나타내는 아래첨자/] ;
			end

		Python_Class ~~~ C1(["KDS 14 31 10 4.4.1.1"]) --> Variable_def
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8

		C["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}\geq&space;0.2>--------------------"]
		D["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{8}{9}(\frac{M_{ux}}{M_{rx}}&plus;\frac{M_{uy}}{M_{ry}})\leq&space;1.0>---------------------------------------------"]
		E["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}<0.2>--------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?\frac{P_{u}}{2P_{r}}&plus;(\frac{M_{ux}}{M_{rx}}&plus;\frac{M_{uy}}{M_{ry}})\leq&space;1.0>-------------------------------------------"]

		Variable_def --> C --> D
		Variable_def --> E --> F
		D & F --> G(["PASS or Fail"])
    """

    @rule_method
    def Required_compressive_strength_obtained_from_load_combinations(fIPu,fIPr,fIphic,fIMux,fIMuy,fIMrx,fIMry,fIphib) -> RuleUnitResult:
        """하중조합으로 구한 소요압축강도

        Args:
            fIPu (float): 하중조합으로 구한 소요압축강도
            fIPr (float): 설계압축강도
            fIphic (float): 압축에 대한 강도저항계수
            fIMux (float): x축 하중조합으로 구한 소요휨강도
            fIMuy (float): y축 하중조합으로 구한 소요휨강도
            fIMrx (float): x축 설계휨강도
            fIMry (float): y축 설계휨강도
            fIphib (float): 휨에 대한 강도저항계수

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법) 4.4.1.1 압축력과 휨을 받는 1축 및 2축 대칭단면 부재의 통과여부
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIPr, float)
        assert fIPr !=0
        assert isinstance(fIphic, float)
        assert isinstance(fIMux, float)
        assert isinstance(fIMuy, float)
        assert isinstance(fIMrx, float)
        assert fIMrx !=0
        assert isinstance(fIMry, float)
        assert fIMry !=0
        assert isinstance(fIphib, float)

        if fIPu / fIPr >= 0.2:
           if fIPu / fIPr + (8 / 9) * (fIMux / fIMrx + fIMuy / fIMry) <= 1.0:
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
          if fIPu / (2 * fIPr) + (fIMux / fIMrx + fIMuy / fIMry) <= 1.0:
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