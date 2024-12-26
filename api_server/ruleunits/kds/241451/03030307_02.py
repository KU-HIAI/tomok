import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030307_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.7 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '감가된 인발저항력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.7 인발
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발];
    B["KDS 24 14 51 3.3.3.7 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:감가된 인발저항력/]
		VarIn1[/입력변수:주면저항에 의한 공칭인발저항력/]
		VarIn2[/입력변수:인발저항력에 대한 저항계수/]

		VarOut1
		VarIn1 ~~~ VarIn2
    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.7 (2)"])
		C --> Variable_def

		F["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=Q_{u}Q_{s}'>---------------------------------"]
		D([감가된 일반저항력])

		Variable_def ---> F ---> D
    """

    @rule_method
    def reduced_pull_resistance(fIQs,fIrespul) -> RuleUnitResult:
        """감가된 인발저항력

        Args:
            fIQs (float): 주면저항에 의한 공칭 인발저항력
            fIrespul (float): 인발저항력에 대한 저항계수

        Returns:
            fOQr (float): 깊은기초 설계기준(일반설계법) 3.3.3.7 인발 (2)의 값
        """

        assert isinstance(fIQs, float)
        assert isinstance(fIrespul, float)

        fOQr = fIrespul * fIQs
        return RuleUnitResult(
            result_variables = {
                "fOQr": fOQr,
            }
        )