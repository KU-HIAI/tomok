import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050703_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.7.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '프리스트레스 힘'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.7 프리스트레스트 구조물
    1.5.7.3 긴장한 뒤 프리스트레스 힘의 계산
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레스 힘];
    B["KDS 24 14 21 1.5.7.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 긴장 도입 직후의 프리스트레싱 강재의 응력/];
    VarIn2[/입력변수: 프리스트레스 강재의 기준항복강도/] ;
	 	VarOut1[/출력변수: 시간 t_0에서 콘크리트에 전달되는 프리스트레스 힘/];


	  VarOut1~~~~VarIn1
		VarOut1~~~~VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.7.3 (1)"])
		C --> Variable_def

		Variable_def--->F
		F["<img src='https://latex.codecogs.com/svg.image?f_{pmo}=min(0.75f_{py},0.85f_{py})'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?P_{mo}=A_{p}f_{pmo}'>--------------------------------------------------------"]
		F--->D

		D--->E
		E(["시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘"]);
    """

    @rule_method
    def prestress_force(fIPmo,fIfpy,fIAp) -> RuleUnitResult:
        """프리스트레스 힘

        Args:
            fIPmo (float) : 시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘
            fIfpy (float) : 프리스트레스 강재의 기준항복강도
            fIAp (float) : 프리스트레싱 강재의 단면적

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  1.5.7.3 긴장한 뒤 프리스트레스 힘의 계산 (1)의 판단 결과
        """

        assert isinstance(fIPmo, float)
        assert isinstance(fIfpy, float)
        assert isinstance(fIAp, float)

        fOfpmo = min(0.75 * fIfpy, 0.85 * fIfpy)

        if fIPmo <= fIAp * fOfpmo :
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