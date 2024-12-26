import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403010301(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.1.3.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '원형강관의 한계상태'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.3 중공단면 폭의 중심에 종방향으로 분포된 횡방향 집중하중
    4.3.1.3.1 원형강관
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 원형강관의 한계상태]
	  B["KDS 14 31 25 4.3.1.3.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/출력변수: 원형강관의 한계상태/]
	  VarIn2[/입력변수: 원형강관의 외경/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 강재의 항복강도/]
	  VarIn5[/입력변수: 집중하중이 작용하는 폭/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
	  VarIn1 ~~~ VarIn2 & VarIn3
	  VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.1.3.1"])
		C --> Variable_def

	  Variable_def --> G & D --> E --> F
	  G["T형접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;50'>--------------"]
	  D["X형접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;40'>----------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?R_n=5.5F_yt^2(1&plus;0.25N/D)Q_f'>---------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------------"])
    """

    @rule_method
    def Limit_State_of_Circular_Steel_Pipe(fID,fIt,fIFy,fIN,fIQf,fITcon,fIXcon) -> RuleUnitResult:
        """원형강관의 한계상태

        Args:
            fID (float): 원형 강관의 외경
            fIt (float): 주강관의 두께
            fIFy (float): 강재의 항복강도
            fIN (float): 집중하중이 작용하는 폭
            fIQf (float): 주관-응력상관변수
            fITcon (float): T형 접합
            fIXcon (float): X형 접합

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.3.1 원형강관의 판단 결과
            fORn (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.1.3.1 원형강관의 값
        """

        assert isinstance(fID, float)
        assert fID > 0
        assert isinstance(fIt, float)
        assert fIt > 0
        assert isinstance(fIFy, float)
        assert isinstance(fIN, float)
        assert fIN > 0
        assert isinstance(fIQf, float)
        assert isinstance(fITcon, float)
        assert isinstance(fIXcon, float)

        fORn = 5.5 * fIFy * fIt ** 2 * (1 + 0.25 * fIN/fID) * fIQf

        if fITcon != 0 and fIXcon == 0 :
          if fID / fIt <= 50:
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

        elif fITcon == 0 and fIXcon != 0 :
          if fID / fIt <= 40:
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

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )