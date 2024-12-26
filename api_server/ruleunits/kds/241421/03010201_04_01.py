import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_04_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (4) ①'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '평균인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (4)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균인장강도];
    B["KDS 24 14 21 3.1.2.1 (4) ①"];
    A ~~~ B
    end
	  subgraph Variable_def;
	  VarIn1[/입력변수: 쪼갬 인장강도의 평균값/];
 	  VarOut1[/출력변수: 평균인장강도/];



	  VarOut1 ~~~VarIn1
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (4) ①"])
		C --> Variable_def

		Variable_def---->D--->F

		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{ctm}=0.9f_{spm'>--------------------------------------------------------"]
		F(["평균인장강도"]);

    """

    @rule_method
    def Concrete_tensile_strength(fIfspm) -> RuleUnitResult:
        """평균인장강도

        Args:
            fIfspm (float): 쪼갬 인장강도의 평균값

        Returns:
            fOfctm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (4) ①의 값
        """

        assert isinstance(fIfspm, float)

        fOfctm = 0.9 * fIfspm

        return RuleUnitResult(
            result_variables = {
                "fOfctm": fOfctm,
          }
        )