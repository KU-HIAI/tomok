import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020606_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.6.6 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = 'PTFE 최소두께'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.6 받침 마찰요소의 설계
    4.2.6.6 미끄럼요소 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: PTFE 최소두께];
    B["KDS 24 90 11 4.2.6.6 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 두께/];
		VarIn2[/입력변수: 돌출높이/];
		VarIn3[/입력변수: PTFE의 직경/];

    VarIn1 & VarIn2 & VarIn3

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.6.6 (2)"])
		C --> Variable_def;
		Variable_def--->K & L


    K{"<img src='https://latex.codecogs.com/svg.image?h=1.75&plus;\frac{L}{1200}\geq&space;2.2mm'>--------------------------------------------------------"};
		L{"<img src='https://latex.codecogs.com/svg.image?2.2h\leq&space;t_{p}\leq&space;8.0mm'>--------------------------------------------------------"};
		K & L--->M
		M(["Pass or Fail"])
    """

    @rule_method
    def Thickness(fItp,fIh,fIL) -> RuleUnitResult:
        """PTFE 최소두께
        Args:
            fItp (float): 두께
            fIh (float): 돌출높이
            fIL (float): PTFE의 직경

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.2.6.6 미끄럼요소 설계 (2)의 판단 결과
        """

        assert isinstance(fItp, float)
        assert isinstance(fIh, float)
        assert isinstance(fIL, float)

        if 1.75 + fIL / 1200 >= 2.2 :
          fIh = 1.75 + fIL / 1200
          if 2.2 * fIh <= fItp <= 8.0 :
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
        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
                  }
              )