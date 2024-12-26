import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403030202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '측벽 국부좌굴의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 측벽 국부좌굴의 한계상태]
	  B["KDS 14 31 25 4.3.3.2.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 측벽 국부좌굴의 한계상태/] ;
    VarIn1[/입력변수: T형 접합에 대한 항복강도/] ;
    VarIn2[/입력변수: X형 접합에 대한 항복강도의 0.8배/] ;
    VarIn3[/입력변수: 주강관의 두께/] ;
    VarIn4[/입력변수: 접합평면에서 측정한 각형 지강관의 높/] ;
    VarIn5[/입력변수: 폭비/] ;
    end
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~  VarIn4 & VarIn5

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2.2 (2)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?M_{n}=0.5F_{y}^{*}t(H_{b}&plus;5t)^{2}'>-----------------------------------------------------"] ;
    H(["<img src='https://latex.codecogs.com/svg.image?\space M_{n}'>-----------"]) ;
    J["측벽 국부좌의 한계상태 검토"]
    E["<img src='https://latex.codecogs.com/svg.image?\beta<0.85'>--------------------"]
    F(["검토안함"]) ;
    Variable_def-->E--No--->J-->D
    D-->H
    E--yes-->F
    """

    @rule_method
    def limit_state_of_sidewall_local_buckling(fIMnA,fIMnB,fIFy,fIt,fIHb,fIbeta) -> RuleUnitResult:
        """측벽 국부좌굴의 한계상태

        Args:
            fIMnA (float): 측벽 국부좌굴의 한계상태 (T형 접합)
            fIMnB (float): 측벽 국부좌굴의 한계상태 (X형 접합)
            fIFy (float) : 주강관의 항복강도
            fIt (float): 주강관의 두께
            fIHb (float): 접합평면에서 측정한 각형 지강관의 높이
            fIbeta (float): 폭비

        Returns:
            fOMn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (2)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (2)의 값 2
            fOFystar (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (2)의 값 3
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.2 T, X형 접합에서 지강관의 면내 휨모멘트 (2)의 판단 결과
        """

        assert isinstance(fOFystar, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIHb, float)
        assert isinstance(fIbeta, float)
        assert fIbeta >= 0.85

        import math

        if fIbeta >= 0.85 :
          fOphi = 1.0
          if fIMnA != 0 and fIMnB == 0 :
            fOFystar = fIFy
            fOMn = 0.5*fOFystar*fIt*(fIHb+5*fIt)**2
            return RuleUnitResult(
                result_variables = {
                    "fOMn": fOMn,
                }
            )
          elif fIMnA == 0 and fIMnB != 0 :
            fOFystar = 0.8 * fIFy
            fOMn = 0.5*fOFystar*fIt*(fIHb+5*fIt)**2
            return RuleUnitResult(
                result_variables = {
                    "fOMn": fOMn,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )