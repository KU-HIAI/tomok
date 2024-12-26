import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030116_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.1.16 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '설계지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.16 최대 허용항타하중
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계지지력];
    B["KDS 24 14 51 3.3.1.16 (4)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수: 설계지지력/];
		VarIn1[/입력변수: 강도 저항계수/];
		VarIn2[/입력변수: 목재의 압축강도/];
		VarIn3[/입력변수: 목재의 단면적/];

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~	VarIn3

    end

    Python_Class ~~~ C(["KDS 24 14 51 3.3.1.16 (4)"])
		C --> Variable_def;

		Variable_def
		J[목재 말뚝]
		D[압축]
		E[인장]
		F["<img src='https://latex.codecogs.com/svg.image?\phi&space;F_{co}A'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?\frac{N}{A}'>---------------------------------"]
		I([Pass or Fail])

		Variable_def ---> J ---> D & E
		D ---> F
		E ---> G
		F & G ---> H(설계지지력) ---> I
		G~~~ |"KDS 24 14 21"| G
		G~~~ |"KDS 24 14 31"| G
    """

    @rule_method
    def design_bearing_capacity(fIphi,fIFco,fIA,fIN) -> RuleUnitResult:
        """설계지지력

        Args:
            fIphi (float): 저항계수
            fIFco (float): 목재의 압축강도
            fIA (float): 목재의 단면적
            fIN (float): 목재의 인장강도

        Returns:
            fODebcac (float): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.16 최대 허용항타하중 (4)의 값 1
            fODebcat (float): 교량 하부구조 설계기준 (한계상태설계법)  3.3.1.16 최대 허용항타하중 (4)의 값 2
        """

        assert isinstance(fIphi, float)
        assert isinstance(fIFco, float)
        assert isinstance(fIA, float)
        assert fIA != 0
        assert isinstance(fIN, float)

        fODebcac = fIphi * fIFco * fIA
        fODebcat = fIN / fIA

        return RuleUnitResult(
            result_variables = {
                "fODebcac": fODebcac,
                "fODebcat": fODebcat,
            }
        )