import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04011002_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.10.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '웨브 국부항복강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.2 웨브 국부항복강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 웨브 국부항복강도]
	  B["KDS 14 31 25 4.1.10.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 웨브국부 공칭강도/]
  	VarIn1[/입력변수: 압축 집중하중의 작용점에서 재단까지의 거리/]
  	VarIn2[/입력변수: 부재깊이/]
  	VarIn3[/입력변수: 플랜지의 바깥쪽면으로부터 웨브 필릿선단까지의 거리/]
  	VarIn4[/입력변수: 집중하중이 작용하는폭/]
  	VarIn5[/입력변수: 웨브의 항복응력/]
  	VarIn6[/입력변수: 웨브두께/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
  	end


    Python_Class ~~~ C(["KDS 14 31 25 4.1.10.2 (2)"])
		C --> Variable_def

	  Variable_def --> G --> D --Pass--> E --> F


  	G{"인장 또는 압축 집중하중의 작용점에서 재단까지의 거리 ≤ 부재깊이 d"}
	  D["Pass or Fail"]
	  E["<img src='https://latex.codecogs.com/svg.image?R_n=(2.5k&plus;N)F_{yw}t_w'>------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def web_local_yield_strength(fIdfaclf,fId,fIk,fIN,fIFyw,fItw) -> RuleUnitResult:
        """웨브 국부항복강도

        Args:
            fIdfaclf (float): 집중하중의 작용점에서 재단까지의 거리
            fId (float): 부재깊이
            fIk (float): 플랜지의 바깥쪽 면으로부터 웨브 필릿선단까지의 거리
            fIN (float): 집중하중이 작용하는폭
            fIFyw (float): 웨브의 항복응력
            fItw (float): 웨브두께

        Returns:
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.2 웨브 국부항복강도 (2)의 값
        """

        assert isinstance(fIdfaclf, float)
        assert isinstance(fId, float)
        assert isinstance(fIk, float)
        assert isinstance(fIN, float)
        assert isinstance(fIFyw, float)
        assert isinstance(fItw, float)

        if fIdfaclf <= fId :
          fORn = ((2.5*fIk)+fIN)*fIFyw*fItw

        return RuleUnitResult(
            result_variables = {
                "fORn": fORn,
            }
        )