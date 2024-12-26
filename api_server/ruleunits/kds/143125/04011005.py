import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04011005(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.10.5'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '무보강 웨브의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.5 웨브 압축좌굴강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 무보강 웨브의 설계강도]
	  B["KDS 14 31 25 4.1.10.5"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 무보강 웨브의 설계강도/]
	  VarIn1[/입력변수: 집중하중에 저항하는 거리/]
	  VarIn2[/입력변수: 부재깊이/]
	  VarIn3[/입력변수: 웨브두께/]
	  VarIn4[/입력변수: 강재의 탄성계수/]
	  VarIn5[/입력변수: 압연강재의 경우 필릿 또는 코너반경을 제외한 플랜지 간 순거리, 조립단면의 경우 연결재선 사이의 거리 또는 용접한 경우에는 플랜지 간 순거리/]
	  VarIn6[/입력변수: 웨브의 최소항복강도/]

	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn6
	  VarIn6 ~~~ VarIn5
	  end


    Python_Class ~~~ C(["KDS 14 31 25 4.1.10.5"])
		C --> Variable_def

	  Variable_def --> H --> D --> E
  	E --Pass--> F
  	E --Fail--> G
  	G --> F
  	H["<img src='https://latex.codecogs.com/svg.image?&space;R_n=\frac{24t_w^3\sqrt{EF_{yw}}}{h}'>--------------------------------"]
  	D["부재 단부로부터 한쌍의 집중하중에 저항하는 거리 ≥ d/2"]
  	E["Pass or Fail"]
  	F(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
  	G["<img src='https://latex.codecogs.com/svg.image?&space;R_n\times&space;0.5'>----------------------"]
    """

    @rule_method
    def design_strength_of_unreinforced_web(fIdirecl,fId,fItw,fIE,fIh,fIFyw) -> RuleUnitResult:
        """무보강 웨브의 설계강도

        Args:
            fIdirecl (float): 집중하중에 저항하는 거리
            fId (float): 부재깊이
            fItw (float): 웨브두께
            fIE (float): 강재의 탄성계수
            fIh (float): 압연강재의 경우 필릿 또는 코너반경을 제외한 플랜지 간 순거리, 조립단면의 경우 연결재선 사이의 거리 또는 용접한 경우에는 플랜지 간 순거리
            fIFyw (float): 웨브의 항복응력

        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.5 웨브 압축좌굴강도의 값
        """

        assert isinstance(fIdirecl, float)
        assert isinstance(fId, float)
        assert isinstance(fItw, float)
        assert fItw > 0
        assert isinstance(fIE, float)
        assert fIE > 0
        assert isinstance(fIh, float)
        assert fIh != 0
        assert isinstance(fIFyw, float)
        assert fIFyw > 0

        if fIdirecl < fId/2 :
          fOphiRn = 0.9 * (24 * (fItw**3) * ((fIE * fIFyw)**0.5)) / fIh * 0.5
        else :
          fOphiRn = 0.9 * (24 * (fItw**3) * ((fIE * fIFyw)**0.5)) / fIh

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )