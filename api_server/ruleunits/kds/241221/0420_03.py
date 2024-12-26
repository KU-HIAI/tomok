import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_0420_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.20 (3)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '장대레일 종하중'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.20 장대레일 종하중 : LR
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 장대레일 종하중];
    B["KDS 24 12 21 4.20 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 장대레일 종하중/];
    VarIn1[/입력변수 : 슬래브의 팽창이 고려될 수 있는 길이/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.20 (3)"])
		C --> Variable_def

    D{"레일 신축이음장치가 없을 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?f_{v0}=\pm&space;3L'>"];
    F["<img src='https://latex.codecogs.com/svg.image?f_{v0}=\pm&space;500'>"];
    G(["장대레일 종하중"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def longitudinal_load_of_longitudinal_rail(fIfvoA,fIfvoB,fIL) -> RuleUnitResult:
        """장대레일 종하중

        Args:
            fIfvoA (float): 장대레일 종하중 (레일신축이음장치가 없을 경우)
            fIfvoB (float): 장대레일 종하중 (구조물의 가동끝단에서 레일 신축이음이 있는 경우)
            fIL (float): 슬래브의 팽창이 고려될 수 있는 길이

        Returns:
            fOfvo (float): 강교 설계기준(한계상태설계법)  4.20 장대레일 종하중 : LR (3)의 값
        """

        assert isinstance(fIL, float)

        if fIfvoA != 0 and fIfvoB == 0 :
          fOfvo = 3 * fIL
          return RuleUnitResult(
              result_variables = {
                  "fOfvo": fOfvo,
              }
          )

        if fIfvoA == 0 and fIfvoB != 0 :
          fOfvo = 500
          return RuleUnitResult(
              result_variables = {
                  "fOfvo": fOfvo,
              }
          )