import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04030301_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.3.1 (2)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '응력상관계수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.1 원형강관
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 응력상관계수]
	  B["KDS 14 31 25 4.3.3.1 (2)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
    VarOut1[/출력변수: 응력상관계수/] ;
    VarOut2[/출력변수: 유요성비/] ;
    VarIn1[/입력변수: 주강관의 소요축강도/] ;
    VarIn2[/입력변수: 주강관의 소요휨강도/] ;
    VarIn3[/입력변수: 주강관의 총단면적/] ;
    VarIn4[/입력변수: 설계응력/] ;
    VarIn5[/입력변수: 주강관의 탄성단면계수/] ;
    VarIn6[/입력변수: 주강관의 항복강도/] ;
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.3.1 (2)"])
		C --> Variable_def

	  D["<img src='https://latex.codecogs.com/svg.image?U=\left|P_{u}/A_{g}F_{c}&plus;M_{u}/SF_{c}\right|'>---------------------------------------------------------------"] ;
    E(["<img src='https://latex.codecogs.com/svg.image?Q_{f}=1.0-0.3U(1&plus;U)'>-------------------------------------------------------------"]) ;
    Variable_def -->D-->E
    """

    @rule_method
    def stress_correlation_coefficient(fIPu,fIMu,fIAg,fIFc,fIS) -> RuleUnitResult:
        """응력상관계수

        Args:
            fIPu (float): 주강관의 소요축강도
            fIMu (float): 주강관의 소요휨강도
            fIAg (float): 주강관의 총단면적
            fIFc (float): 설계응력
            fIS (float): 주강관의 탄성단면계수

        Returns:
            fOQf (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1 원형강관 (2)의 값 1
            fOU (float): 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.1 원형강관 (2)의 값 2
        """

        assert isinstance(fIPu, float)
        assert isinstance(fIMu, float)
        assert isinstance(fIAg, float)
        assert fIAg != 0
        assert isinstance(fIFc, float)
        assert fIFc != 0
        assert isinstance(fIS, float)
        assert fIS != 0

        fOU = abs(fIPu/fIAg/fIFc+fIMu/fIS/fIFc)
        fOQf = 1.0-0.3*fOU*(1+fOU)

        return RuleUnitResult(
            result_variables = {
                "fOQf": fOQf,
            }
        )