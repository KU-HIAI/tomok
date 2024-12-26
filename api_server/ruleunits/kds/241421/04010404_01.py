import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010404_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.4 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '소요 전단철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소요 전단철근량];
    B["KDS 24 14 21 4.1.4.4 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 전단철근과 슬래브 평면 사이의 각/];
		VarIn2[/입력변수: 콘크리트가 기여하는 설계전단강도/];
		VarIn3[/입력변수: 슬래브의 평균 유효깊이/];
		VarIn4[/입력변수: 전단철근의 반경 방향 간격/];
		VarIn5[/입력변수: 기둥 주변의 각 위험단면의 전단철근의 면적/];
		VarIn6[/입력변수: 철근의 재료계수/];
		VarIn7[/입력변수: 전단 보강 철근의 유효항복강도/];
		VarIn8[/입력변수: 기본 위험단면 둘레길이/];
		VarIn9[/입력변수: 전단 보강 철근의 기준항복강도/];
		VarOut1[/출력변수: 소요 전단철근량/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5 & VarIn6
		VarIn5~~~VarIn7 & VarIn8 & VarIn9
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.4 (1)"])
		C --> Variable_def

		Variable_def--->F--->D--->E
		F["<img src='https://latex.codecogs.com/svg.image?\phi&space;_sf_{vy,ef}=250&plus;0.25d\leq\phi&space;_sf_{vy}'>---------------------------------"]
    D["<img src='https://latex.codecogs.com/svg.image?v_{csd}=0.75v_{cd}+(\frac{1.5d}{s_{r}})A_{v}\phi_{s}f_{vy,ef}(\frac{1}{u_{1}d})sin\alpha'>---------------------------------"]
		E(["소요 전단철근량"])
    """

    @rule_method
    def Required_amount_of_shear_reinforcement(fIVcd,fId,fISr,fIAv,fIu1,fIfvy,fIalpha) -> RuleUnitResult:
        """소요 전단철근량

        Args:
            fIVcd (float): 콘크리트가 기여하는 설계전단강도
            fId (float): 슬래브의 평균 유효깊이
            fISr (float): 전단철근의 반경 방향 간격
            fIAv (float): 기둥 주변의 각 위험단면의 전단철근의 면적
            fIu1 (float): 기본 위험단면 둘레길이
            fIfvy (float): 전단 보강 철근의 기준항복강도
            fIalpha (float): 전단철근과 슬래브 평면 사이의 각

        Returns:
            fOreqasr (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (1)의 값 1
            fOpsfvye (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (1)의 값 2
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.4 전단철근이 있는 슬래브 또는 기초판의 뚫림전단강도 (1)의 판단 결과
        """

        assert isinstance(fIVcd, float)
        assert isinstance(fId, float)
        assert fId != 0
        assert isinstance(fISr, float)
        assert fISr != 0
        assert isinstance(fIAv, float)
        assert isinstance(fIu1, float)
        assert fIu1 != 0
        assert isinstance(fIfvy, float)
        assert isinstance(fIalpha, float)
        assert fIalpha != 0

        import math

        fOpsfvye = 250 + 0.25 * fId

        fOreqasr = 0.75 * fIVcd + (1.5 * fId / fISr) * fIAv * fOpsfvye * (1 / (fIu1 * fId)) * math.sin(math.radians(fIalpha))

        if fOpsfvye <= fIfvy :
          return RuleUnitResult(
              result_variables = {
                  "fOreqasr": fOreqasr,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )