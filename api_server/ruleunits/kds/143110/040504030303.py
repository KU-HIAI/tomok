import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040504030303(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.3.3'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '지진하중에 의한 정점부 및 어깨부 휨모멘트'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.3 설계휨모멘트
    4.5.4.3.3.3 지진하중에 의한 휨모멘트
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 지진하중에 의한 정점부 및 어깨부 휨모멘트] ;
		B["KDS 14 31 10 4.5.4.3.3.3"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 지진하중에 의한 정점부 휨모멘트/] ;
    VarOut2[/출력변수: 지진하중에 의한 어깨부 휨모멘트/] ;
    VarIn1[/입력변수: 지진하중에 의한 휨모멘트/] ;
    VarIn2[/입력변수: 수직가속도계수/] ;
    VarIn3[/입력변수: 수평가속도계수/] ;
		end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3

    Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.3.3"])
		C --> Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?A_{V}=\frac{2}{3}A_{H}>---------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{E}=M_{D}A_{V}>---------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?M_{cE}=\kappa&space;M_{E}>--------------------------"]
		S["<img src=https://latex.codecogs.com/svg.image?M_{hE}=(1-\kappa)M_{E}>-------------------------------------"]

		Variable_def --> Q --> W --> R & S
		R --> D(["<img src=https://latex.codecogs.com/svg.image?M_{cE}>-----------"])
		S --> H(["<img src=https://latex.codecogs.com/svg.image?M_{hE}>-----------"])
    """


    @rule_method
    def Peak_and_shoulder_bending_moment_due_to_seismic_load(fIME,fIAH,fIk) -> RuleUnitResult:
        """지진하중에 의한 정점부 및 어깨부 휨모멘트

        Args:
            fIME (float): 지진하중에 의한 휨모멘트
            fIAH (float): 수평가속도계수
            fIk (float): 정점부 휨모멘트 분배계수

        Returns:
            fOMcE (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.3.3 지진하중에 의한 휨모멘트의 값 1
            fOMhE (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.3.3 지진하중에 의한 휨모멘트의 값 2
            fOAV (float): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.3.3 지진하중에 의한 휨모멘트의 값 3
        """

        assert isinstance(fIME, float)
        assert isinstance(fIAH, float)
        assert isinstance(fIk, float)

        fOAV = 2 / 3 * fIAH
        fOMcE = fIk * fIME
        fOMhE = (1 - fIk) * fIME

        return RuleUnitResult(
            result_variables = {
                "fOMcE": fOMcE,
                "fOMhE": fOMhE,
            }
        )