import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020103_06_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.3 (6) ③'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = '프리스트레스트 콘크리트용 그라우트의 체적변화율'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (6)
    """
    content = """
    #### 2.1.3 프리스트레스트 콘크리트용 그라우트
    (6) 그라우트의 덕트 내 충전성은 그라우트의 유동성, 블리딩률, 체적변화율로 판단한다.
    ③ 체적변화율은 KCI-PS102에 따라 수직관 시험을 통해 측정하고 기준값과 비교하여 적절성을 판단하도록 한다. 기준값은 24시간 경과 시 (–1 ∼ 5) %의 범위이다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레스트 콘크리트용 그라우트의 체적변화율];
    B["KCS 14 20 53 2.1.3 (6) ③ "];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (6) ③ "])

    subgraph Variable_def
    VarIn2[/"입력변수: 24시간 경과 시 체적변화율"/];
    VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"-1<=체적변화율<=5"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def volume_change_grout_duct(fIVolCha) -> RuleUnitResult:
        """
        Args:
            fIVolCha (float): 24시간 경과 시 체적변화율

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.3 프리스트레스트 콘크리트용 그라우트 (6) ③의 판단 결과
        """
        assert isinstance(fIVolCha, float)

        if fIVolCha>=-1 and fIVolCha<=5:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })