import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030203_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.3 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '주강관 뒤틀림의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관 뒤틀림의 한계상태]
	  B["KDS 14 31 25 4.3.3.2.3 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 비균일 하중분포로 인한 국부항복의 한계상태/] ;
    VarIn3[/입력변수: 지강관의 두께/] ;
    VarIn4[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
    VarIn5[/입력변수: 주강관의 두께/] ;
    VarIn6[/입력변수: 폭비/] ;

    end
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.3 (4)"])
		C --> Variable_def

    V["주강관 뒤틀림이 다른 조치에 의해 방지"]
    W["주강관 뒤틀림의 한계상태"]
    X["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"]
    Y["<img src='https://latex.codecogs.com/svg.image?M_{n}=2F_{y}t[H_{b}t&plus;[BHt(B&plus;H)]^{0.5}]'>----------------------------------------------------------------------------"]
    Z(["검토안함"]) ;
    AA["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>--------------"] ;

    Variable_def-->V--No--->W-->X-->Y-->AA
    V--yes-->Z
    """

    @rule_method
    def limit_state_of_chord_distortion(fIB,fIbeta,fIt,fIH,fIFy,fIHb) -> RuleUnitResult:
        """주강관 뒤틀림의 한계상태

        Args:
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIbeta (float): 폭 비
            fIt (float): 주강관의 두께
            fIH (float): 주강관의 높이
            fIFy (float): 주강관의 항복강도
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (4)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (4)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (4)의 판단 결과
        """

        assert isinstance(fIB, float)
        assert fIB > 0
        assert isinstance(fIbeta, float)
        assert isinstance(fIt, float)
        assert isinstance(fIH, float)
        assert fIH > 0
        assert isinstance(fIFy, float)
        assert isinstance(fIHb, float)

        fOphi = 1.0
        fOMn = 2*fIFy*fIt*(fIHb*fIt+(fIB*fIH*fIt)*((fIB+fIH)**0.5))

        return RuleUnitResult(
            result_variables = {
                "fOMn": fOMn,
                "fOphi": fOphi,
            }
        )