import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060602_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.2 (2)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-16'
    title = '소요 응답수정계수'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.2 소요연성도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 소요 응답수정계수];
    B["KDS 24 17 11 4.6.6.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 소요 응답수정계수/] ;
    VarIn1[/입력변수: 지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트/] ;
    VarIn2[/입력변수: 기둥의 설계휨강도/];
		VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.6.2 (2)"])
		C --> Variable_def--> E
    D(["소요 응답수정계수"]);
    E["<img src='https://latex.codecogs.com/svg.image?R_{req}=\frac{M_{el}}{\phi&space;M_{n}'>---------------------"]

    E--> D
    """

    @rule_method
    def required_response_modification_factor(fIMel,fIphiMn) -> RuleUnitResult:
        """소요 응답수정계수

        Args:
            fIMel (float): 지진하중을 포함한 하중조합에 따른 기둥의 탄성모멘트
            fIphiMn (float): 기둥의 설계휨강도

        Returns:
            fORreq (float): 교량내진설계기준(한계상태설계법) 4.6.6.2 소요연성도 (2)의 값
        """

        assert isinstance(fIMel, float)
        assert isinstance(fIphiMn, float)

        fORreq = fIMel / fIphiMn
        return RuleUnitResult(
            result_variables = {
                "fORreq": fORreq,
                }
            )