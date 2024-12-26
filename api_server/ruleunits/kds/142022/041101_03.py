import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_041101_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.11.1 (3)'
    ref_date = '2022-01-11'
    doc_date = '2024-11-15'
    title = '위험단면의 둘레길이'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.11 슬래브와 기초판에 대한 전단 설계
    4.11.1 전단 설계 단면
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 위험단면의 둘레길이];
    B["KDS 14 20 22 4.11.1 (3)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 위험단면의 둘레길이/];

    VarIn1[/입력변수: 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리/];
    VarIn2[/입력변수: 집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 가로 길이/];
    VarIn3[/입력변수: 집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 세로 길이/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

    end

    Python_Class ~~~ C(["KDS 14 20 22 4.11.1 (3)"])
		C --> Variable_def

		Variable_def --> D --> E

    D["위험단면의 둘레길이 = (집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 가로 길이 + d) + (집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 세로 길이 + d)"];

		E(["위험단면의 둘레길이"]);
    """

    @rule_method
    def Circumference_length_of_hazardous_section(fId,fIholeco,fIveleco) -> RuleUnitResult:
        """위험단면의 둘레길이

        Args:
            fId (float): 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리
            fIholeco (float): 집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 가로 길이
            fIveleco (float): 집중하중, 반력구역, 기둥, 기둥머리 또는 지판 등의 세로 길이

        Returns:
            fObo (float): 위험단면의 둘레길이
        """

        assert isinstance(fId, float)
        assert isinstance(fIholeco, float)
        assert isinstance(fIveleco, float)

        fObo = (fIholeco + fId)*2 + (fIveleco + fId)*2

        return RuleUnitResult(
            result_variables = {
                "fObo": fObo,
            }
        )