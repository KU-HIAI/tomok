import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010204_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.4 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '콘크리트의 건조수축 변형률'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.4 건조수축
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 건조수축 변형률];
    B["KDS 24 14 21 3.1.2.4 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 콘크리트의 건조수축 변형률,재령 ts에서 외기에 노출된 콘크리트의 재령 t에서의 전체 건조수축 변형률/];
		VarOut2[/출력변수: 개념 건조수축계수/];
    VarOut3[/출력변수: 건조기간에 따른 건조수축 변형률 함수/] ;
		VarOut4[/출력변수: 콘크리트 평균압축강도에 따른 건조수축 변형률 함수/] ;
		VarOut5[/출력변수: 외기습도에 따른 크리프와 건조수축에 미치는 영향계수/] ;
	 	VarIn1[/입력변수: 콘크리트 총 재령/];
		VarIn2[/입력변수: 콘크리트가 외기 중에 노출되었을 때의 재령/];
		VarIn3[/입력변수: 시멘트 종류에 따른 건조수축에 미치는 영향계수/];
		VarIn4[/입력변수: 부재의 크기/];
		VarIn5[/입력변수: 평균상대습도/];
		VarIn6[/입력변수: 콘크리트 평균압축강도/];

		VarOut1 & VarOut2 & VarOut3 & VarOut4 & VarOut5 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.4 (1)"])
		C --> Variable_def

		Variable_def--->D
		D{"<img src='https://latex.codecogs.com/svg.image?\beta_{sc}'>--------------------------------------------------------"}


		D--2종 시멘트---> G
		D--1종, 5종 시멘트---> H
		D--3종 시멘트---> I

	  G["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=4'>---------------------------------"]
	  H["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=5'>---------------------------------"]
	  I["<img src='https://latex.codecogs.com/svg.image?\beta_{sc}=8'>---------------------------------"]
    G & H & I--->J
    J["<img src='https://latex.codecogs.com/svg.image?\varepsilon(f_{cm})=\left[160&plus;10\beta&space;_{sc}(9-f_{cm}/10)\right]\times&space;10^{-6}'>---------------------------------"]

    L["<img src='https://latex.codecogs.com/svg.image?\beta&space;_{RH}=\left\{\begin{matrix}-1.55[1-(1-RH/100)^{3}](40%\leq&space;RH\leq&space;99%)\\0.25(RH\geq&space;99%)\end{matrix}\right.'>---------------------------------"]
    Variable_def--->L
    M["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sho}=\varepsilon&space;_s(f_{cm})\beta&space;_{RH}'>---------------------------------"]
    L & J--->M
    N["<img src='https://latex.codecogs.com/svg.image?\beta&space;_s(t-t_s)=\sqrt{\frac{(t-t_s)}{0.035h^{2}&plus;(t-t_s)}}'>---------------------------------"]
    Variable_def--->N
    N & M--->O--->K
    O["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sh}(t,t_s)=\varepsilon&space;_{sho}\beta&space;_s(t-t_s)'>---------------------------------"]

    K(["콘크리트의 건조수축 변형률"])
    """

    @rule_method
    def Drying_shrinkage_strain_of_concrete(fIt,fIts,fIbetasc,fIh,fIRH,fIfcm) -> RuleUnitResult:
        """콘크리트의 건조수축 변형률

        Args:
            fIt (float): 콘크리트 총 재령
            fIts (float): 콘크리트가 외기 중에 노출되었을 때의 재령
            fIbetasc (float): 시멘트 종류에 따른 건조수축에 미치는 영향계수
            fIh (float): 부재의 크기
            fIRH (float): 평균상대습도
            fIfcm (float): 콘크리트 평균압축강도

        Returns:
            fOepsshr (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (1)의 값 1
            fOepssho (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (1)의 값 2
            fObetast (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (1)의 값 3
            fOepsfcm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (1)의 값 4
            fObetaRH (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.4 건조수축 (1)의 값 5
        """

        assert isinstance(fIt, float)
        assert isinstance(fIts, float)
        assert isinstance(fIbetasc, float)
        assert isinstance(fIh, float)
        assert isinstance(fIRH, float)
        assert isinstance(fIfcm, float)

        fObetast = ((fIt - fIts) / (0.035 * fIh**2 + fIt - fIts))**0.5

        if 40 <= fIRH < 99:
          fObetaRH = -1.55 * (1 - (fIRH / 100)**3)
        elif fIRH >= 99:
          fObetaRH = 0.25

        fOepsfcm = (160 + 10 * fIbetasc  *(9 - fIfcm / 10)) * 10**(-6)
        fOepssho = fOepsfcm * fObetaRH
        fOepsshr = fOepssho * fObetast

        return RuleUnitResult(
            result_variables = {
                "fOepsshr": fOepsshr,
            }
        )