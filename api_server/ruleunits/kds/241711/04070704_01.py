import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070704_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.4 (1)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-13'
    title = 'i번째 모드의 탄성지진응답계수'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.4 다중모드스펙트럼해석법
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: i번째 모드의 탄성지진응답계수];
	  B["KDS 24 17 11 4.7.7.4 (1)"];
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: i번째 모드의 탄성지진응답계수/];
	  VarIn1[/입력변수: 해당모드주기/];
	  VarIn2[/입력변수: 유효주기/];
	  VarIn3[/입력변수: 지진격리교량의 감쇠계수/];
	  VarIn4[/입력변수: 지진격리교량의 지반계수/];
	  VarIn5[/입력변수: 유효수평지반가속도/];
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.4 (1)"])
		C --> Variable_def

	  G["<img src='https://latex.codecogs.com/svg.image?C_{si}=\frac{SS_i}{T_i}'>"];
	  D["<img src='https://latex.codecogs.com/svg.image?C_{si}=\frac{SS_i}{T_iB}'>"];
	  E(["<img src='https://latex.codecogs.com/svg.image?C_{si}'>"]);
	  F{"<img src='https://latex.codecogs.com/svg.image?T_i\leq&space;0.8T_{eff}'>"};

  	Variable_def ---> F
	  F -- Yes ---> G
	  F -- No ---> D
	  G & D ---> E
    """

    @rule_method
    def Elastic_seismic_response_coefficient_of_the_ith_mode(fITi,fITeff,fIS,fISi,fIB) -> RuleUnitResult:
        """i번째 모드의 탄성지진응답계수

        Args:
            fITi (float): 해당모드주기
            fITeff (float): 유효주기
            fIS (float): 유효수평지반가속도
            fISi (float): 지진격리교량의 지반계수
            fIB (float): 지진격리교량의 감쇠계수

        Returns:
            fOCsi (float): 교량내진설계기준(한계상태설계법) 4.7.7.4 다중모드스펙트럼해석법 (1)의 값
        """

        assert isinstance(fITi, float)
        assert fITi > 0
        assert isinstance(fITeff, float)
        assert isinstance(fIS, float)
        assert isinstance(fISi, float)
        assert isinstance(fIB, float)
        assert fIB > 0


        if fITi <= 0.8 * fITeff :
          fOCsi = fIS * fISi / fITi
          return RuleUnitResult(
              result_variables = {
                  "fOCsi": fOCsi,
                  }
              )
        else:
          fOCsi = fIS * fISi / fITi / fIB
          return RuleUnitResult(
              result_variables = {
                  "fOCsi": fOCsi,
                  }
              )