import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030201_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '유요성비'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 유요성비]
	  B["KDS 14 31 25 4.3.2.1 (2)"]
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

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.1 (2)"])
		C --> Variable_def

	  E["<img src='https://latex.codecogs.com/svg.image?&space;Q_{f}=1.0-0.3U(1&plus;U)'>----------------------------------------------------------"] ;
    D[주장관이 압축인 경우]

		Variable_def --> D --> E --> R(["<img src='https://latex.codecogs.com/svg.image?&space;Q_{f}'>--------"]);
    D[주장관이 압축인 경우]
    """

    @rule_method
    def Effectiveness_ratio(fIPu,fIMu,fIAg,fIS,fIFy) -> RuleUnitResult:
        """유요성비

        Args:
            fIPu (float): 주강관의 소요압축강도
            fIMu (float): 주강관의 소요휨강도
            fIAg (float): 주강관의 총단면적
            fIS (float): 주강관의 탄성단면계수
            fIFy (float): 강재의 항복강도

        Returns:
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1 원형강관 (2)의 값 1
            fOU (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1 원형강관 (2)의 값 2
            fOFc (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.1 원형강관 (2)의 값 3
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIMu, float)
        assert isinstance(fIAg, float)
        assert fIAg != 0
        assert isinstance(fIS, float)
        assert fIS != 0
        assert isinstance(fIFy, float)
        assert fIFy != 0

        fOFc = fIFy
        fOU = abs(fIPu / (fIAg * fOFc) + fIMu / (fIS * fOFc))
        fOQf = 1.0 - 0.3 * fOU * (1 + fOU)

        return RuleUnitResult(
            result_variables = {
                "fOQf": fOQf,
            }
        )