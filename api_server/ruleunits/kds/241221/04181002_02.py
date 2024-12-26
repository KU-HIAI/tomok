import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04181002_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.10.2 (2)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '감소계수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.10.2 갑판실과의 충돌
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 감소계수];
    B["KDS 24 12 21 4.18.10.2 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 감소계수/];
    VarIn1[/입력변수 : 선박의 적재중량 톤수/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.10.2 (2)"])
		C --> Variable_def

    D{"선박이 100,000DWT 이상인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?R_{DH}=0.1'>"];
    F["<img src='https://latex.codecogs.com/svg.image?R_{DH}=0.2-(DWT/10,000)\times&space;0.10'>----------------------"];
    G(["감소계수"]);
    Variable_def--->D--Yes--->E--->G
    D--No--->F--->G
    """

    @rule_method
    def reduction_factor(fIDWT) -> RuleUnitResult:
        """감소계수

        Args:
            fIDWT (float): 선박의 적재중량톤수

        Returns:
            fORdh (float): 강교 설계기준(한계상태설계법)  4.18.10.2 갑판실과의 충돌 (2)의 값
        """

        assert isinstance(fIDWT, float)

        if fIDWT >= 100000:
          fORdh = 0.1

        else:
          fORdh = 0.2 - (fIDWT / 10000) * 0.1

        return RuleUnitResult(
            result_variables = {
                "fORdh": fORdh,
            }
        )