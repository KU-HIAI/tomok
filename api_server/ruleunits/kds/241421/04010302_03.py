import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010302_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.3.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '종방향 비틀림 철근의 소요 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.3 비틀림
    4.1.3.2 설계
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 종방향 비틀림 철근의 소요 단면적];
    B["KDS 24 14 21 4.1.3.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 작용 계수하중에 의한 비틀림모멘트/];
		VarIn2[/입력변수: 면적 Ao의 표면 둘레 길이/];
		VarIn3[/입력변수: 철근의 재료계수/];
		VarIn4[/입력변수: 종방향 철근의 항복응력/];
		VarIn5[/입력변수: 속빈 공간을 포함하는, 벽체의 중심선으로 둘러싸인 면적/];
		VarIn6[/입력변수: 압축 스트럿의 경사각/];
		VarOut1[/출력변수: 소요 단면적/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.3.2 (3)"])
		C --> Variable_def

		Variable_def--->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\sum&space;A_{sl}=\frac{T_up_o}{2\phi&space;_sf_yA_o}cot\theta&space;'>---------------------------------"]
		E(["소요단면적"])

    """

    @rule_method
    def Required_cross_sectional_area(fITu,fIpo,fIphis,fIfy,fIAo,fItheta) -> RuleUnitResult:
        """종방향 비틀림 철근의 소요 단면적

        Args:
            fITu (float): 작용 계수하중에 의한 비틀림모멘트
            fIpo (float): 면적 Ao의 표면 둘레 길이
            fIphis (float): 철근의 재료계수
            fIfy (float): 종방향 철근의 항복응력
            fIAo (float): 속빈 공간을 포함하는, 벽체의 중심선으로 둘러싸인 면적
            fItheta (float): 압축 스트럿의 경사각

        Returns:
            fOsumAsl (float): 깊은기초 설계기준(일반설계법)  4.1.3.2 설계 (3)의 값
        """

        assert isinstance(fITu, float)
        assert isinstance(fIpo, float)
        assert isinstance(fIphis, float)
        assert fIphis != 0
        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert isinstance(fIAo, float)
        assert fIAo != 0
        assert isinstance(fItheta, float)
        assert fItheta != 0

        import math

        fOsumAsl = (fITu*fIpo)/(2*fIphis*fIfy*fIAo)*(1/math.tan(math.radians(fItheta)))

        return RuleUnitResult(
            result_variables = {
                "fOsumAsl": fOsumAsl,
            }
        )