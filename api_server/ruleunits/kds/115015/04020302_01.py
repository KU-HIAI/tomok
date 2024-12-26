import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04020302_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.2.3.2 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '케이슨 기초지반의 연직지반반력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 케이슨기초
    4.2.3 지반반력 및 침하량
    4.2.3.2 고려사항
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 케이슨 기초지반의 연직지반반력];
    B["KDS 11 50 15 4.2.3.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 케이슨 기초지반의 연직지반반력/];
    VarIn1[/입력변수: 케이슨을 통해 전달되는 모든 연직하중/] ;
    VarIn2[/입력변수: 케이슨 저면적/];

		VarOut~~~VarIn1
		VarOut~~~VarIn2

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.2.3.2 (1)"])
		C --> Variable_def;

		Variable_def-->F
		F["케이슨 기초지반의 연직지반반력= 케이슨을 통해 전달되는 모든 연직하중/케이슨 저면적"];
    D(["케이슨 기초지반의 연직지반반력"]);

    F--->D
    """

    @rule_method
    def vertical_ground_reaction_force_of_caisson_foundationground(fIaglgcf,flbotacf) -> RuleUnitResult:
        """케이슨 기초지반의 연직지반반력

        Args:
            fIaglgcf (float): 케이슨을 통하여 지반에 전달되는 모든 연직하중
            flbotacf (float): 케이슨의 저면적

        Returns:
            fOvgrfcf (float): 깊은기초 설계기준(일반설계법)  4.2.3.2 고려사항 (1)의 값
        """

        assert isinstance(fIaglgcf, float)
        assert isinstance(flbotacf, float)
        assert flbotacf > 0

        fOvgrfcf = fIaglgcf / flbotacf

        return RuleUnitResult(
              result_variables = {
                  "fOvgrfcf": fOvgrfcf,
              }
          )