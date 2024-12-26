import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060203_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.2.3 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-13'
    title = '단순지지 바닥판의 지간'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.3 바닥판의 지간
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단순지지 바닥판의 지간];
    B["KDS 24 10 11 4.6.2.3 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 지간/];
    VarIn2[/입력변수 : 바닥판의 순 지간/];
    VarIn3[/입력변수 : 바닥판의 두께/];
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.2.3 (1)"])
		C --> Variable_def

    D{"파닥판의 지간<바닥판의 순지간+바닥판의 두께"};
    F(["Pass or Fail"]);
    Variable_def--->D--->F
    """

    @rule_method
    def span_of_simple_support_floorboard(fId,fIdspla,fItdeck) -> RuleUnitResult:
        """단순지지 바닥판의 지간

        Args:
            fId (float): 지간
            fIdspla (float): 바닥판의 순 지간
            fItdeck (float): 바닥판의 두께

        Returns:
            pass_fail (bool): 교량 설계 일반사항(한계상태설계법) 바닥판의 지간 KDS 24 10 11 4.6.2.3 (1)의 판단 결과
        """

        assert isinstance(fId, float)
        assert isinstance(fIdspla, float)
        assert isinstance(fItdeck, float)

        if fIdspla + fItdeck >= fId:
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