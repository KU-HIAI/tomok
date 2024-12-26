import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04020302_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.2.3.2 (3)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '연직하중에 의한 케이슨 상단의 총 침하량'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 케이슨기초
    4.2.3 지반반력 및 침하량
    4.2.3.2 고려사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 연직하중에 의한 케이슨 상단의 총 침하량];
    B["KDS 11 50 15 4.2.3.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 연직하중에 의한 케이슨 상단의 총 침하량/];
    VarIn1[/입력변수: 케이슨 본체의 탄성변위량/] ;
    VarIn2[/입력변수: 케이슨 기초지반의 침하량/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.2.3.2 (3)"])
		C --> Variable_def;

		Variable_def-->E
		E["연직하중에 의한 케이슨 상단의 총 침하량= 케이슨 본체의 탄성변위량+케이슨 기초지반의 침하량"];
    D(["연직하중에 의한 케이슨 상단의 총 침하량"]);

    E--->D
    """

    @rule_method
    def total_subsidence_at_the_top_of_the_caisson(fIediscb,fItosecf) -> RuleUnitResult:
        """연직하중에 의한 케이슨 상단의 총 침하량

        Args:
            fIediscb (float): 케이슨 본체의 탄성변위량
            fItosecf (float): 케이슨 기초지반의 침하량

        Returns:
            fOtosetc (float): 깊은기초 설계기준(일반설계법)  4.2.3.2 고려사항 (3)의 값
        """

        assert isinstance(fIediscb, float)
        assert isinstance(fItosecf, float)

        fOtosetc = fIediscb + fItosecf

        return RuleUnitResult(
              result_variables = {
                  "fOtosetc": fOtosetc,
              }
          )