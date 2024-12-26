import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010203_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '전체 변형률'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.3 크리프
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전체 변형률];
    B["KDS 24 14 21 3.1.2.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 시간 t'에서 작용응력/];
		VarIn2[/입력변수: 설계기준압축강도/];
    VarIn3[/입력변수: 콘크리트의 압축강도/] ;
		VarIn4[/입력변수: 부재의 크기/] ;
		VarIn5[/입력변수: 평균 상대습도/] ;
		VarIn6[/입력변수: 재하할 때의 재령/] ;
		VarIn7[/입력변수: 재하기간/] ;
		VarIn8[/입력변수: 시멘트의 종류/] ;
		VarIn9[/입력변수: 양생온도/] ;
		VarIn10[/입력변수: 온도변화/] ;
		VarIn11[/입력변수: 작용응력의 크기/] ;
		VarIn12[/입력변수: 재령t'일에서의 초기접선 탄성계수/] ;
		VarIn13[/입력변수: 재령 28일에서의 초기접선 탄성계수/] ;
		VarIn14[/입력변수: 강도보정계수/] ;
	 	VarOut1[/출력변수: 전체 변형률/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.3 (1)"])
		C --> Variable_def

		Variable_def--->G
		G["<img src='https://latex.codecogs.com/svg.image?E_{ci}=1.18E_{c}'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?E_{ci}(t^{\prime})=\sqrt{\beta&space;_{cc}(t)}E_{ci}'>---------------------------------"]
		G--->D
		D--->E
		E["<img src='https://latex.codecogs.com/svg.image?\varepsilon_{c\sigma}(t,t^{\prime})=f_{c}(t^{\prime})[\frac{1}{E_{ci}(t^{\prime})}+\frac{\varphi(t,t^{\prime})}{E_{ci}}]'>---------------------------------"]
		E--->F
		F([전체변형률])
    """

    @rule_method
    def total_strain(fIfctpri,fIbetcct,fIEc) -> RuleUnitResult:
        """전체 변형률

        Args:
            fIfctpri (float): 전체 변형률
            fIbetcct (float): 강도 보정 계수
            fIEc (float): 보통 콘크리트의 탄성계수

        Returns:
            fOepstpr (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (1)의 값 1
            fOEcitpr (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (1)의 값 2
            fOEci (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (1)의 값 3
        """

        assert isinstance(fIfctpri, float)
        assert isinstance(fIbetcct, float)
        assert isinstance(fIEc, float)

        fOEci = 1.18 * fIEc
        fOEcitpr = (fIbetcct)**0.5 * fOEci
        fOepstpr = fIfctpri * (1 / fOEcitpr + fIfctpri / fOEci)

        return RuleUnitResult(
            result_variables = {
                "fOepstpr": fOepstpr,
            }
        )