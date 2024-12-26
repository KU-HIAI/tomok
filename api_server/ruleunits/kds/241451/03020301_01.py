import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03020301_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3.1 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '감소된 지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.1 지지력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 감소된 지지력];
    B["KDS 24 14 51 3.2.3.1 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarOut1[/출력변수: 감소된 지지력/];
		VarIn1[/입력변수: 저항계수/];
		VarIn2[/입력변수: 공칭지지력/];

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.2.3.1 (1)"])
		C --> Variable_def;

		Variable_def--->D

		E(["감소된 지지력"])
		D{"<img src='https://latex.codecogs.com/svg.image?&space;q_{R}=\phi&space;q_{n}=\phi&space;q_{ult}'>---------------------------------"}

		D-->E
    """

    @rule_method
    def Diminished_Support (fIphi,fIqn) -> RuleUnitResult:
        """감소된 지지력

        Args:
            fIphi (float): 저항계수
            fIqn (float): 공칭지지력

        Returns:
            fOqR (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (1)의 값
        """

        assert isinstance(fIphi, float)
        assert isinstance(fIqn, float)

        fOqR = fIphi * fIqn

        return RuleUnitResult(
            result_variables = {
                "fOqR": fOqR,
            }
        )