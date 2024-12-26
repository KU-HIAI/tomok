import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010102_07_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.2 (7) ②'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '최소 주인장 철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (7)
    ②
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최소 주인장 철근량];
    B["KDS 24 14 21 4.1.1.2 (7) ②"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 프리스트레스 영향을 무시한 거더의 균열휨모멘트/];
    VarIn2[/입력변수: 철근만에 의한 단면 내부팔길이/] ;
		VarIn3[/입력변수: 철근의 항복강도/] ;
    VarIn4[/입력변수: 주인장 철근량/] ;

		VarOut1[/출력변수: 최소 주인장 철근량/];

		VarOut1  ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.2 (7) ②"])
		C --> Variable_def

		Variable_def --> D --> E(["pass/fail"])

    D["\n <img src='https://latex.codecogs.com/svg.image? A_{s,min} = \frac{M_{cr}}{z_{s}f_{y}} < A_{s}'>-----------------------------"];
    """

    @rule_method
    def minimum_amount_of_main_tensile_reinforcement(fIMcr,fIzs,fIfy,fIAs) -> RuleUnitResult:
        """최소 주인장 철근량

        Args:
            fIMcr (float): 프리스트레스 영향을 무시한 거더의 균열휨모멘트
            fIzs (float): 철근만에 의한 단면 내부팔길이
            fIfy (float): 철근의 항복강도
            fIAs (float): 주인장 철근량

        Returns:
            fOAsmin (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (7) ②의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (7) ②의 판단결과
        """

        assert isinstance(fIMcr, float)
        assert isinstance(fIzs, float)
        assert 0 != fIzs
        assert isinstance(fIfy, float)
        assert 0 != fIfy

        fOAsmin = fIMcr / (fIzs*fIfy)

        if fOAsmin < fIAs :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  "fOAsmin": fOAsmin,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
                  "fOAsmin": fOAsmin,
              }
          )