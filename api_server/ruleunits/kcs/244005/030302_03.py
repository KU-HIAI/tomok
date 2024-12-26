import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030302_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.3.2 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '디스크받침의 성능시험'

    description = """
    교량받침
    3. 시공
    3.3 포트받침 및 디스크받침
    3.3.2 표본선정과 시험
    (3)
    """
    content = """
    #### 3.3.2 표본선정과 시험
    (3) 성능시험
    ① 포트받침의 성능시험은 KS F 4424(교량 지지용 포트 받침)에 따라 실시한다.
    ② 디스크받침의 성능시험은 1시간 동안 설계용량의 150%까지의 하중과 0.02 rad의 회전량과 설계회전량 중에서 큰 회전을 함께 가해서 실시한다.
    ③ 받침은 시험동안 그리고 시험 후에 분해하여 육안으로 검사하여야 한다. 돌출되거나 변형된 폴리에테르 우레탄 또는 PTFE, 손상된 구속링 또는
     균열이 발생한 강재 등과 같이 육안으로 관찰되는 결함은 불합격의 원인이 된다. 시험하는 동안에 폴리에테르우레탄 디스크와 받침판 사이에서 그리고
     상부 미끄럼 강판과 상부 받침판 사이에서 연속적이고 균일한 접촉이 유지되어야 한다. 들뜬 것이 발견되면, 이것은 해당 로트의 불합격 요인이 된다.

    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 디스크받침의 성능시험];
    B["KCS 24 40 05 3.3.2 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.3.2 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 디스크받침의 하중 시험/];
    VarOut2[/출력변수: 디스크받침의 회전 시험/];
    VarIn1[/입력변수: 설계 하중 용량/];
    VarIn2[/입력변수: 설계회전량/];
    VarOut1 &  VarOut2 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{시험 종류}
    C --> D["디스크받침의 하중 시험 = 설계 하중 용량 * 1.5"]
    C --> E["디스크받침의 회전 시험 = max(0.02 rad, 설계회전량)"]
    D & E --> F(["디스크받침의 성능시험"])
    """

    @rule_method

    def load_test(fIDesLoa,fIDesRot) -> RuleUnitResult:
        """
        Args:
            fIDesLoa (float): 설계 하중 용량
            fIDesRot (float): 설계회전량

        Returns:
            fOLoaTes (float): 디스크받침의 하중 시험
            fORotTes (float): 디스크받침의 회전 시험
        """
        assert isinstance(fIDesLoa, float)
        assert isinstance(fIDesRot, float)

        fOLoaTes = fIDesLoa*1.5
        fORotTes = max(fIDesRot, 0.02)

        return RuleUnitResult(
            result_variables = {
                "fOLoaTes": fOLoaTes,
                "fORotTes": fORotTes
                })