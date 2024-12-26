import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0403030209_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.3.2.9 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '경사진 웨브의 전단강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.9 전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 경사진 웨브의 전단강도] ;
		B["KDS 14 31 10 4.3.3.2.9 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
		VarOut1[/출력변수: 계수하중에 의한 전단력/] ;
    VarIn1[/입력변수: 경사진 웨브 1개에 작용하는 계수하중에 의한 전단력/] ;
    VarIn2[/입력변수: 연직축에 대한 웨브의 경사각/] ;
		end

		VarOut1 ~~~ VarIn1 & VarIn2

    Python_Class ~~~ C(["KDS 14 31 10 4.3.3.2.9 (1)"])
		C --> Variable_def

		D["<img src=https://latex.codecogs.com/svg.image?V_{ui}=\frac{V_{u}}{cos\theta}>--------------------"]

		Variable_def --> D -->E(["<img src=https://latex.codecogs.com/svg.image?V_{ui}>-------"])
    """

    @rule_method
    def shear_strength_of_inclined_web(fIVu,fItheta) -> RuleUnitResult:
        """경사진 웨브의 전단강도

        Args:
            fIVu (float): 경사진 웨브 1개에 작용하는 계수하중에 의한 전단력
            fItheta (float): 연직축에 대한 웨브의 경사각

        Returns:
            fOVui (float): 강구조부재설계기준(하중저항계수설계법)  4.3.3.2.9 전단강도 (1)의 값
        """

        assert isinstance(fIVu, float)
        assert isinstance(fItheta, float)

        import math

        fOVui = fIVu / math.cos(fItheta)

        return RuleUnitResult(
            result_variables = {
                "fOVui": fOVui,
            }
        )