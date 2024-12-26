import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060604_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.4 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '소요 변위연성도'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.4 전단 설계
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 소요 변위연성도]
	  B["KDS 24 17 11 4.6.6.4 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut1[/출력변수: 소요 변위연성도/] ;
	  VarOut2[/출력변수: 공칭전단강도/] ;
	  VarOut3[/출력변수: 계수/] ;
    VarIn1[/입력변수: 소요 변위연성도/] ;
    VarIn2[/입력변수: 콘크리트의 설계기준 압축강도/];
    VarIn3[/입력변수: 기둥 총 단면적/];
    VarIn4[/입력변수: 단면의 복부폭/];
    VarIn5[/입력변수: 단면유효깊이/];
    end

	  Python_Class ~~~ C(["KDS 24 17 11 4.6.6.4 (4)"])
		C --> Variable_def

	  Variable_def --> G
    D["<img src='https://latex.codecogs.com/svg.image?V_{c}=k\sqrt{f_{ck}}A_{e}'>------------------------------------"];
    E["<img src='https://latex.codecogs.com/svg.image?k=0.3-0.1(\mu&space;_{\triangle}-2)'>------------------------------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?V_{c}'>-------"]) ;
    G{"<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\Delta}\leq&space;2.0'>------------------"};
    G--Yes--> H["K = 0.3"] --> D
    G--No--> E --> D
    D-->F
    Variable_def -->I & J
    I["원형 단면, 사각형 단면"];
    J["I형 단면, 사각형 중공단면"];
    K["<img src='https://latex.codecogs.com/svg.image?A_{e}=A_{g}\times&space;0.8'>-------------------------------"];
    L["<img src='https://latex.codecogs.com/svg.image?A_{e}=b_{w}d'>-----------------------"];
    M["<img src='https://latex.codecogs.com/svg.image?A_{e}'>--------"];
    I-->K-->M
    J-->L-->M
    M-->D
    """

    @rule_method
    def nominal_shear_strength_of_concrete(fImudelt,fIfck,fIAg,fIbw,fId) -> RuleUnitResult:
        """소요 변위연성도

        Args:
            fImudelt (float): 소요 변위연성도
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIAg (float): 기둥 총 단면적
            fIbw (float): 단면의 복부폭
            fId (float): 단면유효깊이

        Returns:
            fOVc (float): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (4)의 값 1
            fOk (float): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (4)의 값 2
            fOAe (float): 교량내진설계기준(한계상태설계법) 4.6.6.4 전단 설계 (4)의 값 3
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