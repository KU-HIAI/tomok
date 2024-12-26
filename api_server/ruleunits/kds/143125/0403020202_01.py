import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020202_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.2 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '주강관벽 소성화의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 주강관벽 소성화의 한계상태]
	  B["KDS 14 31 25 4.3.2.2.2 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 지주강관벽 소성화의 한계상태/] ;

	  VarIn1[/입력변수: 강재의 최소인장강도/]
	  VarIn2[/입력변수: 주강관의 두께/]
	  VarIn3[/입력변수: 각형강관에서만 적용할 수 있는 하중길이 변수/]
	  VarIn4[/입력변수: 폭비/]
	  VarIn5[/입력변수: 주강관 응력상관계수/]

	  VarOut1  ~~~ VarIn1 &  VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 &  VarIn5

		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.2 (1)"])
		C --> Variable_def

	  Variable_def -->D
    D-->E

    E -->U(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>--------------------"])

    E(["<img src='https://latex.codecogs.com/svg.image?P_{n}sin\theta=F_{y}t^{2}[2\eta/(1-\beta)&plus;4/(1-\beta)^{0.5}]Q_{f}'>---------------------------------------------------------------------------------------------------"]);
    D["<img src='https://latex.codecogs.com/svg.image?\phi=1.00'>--------------------------------------------"] ;
    """

    @rule_method
    def Limit_state_of_plasticization_of_branch_member(fIFy,fIt,fIeta,fIbeta,fIQf)  -> RuleUnitResult:
        """주강관벽 소성화의 한계상태

        Args:
            fIFy (float): 강재의 최소인장강도
            fIt (float): 주강관의 두께
            fIeta (float): 각형강관에서만 적용할 수 있는 하중길이 변수
            fIbeta (float): 폭비
            fIQf (float): 주강관 응력상관계수

        Returns:
            fOPnsint (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (1)의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (1)의 값 2
            sOnone (string): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.2 T, Y, X형 접합의 압축력을 받는 지강관 (1)의 판단 결과
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fIeta, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIQf, float)

        if fIbeta <= 0.85:
          fOphi = 1.0
          fOPnsint = fIFy*fIt**2*(2*fIeta/(1-fIbeta)+4/(1-fIbeta)**0.5)*fIQf

          return RuleUnitResult(
              result_variables = {
                  "fOPnsint": fOPnsint,
                  "fOphi": fOphi,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )