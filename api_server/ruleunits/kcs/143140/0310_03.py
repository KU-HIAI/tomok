import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_0310_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.10 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-10-31'
    title = '소지 표면온도 조건'

    description = """
    도장
    3. 시공
    3.10 도장작업 시의 기후조건
    (3)
    """

    content = """
    #### 3.10 도장작업 시의 기후조건
    (3) 소지 표면온도는 응축을 방지하기 위해 이슬점 이슬점보다 3 ℃ 이상 높아야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소지 표면온도];
    B["KCS 14 31 10 3.3.4 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 소지 표면온도/];
    VarIn2[/입력변수: 이슬점/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"소지 표면온도 ≥ 이슬점 + 3 ℃"}
		C --> End([Pass or Fail])
    """

    @rule_method
    def Surface_Temperature_of_Body(fISurTem, fIDewPoi) -> bool:
        """ 소지 표면온도 조건
        Args:
        fISurTem (float): 소지 표면온도
        fIDewPoi (float): 이슬점

        Returns:
        pass_fail (bool): 도장 3.10 도장작업 시의 기후조건 (3)의 판단 결과
        """
        assert isinstance(fISurTem, float)
        assert isinstance(fIDewPoi, float)

        if fISurTem >= fIDewPoi + 3:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )