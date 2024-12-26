import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_020302_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 2.3.2 (4)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-16'
    title = '급수계량기 측정가능 수량'

    description = """
    앵커
    2. 자재
    2.3 장비
    2.3.2 그라우트 믹서 및 펌프
    (4)
    """

    content = """
    #### 2.3.2. 그라우트 믹서 및 펌프
    (4) 급수계량기는 그라우트 혼합에 사용된 수량을 2ℓ/㎥ 까지 측정할 수 있어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 급수계량기 측정가능 수량];
    B["KCS 11 60 00 2.3.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 2.3.2 (4)"])

    subgraph Variable_def
    VarIn[/입력변수: 급수계량기 측정가능 수량/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"급수계량기 측정가능 수량 >= 2ℓ/㎥"}
    C--> D(["Pass or Fail"])
    """

    @rule_method
    def Measurable_Quantity_for_Water_Metering(fIQuaWat) -> bool:
        """급수계량기 측정가능 수량
        Args:
          fIQuaWat (float): 급수계량기 측정가능 수량

        Returns:
          pass_fail (bool): 앵커 2.3.2 그라우트 믹서 및 펌프 (4)의 판단 결과
        """
        assert isinstance(fIQuaWat, float)

        if fIQuaWat >= 2:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )