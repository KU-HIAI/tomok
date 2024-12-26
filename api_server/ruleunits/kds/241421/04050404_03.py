import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050404_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.4.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '정착길이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.4 철근의 정착
    4.5.4.4 기본정착길이
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 정착길이];
    B["KDS 24 14 21 4.5.4.4 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 정착길이/];
		VarIn2[/입력변수: 철근의 설계 응력/];
		VarIn3[/입력변수: 이형 철근의 부착강도에 대한 설계값/];
		VarOut1[/출력변수: 정착길이/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.4.4 (3)"])
		C --> Variable_def

		Variable_def--->D

		D["<img src='https://latex.codecogs.com/svg.image?l_b=(d_b/4)(\sigma&space;_{sd}/f_{bd})'>---------------------------------"]
		D~~~|KDS 24 14 21 4.5.4.3|D
		D--->F

		F(["정착길이"])
    """

    @rule_method
    def development_legnth(fIdb,fIsigmasd,fIfbd) -> RuleUnitResult:
        """정착길이

        Args:
            fIdb (float): 정착길이
            fIsigmasd (float): 철근의 설계 응력
            fIfbd (float): 이형 철근의 부착강도에 대한 설계값

        Returns:
            fOlb (float): 콘크리트교 설계기준 (한계상태설계법)  4.5.4.4 기본정착길이 (3)의 값
        """

        assert isinstance(fIdb, float)
        assert isinstance(fIsigmasd, float)
        assert isinstance(fIfbd, float)
        assert fIfbd != 0

        fOlb = (fIdb/4)*(fIsigmasd/fIfbd)

        return RuleUnitResult(
            result_variables = {
                "fOlb": fOlb,
            }
        )