import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04010505_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.1.5.5 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '활하중 응력범위'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.5 모듈러형 신축이음
    4.1.5.5 피로한계상태 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 활하중 응력범위];
    B["KDS 24 90 11 4.1.5.5 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
    VarIn1[/입력변수: 활하중 응력범위/];
    VarIn2[/입력변수: 피로 진폭 한계값/];
    VarIn2 ~~~ |"KDS 14 31 20 Table 4.1-3"| VarIn2

    end
    Python_Class ~~~ C(["KDS 24 90 11 4.1.5.5 (2)"])
		C --> Variable_def;

		D["\n <img src='https://latex.codecogs.com/svg.image?  \Delta f \leq \frac{1}{2}\Delta F_{TH}'>-----------------------------"];
		Variable_def --> D --> E(["Pass or Fail"])
    """

    @rule_method
    def Live_Load_Stress_Range(fIdeltaf,fIdeltaFTH) -> RuleUnitResult:
        """활하중 응력범위
        Args:
            fIdeltaf (float): 활하중 응력범위
            fIdeltaFTH (float): 피로 진폭 한계값

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.1.5.5 피로한계상태 설계원칙 (2)의 판단 결과
        """

        assert isinstance(fIdeltaf, float)
        assert isinstance(fIdeltaFTH, float)

        if fIdeltaf <= 0.5 * fIdeltaFTH :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )