import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041807_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.7 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '수리동적질량계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.7 선박충돌에너지
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 수리동적질량계수];
    B["KDS 24 12 21 4.18.7 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 수리동적질량계수/];
    VarIn1[/입력변수 : 용골과 수로바닥과의 간격/];
    VarIn2[/입력변수 : 선박의 흘수/];
    VarIn3[/입력변수 : 선박의 바닥과 수로의 바닥간의 간격/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.7 (2)"])
		C --> Variable_def

    L["용골과 수로바닥과의 간격=선박의 바닥과 수로의 바닥간의 간격"]
    K{"용골과 수로바닥과의 간격과 선박의 흘수 관계"}
    D["용골과 수로바닥과의 간격>선박의 흘수X0.5"];
    E["용골과 수로바닥과의 간격<선박의 흘수X0.1"];
    F["선박의 흘수X0.1<용골과 수로바닥과의 간격<선박의 흘수X0.5"];
    G["<img src='https://latex.codecogs.com/svg.image?C_{H}=1.05'>-------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?C_{H}=1.25'>-------------------------------"];
    I["적절히 보간"];
    J(["등가 정적선박충격하중"]);
    Variable_def--->L--->K--->D--->G--->J
    K--->E--->H--->J
    K--->F--->I--->J
    """

    @rule_method
    def mathematical_dynamic_mass_factor(fIdkeebw,fIdraft) -> RuleUnitResult:
        """수리동적질량계수

        Args:
            fIdkeebw (float): 용골과 수로바닥과의 간격
            fIdraft (float): 선박의 흘수

        Returns:
            fOCH (float): 강교 설계기준(한계상태설계법)  4.18.7 선박충돌에너지 (2)의 값
        """

        assert isinstance(fIdkeebw, float)
        assert isinstance(fIdraft, float)

        if fIdkeebw > fIdraft*0.5:
          fOCH = 1.05
        if fIdkeebw < fIdraft*0.1:
          fOCH = 1.25
        if fIdraft*0.1 <= fIdkeebw <= fIdraft*0.5:
          fOCH = 1.25 - 0.2 * (fIdkeebw - fIdraft * 0.1) / (fIdraft * 0.5 - fIdraft * 0.1)

        return RuleUnitResult(
            result_variables = {
                "fOCH": fOCH,
            }
        )