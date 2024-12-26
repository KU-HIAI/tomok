import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_04040303_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '비강관 부재들의 설계비틀림강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.3 비틀림 또는 비틀림, 휨, 전단력 또는/과 축력 등을 동시에 받는 부재
    4.4.3.3 비틀림과 조합응력을 받는 비강관 부재
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 비강관 부재들의 설계비틀림강도] ;
		B["KDS 14 31 10 4.4.3.3 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 설계비틀림강도/] ;
      VarIn1[/입력변수: 수직응력항복 한계상태/] ;
      VarIn2[/입력변수: 전단응력항복 한계상태/] ;
      VarIn3[/입력변수: 좌굴한계상태/] ;
      VarIn4[/입력변수: 강재의 항복강도/] ;
      VarIn5[/입력변수: 단면의 좌굴응력/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ C1(["KDS 14 31 10 4.4.3.3 (1)"])--> Variable_def

		C["수직응력항복 한계상태"]
		D["전단응력항복 한계상태"]
		R["좌굴 한계상태"]

		E["<img src=https://latex.codecogs.com/svg.image?F_{n}=F_{y}>-----------------"]
		F["<img src=https://latex.codecogs.com/svg.image?F_{n}=0.6F_{y}>-----------------------"]
		G["<img src=https://latex.codecogs.com/svg.image?F_{n}=F_{cr}>-------------------"]
		T["<img src=https://latex.codecogs.com/svg.image?Min(F_{n}=F_{y}or&space;0.6F_{y}or&space;F_{cr})>----------------------------------------"]


		Variable_def --> C & D & R

		C --> E
		D --> F
		R --> G
		E & F & G --> T --> Q(["<img src=https://latex.codecogs.com/svg.image?F_{n}>---------"])
    """

    @rule_method
    def Design_torsional_strength(fIFy,fIFcr) -> RuleUnitResult:
        """비강관 부재들의 설계비틀림강도

        Args:
            fOFn (float): 설계비틀림강도
            fOnosyls (float): 수직응력항복 한계상태
            fOshsyls (float): 전단응력항복 한계상태
            fObulist (float): 좌굴한계상태
            fIFy (float): 강재의 항복강도
            fIFcr (float): 단면의 좌굴응력


        Returns:
            fOFn (float): 강구조부재설계기준(하중저항계수설계법)  4.4.3.3 비틀림과 조합응력을 받는 비강관 부재 (1)의 값 1
            fOnosyls (float): 강구조부재설계기준(하중저항계수설계법)  4.4.3.3 비틀림과 조합응력을 받는 비강관 부재 (1)의 값 2
            fOshsyls (float): 강구조부재설계기준(하중저항계수설계법)  4.4.3.3 비틀림과 조합응력을 받는 비강관 부재 (1)의 값 3
            fObulist (float): 강구조부재설계기준(하중저항계수설계법)  4.4.3.3 비틀림과 조합응력을 받는 비강관 부재 (1)의 값 4
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIFcr, float)

        fOnosyls = fIFy

        fOshsyls = 0.6 * fIFy

        fObulist = fIFcr

        fOFn = min(fOnosyls,fOshsyls,fObulist)

        return RuleUnitResult(
          result_variables = {
            "fOFn": fOFn,
            "fOnosyls": fOnosyls,
            "fOshsyls": fOshsyls,
            "fObulist": fObulist,
           }
         )