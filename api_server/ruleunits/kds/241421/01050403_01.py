import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.4.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '소성회전'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.4 소성해석
    1.5.4.3 회전 능력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소성회전];
    B["KDS 24 14 21 1.5.4.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 단면의 압축 연단에서 중립축까지 깊이/];
    VarIn2[/입력변수: 단면의 유효깊이/] ;
    VarIn3[/입력변수: 28일 콘크리트 공시체의 기준압축강도/] ;
		VarIn4[/입력변수: 회전각/] ;
		VarIn5[/입력변수: 허용 소성회전각/] ;

		VarIn1~~~VarIn4
   	VarIn2~~~VarIn4
		VarIn3~~~VarIn4

   	VarIn2~~~VarIn5
		VarIn3~~~VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.4.3 (1)"])
		C --> Variable_def

		Variable_def---->G
		Variable_def---->F
		G--->D
		G{"<img src='https://latex.codecogs.com/svg.image?c/d\leq&space;0.3(f_{ck}\leq40MPa)\:\:\:or\;\:c/d\leq&space;0.23(f_{ck}>40MPa)'>--------------------------------------------------------"};
		D([Pass or Fail]) ;
		F{"<img src='https://latex.codecogs.com/svg.image?\Theta_{s}\leq\Theta_{PI,d}'>--------------------------------------------------------"};
		F---->D
    """

    @rule_method
    def plasticity_rotation(fIc,fId,fIfck,fIThetas,fIThetap) -> RuleUnitResult:
        """소성회전

        Args:
            fIc (float) : 단면의 압축 연단에서 중립축까지 깊이
            fId (float) : 단면의 유효깊이
            fIfck (float) : 28일 콘크리트 공시체의 기준압축강도
            fIThetas (float) : 회전각
            fIThetap (float) : 허용 소성회전각

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  1.5.4.3 회전 능력 (1)의 판단 결과
        """

        assert isinstance(fIc, float)
        assert isinstance(fId, float)
        assert fId != 0
        assert isinstance(fIfck, float)
        assert isinstance(fIThetas, float)
        assert isinstance(fIThetap, float)

        if fIfck <= 40 :
          if fIc/fId <= 0.30 and fIThetas <= fIThetap :
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

        else:
          if fIc/fId <= 0.23 and fIThetas <= fIThetap :
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