import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010402_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '최대전단응력계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.2 뚫림전단 설계
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대전단응력계수];
    B["KDS 24 14 21 4.1.4.2 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 기본 위험단면 둘레길이/];
		VarIn2[/입력변수: 기둥 치수  c1과 c2의 비에 따른 계수/];
		VarIn3[/입력변수: 하중 편심방향과 평행한 방향의 기둥 치수/];
		VarIn4[/입력변수: 하중 편심방향과 직각인 방향의 기둥 치수/];
		VarIn5[/입력변수: 위험단면둘레 1차모멘트/];
		VarIn6[/입력변수: 편심 거리/];
		VarIn7[/입력변수: 계수하중에 의한 단면의 휨모멘트 값/];
		VarIn8[/입력변수: 원형 단면 기둥의 지름/];
    VarIn9[/입력변수: 계수하중에 의한 전단력/];
    VarIn10[/입력변수: 슬래브의 평균 유효깊이/];
		VarOut1[/출력변수: β/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
    VarIn5~~~VarIn7 & VarIn8 & VarIn9 & VarIn10
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.2 (4)"])
		C --> Variable_def

		Variable_def---> I--사각형기둥인경우--->D--->E
		I{"기둥의 형상에 따라"}
		D["<img src='https://latex.codecogs.com/svg.image?\beta=1&plus;k\frac{M_u}{V_u}\cdot\frac{u_1}{W_1}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?W_1=\frac{c_1^2}{2}&plus;c_1c_2&plus;4c_2d&plus;16d^2&plus;2\pi&space;dc_1'>---------------------------------"]
		I--내부 원형 기둥인경우--->F--->G
		F["<img src='https://latex.codecogs.com/svg.image?e=\frac{M_u}{D}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\beta=1&plus;0.6\pi\frac{e}{D&plus;4d}'>---------------------------------"]
		E & G--->H
		H(["β"])
    """

    @rule_method
    def Correction_factor_of_maximum_shear_stress(fIbetaA,fIbetaB,fIVu,fIu1,fIk,fIc1,fIc2,fId,fIMu,fIDc) -> RuleUnitResult:
        """최대전단응력계수

        Args:
            fIbetaA (float): 최대전단응력에 곱하는 계수 (사각형 기둥의 경우)
            fIbetaB (float): 최대전단응력에 곱하는 계수 (내부 원형기둥인 경우)
            fIVu (float): 계수하중에 의한 전단력
            fIu1 (float): 기본 위험단면 둘레길이
            fIk (float): 기둥 치수  c1과 c2의 비에 따른 계수
            fIc1 (float): 하중 편심방향과 평행한 방향의 기둥 치수
            fIc2 (float): 하중 편심방향과 직각인 방향의 기둥 치수
            fId (float): 슬래브의 평균 유효깊이
            fIMu (float): 계수하중에 의한 단면의 휨모멘트 값
            fIDc (float): 원형 단면 기둥의 지름

        Returns:
            fOlalbcp (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.4.2 뚫림전단 설계 (4)의 값 1
            fObeta (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.4.2 뚫림전단 설계 (4)의 값 2
            fOw1 (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.4.2 뚫림전단 설계 (4)의 값 3
            fOe (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.4.2 뚫림전단 설계 (4)의 값 4
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과
        """

        assert isinstance(fIVu, float)
        assert fIVu != 0
        assert isinstance(fIu1, float)
        assert isinstance(fIk, float)
        assert isinstance(fIc1, float)
        assert fIc1 != 0
        assert isinstance(fIc2, float)
        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIMu, float)
        assert isinstance(fIDc, float)
        assert fIDc > 0

        import math

        fOwone = (fIc1**2) / 2 + fIc1 * fIc2 + 4 * fIc2 * fId + 16 * fId**2 + 2 * math.pi * fId * fIc1
        fOe = fIMu / fIDc

        if fIbetaA != 0 and fIbetaB == 0 :
          fObeta = 1 + fIk * (fIMu / fIVu) * (fIu1 / fOw1)
          return RuleUnitResult(
              result_variables = {
                  "fObeta": fObeta,
              }
          )
        elif fIbetaA == 0 and fIbetaB != 0 :
          fObeta = 1 + 0.6 * math.pi * fOe / (fIDc + 4 * fId)
          return RuleUnitResult(
              result_variables = {
                  "fObeta": fObeta,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )