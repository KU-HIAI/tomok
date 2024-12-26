import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302010206(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.1.2.6'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '원형강관의 공칭전단강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.2 전단강도
    4.3.2.1.2.6 원형강관
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 원형강관의 공칭전단강도]
	  B["KDS 14 31 10 4.3.2.1.2.6"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 공칭전단강도/]
	  VarIn1[/입력변수: 국부좌굴강도/]
	  VarIn2[/입력변수: 강관의 전단면적/]
	  VarIn3[/입력변수: 강재의 탄성계수/]
	  VarIn4[/입력변수: 항복강도/]
	  VarIn5[/입력변수: 최대전단력의 작용점과 전단력이 0인 점 사이의 거리/]
	  VarIn6[/입력변수: 강관의 외경/]
	  VarIn7[/입력변수: 강관의 두께/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7
	  end

	  Python_Class ~~~ C(["KDS 14 31 10 4.3.2.1.2.6"])
		C --> Variable_def --> G --> D --> E --> F

	  G["원형강관의 공칭전단강도 Vn"]
	  D["max(<img src='https://latex.codecogs.com/svg.image?F_{cr}=\frac{1.60E}{\sqrt{\frac{L_v}{D}}\left(\frac{D}{t}\right)^\frac{5}{4}}'> , <img src='https://latex.codecogs.com/svg.image?F_{cr}=\frac{0.78E}{(\frac{D}{t})^\frac{3}{2}}'>)------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?V_n=F_{cr}A_g/2'>----------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?V_n'>---------------"])
    """

    @rule_method
    def niominal_shear_strength_of_pipe(fIAg,fIE,fIFy,fILv,fID,fIt) -> RuleUnitResult:
        """원형강관의 공칭전단강도

        Args:
            fIAg (float): 강관의 전단면적
            fIE (float): 강재의 탄성계수
            fIFy (float): 항복강도
            fILv (float): 최대전단력 작용점과 전단력이 0인 점 사이의 거리
            fID (float): 강관의 외경
            fIt (float): 강관의 두께

        Returns:
            fOVn (float): 강구조부재설계기준(하중저항계수설계법)  4.3.2.1.2.6 원형강관의 값 1
            fOFcr (float): 강구조부재설계기준(하중저항계수설계법)  4.3.2.1.2.6 원형강관의 값 2
        """

        assert isinstance(fIAg, float)
        assert isinstance(fIE, float)
        assert isinstance(fIFy, float)
        assert isinstance(fILv, float)
        assert fILv > 0
        assert isinstance(fID, float)
        assert fID > 0
        assert isinstance(fIt, float)
        assert fIt > 0

        fOFcr = max((1.60 * fIE) / ((fILv / fID) ** 0.5) * (fID / fIt) ** (5 / 4), (0.78 * fIE) / (fID / fIt) ** 1.5)

        if fOFcr <= 0.6 * fIFy :
          fOVn = fOFcr * fIAg / 2
          return RuleUnitResult(
              result_variables = {
                  "fOVn": fOVn,
              }
          )
        else:
          fOFcr = 0.6 * fIFy
          fOVn = fOFcr * fIAg / 2
          return RuleUnitResult(
              result_variables = {
                  "fOVn": fOVn,
              }
          )