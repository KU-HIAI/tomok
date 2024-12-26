import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060602_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.6.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '비합성 기둥의 축방향 긴장재 및 철근'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.2 기둥의 축방향 철근
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 비합성 기둥의 축방향 긴장재 및 철근];
    B["KDS 24 14 21 4.6.6.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:겹침이음 위치가 아닌 일반 단면에서의 축방향 철근 단면적/];
		VarIn2[/입력변수:기둥의 단면적/];
		VarIn3[/입력변수:프리스트레싱 강재의 단면적/];
		VarIn4[/입력변수:프리스트레싱 강재의 설계인장강도/];
		VarIn5[/입력변수:축방향 철근의 설계기준항복강도/];
		VarIn6[/입력변수:콘크리트의 설계기준압축강도/];


		VarIn1 & VarIn2 & VarIn3~~~VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.6.2 (2)"])
		C --> Variable_def

		Variable_def--->E

		E{"<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{A_sf_y}{A_gf_{ck}}&plus;\frac{A_{ps}f_{pu}}{A_gf_{ck}}\geq&space;0.135'>---------------------------------"}
		E ---> H(["Pass or Fail"])
    """

    @rule_method
    def Axial_reinforcement_of_non_synthetic_column(fIAs,fIAg,fIAps,fIfpu,fIfy,fIfck) -> RuleUnitResult:
        """비합성 기둥의 축방향 긴장재 및 철근

        Args:
            fIAs (float): 겹침이음 위치가 아닌 일반 단면에서의 축방향 철근 단면적
            fIAg (float): 기둥의 단면적
            fIAps (float): 프리스트레싱 강재의 단면적
            fIfpu (float): 프리스트레싱 강재의 설계인장강도
            fIfy (float): 축방향 철근의 설계기준항복강도
            fIfck (float): 콘크리트의 설계기준압축강도

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.6.2 기둥의 축방향 철근 (2)의 판단 결과
        """

        assert isinstance(fIAs, float)
        assert isinstance(fIAg, float)
        assert isinstance(fIAps, float)
        assert isinstance(fIfpu, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIfck, float)

        if (fIAs*fIfy)/(fIAg*fIfck) + (fIAps*fIfpu)/(fIAg*fIfck) >= 0.135:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )