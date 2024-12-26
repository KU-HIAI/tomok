import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030602_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.6.2 (3)'
    ref_date = '2020-12-03'
    doc_date = '2023-10-06'
    title = '인발시험'

    description = """
    앵커
    3. 시공
    3.6 현장품질관리
    3.6.2 시험 일반
    (3)
    """

    content = """
    #### 3.6.2. 시험 일반
    (3) 인발시험
    ⑤ 시험의 방법은 특별히 정한 경우를 제외하고 다음과 같이 한다.
    가. 계획 최대시험하중은 설계하중의 1.2배 또는 예상되는 인발저항력 중 큰 값으로 한다.
    나. 초기하중은 계획 최대시험하중의 0.1배로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인발시험];
    B["KCS 11 60 00 3.6.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.6.2 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 계획 최대시험하중/];
    VarOut2[/출력변수: 초기하중/];
    VarIn1[/입력변수: 설계하중/];
    VarIn2[/입력변수: 인발저항력/];
    VarIn3[/입력변수: 계획 최대시험하중/];
    end
    VarOut1 & VarOut2 & VarIn1 ~~~ VarIn2

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"계획 최대시험하중
= max(설계하중 * 1.2, 인발저항력)"}
    Variable_def --> C2{"초기하중  = 계획 최대시험하중 * 0.1"}
    C1--> D1["계획 최대시험하중"];
    C2--> D2["초기하중"];
    D1--> E1(["계획 최대시험하중"])
    D2--> E2(["초기하중"]);
    """

    @rule_method
    def Planned_Maximum_Test_Load(fIDesLoa, fIPulRes) -> float:
        """인발시험
        Args:
            fIDesLoa (float): 설계하중
            fIPulRes (float): 인발저항력

        Returns:
            fOMaxLoa (float): 계획 최대시험하중
            fOIniLoa (float): 초기하중
        """
        assert isinstance(fIDesLoa, float)
        assert isinstance(fIPulRes, float)


        fOMaxLoa = max(1.2 * fIDesLoa, fIPulRes)
        fOIniLoa = fOMaxLoa * 0.1

        return RuleUnitResult(
            result_variables={
                "fOMaxLoa": fOMaxLoa,
                "fOIniLoa": fOIniLoa,
            }
        )