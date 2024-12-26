import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040205_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.2.6.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '조립부재의 수정된 기둥세장비'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.6 조립 압축재
    4.2.6.1 압축강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[압축강도] ;
		B["KDS 14 31 10 4.2.6.1 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 조립부재의 수정된 기둥세장비/]
    VarIn1[/입력변수: 고려하는 좌굴방향으로 단일부재로 거동하는 조립부재의 세장비/]
    VarIn2[/입력변수: Ki/]
    VarIn3[/입력변수: 접합재 사이의 길이/]
    VarIn4[/입력변수: 개별부재의 최소단면 2차반경/]
		end

		Python_Class ~~~ C(["KDS 14 31 10 4.2.6.1 (2)"]) --> Variable_def
    D["용접이나 볼트로 접합된 경우"] ;
    F(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{KL}{r}\right)_{m}=\left(\frac{KL}{r}\right)_{o}'>-----------------------------------------------------------------------"]) ;
    G(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{KL}{r}\right)_{m}=\sqrt{\left(\frac{KL}{r}\right)_{0}^{2}&plus;\left(\frac{K_{i}a}{r_{i}}\right)^{2}}'>-------------------------------------------------------------------------------"]) ;
    H["<img src='https://latex.codecogs.com/svg.image?\frac{a}{r_{i}}\leq&space;40'>---------------------------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\frac{a}{r_{i}}>40'>-----------------------------"] ;

	  Variable_def-->D

    D-->H & I
    H-->F
    I-->G
    """

    @rule_method
    def Modified_Column_Slender_Ratio_of_Assemblies(fIKLro,fIa,fIri) -> RuleUnitResult:
        """유효세장비

        Args:
            fIKLro (float): 고려하는 좌굴방향으로 단일부재로 거동하는 조립부재의세장비
            fIa (float): 접합재 사이의 길이
            fIri (float): 개별부재의 최소 단면2차반경

        Returns:
            fOKLrm (float): 강구조부재설계기준(하중저항계수설계법)  4.2.6.1 압축강도 (2)의 값
        """

        assert isinstance(fIKLro, float)
        assert isinstance(fIa, float)
        assert fIa != 0
        assert isinstance(fIri, float)
        assert fIri != 0


        fOKLrm = (fIKLro ** 2 + (fIa / fIri) ** 2) ** 0.5

        return RuleUnitResult(
          result_variables = {
            "fOKLrm": fOKLrm,
            }
        )