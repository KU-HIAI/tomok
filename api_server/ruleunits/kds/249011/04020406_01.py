import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020406_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.6 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '탄성패드 설계'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.6 탄성패드 설계
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성패드 설계];
    B["KDS 24 90 11 4.2.4.6 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 설계최대 회전각/];
		VarIn2[/입력변수: 탄성패드의 직경/];
		VarOut1[/출력변수: 탄성패드의 최소두께/];

    VarOut1~~~~VarIn1 & VarIn2

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.4.6 (1)"])
		C --> Variable_def;
		Variable_def--->K--->L

    K["<img src='https://latex.codecogs.com/svg.image?t_{min}=3.33\alpha&space;_{dmax}d\geq\frac{15}{d}'>--------------------------------------------------------"];
		L(["탄성패드의 최소두께"])
    """

    @rule_method
    def Minimum_Thickness_Of_The_Elastic_Pad(fIalphadmax, fIdprime) -> RuleUnitResult:
        """탄성패드 설계
        Args:
            fIalphadmax (float): 설계최대 회전각
            fIdprime (float): 탄성패드의 직경

        Returns:
            fOtmin (float): 교량 기타시설설계기준 (한계상태설계법) 4.2.4.6 탄성패드 설계 (1)의 값
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.4.6 탄성패드 설계 (1)의 판단 결과
        """

        assert isinstance(fIalphadmax, float)
        assert isinstance(fIdprime, float)

        fOtmin = 3.33 * fIalphadmax * fIdprime

        if fOtmin > fIdprime / 15:
          return RuleUnitResult(
                  result_variables = {
                      "fOtmin": fOtmin,
                      "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
                  result_variables = {
                      "fOtmin": fOtmin,
                      "pass_fail": False,
                }
            )