import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010302(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.3.2'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '각형강관의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.3 중공단면 폭의 중심에 종방향으로 분포된 횡방향 집중하중
    4.3.1.3.2 각형강관
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 각형강관의 한계상태]
	  B["KDS 14 31 25 4.3.1.3.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/출력변수: 각형강관의 한계상태/]
	  VarIn2[/입력변수: 접합평면과 90도를 이루는 각형 강관폭/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 강재의 항복강도/]
	  VarIn5[/입력변수: 판재의 두께/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
    VarIn7[/입력변수: 유요성비/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.3.2"])
		C --> Variable_def

	  Variable_def --> G & D --> E --> F
	  G["하중을 받는 관벽에 관한 <img src='https://latex.codecogs.com/svg.image?B/t\leq&space;40(\phi=1.00)'>--------------"]
	  D["<img src='https://latex.codecogs.com/svg.image?Q_f=(1-U^2)^{0.5}'>------------------------------"]
	  E["<img src=https://latex.codecogs.com/svg.image?R_n=[F_yt^2/(1-t_p/B)][2N/B&plus;4(1-t_p/B)^{0.5}Q_f]'>------------------------------------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------------"])
    """

    @rule_method
    def Limit_State_of_Rectangular_Steel_Pipe(fIB,fIt,fIFy,fItp,fIU,fIN) -> RuleUnitResult:
        """각형강관의 한계상태

        Args:
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIt (float): 주강관의 두께
            fIFy (float): 강재의 항복강도
            fItp (float): 판재의 두께
            fIU (float): 유요성비
            fIN (float): 집중하중이 작용하는 폭

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.3.2 각형강관의 판단 결과
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.3.2 각형강관의 값 1
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.3.2 각형강관의 값 2
        """

        assert isinstance(fIB, float)
        assert fIB != 0
        assert isinstance(fIt, float)
        assert fIt != 0
        assert isinstance(fIFy, float)
        assert isinstance(fItp, float)
        assert isinstance(fIU, float)
        assert isinstance(fIN, float)
        assert fItp < fIB

        fOQf = (1 - fIU ** 2) ** 0.5
        fORn = (fIFy * fIt ** 2 / (1 - fItp/fIB)) * (2 * fIN/fIB + 4 * (1 - fItp / fIB) ** 0.5 * fOQf)

        if fIB/fIt <= 40:
          return RuleUnitResult(
              result_variables = {
                  "fORn": fORn,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )