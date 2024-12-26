import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030204_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.2.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '탄성받침의 외부판 용접'

    description = """
    교량받침
    3. 시공
    3.2 탄성받침
    3.2.4 설치
    (1)
    """
    content = """
    #### 3.2.4 설치
    (1) 탄성받침 외부판은 용접부와 고무사이에 적어도 38 mm의 이격이 존재하지 않는다면 용접을 해서는 안 된다. 어떠한 경우라도 고무와 부착부는 200 ℃ 이상으로 가열되어서는 안 된다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성받침의 외부판 용접];
    B["KCS 24 40 05 3.2.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.2.4 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: 용접부와 고무사이 이격/];
    VarIn2[/입력변수: 고무와 부착부 가열 온도/];
    VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용접부와 고무사이 이격 ≥ 38 mm &
    고무와 부착부 가열 온도 < 200 ℃"}
    C --> End([Pass or Fail])
    """

    @rule_method

    def weld_bearing(fIDisWel,fITemWel) -> RuleUnitResult:
        """
        Args:
            fIDisWel (float): 용접부와 고무사이 이격
            fITemWel (float): 고무와 부착부 가열 온도

        Returns:
            pass_fail (bool): 교량받침 3.2.4 설치 (1)의 판단 결과
        """
        assert isinstance(fIDisWel, float)
        assert isinstance(fITemWel, float)

        if fIDisWel >= 38 and fITemWel < 200:
            pass_fail = True
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })