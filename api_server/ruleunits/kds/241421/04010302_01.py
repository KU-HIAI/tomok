import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010302_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.3.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '비틀림모멘트에 의해 유발되는 전단력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.3 비틀림
    4.1.3.2 설계
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비틀림모멘트에 의해 유발되는 전단력];
    B["KDS 24 14 21 4.1.3.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 비틀림모멘트에 의해 유발되는 전단력/];
    VarOut2[/출력변수: 벽을 따라 흐르는 전단류/];
    VarOut3[/출력변수: 유효 벽두께/];
    VarIn1[/입력변수: 작용 계수하중에 의한 비틀림모멘트/];
		VarIn2[/입력변수: 속빈 공간을 포함하는, 벽체의 중심선으로 둘러싸인 면적/];
		VarIn3[/입력변수: i번 벽체의 전단응력/];
    VarIn4[/입력변수: 인접 벽체와의 교차점 사이의 거리로 정의된 i번 벽의 측면길이/];
    VarIn5[/입력변수: 단면의 바깥쪽 둘레로 싸인 면적/];
    VarIn6[/입력변수: 단면 바깥쪽 둘레 길이/];
    VarIn7[/입력변수: 횡방향 철근의 피복 두께/];

		VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn5 & VarIn6 & VarIn7

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.3.2 (1)"])
		C --> Variable_def

		Variable_def--->D--->F--->E
		F["<img src='https://latex.codecogs.com/svg.image?V_{u,i}=qy_i'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?q=v_it_i=\frac{T}{2A_o}i'>---------------------------------"]
		E(["비틀림모멘트에 의해 유발되는 전단력"])

    """

    @rule_method
    def Shear_force_induced_by_torsional_moment(fITu,fIAo,fIvi,fIyi,fIAcp,fIPcp,fItc) -> RuleUnitResult:
        """비틀림모멘트에 의해 유발되는 전단력

        Args:
            fITu (float): 작용 계수하중에 의한 비틀림모멘트
            fIAo (float): 속빈 공간을 포함하는, 벽체의 중심선으로 둘러싸인 면적
            fIvi (float): i번 벽체의 전단응력
            fIyi (float): 인접 벽체와의 교차점 사이의 거리로 정의된 i번 벽의 측면 길이
            fIAcp (float): 단면의 바깥쪽 둘레로 싸인 면적
            fIPcp (float): 단면 바깥쪽 둘레 길이
            fItc (float): 횡방향 철근의 피복 두께

        Returns:
            fOVui (float): 깊은기초 설계기준(일반설계법)  4.1.3.2 설계 (1)의 값 1
            fOq (float): 깊은기초 설계기준(일반설계법)  4.1.3.2 설계 (1)의 값 2
            fOti (float): 깊은기초 설계기준(일반설계법)  4.1.3.2 설계 (1)의 값 3
        """

        assert isinstance(fITu, float)
        assert isinstance(fIAo, float)
        assert fIAo != 0
        assert isinstance(fIvi, float)
        assert isinstance(fIyi, float)
        assert isinstance(fIAcp, float)
        assert isinstance(fIPcp, float)
        assert fIPcp != 0
        assert isinstance(fItc, float)

        fOti = fIAcp / fIPcp
        fOq = max(fIvi * fOti, fITu / (2 * fIAo))
        fOVui = fOq * fIyi

        return RuleUnitResult(
            result_variables = {
                "fOVui": fOVui,
            }
        )