import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010204_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.4 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '종방향 전단응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 전단응력];
    B["KDS 24 14 21 4.1.2.4 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 구간 Δx에서 플랜지 단면에 작용하는 종방향력의차이/];
		VarIn2[/입력변수: 계면에서 플랜지의 두께/];
		VarIn3[/입력변수: 검토하는 구간 길이/];
		VarOut1[/출력변수: 종방향 전단응력/];
		VarOut1~~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.4 (1)"])
		C --> Variable_def

		Variable_def--->E--->D
		E["<img src='https://latex.codecogs.com/svg.image?v&space;_{uf}=\frac{\Delta&space;C}{t_{f}\Delta&space;x}'>---------------------------------"]
		D(["종방향 전단응력"])
    """

    @rule_method
    def Longitudinal_shear_stress(fIdeltaC,fIdeltax,fItf) -> RuleUnitResult:
        """종방향 전단응력

        Args:
            fIdeltaC (float): 구간 Δx에서 플랜지 단면에 작용하는 종방향력의차이
            fIdeltax (float): 계면에서 플랜지의 두께
            fItf (float): 검토하는 구간 길이

        Returns:
            fOvuf (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (1)의 값
        """

        assert isinstance(fIdeltaC, float)
        assert isinstance(fIdeltax, float)
        assert fIdeltax != 0
        assert isinstance(fItf, float)
        assert fItf != 0

        fOvuf = fIdeltaC / fItf / fIdeltax

        return RuleUnitResult(
            result_variables = {
                "fOvuf": fOvuf,
            }
        )