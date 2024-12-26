import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040203_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '공칭압축강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도] ;
		B["KDS 14 31 10 4.2.3 (1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 공칭압축강도/]
    VarIn1[/입력변수: 횡좌굴에 대한 비지지길이/]
    VarIn2[/입력변수: 단면2차반경/]
    VarIn3[/입력변수: 유효좌굴길이계수/]
    VarIn4[/입력변수: 좌굴 응력/]
    VarIn5[/입력변수: 부재의 총단면적/]
    VarIn6[/입력변수: 탄성좌굴해석을 통하여 구하는 탄성좌굴응력/]
    VarIn7[/입력변수: 강재의 항복강도/]
    VarIn8[/입력변수: 강재의 탄성계수/]
    VarIn9[/입력변수: 부재의 횡좌굴에 대한 비지지길이/]
    VarIn10[/입력변수: 좌굴축에 대한 단면2차반경/]
    VarIn1~~~ VarIn6
    VarIn2~~~ VarIn7
    VarOut1~~~ VarIn3~~~ VarIn8
    VarIn4~~~ VarIn9
    VarIn5~~~ VarIn10

		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.3 (1)"])
		C --> Variable_def

		Variable_def --> D --> E

	  D(["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{cr}A_{q}'>-----------------------------------"]) ;
    E(["공칭압축강도"]) ;

    """

    @rule_method
    def nominal_compressive_strength(fIFcr,fIAg) -> RuleUnitResult:
        """공칭압축강도

        Args:
            fIFcr (float): 좌굴응력
            fIAg (float): 부재의 총단면적

        Returns:
            fOPn (float): 강구조부재설계기준(하중저항계수설계법)  4.2.3 비세장판 단면을 가진 부재의 휨좌굴에 대한 압축강도 (1)의 값
        """

        assert isinstance(fIFcr, float)
        assert isinstance(fIAg, float)

        fOPn = fIFcr * fIAg

        return RuleUnitResult(
            result_variables = {
                "fOPn": fOPn,
            }
        )