import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050707_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.7.7 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '사용한계상태에서 프리스트레스 힘'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.7 프리스트레스트 구조물
    1.5.7.7 사용한계상태 및 피로한계상태 시에서의 프리스트레스 효과
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 사용한계상태에서 프리스트레스 힘];
    B["KDS 24 14 21 1.5.7.7 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 상한 계수긴장력/];
		VarOut2[/출력변수: 하한 계수긴장력/];
    VarIn1[/입력변수: 상한 하중계수/];
    VarIn2[/입력변수: 하한 하중계수/];
    VarIn3[/입력변수: 시간 t가 t0를 초과할 때의 프리스트레스 힘의 평균값/];

	  VarOut1 & VarOut2~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.7.7 (1)"])
		C --> Variable_def

		Variable_def---->D-->G
		Variable_def---->F-->H

		D["<img src='https://latex.codecogs.com/svg.image?&space;P_{k,u}=\gamma_{ps,u}P_{m,t}'>--------------------------------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?P_{k,l}=\gamma_{ps,l}P_{m,t}'>--------------------------------------------------------"]

		G(["상한 수긴장력"]);
		H(["하한 계수긴장력"]);
    """

    @rule_method
    def prestress_force_at_serviceability_limit_state(fIgampsu,fIgampsl,fIPmt) -> RuleUnitResult:
        """사용한계상태에서 프리스트레스 힘

        Args:
            fIgampsu (float) : 상한 하중계수
            fIgampsl (float) : 하한 하중계수
            fIPmt (float) : 시간 t가 t0를 초과할 때의 프리스트레스 힘의 평균값


        Returns:
            fOPku (float): 콘크리트교 설계기준 (한계상태설계법)  1.5.7.7 사용한계상태 및 피로한계상태 시에서의 프리스트레스 효과 (1)의 값 1
            fOPkl (float): 콘크리트교 설계기준 (한계상태설계법)  1.5.7.7 사용한계상태 및 피로한계상태 시에서의 프리스트레스 효과 (1)의 값 2
        """

        assert isinstance(fIgampsu, float)
        assert isinstance(fIgampsl, float)
        assert isinstance(fIPmt, float)

        fOPku = fIgampsu * fIPmt
        fOPkl = fIgampsl * fIPmt

        return RuleUnitResult(
            result_variables = {
                "fOPku": fOPku,
                "fOPkl": fOPkl,
            }
        )