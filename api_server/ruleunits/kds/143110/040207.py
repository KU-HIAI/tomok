import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040205_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.7'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '공칭압축강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.7 세장판단면을 갖는 압축부재
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[세장판단면을 갖는 압축부재] ;
		B["KDS 14 31 10 4.2.7"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 좌굴응력/]
    VarIn2[/입력변수: 세장비/]
    VarIn3[/입력변수: root E/QFy/]
    VarIn4[/입력변수: QFy/Fe/]
    VarIn5[/입력변수: 모든 세장 압축요소를 고려하는 순 감도계수/]
    VarIn6[/입력변수: 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarOut1~~~ VarIn4
    VarIn1~~~ VarIn5
    VarIn2~~~ VarIn6
    VarIn3~~~ VarIn7
		end

		Python_Class ~~~ C1(["KDS 14 31 10 4.2.7"])-->Variable_def
    C["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{g}'>------------------------------"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?P_{n}'>-------------"]) ;


    Variable_def-->C-->D
    """

    @rule_method
    def Nominal_Compressive_Strength(fIFcr,fIAg) -> RuleUnitResult:
        """공칭압축강도

        Args:
            fIFcr (float): 좌굴응력
            fIAg (float): 공칭면적

        Returns:
            fOPn (float): 강구조부재설계기준(하중저항계수설계법)  4.2.7 세장판단면을 갖는 압축부재의 값
        """

        assert isinstance(fIFcr, float)
        assert isinstance(fIAg, float)

        fOPn = fIFcr * fIAg

        return RuleUnitResult(
          result_variables = {
            "fOPn": fOPn,
            }
        )