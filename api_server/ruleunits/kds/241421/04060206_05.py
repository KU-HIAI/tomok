import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060206_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.6 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '전단철근비'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.6 전단철근
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근비];
    B["KDS 24 14 21 4.6.2.6 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 길이 s내의 전단철근 단면적/];
		VarIn2[/입력변수: 부재의 종방향 축을 따른 전단철근의 간격/];
		VarIn3[/입력변수: 부재의 복부 폭/]
		VarIn4[/입력변수: 전단철근과 부재축과의 각/]
		VarIn5[/입력변수: 28일 콘크리트 공시체의 기준 압축강도/]
		VarIn6[/입력변수: 철근의 기준항복강도/]
		VarOut1[/출력변수: 전단철근비/]
		VarOut2[/출력변수: 최소 전단철근비/]
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarOut2~~~VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.6 (5)"])
		C --> Variable_def

		Variable_def--->F--->E--->H-->I

		E["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v}=A_v/(sb_wsin\alpha)'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v,min}=(0.08\sqrt{f_{ck}})/f_y'>---------------------------------"]

		H["<img src='https://latex.codecogs.com/svg.image?\rho&space;_{v}\geq\rho&space;_{v,min}'>---------------------------------"]

		I(["전단철근비 & Pass and Fail"])
    """

    @rule_method
    def Shear_reinforcement_ratio(fIAv,fIs,fIbw,fIalpha,fIfck,fIfy) -> RuleUnitResult:
        """전단철근비

        Args:
            fIAv (float): 길이 s내의 전단철근 단면적
            fIs (float): 부재의 종방향 축을 따른 전단철근의 간격
            fIbw (float): 부재의 복부 폭
            fIalpha (float): 전단철근과 부재축과의 각
            fIfck (float): 28일 콘크리트 공시체의 기준 압축강도
            fIfy (float): 철근의 기준항복강도

        Returns:
            fOrhov (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (5)의 값 1
            fOrhovmi (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (5)의 값 2
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.6 전단철근 (5)의 판단 결과
        """

        assert isinstance(fIAv, float)
        assert isinstance(fIs, float)
        assert fIs != 0
        assert isinstance(fIbw, float)
        assert fIbw != 0
        assert isinstance(fIalpha, float)
        assert 0 < fIalpha < 180
        assert isinstance(fIfck, float)
        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert fIfck > 0

        import math

        fOrhovmi = (0.08 * fIfck ** 0.5) / fIfy
        fOrhov = fIAv / (fIs * fIbw * math.sin(math.radians(fIalpha)))

        if fOrhov >= fOrhovmi :
          return RuleUnitResult(
              result_variables = {
                  "fOrhov": fOrhov,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )