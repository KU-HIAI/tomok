import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010501(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.5.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '1개의 벽체에 대한 국부항복 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.5 각형강관의 단부 마구리판에 작용하는 축방향 집중하중
    4.3.1.5.1 1개의 벽체에 대한 국부항복 한계상태
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 1개의 벽체에 대한 국부항복 한계상태]
	  B["KDS 14 31 25 4.3.1.5.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 국부항복 한계상태/]
	  VarIn1[/입력변수: 저항계수/]
	  VarIn2[/입력변수: 강재의 항복강도/]
	  VarIn3[/입력변수: 벽체의 두께/]
	  VarIn4[/입력변수: 판재의 두께/]
	  VarIn5[/입력변수: 집중하중이 작용하는 폭/]
	  VarIn6[/입력변수: 접합평면과 90도를 이루는 각형 강관폭/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.5.1"])
		C --> Variable_def

	  Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=F_yt\left[5t_p&plus;N\right]\leq&space;BF_yt'>-----------------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    @rule_method
    def Local_yield_limit_state(fIFy,fIt,fItp,fIN,fIB) -> RuleUnitResult:
        """1개의 벽체에 대한 국부항복 한계상태

        Args:
            fIFy (float): 강재의 항복강도
            fIt (float): 벽체의 두께
            fItp (float): 판재의 두께
            fIN (float): 집중하중이 작용하는 폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.1 1개의 벽체에 대한 국부항복 한계상태의 판단 결과
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.1 1개의 벽체에 대한 국부항복 한계상태의 값 1
            fOphi (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.5.1 1개의 벽체에 대한 국부항복 한계상태의 값 2
        """

        assert isinstance(fIFy, float)
        assert isinstance(fIt, float)
        assert isinstance(fItp, float)
        assert isinstance(fIN, float)
        assert isinstance(fIB, float)

        fORn = fIFy * fIt * (5 * fItp + fIN)
        fOphi = 1.0

        if fORn <= fIB * fIFy * fIt:
          return RuleUnitResult(
              result_variables = {
                  "fORn": fORn,
                  "fOphi": fOphi,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )