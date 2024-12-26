import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020304_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.4 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '설계 균열폭'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계 균열폭];
    B["KDS 24 14 21 4.2.3.4 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 최대 균열 간격/];
		VarIn2[/입력변수: 적합한 하중조합에 의해 발생된 철근 평균변형률/];
		VarIn3[/입력변수: 인접된 균열 사이 콘크리트의 평균 변형률/];
		VarOut1[/출력변수: 설계 균열폭/];
    VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.4 (1)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?\omega&space;_k=l_{r,max}(\varepsilon&space;_{sm}-\varepsilon&space;_{cm})'>---------------------------------"]
		F(["설계 균열폭"])
    """

    @rule_method
    def design_crack_width(fIlrmax,fIepsism,fIepsicm) -> RuleUnitResult:
        """설계 균열폭

        Args:
            fIlrmax (float): 최대 균열 간격
            fIepsism (float): 적합한 하중조합에 의해 발생된 철근평균변형률
            fIepsicm (float): 인접된 균열 사이 콘크리트의 평균 변형률

        Returns:
            fOwk (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 값
        """

        assert isinstance(fIlrmax, float)
        assert isinstance(fIepsism, float)
        assert isinstance(fIepsicm, float)

        fOwk = fIlrmax * (fIepsism - fIepsicm)

        return RuleUnitResult(
            result_variables = {
                "fOwk": fOwk,
            }
        )