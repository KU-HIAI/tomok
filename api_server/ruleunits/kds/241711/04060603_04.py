import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241711_04060603_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 17 11 4.6.6.3 (4)'
    ref_date = '2022-02-25'
    doc_date = '2024-02-15'
    title = '총 소요 단면적'

    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.3 심부구속 횡방향철근량
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 심부구속 횡방향철근의 총 소요 단면적];
    B["KDS 24 17 11 4.6.6.3 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 총 소요 단면적/] ;
    VarIn1[/입력변수: 띠철근의 수직간격/] ;
    VarIn2[/입력변수: 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 심부의 단면 치수/];
		VarIn3[/입력변수: 콘크리트의 설계기준 압축강도/];
		VarIn4[/입력변수: 횡방향철근의 설계기준 항복강도/];
		VarIn5[/입력변수: 교량내진설계기준 한계상태설계법 4.6.6.3 심부구속 횡방향철근량 2의 식 4.6-16의 계수/];
		VarIn6[/입력변수: 교량내진설계기준 한계상태설계법 4.6.6.3 심부구속 횡방향철근량 2의 식 4.6-17의 계수/];
		VarIn7[/입력변수: 교량내진설계기준 한계상태설계법 4.6.6.3 심부구속 횡방향철근량 2의 식 4.6-18의 계수/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5 & VarIn6 & VarIn7

    end

    Python_Class ~~~ C(["KDS 24 17 11 4.6.6.3 (4)"])
		C --> Variable_def-->D -->F
    D["<img src='https://latex.codecogs.com/svg.image?&space;A_{sb}=0.9ah_{c}(0.008\alpha\beta\frac{f_{ck}}{f_{yh}}&plus;\gamma)'>------------------------------------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?&space;A_{sb}'>----------------"]) ;
    """

    @rule_method
    def total_required_cross_sectional_area(fIa,fIhc,fIfck,fIfyh,fIalpha,fIbeta,fIgamma) -> RuleUnitResult:
        """총 소요 단면적

        Args:
            fIa (float): 띠철근의 수직간격
            fIhc (float): 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 심부의 단면 치수
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도
            fIalpha (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량(2)의 식 (4.6-16)의 계수
            fIbeta (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량(2)의 식 (4.6-17)의 계수
            fIgamma (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량(2)의 식 (4.6-18)의 계수

        Returns:
            fOAsh (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량 (4)의 값
        """

        assert isinstance(fIa, float)
        assert isinstance(fIhc, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIfyh, float)
        assert isinstance(fIalpha, float)
        assert isinstance(fIbeta, float)
        assert isinstance(fIgamma, float)

        fOAsh = 0.9 * fIa * fIhc * (0.008 * fIalpha * fIbeta * fIfck / fIfyh + fIgamma)

        return RuleUnitResult(
            result_variables = {
                "fOAsh": fOAsh,
                }
            )