import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04070702_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.7.7.2 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-14'
    title = '탄성지진응답계수'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.2 등가정적하중법
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 탄성지진응답계수]
	  B["KDS 24 17 11 4.7.7.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 탄성지진응답계수/]
  	VarIn1[/입력변수: 지진격리받침의 유효강성/]
	  VarIn2[/입력변수: 상부구조의 총변위/]
	  VarIn3[/입력변수: 상부구조물의 총중량/]
	  VarIn4[/입력변수: 유효수평지반가속도/]
	  VarIn5[/입력변수: 지진격리교량의지반계수/]
	  VarIn6[/입력변수: 유효주기/]
	  VarIn7[/입력변수: 지진격리교량의 감쇠계수/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
	  VarIn2 & VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end

	  Python_Class ~~~ C(["KDS 24 17 11 4.7.7.2 (2)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?C_s=\frac{K_{eff}\times&space;d}{W}=\frac{S\cdot&space;S_i}{T_{eff}B}'>------------------------------------------------------"];

	  E(["<img src='https://latex.codecogs.com/svg.image?C_s'>"]);

	  Variable_def --> D --> E
    """

    @rule_method
    def Elastic_siesmic_response_coefficient(fIkeff,fId,fIW,fIS,fISi,fITeff,fIB) -> RuleUnitResult:
        """탄성지진응답계수

        Args:
            fIkeff (float): 지진격리받침의 유효강성
            fId (float): 상부구조의 총변위
            fIW (float): 상부구조물의 총중량
            fIS (float): 유효수평지반가속도
            fISi (float): 지진격리교량의 지반계수
            fITeff (float): 유효주기
            fIB (float): 지진격리교량의 감쇠계수

        Returns:
            fOCs (float): 교량내진설계기준(한계상태설계법) 4.7.7.2 등가정적하중법 (2)의 값
        """

        assert isinstance(fIkeff, float)
        assert isinstance(fId, float)
        assert isinstance(fIW, float)
        assert fIW > 0
        assert isinstance(fIS, float)
        assert isinstance(fISi, float)
        assert isinstance(fITeff, float)
        assert fITeff > 0
        assert isinstance(fIB, float)
        assert fIB > 0

        fOCs = max(fIkeff * fId / fIW , fIS * fISi / fITeff / fIB)

        if fOCs >= 2.5 * fIS:
          fOCs = 2.5 * fIS

        return RuleUnitResult(
            result_variables = {
                "fOCs": fOCs,
                }
            )