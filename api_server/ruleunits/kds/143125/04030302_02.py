import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.2 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '유요성비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 유요성비]
	  B["KDS 14 31 25 4.3.3.2 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarOut1[/출력변수: 주강관 응력상관계수/] ;
	  VarIn1[/입력변수: 유요성비/]
		VarIn2[/입력변수: 주강관의 소요압축강도/]
		VarIn3[/입력변수: 주강관의 소요휨강도/]
		VarIn4[/입력변수: 주강관의 총단면적/]
	  VarIn5[/입력변수: 설계응력/]
    VarIn6[/입력변수: 주강관의 탄성계수/]
    VarIn7[/입력변수: 강재의 항복강도/]
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.2 (2)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?U=\left|P_{r}/A_{g}F_{c}&plus;M_{r}/SF_{c}\right|'>---------------------------------------------------------"] ;
    E["<img src='https://latex.codecogs.com/svg.image?Q_{f}=(1.3-0.4U/\beta)\leq&space;1'>------------------------------------------------------------------"] ;

    Variable_def-->D-->E-->F(["<img src='https://latex.codecogs.com/svg.image?Q_{f}'>------------"])
    """

    @rule_method
    def Effectiveness_ratio(fIPu,fIMu,fIAg,fIFc,fIS,fIbeta) -> RuleUnitResult:
        """유요성비

        Args:
            fIPu (float): 주강관의 소요압축강도
            fIMu (float): 주강관의 소요휨강도
            fIAg (float): 주강관의 총단면적
            fIFc (float): 설계응력
            fIS (float): 주강관의 탄성단면계수
            fIbeta (float): 폭비

        Returns:
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2 각형강관 (2)의 값 1
            fOU (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2 각형강관 (2)의 값 2
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2 각형강관 (2)의 판단 결과
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIMu, float)
        assert isinstance(fIAg, float)
        assert fIAg != 0
        assert isinstance(fIFc, float)
        assert fIFc != 0
        assert isinstance(fIS, float)
        assert fIS != 0
        assert isinstance(fIbeta, float)
        assert fIbeta != 0

        fOU = abs(fIPu/fIAg/fIFc+fIMu/fIS/fIFc)
        fOQf = 1.3 - 0.4 * fOU / fIbeta

        if fOQf <= 1.0 :
          return RuleUnitResult(
              result_variables = {
                  "fOQf": fOQf,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )