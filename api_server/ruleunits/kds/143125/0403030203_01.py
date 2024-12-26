import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '주강관벽 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관벽 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.3.2.3 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 소성화의 한계상태/] ;
    VarIn1[/입력변수: 지강관의 항복강도/] ;
    VarIn2[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
    VarIn3[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
    VarIn4[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
    VarIn5[/입력변수: 주강관의 두께/] ;
    VarIn6[/입력변수: 폭비/] ;
    VarIn7[/입력변수: 접합평면과 90를 이루는 각형 강관폭 /] ;
    VarIn8[/입력변수: 응력상관계수 /] ;
    end
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.3 (1)"])
		C --> Variable_def

	  AC["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{y}t^{2}[0.5H_{b}(1&plus;\beta)/(1-\beta)&plus;[2BB_{b}(1&plus;\beta)/(1-\beta)]^{0.5}]Q_{f}'>-------------------------------------------------------------------------------------------------------------------------"] ;

    H["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>------------------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>-----------------------"]
    J["주강관벽 소성화의 한계상태"]
    E["<img src='https://latex.codecogs.com/svg.image?\beta>0.85'>--------------------"]
    F(["검토안함"]) ;
    Variable_def-->E--No--->J-->AC-->I-->H
    E--yes-->F
    """

    @rule_method
    def limit_state_of_chord_plastification(fIFy,fIt,fIHb,fIbeta,fIB,fIBb,fIQf) -> RuleUnitResult:
        """주강관벽 소성화의 한계상태

        Args:
            fIFy (float): 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIbeta (float): 폭 비
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIBb (float): 접합평면과 90를 이루는 각형 지강관의 폭
            fIQf (float): 응력상관계수

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (1)의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIHb, float)
        assert isinstance(fIbeta, float)
        assert 0 <= fIbeta < 0.85
        assert isinstance(fIB, float)
        assert isinstance(fIBb, float)
        assert isinstance(fIQf, float)

        fOphi = 1.0

        if 0 <= fIbeta < 0.85 :
          fOMnA = fIFy * fIt**2 * (0.5 * fIHb * (1 + fIbeta) / (1 - fIbeta) + ((2 * fIB * fIBb) * (1 + fIbeta) / (1 - fIbeta))**0.5) * fIQf

        return RuleUnitResult(
            result_variables = {
                "fOMn": fOMn,
                "fOphi": fOphi,
            }
        )