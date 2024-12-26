import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060301_13(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.3.1 (13)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '종방향 강성도 변수'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.3 보-슬래브 교량의 근사적 해석방법
    4.6.3.1 적용
    (13)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 강성도 변수];
    B["KDS 24 10 11 4.6.3.1 (13)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수: 종방향 강성도 변수/];
    VarIn1[/입력변수: 보재료의 탄성계수/];
    VarIn2[/입력변수: 바닥판재료의 탄성계수/];
    VarIn3[/입력변수: 보의 단면2차모멘트/];
    VarIn4[/입력변수: 보의 중심과 바닥판의 중심사이의 거리/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn2
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.3.1 (13)"])
		C --> Variable_def

    F["<img src='https://latex.codecogs.com/svg.image?n=\frac{E_{B}}{E_{D}}'>"];
    D["<img src='https://latex.codecogs.com/svg.image?K_{g}=n(I+Ae_{g}^{2})'>-------------------------------------"];
    E(["종방향 강성도 변수"]);
    Variable_def--->F--->D--->E
    """

    @rule_method
    def Longitudinal_stiffness_parameters(fIED,fII,fIEB,fIeg,fIA) -> RuleUnitResult:
        """종방향 강성도 변수

        Args:
            fIED (float): 바닥판재료의 탄성계수
            fII (float): 보의 단면2차모멘트
            fIEB (float): 보재료의 탄성계수
            fIeg (float): 보의 중심과 바닥판의 중심사이의 거리
            fIA (float): 보의 단면적

        Returns:
            fOKg (float): 교량 설계 일반사항(한계상태설계법)  4.6.4 슬래브교에 대한 등가 스트립 폭 (2)의 값
        """

        assert isinstance(fIED, float)
        assert fIED != 0
        assert isinstance(fII, float)
        assert isinstance(fIEB, float)
        assert isinstance(fIeg, float)
        assert isinstance(fIA, float)

        fOKg =fIEB/fIED*(fII+fIA*fIeg**2)

        return RuleUnitResult(
            result_variables = {
                "fOKg": fOKg,
            }
        )