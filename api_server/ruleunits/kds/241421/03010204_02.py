import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010204_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '콘크리트 건조수축의 영향계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.4 건조수축
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 건조수축의 영향계수];
    B["KDS 24 14 21 3.1.2.4 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 외기습도에 따른 크리프와 건조수축에 미치는영향계수/];
    VarOut2[/출력변수: 건조기간에 따른 건조수축 변형률 함수/];
		VarOut3[/출력변수: 외기습도에 따른 크리프와 건조수축에 미치는 영향계수/];
		VarIn1[/입력변수: 상대습도/];
    VarIn2[/입력변수: 외기 온도/] ;
		VarIn3[/입력변수: 재령일/] ;
		VarIn4[/입력변수: 콘크리트가 외기 중에 노출되었을 때의 재령일/] ;
	 	VarIn5[/입력변수: 부재 크기/];

		VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.4 (2)"])
		C --> Variable_def

		Variable_def--->E & D

		E["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{RH,T}=[1&plus;(\frac{8}{103-RH})(\frac{T-20}{40})]\beta&space;_{RH}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{(t-t_s)}=\sqrt{\frac{(t-t_s)}{0.035h^{2}exp[-0.06(T-20)]&plus;(t-t_s)}}'>---------------------------------"]
		E--->K
		K(["외기습도에 따른 크리프와 건조수축에 미치는 영향계수"])
		D--->L
		L(["건조기간에 따른 건조수축 변형률 함수"])
    """

    @rule_method
    def coefficient_of_drying_shrinkage_of_concrete(fIRH,fITemp,fIt,fIts,fIh) -> RuleUnitResult:
        """콘크리트 건조수축의 영향계수

        Args:
            fIRH (float): 상대습도
            fITemp (float): 외기 온도
            fIt (float): 재령(일)
            fIts (float): 콘크리트가 외기 중에 노출되었을 때의 재령(일)
            fIh (float): 부재 크기

        Returns:
            fObetRHT (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (2)의 값 1
            fObetast (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (2)의 값 2
            fObetaRH (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (2)의 값 3
        """

        assert isinstance(fIRH, float)
        assert isinstance(fITemp, float)
        assert isinstance(fIt, float)
        assert isinstance(fIts, float)
        assert isinstance(fIh, float)

        import numpy as np

        if 40 <= fIRH < 99:
            fObetaRH = -1.55*(1-(fIRH/100)**3)
        elif fIRH >= 99:
            fObetaRH = 0.25

        fObetRHT = (1 + 8/(103-fIRH)*(fITemp-20)/40)*fObetaRH
        fObetast = ((fIt-fIts)/((0.035*fIh**2)*np.exp(-0.06*(fITemp-20))+fIt-fIts))**0.5

        return RuleUnitResult(
            result_variables = {
                "fObetRHT": fObetRHT,
                "fObetast": fObetast,
            }
        )