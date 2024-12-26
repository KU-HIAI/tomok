import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04030101_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.3.1.1 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '재하차로의 수'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.3 활하중
    4.3.1 차량활하중 : LL
    4.3.1.1 재하차로의 수
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 재하차로의 수];
    B["KDS 24 12 21 4.3.1.1 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 재하차로의 수/];
    VarIn1[/입력변수 : 연석, 방호울타리간의 교폭/];
    VarIn2[/입력변수 : 발주자에 의해 정해진 계획차로의 폭/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.3.1.1 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?N=\frac{W_{C}}{W_{P}}'>의 정수부"];
    E{"N=1 and Wc &ge; 6.0m"};
    F(["재하차로의 수"]);
    G["N=2"];
    Variable_def--->D--->F
    D--->E--->G--->F
    """

    @rule_method
    def number_of_loading_lane(fIWc,fIWP) -> RuleUnitResult:
        """재하차로의 수

        Args:
            fIWc (float): 연석, 방호울타리간의 교폭
            fIWP (float): 발주자에 의해 정해진 계획차로의 폭


        Returns:
            iON (int): 강교 설계기준(한계상태설계법)  4.3.1.1 재하차로의 수 (1)의 값
        """

        import math

        assert isinstance(fIWc, float)
        assert isinstance(fIWP, float)
        assert fIWP != 0

        iON = math.floor(fIWc/fIWP)

        if iON == 1 and fIWc >= 6:
          iON = 2

        return RuleUnitResult(
            result_variables = {
                "iON": iON,
            }
        )