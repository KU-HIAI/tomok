import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020303_06(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.3 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '평균지름'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.3 간접 균열 제어
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 평균지름];
    B["KDS 24 14 21 4.2.3.3 (6)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 평균 지름/];
		VarIn2[/입력변수: 철근 i의 지름/];
		VarIn3[/입력변수: 등가지름/];
		VarOut1[/출력변수: 철근지름/];
    VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.3 (6)"])
		C --> Variable_def

		Variable_def--상이한 철근 지름 혼합하여 사용한 단면-->D--->F
		Variable_def--다발철근을 사용할 경우-->E--->F
		D["<img src='https://latex.codecogs.com/svg.image?d_{b,m}=\sum&space;d^2_{b,i}/d_{b,i}'>---------------------------------"]
		E["철근지름=등가지름"]
		F(["평균지름"])
    """

    @rule_method
    def average_diameter(fIdbi) -> RuleUnitResult:
        """평균지름

        Args:
            fIdbi (float): 철근 i 지름

        Returns:
            fOdbm (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (6)의 값
        """

        assert isinstance(fIdbi, float)

        temp1 = sum(fIdbi[j] for j in range(i))
        temp2 = sum((fIdbi[j])**2 for j in range(i))

        fOdbm = temp2 / temp1

        return RuleUnitResult(
            result_variables = {
                "fOdbm": fOdbm,
            }
        )