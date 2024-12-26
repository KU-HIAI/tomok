import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010305_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.3.5 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '볼트구멍의 지압강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.5 볼트구멍의 지압강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 볼트구멍의 지압강도]
	  B["KDS 14 31 25 4.1.3.5(1)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 볼트구멍에서 설계강도/]
    VarIn1[/입력변수: 구멍의 끝과 피접합체의 끝 또는 인접구멍의 끝까지의 거리/]
    VarIn2[/입력변수: 피접합체의 두께/]
    VarIn3[/입력변수: 피접합체의 공칭인장강도/]
    VarIn4[/입력변수: 볼트 공칭직경/]
    VarOut ~~~ VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
  	end

	  Python_Class ~~~ C(["KDS 14 31 25 4.1.3.5(1)"])
		C --> Variable_def

    Variable_def  --> D & I

    D --> E & F
    E --> G
    F --> H
    I --> J
    G & H & J --> K

	  D["표준구멍,과대구멍,단슬롯의 모든방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우"]
	  E["사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 있는 경우"]
    G([조합응력효과 무시])
    F["사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 없는 경우"]
    G["<img src='https://latex.codecogs.com/svg.image?R_n=1.2L_ctF_u\leq&space;2.4dtF_u'>---------------------------------------------------"]
    H["<img src='https://latex.codecogs.com/svg.image?R_n=1.5L_ctF_u\leq&space;3.0dtF_u'>-----------------------------------------------------"]
    I["장슬롯의 길이방향에 직각으로 작용하는 지압력의 경우"]
    J["<img src='https://latex.codecogs.com/svg.image?R_n=1.0L_ctF_u\leq&space;2.0dtF_u'>----------------------------------------------------"]
    K(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>-----------------"])
    """

    @rule_method
    def bearing_strength_of_bolt_hole(fIphiRnA,fIphiRnB,fIphiRnC,fILc,fIt,fIFu,fId) -> RuleUnitResult:
        """볼트구멍의 지압강도

        Args:
            fIphiRnA (float): 볼트구멍에서 설계강도 (표준구멍, 과대구멍, 단슬롯의 모든 방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우 사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 있는 경우)
            fIphiRnB (float): 볼트구멍에서 설계강도 (표준구멍, 과대구멍, 단슬롯의 모든 방향에 대한 지압력 또는 장슬롯의 길이방향에 평행으로 작용하는 지압력의 경우 사용하중상태에서 볼트구멍의 변형을 설계에 고려할 필요가 없는 경우)
            fIphiRnC (float): 볼트구멍에서 설계강도 (장슬롯의 길이방향에 직각으로 작용하는 지압력의 경우)
            fILc (float): 구멍의 끝과 피접합재의 끝 또는 인접구멍의 끝까지의 거리
            fIt (float): 피접합재의 두께
            fIFu (float): 피접합재의 공칭인장강도
            fId (float): 볼트 공칭직경

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.5 볼트구멍의 지압강도 (1)의 값
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.5 볼트구멍의 지압강도 (1)의 판단 결과
        """

        assert isinstance(fILc, float)
        assert isinstance(fIt, float)
        assert isinstance(fIFu, float)
        assert isinstance(fId, float)

        if fIphiRnA != 0 and fIphiRnB == 0 and fIphiRnC == 0 :
          fOphiRn = 0.75 * (1.2 * fILc * fIt * fIFu)
          if fOphiRn <= 0.75 * (2.4 * fId * fIt * fIFu) :
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )
          else:
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )

        elif fIphiRnA == 0 and fIphiRnB != 0 and fIphiRnC == 0 :
          fOphiRn = 0.75 * (1.5 * fILc * fIt * fIFu)
          if fOphiRn <= 0.75 * (3.0 * fId * fIt * fIFu) :
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )
          else:
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )

        elif fIphiRnA == 0 and fIphiRnB == 0 and fIphiRnC != 0 :
          fOphiRn = 0.75 * (1.0 * fILc * fIt * fIFu)
          if fOphiRn <= 0.75 * (2.0 * fId * fIt * fIFu) :
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )
          else:
            return RuleUnitResult(
                  result_variables = {
                      "fOphiRn": fOphiRn,
                      "pass_fail": True,
                  }
              )

        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )