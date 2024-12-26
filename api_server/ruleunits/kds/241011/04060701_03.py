import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241011_04060701_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 10 11 4.6.7.1 (3)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-22'
    title = '내측거더의 플랜지 유효폭'

    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.7 플랜지 유효폭
    4.6.7.1 일반사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 내측거더의 플랜지 유효폭];
    B["KDS 24 10 11 4.6.7.1 (3)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 내측거더의 플랜지 유효폭/];
    VarIn1[/입력변수 : 등가지간장/];
    VarIn2[/입력변수 : 슬래브 평균두께/];
    VarIn3[/입력변수 : 복부 두께/];
    VarIn4[/입력변수 : 주거더 상부플랜지폭/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ C(["KDS 24 10 11 4.6.7.1 (3)"])
		C --> Variable_def

    D["내측거더의 플랜지 유효폭=Min(등가지간장/4,인접한 보 사이의 평균간격, (슬래브 평균두께X12+Max(복부 두께, 주거더 상부플랜지폭/2)))"];
    E(["내측거더의 플랜지 유효폭"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Flange_effective_width_of_inner_girder(fILeqsp,fItavsl,fItabdor,fIWuppfl,fISavbea) -> RuleUnitResult:
        """내측거더의 플랜지 유효폭

        Args:
            fILeqsp (float): 등가지간장
            fItavsl (float): 슬래브 평균두께
            fItabdor (float): 복부 두께
            fIWuppfl (float): 주거더 상부플랜지폭
            fISavbea (float): 보 사이의 평균 간격

        Returns:
            fOWinfl (float): 교량 설계 일반사항(한계상태설계법)  4.6.7.1 일반사항 (3)의 값
        """

        assert isinstance(fILeqsp, float)
        assert isinstance(fItavsl, float)
        assert isinstance(fItabdor, float)
        assert isinstance(fIWuppfl, float)
        assert isinstance(fISavbea, float)

        fOWinfl=min(fILeqsp / 4, 12 * fItavsl + max(fItabdor, fIWuppfl / 2), fISavbea)

        return RuleUnitResult(
            result_variables = {
                "fOWinfl": fOWinfl,
            }
        )