import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04011001(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.10.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '플랜지의 설계강도'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.1 플랜지 국부휨강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 플랜지의 설계강도]
	  B["KDS 14 31 25 4.1.10.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut[/출력변수: 플랜지의 설계강도/]
  	VarIn1[/입력변수: 공칭지압강도/]
  	VarIn2[/입력변수: 저항계수/]
  	VarIn3[/입력변수: 플랜지의 항복강도/]
  	VarIn4[/입력변수: 하중을 받는 플랜지의 두께/]
  	VarIn5[/입력변수: 하중구간의 길이/]
  	VarIn6[/입력변수: 플랜지 부재의 폭/]

  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
  	end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.10.1"])
		C --> Variable_def

	  Variable_def --> K --> D --Pass--> E
  	D --Fail--> F --> G --> H --Pass--> I
  	H --Fail --> J

  	K["하중구간의 길이 <<img src='https://latex.codecogs.com/svg.image?&space;0.15b_f'>"]
  	D["Pass or Fail"]
  	E["검토 x"]
  	F["<img src='https://latex.codecogs.com/svg.image?R_n=6.25t_f^2F_{yf}'>------------------------------"]
  	G["부재단부로부터 집중하중에 저항하는 거리 <<img src='https://latex.codecogs.com/svg.image?10t_f'>"]
  	H["Pass or Fail"]
	  I(["<img src='https://latex.codecogs.com/svg.image?R_n'> x 0.5"])
	  J(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def design_strength_of_flange(fIPhi,fIFyf,fItf,fIlelose,fIbf) -> RuleUnitResult:
        """플랜지의 설계강도

        Args:
            fIPhi (float): 저항계수
            fIFyf (float): 플랜지의 항복강도
            fItf (float): 하중을 받는 플랜지의 두께
            fIlelose (float): 하중구간의 길이
            fIbf (float): 플랜지 부재의 폭


        Returns:
            fOphiRn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.1 플랜지 국부휨강도의 값 1
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.1 플랜지 국부휨강도의 값 2
        """

        assert isinstance(fIPhi, float)
        assert isinstance(fIFyf, float)
        assert isinstance(fItf, float)
        assert isinstance(fIlelose, float)
        assert isinstance(fIbf, float)

        fORn = (6.25)*(fItf*fItf)*fIFyf
        if fIlelose < (0.15)*fIbf :
          fOphiRn = fIPhi * fORn
        if fIlelose < (10)*fItf :
          fOphiRn = fIPhi * fORn * 0.5

        return RuleUnitResult(
            result_variables = {
                "fOphiRn": fOphiRn,
            }
        )