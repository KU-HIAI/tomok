import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030303_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '공칭 단위선단 지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.3 말뚝 지지력의 반경험적 평가
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝 지지력의 반경험적 평가];
    B["KDS 24 14 51 3.3.3.3 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:공칭 단위선단지지력/]
		VarIn1[/입력변수:선단근처 점성토의 비배수 전단강도/]

		VarOut1
		VarIn1

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.3 (3)"])
		C --> Variable_def;

		E["<img src='https://latex.codecogs.com/svg.image?q_{p}=9S_{u}'>---------------------------------"]
		D([공칭 단위선단지지력])

		Variable_def -- 포화된 점성토에 설치된 말뚝 ---> E ---> D
    """

    @rule_method
    def Nominal_unit_end_support(fISu) -> RuleUnitResult:
        """공칭 단위선단 지지력

        Args:
            fISu (float): 선단근처 점성토의 비배수 전단강도

        Returns:
            fOqp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.3(3) 공칭 단위선단지지력의 값
        """

        assert isinstance(fISu, float)

        fOqp = 9 * fISu
        return RuleUnitResult(
            result_variables = {
                "fOqp": fOqp,
                }
            )