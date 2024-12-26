import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142053_020103_11(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 53 2.1.3 (11)'
    ref_date = '2022-01-11'
    doc_date = '2023-09-19'
    title = 'PS 강재의 부식 저항성'

    description = """
    프리스트레스트 콘크리트
    2. 자재
    2.1 구성재료
    2.1.3 프리스트레스트 콘크리트용 그라우트
    (11)
    """
    content = """
    #### 2.1.3 프리스트레스트 콘크리트용 그라우트
    (11) PS 강재의 부식 저항성은 일반적으로 비빌 때 그라우트 중에 함유되는 염화물의 총량으로 설정하며, KCI-PS102에 따라 측정한 전 염화물 함유량을 기준으로 사용되는 단위 시멘트량의 0.08 % 이하로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: PS 강재의 부식 저항성];
    B["KCS 14 20 53 2.1.3 (11)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 53 2.1.3 (11)"])

    subgraph Variable_def
    VarIn1[/입력변수: 그라우트 중 염화물의 총량/];
    VarIn2[/입력변수: 단위 시멘트량/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"그라우트 중 염화물의 총량 <= 단위 시멘트량 * 0.08%"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def corrosion_resistance_PS_steel(fIAmoChl,fIUniCon) -> RuleUnitResult:
        """
        Args:
            fIAmoChl (float): 그라우트 중 염화물의 총량
            fIUniCon (float): 단위 시멘트량

        Returns:
            pass_fail (bool): 프리스트레스트 콘크리트 2.1.4 프리스트레스트 콘크리트 부속 재료 (11)의 판단 결과
        """
        assert isinstance(fIAmoChl, float)
        assert isinstance(fIUniCon, float)

        if fIAmoChl<=fIUniCon*0.0008:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })