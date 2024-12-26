import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균압축강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균압축강도];
    B["KDS 24 14 21 3.1.2.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 평균압축강도와 기준압축강도의 차이/];
    VarIn2[/입력변수: 기준압축강도/] ;
 	  VarOut1[/출력변수: 평균압축강도/];
	  VarOut1~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (2)"])
		C --> Variable_def

		Variable_def---->D
	  D{"<img src='https://latex.codecogs.com/svg.image?&space; f_{ck}'>--------------------------------------------------------"}
		D--40MPa이하--->E
		D--60MPa이상--->H
    D--그 이외--->G
		E["<img src='https://latex.codecogs.com/svg.image?&space;\Delta f=4MPa'>--------------------------------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?&space;\Delta f=6MPa'>--------------------------------------------------------"]
		G["직선보간"]
		I["<img src='https://latex.codecogs.com/svg.image?&space;f_{cm}=\Delta f+f_{ck}'>--------------------------------------------------------"]
		E & H & G--->I--->J
		J(["평균압축강도"])
    """

    @rule_method
    def Average_compressive_strength(fIfck) -> RuleUnitResult:
        """평균압축강도

        Args:
            fOfcm (float): 평균압축강도
            fOdeltaf (float): 평균압축강도와 기준압축강도의 차이
            fIfck (float): 기준압축강도

        Returns:
            fOfcm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (2)의 값 1
            fOdeltaf (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (2)의 값 2
        """

        assert isinstance(fIfck, float)

        if fIfck <= 40:
          fOdeltaf = 4
        elif fIfck >= 60:
          fOdeltaf = 6
        else:
          fOdeltaf = fIfck / 10

        fOfcm = fIfck + fOdeltaf

        return RuleUnitResult(
            result_variables = {
                "fOfcm": fOfcm,
                }
            )