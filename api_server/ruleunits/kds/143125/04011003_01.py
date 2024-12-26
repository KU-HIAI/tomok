import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04011003_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.10.3 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '웨브 크리플링 공칭강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.3 웨브 크리플링강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 웨브 크리플링 공칭강도]
	  B["KDS 14 31 25 4.1.10.3 (1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 웨브 크리플링 공칭강도/]
  	VarIn1[/입력변수: 부재깊이/]
  	VarIn2[/입력변수: 웨브두께/]
  	VarIn3[/입력변수: 집중하중이 작용하는폭/]
  	VarIn4[/입력변수: 플랜지 두께/]
	  VarIn5[/입력변수: 강재의 탄성계수/]
	  VarIn6[/입력변수: 웨브의 항복응력/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
  	end


    Python_Class ~~~ C(["KDS 14 31 25 4.1.10.3 (1)"])
		C --> Variable_def

	  Variable_def --> G --> D --Pass--> E --> F


	  G["집중하중이 제단에서 떨어진거리 ≥ d/2 에서 작용"]
	  D["Pass or Fail"]
	  E["<img src='https://latex.codecogs.com/svg.image?R_n=0.80t_w^2\left[1&plus;3(\frac{N}{d})\left(\frac{t_w}{t_f}\right)^{1.5}\right]\sqrt{\frac{EF_{yw}t_f}{t_w}}'>-----------------------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def web_crippling_nominal_strength(fId,fItw,fIN,fItf,fIE,fIFyw) -> RuleUnitResult:
        """웨브 크리플링 공칭강도

        Args:
            fId (float): 부재깊이
            fItw (float): 웨브두께
            fIN (float): 집중하중이 작용하는 폭
            fItf (float): 플랜지 두께
            fIE (float): 강재의 탄성계수
            fIFyw (float): 웨브의 항복응력

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.3 웨브 크리플링강도 (1)의 값
        """

        assert isinstance(fId, float)
        assert fId != 0
        assert isinstance(fItw, float)
        assert fItw > 0
        assert isinstance(fIN, float)
        assert isinstance(fItf, float)
        assert fItf > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIFyw, float)
        assert fIFyw > 0

        if fIN >= fId/2 :
          fORn = 0.80*(fItw**2)*(1+3*(fIN/fId)*(fItw/fItf)**1.5)*(fIE*fIFyw*fItf/fItw)**0.5

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )