import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04180502_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5.2 (3)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '항로이탈확률'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.2 항로이탈확률
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 항로이탈확률 근사적 방법];
    B["KDS 24 12 21 4.18.5.2 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 항로이탈확률/];
    VarIn1[/입력변수 : 항로이탈의 기본율/];
    VarIn2[/입력변수 : 교량의 위치에 따른 보정계수/];
    VarIn3[/입력변수 : 선박의 통과경로에 평행한 유속에 대한 보정계수/];
    VarIn4[/입력변수 : 선박의 통과경로의 직각방향 유속에 대한 보정계수/];
    VarIn5[/입력변수 : 통행선박의 밀도에 대한 보정계수/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.5.2 (3)"])
		C --> Variable_def

    D{"선박의 경우"};
    E{"바지선의 경우"};
    F["<img src='https://latex.codecogs.com/svg.image?BR=0.6\times10^{-4}'>--------------------------------------"];
    G["<img src='https://latex.codecogs.com/svg.image?BR=1.2\times10^{-4}'>--------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?PA=(BR)(R_{B})(R_{C})(R_{XC})(R_{D})'>------------------------------------------------------------------------------------"];
    I(["항로이탈확률"]);
    Variable_def--->D--->F--->H--->I
    Variable_def--->E--->G--->H
    """

    @rule_method
    def probability_of_departure_from_course(fIBRA,fIBRB,fIRb,fIRc,fIRxc,fIRd) -> RuleUnitResult:
        """항로이탈확률

        Args:
            fIBRA (float): 항로이탈의 기본율 (선박의 경우)
            fIBRB (float): 항로이탈의 기본율 (바지선의 경우)
            fIRb (float): 보정계수
            fIRc (float): 통과경로에 평행한 유속에 대한 보정계수
            fIRxc (float): 통과경로에 직각방향 유속에 대한 보정계수
            fIRd (float): 통행선박의 밀도에 대한 보정계수

        Returns:
            fOPA (float): 강교 설계기준(한계상태설계법)  4.18.5.2 항로이탈확률 (3)의 값 1
            fOBR (float): 강교 설계기준(한계상태설계법)  4.18.5.2 항로이탈확률 (3)의 값 2
        """

        assert isinstance(fIRb, float)
        assert isinstance(fIRc, float)
        assert isinstance(fIRxc, float)
        assert isinstance(fIRd, float)

        if fIBRA != 0 and fIBRB == 0 :
          fOBR = 0.6*10**-4
          fOPA = fOBR * fIRb * fIRc * fIRxc * fIRd
          return RuleUnitResult(
              result_variables = {
                  "fOPA": fOPA,
              }
          )

        if fIBRA == 0 and fIBRB != 0 :
          fOBR = 1.2*10**-4
          fOPA = fOBR * fIRb * fIRc * fIRxc * fIRd
          return RuleUnitResult(
              result_variables = {
                  "fOPA": fOPA,
              }
          )