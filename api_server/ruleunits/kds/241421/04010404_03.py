import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010404_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '전단철근이 필요하지 않은 위험단면 둘레길이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근이 필요하지 않은 위험단면 둘레길이];
    B["KDS 24 14 21 4.1.4.4 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 전단력/];
		VarIn2[/입력변수: 콘크리트가 기여하는 설계전단강도/];
		VarIn3[/입력변수: 유효깊이/];

		VarOut1[/출력변수: 둘레길이/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.4 (3)"])
		C --> Variable_def

		Variable_def--->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?u_{out,ef}=\frac{V_u}{v&space;_{cd}d}'>---------------------------------"]
		E(["둘레 길이"])
    """

    @rule_method
    def perimeter_of_critical_section(fIVu,fIVcd,fId) -> RuleUnitResult:
        """전단철근이 필요하지 않은 위험단면 둘레길이

        Args:
            fIVu (float): 전단력
            fIVcd (float): 콘크리트가 기여하는 설계전단강도
            fId (float): 유효깊이

        Returns:
            fOuout (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (3)의 값
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIVcd, float)
        assert fIVcd != 0
        assert isinstance(fId, float)
        assert fId != 0

        fOuout = fIVu / (fIVcd * fId) * 1000

        return RuleUnitResult(
            result_variables = {
                "fOuout": fOuout,
            }
        )