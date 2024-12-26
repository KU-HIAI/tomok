import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04110402_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.11.4.2 (1)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '아치리브 복부판의 세장비'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.4 충복아치
    4.11.4.2 복부판의 세장비
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 아치리브 복부판의 세장비];
    B["KDS 24 14 31 4.11.4.2 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarOut1[/출력변수: 아치리브 복부판의 세장비/] ;
		VarIn1[/입력변수: 설계하중에 의한 축방향응력/] ;
    VarIn2[/입력변수: 표 4.11.1에 규정된 보강재의 좌굴계수/];
    VarIn3[/입력변수: 탄성계수/];

		VarOut1
		VarIn1 ~~~ VarIn2 & VarIn3
		end

		Python_Class ~~~ C(["KDS 24 14 31 4.11.4.2 (1)"])
		C --> Variable_def

		Variable_def --> D --> E

		D["<img src='https://latex.codecogs.com/svg.image?\frac{D}{t_{w}}=k\sqrt{\frac{E}{f_{a}}}'>---------------------"];

		E([아치리브 복부판의 세장비])
    """

    @rule_method
    def slenderness_ratio_of_arch_rib_web(fIfa,fIk,fIE) -> RuleUnitResult:
        """아치리브 복부판의 세장비

        Args:
            fIfa (float): 설계하중에 의한 축방향응력
            fIk (float): 좌굴계수
            fIE (float): 탄성계수

        Returns:
            fOsraarw (float): 강교 설계기준(한계상태설계법)  4.11.4.2 복부판의 세장비 (1)의 값
        """

        assert isinstance(fIfa, float)
        assert fIfa > 0
        assert isinstance(fIk, float)
        assert isinstance(fIE, float)
        assert fIE > 0

        fOsraarw = fIk * (fIE / fIfa)**0.5

        return RuleUnitResult(
            result_variables = {
                "fOsraarw": fOsraarw,
            }
        )