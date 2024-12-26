import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041811_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.11 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '표준호퍼바지선'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.10 상부구조물에 작용하는 선박의 충격력
    4.18.11 교각에 작용하는 바지선의 충격력
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표준호퍼바지선];
    B["KDS 24 12 21 4.18.11 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 폭/];
    VarIn2[/입력변수 : 길이/];
    VarIn3[/입력변수 : 깊이/];
    VarIn4[/입력변수 : 비적재 흘수/];
    VarIn5[/입력변수 : 적재 흘수/];
    VarIn6[/입력변수 : 질량/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3~~~VarIn6
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.11 (1)"])
		C --> Variable_def

    D["폭=10,700mm, 길이 =60,000mm, 깊이=3,700mm,
    비적재 흘수 =520mm, 적재 흘수=2,700mm, 질량 =1,730미터톤"];
    E{"내륙하천에서 운항되는 바지선인 경우"};
    Variable_def--->E--->D
    """

    @rule_method
    def standard_hopper_barge_ship(fOW,fOL,fODepth,fOdraunl,fOdraloa,fOM) -> RuleUnitResult:
        """표준호퍼바지선

        Args:
            fOW (float): 폭
            fOL (float): 길이
            fODepth (float): 깊이
            fOdraunl (float): 비적재 홀수
            fOdraloa (float): 적재 홀수
            fOM (float): 질량

        Returns:
            fOW (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 1
            fOL (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 2
            fODepth (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 3
            fOdraunl (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 4
            fOdraloa (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 5
            fOM (float): 강교 설계기준(한계상태설계법)  4.18.11 교각에 작용하는 바지선의 충격력 (1)의 값 6
        """

        fOW = 10700
        fOL = 60000
        fODepth = 3700
        fOdraunl = 520
        fOdraloa = 2700
        fOM = 1730

        return RuleUnitResult(
            result_variables = {
                "fOW": fOW,
                "fOL": fOL,
                "fODepth": fODepth,
                "fOdraunl": fOdraunl,
                "fOdraloa": fOdraloa,
                "fOM": fOM,
            }
        )