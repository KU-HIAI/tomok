import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040303(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '설계휨모멘트'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.3 설계휨모멘트
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 설계휨모멘트] ;
		B["KDS 14 31 10 4.5.4.3.3"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 박스형 파형강판 구조물의 정점부 설계휨모멘트/] ;
    VarOut2[/출력변수: 박스형 파형강판 구조물의 어깨부 설계휨모멘트/] ;
    VarIn1[/입력변수: 고정하중 하중계수/] ;
    VarIn2[/입력변수: 고정하중에 의한 정점부 휨모멘트/] ;
    VarIn3[/입력변수: 활하중 하중계수/] ;
    VarIn4[/입력변수: 활하중에 의한 정점부 휨모멘트/] ;
    VarIn5[/입력변수: 충격계수/] ;
    VarIn6[/입력변수: 지진하중 하중계수/] ;
    VarIn7[/입력변수: 지진하중에 의한 정점부 휨모멘트/] ;
    VarIn8[/입력변수: 고정하중 하중계수/] ;
    VarIn9[/입력변수: 고정하중에 의한 어깨부 휨모멘트/] ;
    VarIn10[/입력변수: 활하중 하중계수/] ;
    VarIn11[/입력변수: 활하중에 의한 어깨부 휨모멘트/] ;
    VarIn12[/입력변수: 충격계수/] ;
    VarIn13[/입력변수: 지진하중 하중계수/] ;
    VarIn14[/입력변수: 지진하중에 의한 어깨부 휨모멘트/] ;
		end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14

    Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.3"])
		C --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?M_{cf}=\alpha&space;_{D}M_{cD}&plus;max\left\{\alpha&space;_{L}M_{cL}(1&plus;i),\alpha&space;_{E}M_{cE}\right\}>------------------------------------------------------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{hf}=\alpha&space;_{D}M_{hD}&plus;max\left\{\alpha&space;_{L}M_{hL}(1&plus;i),\alpha&space;_{E}M_{hE}\right\}>------------------------------------------------------------------------------------"]
		R(["<img src=https://latex.codecogs.com/svg.image?M_{cf}>---------"])
		S(["<img src=https://latex.codecogs.com/svg.image?M_{hf}>---------"])

		Variable_def --> Q & W
		Q --> R
		W --> S
    """


    @rule_method
    def Design_bending_moment(fIalphaD,fIMcD,fIalphaL,fIMcL,fIi,fIalphaE,fIMcE,fIMhD,fIMhL,fIMhE) -> RuleUnitResult:
        """설계휨모멘트

        Args:
            fIalphaD (float): 고정하중 하중계수
            fIMcD (float): 고정하중에 의한 정점부 휨모멘트
            fIalphaL (float): 활하중 하중계수
            fIMcL (float): 활하중에 의한 정점부 휨모멘트
            fIi (float): 충격계수
            fIalphaE (float): 지진하중 하중계수
            fIMcE (float): 지진하중에 의한 정점부 휨모멘트
            fIMhD (float): 고정하중에 의한 어깨부 휨모멘트
            fIMhL (float): 활하중에 의한 어깨부 휨모멘트
            fIMhE (float): 지진하중에 의한 어깨부 휨모멘트

        Returns:
            fOMcf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.3 설계휨모멘트의 값 1
            fOMhf (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.3 설계휨모멘트의 값 2
        """

        assert isinstance(fIalphaD, float)
        assert isinstance(fIMcD, float)
        assert isinstance(fIalphaL, float)
        assert isinstance(fIMcL, float)
        assert isinstance(fIi, float)
        assert isinstance(fIalphaE, float)
        assert isinstance(fIMcE, float)
        assert isinstance(fIMhD, float)
        assert isinstance(fIMhL, float)
        assert isinstance(fIMhE, float)

        fOMcf = fIalphaD * fIMcD + max(fIalphaL * fIMcL * (1 + fIi), fIalphaE * fIMcE)
        fOMhf = fIalphaD * fIMhD + max(fIalphaL * fIMhL * (1 + fIi), fIalphaE * fIMhE)

        return RuleUnitResult(
            result_variables = {
                "fOMcf": fOMcf,
                "fOMhf": fOMhf,
            }
        )