import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020608_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.8 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '받침판 두께'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.8 지지판(backing plate) 설계
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침판의 두께];
    B["KDS 24 90 11 4.2.6.8 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 지지판의 두께/];
		VarIn2[/입력변수: 지지판의 단변/];
		VarIn3[/입력변수: 지지판의 장변/];

    VarIn1 & VarIn2 & VarIn3

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.6.8 (3)"])--->Variable_def;
		Variable_def--->K

    K["<img src='https://latex.codecogs.com/svg.image?max(t_{b}\geq&space;0.04\times\sqrt{a_{b}^{2}&plus;b_{b}^{2}},10mm)'>--------------------------------------------------------"];
    K --->M
		M(["지지판의 두께"])
    """

    @rule_method
    def Thickness_Of_Backing_Plate(fIthbapl,fIab,fIbb) -> RuleUnitResult:
        """받침판 변형
        Args:
            fIthbapl (float): 지지판의 두께
            fIab (float): 지지판의 단변
            fIbb (float): 지지판의 장변

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.6.8 지지판(backing plate) 설계 (3)의 판단 결과
        """

        assert isinstance(fIthbapl, float)
        assert isinstance(fIab, float)
        assert fIab > 0
        assert isinstance(fIbb, float)
        assert fIbb > 0

        if fIthbapl >= 0.04*(fIab+fIbb)**0.5 :
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