import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040303011102_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.1.11.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '지압보강재의 설계지압강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.2 하중집중점 지압보강재
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지압보강재의 설계지압강도] ;
		B["KDS 14 31 10 4.3.3.1.11.2 (3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut1[/출력변수: 지압보강재의 설계지압강도/] ;
    VarOut2[/출력변수: 지압보강재의 공칭지압강도/] ;
		VarIn1[/입력변수: 지압에 대한 강도 저항계수/] ;
    VarIn2[/입력변수: 웨브 용접면으로부터 돌출된 지압보강재의 단면적/] ;
    VarIn3[/입력변수: 지압보강재의 최소항복강도/] ;
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.3.3.1.11.2 (3)"])
		C --> Variable_def

		D["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{n}=1.4A_{pn}F_{ys}>------------------------------"]
		E["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{r}=\phi&space;_{b}(R_{sb})_{n}>----------------------------"]
		Variable_def --> D --> E --> F(["<img src=https://latex.codecogs.com/svg.image?(R_{sb})_{r}>-----------"])
    """

    @rule_method
    def design_acupressure_strength_of_acupressure_reinforcement(fIphib,fIApn,fIFys) -> RuleUnitResult:
        """지압보강재의 설계지압강도

        Args:
            fIphib (float): 지압에 대한 강도저항계수
            fIApn (float): 웨브 용접면으로부터 돌출된 지압보강재의 단면적
            fIFys (float): 지압보강재의 최소항복강도

        Returns:
            fORsbr (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.2 중간수직보강재 (3)의 값 1
            fORsbn (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.1.11.2 중간수직보강재 (3)의 값 2
        """

        assert isinstance(fIphib, float)
        assert isinstance(fIApn, float)
        assert isinstance(fIFys, float)

        fORsbn = 1.4 * fIApn * fIFys
        fORsbr = fIphib * fORsbn

        return RuleUnitResult(
            result_variables = {
                "fORsbr": fORsbr,
            }
        )