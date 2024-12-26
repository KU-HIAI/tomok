import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030203_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.3 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '비균일 하중분포로 인한 국부항복의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 조합력을 받는 접합부]
	  B["KDS 14 31 25 4.3.3.2.3 (3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 설계강도/] ;
    VarOut2[/출력변수: 소성화의 한계상태/] ;
    VarIn1[/입력변수: 지강관의 항복강도/] ;
    VarIn2[/입력변수: 휨축에 대한 지강관의 소성단면계수/] ;
    VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
    VarIn4[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
    VarIn5[/입력변수: 지강관의 두께/] ;
    VarIn6[/입력변수: 접합평면과 90º를 이루는 각형 강관폭/] ;
    VarIn7[/입력변수: 주강관의 항복강도/] ;

    end
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.3 (3)"])
		C --> Variable_def

    P["비균일 하중분포로 인한 국부항복의 한계상태"]
    Q["<img src='https://latex.codecogs.com/svg.image?b_{eoi}=[10/(B/t)][F_{y}t/(F_{yb}t_{b})]B_{b}\leq&space;B_{b}'>-------------------------------------------------------------------------------------------"]
    R["<img src='https://latex.codecogs.com/svg.image?M_{n}=F_{yb}[Z_{b}-0.5(1-b_{eoi}/B_{b})^{2}B_{b}^{2}t_{b}]'>-------------------------------------------------------------------------------------"]
    S["<img src='https://latex.codecogs.com/svg.image?\phi&space;M_{n}'>------------------"] ;
    T(["검토안함"]) ;
    U["<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>-----------------------"]


    Variable_def-->O--No--->P-->Q-->U
    U-->R-->S
    O--yes-->T

    """

    @rule_method
    def limit_state_of_local_yielding_non_uniform_load(fIFyb,fIZb,fIB,fIBb,fItb,fIbeta,fIt,fIFy) -> RuleUnitResult:
        """비균일 하중분포로 인한 국부항복의 한계상태

        Args:
            fIFyb (float): 지강관의 항복강도
            fIZb (float): 휨축에 대한 지강관의 소성단면계수
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIBb (float): 접합평면과 90°를 이루는 각형 지강관의 폭
            fItb (float): 지강관의 두께
            fIbeta (float): 폭 비
            fIt (float): 주강관의 두께
            fIFy (float): 주강관의 항복강도

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (3)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (3)의 값 2
            fObeoi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (3)의 값 3
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.3 T, X형 접합에서 지강관의 면외 휨모멘트 (3)의 판단 결과
        """

        assert isinstance(fIFyb, float)
        assert fIFyb !=0
        assert isinstance(fIZb, float)
        assert isinstance(fIB, float)
        assert fIB !=0
        assert isinstance(fIBb, float)
        assert fIBb !=0
        assert isinstance(fItb, float)
        assert fItb !=0
        assert isinstance(fIbeta, float)
        assert fItb >= 0.85
        assert isinstance(fIt, float)
        assert fIt !=0
        assert isinstance(fIFy, float)
        assert fItb !=0

        fOphi = 0.95

        fObeoi = (10/(fIB/fIt))*(fIFy*fIt/(fIFyb*fItb))*fIBb

        if fIbeta >= 0.85 :
          fOMn = 0.95*fIFyb*(fIZb-0.5*((1-(fObeoi/fIBb)**2)*fIBb**2*fItb))

        if fObeoi <= fIBb:
          return RuleUnitResult(
              result_variables = {
                  "fOMn": fOMn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )