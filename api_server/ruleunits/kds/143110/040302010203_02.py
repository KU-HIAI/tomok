import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010203_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.2.3 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.2 전단강도
    4.3.2.1.2.3 인장역작용을 이용한 설계공칭전단강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도]
	  B["KDS 14 31 10 4.3.2.1.2.3 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도/]
	  VarIn1[/입력변수: 웨브의 높이/]
	  VarIn2[/입력변수: 웨브 두께/]
	  VarIn3[/입력변수: 웨브 판 좌굴계수/]
    VarIn4[/입력변수: 강재의 탄성계수/]
    VarIn5[/입력변수: 웨브의 최소항복강도/]
    VarIn6[/입력변수: 웨브의 단면적/]
    VarIn7[/입력변수: 웨브 전단항복응력에 대한 선형좌굴 이론에 따른 웨브 임계응력의 비율을 나타내는 정수/]
    VarIn8[/입력변수: 보강재의 간격/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 ~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8


  	end
	  Python_Class ~~~ C1(["KDS 14 31 10 4.3.2.1.2.3 (2)"]) -->Variable_def --> D & E
	  D --> F
	  E --> G
	  F & G --> H
	  D["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 ≥커버플레이트x3/4인 연속용접"]
	  E["커버플레이트 단부면의 전체폭에 걸쳐 용접치수 <커버플레이트x3/4인 연속용접"]
	  F["연장길이=커버플레이트 폭"]
	  G["연장길이=(커버플레이트 폭)x1.5"]
	  H(["연장길이"])
    """

    @rule_method
    def niominal_shear_strength(fIh,fItw,fIKv,fIE,fIFyw,fIAw,fICv,fIa) -> RuleUnitResult:
        """인장역항복의 한계상태에 따른 인장역작용을 이용한 공칭전단강도

        Args:
            fIh (float): 웨브의 높이
            fItw (float): 웨브 두께
            fIKv (float): 웨브 판 좌굴계수
            fIE (float): 강재의 탄성계수
            fIFyw (float): 웨브의 최소항복강도
            fIAw (float): 웨브의 단면적
            fICv (float): 웨브 전단항복응력에 대한 선형좌굴 이론에 따른 웨브 임계응력의 비율을 나타내는 정수
            fIa (float): 보강재의 간격

        Returns:
            fOVn (float): 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.2.3 (2)의 값
        """

        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fItw, float)
        assert fItw != 0
        assert isinstance(fIKv, float)
        assert fIKv > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFyw, float)
        assert fIFyw > 0
        assert isinstance(fIAw, float)
        assert isinstance(fICv, float)
        assert isinstance(fIa, float)
        assert fIa > 0


        if fIh / fItw <= 1.10 * (fIKv * fIE / fIFyw) ** 0.5:
            fOVn = 0.6 * fIFyw * fIAw

            return RuleUnitResult(
            result_variables = {
              "fOVn": fOVn,
               }
            )
        else:
            fOVn = 0.6 * fIFyw * fIAw * (fICv + (1 - fICv) / (1.15 * (1 + (fIa / fIh) ** 2)))
            return RuleUnitResult(
            result_variables = {
              "fOVn": fOVn,
               }
            )