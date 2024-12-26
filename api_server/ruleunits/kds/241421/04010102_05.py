import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010102_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '최소편심 및 휨모멘트'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소편심 및 휨모멘트];
    B["KDS 24 14 21 4.1.1.2 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 축력/];
    VarIn2[/입력변수: 최소 편심 eo/] ;
		VarIn3[/입력변수: 단면의 깊이/] ;
		VarIn4[/입력변수: 실제 휨모멘트/] ;
		VarOut1[/출력변수: 계산한 휨모멘트/];

		VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.2 (5)"])
		C --> Variable_def

		Variable_def--->F
		F--->D-->E
		F{"<img src='https://latex.codecogs.com/svg.image?&space;20mm\leq&space;e_{0}=h/30'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?M_{u}&space;\geq&space;e_{o}N_{u}'>---------------------------------"}
		E(["Pass or Fail"])
    """

    @rule_method
    def Minimum_eccentricity_and_bending_moment(fINu,fIMu,fIh) -> RuleUnitResult:
        """최소편심 및 휨모멘트

        Args:
            fINu (float): 축력
            fIMu (float): 휨모멘트
            fIh (float): 단면의 깊이

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (5)의 판단 결과
            fOeo (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (5)의 값
        """

        assert isinstance(fINu, float)
        assert isinstance(fIMu, float)
        assert isinstance(fIh, float)

        fOeo = fIh / 30

        if fOeo >= 20 and fIMu > fOeo * fINu :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )