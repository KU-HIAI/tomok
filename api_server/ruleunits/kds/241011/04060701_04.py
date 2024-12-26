import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060701_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.7.1 (4)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '외측거더의 플랜지 유효폭'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.1 일반사항
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 외측거더의 플랜지 유효폭];
    B["KDS 24 10 11 4.6.7.1 (4)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 외측거더의 플랜지 유효폭/];
    VarIn1[/입력변수 : 내측거더 유효폭의 절반/];
    VarIn2[/입력변수 : 등가지간장/];
    VarIn3[/입력변수 : 슬래브 평균두께/];
    VarIn4[/입력변수 : 복부 두께/];
    VarIn5[/입력변수 : 주거더 상부플랜지폭/];
    VarIn6[/입력변수 : 내민부분의 폭/];
    VarIn3~~~VarIn6
    VarOut~~~VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.7.1 (4)"])
		C --> Variable_def

    D["외측거더의 플랜지 유효폭=내측거더 유효폭X0.5+Min(등가지간장/8,내민부분의 폭, (스래브 평균두께X6+Max(복부 두께X0.5, 주거더 상부플랜지폭/4)))"];
    E(["외측거더의 플랜지 유효폭"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Flange_effective_width_of_outer_girder(fIWingd,fILeqsp,fItavsl,fItabdor,fIWuppfl,fIWoverh) -> RuleUnitResult:
        """외측거더의 플랜지 유효폭

        Args:
            fIWingd (float): 내측거더 유효폭의 절반
            fILeqsp (float): 등가지간장
            fItavsl (float): 슬래브 평균두께
            fItabdor (float): 복부 두께
            fIWuppfl (float): 주거더 상부플랜지폭
            fIWoverh (float): 내민부분(overhang)의 폭

        Returns:
            fOWoutfl (float): 깊은기초 설계기준(일반설계법)  4.6.7.1 일반사항 (4)의 값
        """

        assert isinstance(fIWingd, float)
        assert isinstance(fILeqsp, float)
        assert isinstance(fItavsl, float)
        assert isinstance(fItabdor, float)
        assert isinstance(fIWuppfl, float)
        assert isinstance(fIWoverh, float)

        fOWoutfl = fIWingd / 2 + min(fILeqsp / 8, 6 * fItavsl + max(fItabdor/2, fIWuppfl/4), fIWoverh)

        return RuleUnitResult(
            result_variables = {
                "fOWoutfl": fOWoutfl,
            }
        )