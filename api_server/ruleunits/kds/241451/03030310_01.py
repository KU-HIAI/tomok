import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030310_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.10 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '감가된 지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.10 무리말뚝의 축방향 지지력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 감가된 지지력];
    B["KDS 24 14 51 3.3.3.10 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:감가된 지지력/]
		VarIn1[/입력변수:무리말뚝의 공칭 지지력/]
		VarIn2[/입력변수:무리말뚝의 저항계수/]

		VarOut1
		VarIn1 ~~~ VarIn2

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.10 (1)"])
		C --> Variable_def

		E["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=\phi&space;_{g}Q_{g}'>---------------------------------"]
		D([무리말뚝의 감가된 지지력])
		Variable_def ---> E ---> D
    """

    @rule_method
    def diminished_support(fIQg,fIphig) -> RuleUnitResult:
        """감가된 지지력

        Args:
            fIQg (float): 무리말뚝의 공칭 지지력
            fIphig (float): 무리말뚝의 저항계수

        Returns:
            fOQr (float): 깊은기초 설계기준(일반설계법) 3.3.3.7 인발 (3)의 값 1
        """

        assert isinstance(fIQg, float)
        assert isinstance(fIphig, float)

        fOQr = fIphig * fIQg

        return RuleUnitResult(
            result_variables = {
                "fOQr": fOQr,
              }
        )