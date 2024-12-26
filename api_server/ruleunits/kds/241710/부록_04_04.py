import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241710_부록_04_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 10 부록 4 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-20'
    title = '콘크리트에 의한 공칭전단강도'

    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
		(4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 콘크리트에 의한 공칭전단강도]
	  B["KDS 24 17 10 부록 4 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def;
		VarIn1[/입력변수:소요 변위연성도/];
		VarIn2[/입력변수:전단 유효단면적/];
		VarIn3[/입력변수:기둥 총단면적/];
		VarIn4[/입력변수:복부 폭/];
		VarIn5[/입력변수:유효깊이/];


		VarOut1[/출력변수:콘크리트에 의한 전단강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3 & VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 17 10 부록 4 (4)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?&space;V_{c}=k\sqrt{f_{ck}}A_{e}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?k=0.3-0.1(\mu&space;_{\Delta}-2)'>---------------------------------"]
		I{소요변위 연성도 > 2}
		F{소요변위 연성도 ≤ 2}
		G([콘크리트에 의한 공칭전단강도])
		H[k = 0.3]

		Variable_def ---> I & F
		I ---> E  --->D
		F ---> H ---> D ---> G
    """

    @rule_method
    def Nominal_shear_strength_of_concrete(fImudelt,fIfck,fIAg,fIbw,fId) -> RuleUnitResult:
        """콘크리트에 의한 공칭전단강도

        Args:
            fImudelt (float): 소요 변위연성도
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIAg (float): 기둥 총 단면적
            fIbw (float): 단면의 복부폭
            fId (float): 단면유효깊이

        Returns:
            fOVc (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (4)의 값 1
            fOk (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (4)의 값 2
            fOAe (float): 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (4)의 값 3
        """

        assert isinstance(fImudelt, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIAg, float)
        assert isinstance(fIbw, float)
        assert isinstance(fId, float)

        if fImudelt <= 2.0:
          fOk = 0.3
        else:
          fOk = 0.3 - 0.1 * (fImudelt - 2)

        if fId == 0  or fIbw == 0 :
          fOAe = 0.8 * fIAg
        else:
          fOAe = fIbw * fId

        fOVc = fOk * (fIfck ** 0.5) * fOAe

        return RuleUnitResult(
            result_variables = {
                "fOVc": fOVc,
            }
        )