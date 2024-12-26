import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010205_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.5 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '콘크리트 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.5 응력-변형률 관계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 응력];
    B["KDS 24 14 21 3.1.2.5 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 압축변형률/];
		VarIn2[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
    VarIn3[/입력변수: 콘크리트에 대한 재료계수/] ;
		VarIn4[/입력변수: 상승 곡선부의 형상을 나타내는 지수/] ;
		VarIn5[/입력변수: 최대 응력에 처음 도달할 때의 변형률/] ;
	 	VarIn6[/입력변수: 극한변형률/];
    VarOut1[/출력변수: 콘크리트 응력/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.5 (2)"])
		C --> Variable_def

		Variable_def--->G & D

		G{"<img src='https://latex.codecogs.com/svg.image?0\leq\varepsilon&space;_c\leq\varepsilon&space;_{co}'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{co}<\varepsilon&space;_c\leq\varepsilon&space;_{cu}'>---------------------------------"}
		G--->K
		K["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})[1-(1-\frac{\varepsilon&space;_c}{\varepsilon&space;_{co}})^{n}]'>---------------------------------"]
		D--->E
		E["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})'>---------------------------------"]
		F(["콘크리트 강도"])
		K & E--->F
    """

    @rule_method
    def stress_of_concrete(fIepsc,fIfck,fIphic) -> RuleUnitResult:
        """콘크리트 응력

        Args:
            fIepsc (float): 콘크리트의 압축변형률
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도
            fIphic (float): 콘크리트에 대한 재료계수

        Returns:
            fOfc (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2)의 값 1
            fOn (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2)의 값 2
            fOepsco (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2)의 값 3
            fOepscu (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2)의 값 4
            pass_fail (bool): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2)의 판단 결과
        """

        assert isinstance(fIepsc, float)
        assert fIepsc >= 0
        assert isinstance(fIfck, float)
        assert isinstance(fIphic, float)

        if fIfck <= 40:
          fOn = 2.0
          fOepsco = 0.002
          fOepscu = 0.0033
        else:
          fOn = 1.2 + 1.5+((100-fIfck)/60)**4
          fOepsco = 0.002 + (fIfck-40)/100000
          fOepscu = 0.0033 - (fIfck-40)/100000

        if 0 <= fIepsc <= fOepsco:
          fOfc = fIphic * 0.85 * fIfck * (1 - (1 - fIepsc / fOepsco)**fOn)
        else:
          fOfc = fIphic * 0.85 * fIfck

        if fOn <= 2.0 and fOepsco >= 0.002 and fOepscu <= 0.0033 :
          return RuleUnitResult(
              result_variables = {
                  "fOfc": fOfc,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOfc": fOfc,
                  "pass_fail": False,
              }
          )