import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030116_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.1.16 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '설계지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.16 최대 허용항타하중
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계지지력];
    B["KDS 24 14 51 3.3.1.16 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출변수: 설계지지력/];
		VarIn1[/입력변수: 강도 저항계수/];
		VarIn2[/입력변수: 강재의 항복강도/];
		VarIn3[/입력변수: 부재의 총단면적/];
		VarIn4[/입력변수: 강도 저항계수/];
		VarIn5[/입력변수: 강재의 항복강도/];
		VarIn6[/입력변수: 부재의 순단면적/];

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~	VarIn3
		VarIn4 ~~~ VarIn5 ~~~	VarIn6

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.3.1.16 (1)"])
		C --> Variable_def;

		Variable_def
		J[강재말뚝]
		D[압축]
		E[인장]
		F["<img src='https://latex.codecogs.com/svg.image?0.90\phi&space;F_{y}A_{g}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?0.90\phi&space;F_{y}A_{n}'>---------------------------------"]
		I([Pass or Fail])

		Variable_def ---> J ---> D & E
		D ---> F
		E ---> G
		F & G ---> H(설계지지력) ---> I
		G~~~ |"KDS 24 14 21"| G
		G~~~ |"KDS 24 14 31"| G
    """

    @rule_method
    def design_bearing_capacity(fIphi,fIFy,fIAg,fIAn) -> RuleUnitResult:
        """설계지지력

        Args:
            fIphi (float): 저항계수
            fIFy (float): 강재의 항복강도
            fIAg (float): 부재의 총단면적
            fIAn (float): 부재의 순단면적

        Returns:
            fODebcac (float): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.16 최대 허용항타하중 (1)의 값 1
            fODebcat (float): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.16 최대 허용항타하중 (1)의 값 2
        """

        assert isinstance(fIphi, float)
        assert isinstance(fIFy, float)
        assert isinstance(fIAg, float)
        assert isinstance(fIAn, float)

        fODebcac = 0.90 * fIphi * fIFy * fIAg
        fODebcat = 0.90 * fIphi * fIFy * fIAn

        return RuleUnitResult(
            result_variables = {
                "fODebcac": fODebcac,
                "fODebcat": fODebcat,
            }
        )