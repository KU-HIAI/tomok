import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020309(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.9'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '전단변형률'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.9 전단변형률
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단변형률];
    B["KDS 24 90 11 4.2.3.9"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: vx,d와 vy,d의 벡터합으로 계산되는 받침의 수평상대변위/];
		VarIn2[/입력변수: 상하 덮개를 포함한 탄성중합체의 총 두께/];
		VarOut1[/출력변수: 이동 변위로 인한 탄성중합체의 전단변형률/];
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.9"]) --> Variable_def;
		Variable_def-->F--->I

    F["<img src='https://latex.codecogs.com/svg.image?\epsilon&space;_{q,d}=\frac{{xy,d}}{T_{q}}'>------------------------------"];

    I(["이동 변위로 인한 탄성중합체의 전단변형률"])
    """

    @rule_method
    def Shear_Strain(fIvxyd, fITq) -> RuleUnitResult:
        """전단변형률

        Args:
            fIvxyd (float): vx,d와 vy,d의 벡터합으로 계산되는 받침의 수평상대변위
            fITq (float): 상하 덮개를 포함한 탄성중합체의 총 두께

        Returns:
            fOepsilonqd (float): 압축하중에 의한 설계변형률  4.2.3.9 전단변형률의 값
        """
        assert isinstance(fOepsilonqd, float)
        assert isinstance(fIvxyd, float)
        assert isinstance(fITq, float)
        assert fITq != 0

        fOepsilonqd = fIvxyd/fITq

        return RuleUnitResult(
            result_variables = {
                "fOepsilonqd": fOepsilonqd,
            }
        )