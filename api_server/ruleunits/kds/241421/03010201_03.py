import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균압축강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균압축강도];
    B["KDS 24 14 21 3.1.2.1 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 재령 28일에서 콘크리트 평균압축강도/];
    VarIn2[/입력변수: 평균압축강도/] ;
    VarIn3[/입력변수: 강도 보정 계수/] ;
    VarIn4[/입력변수: 콘크리트의 재령/] ;
    VarIn5[/입력변수: 시멘트 종류와 양생방법에 따른 상수/] ;
 	  VarOut1[/출력변수: 재령 t일에서 콘크리트 평균압축강도/];
	  VarOut1~~~VarIn1 & VarIn2 &  VarIn3 &  VarIn4 &  VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (3)"])
		C --> Variable_def

		Variable_def---->D
	  D{"<img src='https://latex.codecogs.com/svg.image?&space; \beta_{sc}'>--------------------------------------------------------"}
		D--1종 시멘트 습윤 양생--->E
		D--1종 시멘트 증기 양생--->F
    D--3종 시멘트 습윤 양생--->G
		D--3종 시멘트 증기 양생--->H
		D--2종 시멘트--->I
		E["시멘트 종류와 양생방법에 따른 상수=0.35"]
		F["시멘트 종류와 양생방법에 따른 상수=0.15"]
    G["시멘트 종류와 양생방법에 따른 상수=0.25"]
    H["시멘트 종류와 양생방법에 따른 상수=0.12"]
    I["시멘트 종류와 양생방법에 따른 상수=0.40"]
		J["<img src='https://latex.codecogs.com/svg.image?&space;\beta_{cc}=exp\left\{\beta_{sc}[1-(\frac{28}{t})^{1/2}]\right\}'>--------------------------------------------------------"]
    E & F & G & H & I---->J
    K["<img src='https://latex.codecogs.com/svg.image?f_{cm}(t)=\beta&space;_{cc}(t)f_{cm}'>--------------------------------------------------------"]
    J---->K--->L
    L(["재령 t일에서 콘크리트 평균압축강도"])
    """

    @rule_method
    def Average_compressive_strength(fIfcm,fIt,fIbetasc) -> RuleUnitResult:
        """콘크리트의 각 재령에서 평균압축강도

        Args:
            fIfcm (float): 재령 28일에서 콘크리트 평균압축강도
            fIt (float): 콘크리트의 재령
            fIbetasc (float): 시멘트 종류와 양생방법에 따른 상수

        Returns:
            fOfcmt (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (3)의 값 1
            fObetacc (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (3)의 값 2
        """

        assert isinstance(fIfcm, float)
        assert isinstance(fIt, float)
        assert isinstance(fIbetasc, float)

        import numpy as np
        fObetacc = np.exp(fIbetasc * (1 - (28/fIt)**0.5))
        fOfcmt = fObetacc * fIfcm

        return RuleUnitResult(
            result_variables = {
                "fOfcmt": fOfcmt,
                }
            )