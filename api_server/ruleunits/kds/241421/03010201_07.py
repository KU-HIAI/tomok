import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010201_07(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.1 (7)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '경량콘크리트의 인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (7)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경량콘크리트의 인장강도];
    B["KDS 24 14 21 3.1.2.1 (7)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 평균인장강도/];
    VarIn2[/입력변수: 절대건조 밀도의 상한값/];
 	  VarOut1[/출력변수: 경량콘크리트의 인장강도/];

	  VarOut1~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.1 (7)"])
		C --> Variable_def

		Variable_def---->D-->G

		D["경량콘크리트 인장강도<img src='https://latex.codecogs.com/svg.image?&space;=f_{ctm}(0.4+0.6\gamma_{g}/2200) '>--------------------------------------------------------"]

		D~~~ |"KDS 24 14 21 Table 3.1-1"| D
		G(["경량콘크리트의 인장강도"]);
    """

    @rule_method
    def Tensile_strength_of_lightweight_concrete(fIfctm,fIgammag) -> RuleUnitResult:
        """경량콘크리트의 인장강도

        Args:
            fIfctm (float): 평균인장강도
            fIgammag (float): 절대건조 밀도의 상한값

        Returns:
            fOtestlc (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (7)의 값 1
            fOetal (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.1 강도 (7)의 값 2
        """

        assert isinstance(fIfctm, float)
        assert isinstance(fIgammag, float)

        fOetal = 0.40 + 0.60 * fIgammag / 2200
        fOtestlc = fOetal * fIfctm

        return RuleUnitResult(
            result_variables = {
                "fOtestlc": fOtestlc,
            }
        )