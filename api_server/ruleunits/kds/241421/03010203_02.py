import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010203_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '크리프 계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.3 크리프
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 크리프 계수];
    B["KDS 24 14 21 3.1.2.3 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 개념 크리프계수/];
		VarIn2[/입력변수: 외기의 상대습도와 부재 두께가 크리프에 미치는 영향계수/];
    VarIn3[/입력변수: 콘크리트의 평균압축강도가 크리프에 미치는 영향함수/] ;
		VarIn4[/입력변수: 지속하중이 가해지는 시간 t'가 크리프에 미치는 영향함수/] ;
		VarIn5[/입력변수: 재하기간에 따라 크리프에 미치는 영향함수/] ;
		VarIn6[/입력변수: 외기의 상대습도와 부재의 두께에 따른 계수/] ;
		VarIn7[/입력변수: 개념부재치수/] ;
		VarIn8[/입력변수: 단면적 Ac의 둘레중에서 수분이 외기로 확산되는 둘레길이/] ;
		VarIn9[/입력변수: 평균압축강도/] ;
		VarIn10[/입력변수: 상대습도/] ;
	 	VarOut1[/출력변수: 크리프계수/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.3 (2)"])
		C --> Variable_def

		Variable_def--->J
		J["<img src='https://latex.codecogs.com/svg.image?\varphi_{RH}=1+\frac{1-0.01RH}{0.1\sqrt[3]{h}}'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\beta(f_{cm})=\frac{16.8}{\sqrt{f_{cm}}}'>---------------------------------"]
		Variable_def--->D
		Variable_def--->E
		E["<img src='https://latex.codecogs.com/svg.image?\beta(t^{\prime})=\frac{1}{0.1+\left(t^\prime\right)^{0.2}}'>---------------------------------"]
		J & D & E--->
		F["<img src='https://latex.codecogs.com/svg.image?\varphi_{RH}=\beta(f_{cm})\beta(t^{\prime})'>---------------------------------"]
		Variable_def--->G
		Variable_def--->H
		G["<img src='https://latex.codecogs.com/svg.image?\beta_{c}(t-t^{\prime})=[\frac{(t-t^{\prime})}{\beta_{H}+(t-t^{\prime})}]^{0.3}'>---------------------------------"]
    H["<img src='https://latex.codecogs.com/svg.image?\beta_{H}=1.5[1+(0.012RH)^{18}]h+250\leq1500'>---------------------------------"]
    I["<img src='https://latex.codecogs.com/svg.image?\varphi(t,t^{\prime})=\varphi_{0}\beta_{c}(t-t^{\prime})'>---------------------------------"]
    F & G & H--->I-->X(["크리프계수"])
    """

    @rule_method
    def creep_coefficient(fItprime,fIt,fIh,fIu,fIfcm,fIRH) -> RuleUnitResult:
        """크리프 계수

        Args:
            fItprime (float): 재하할 때의 재령
            fIt (float): 재하할 때의 재령 + 재하기간
            fIh (float): 개념부재치수
            fIu (float): 단면적 A_{c}의 둘레 중에서 수분이 외기로 확산되는 둘레길이
            fIfcm (float): 평균압축강도
            fIRH (float): 상대습도

        Returns:
            fOphittp (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 1
            fOphio (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 2
            fOphiRH (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 3
            fObetfcm (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 4
            fObetatp (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 5
            fObetaH (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 6
            fObetact (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 값 7
            pass_fail (bool): 콘크리트교 설계기준(한계상태설계법) 3.1.2.3 크리프 (2)의 판단 결과
        """

        assert isinstance(fItprime, float)
        assert isinstance(fIt, float)
        assert isinstance(fIh, float)
        assert isinstance(fIu, float)
        assert isinstance(fIfcm, float)
        assert isinstance(fIRH, float)

        fOphiRH = 1 + (1 - 0.01 * fIRH) / (0.10 * fIh**(1/3))
        fObetfcm = 16.8 / fIfcm**0.5
        fObetatp = 1 / (0.1 + fItprime**0.2)
        fOphio = fOphiRH * fObetfcm * fObetatp
        fObetaH = 1.5 * (1 + (0.012 * fIRH)**18) * fIh + 250
        fObetact = ((fIt-fItprime)/(fObetaH + fIt-fItprime))**0.3

        if fObetaH <= 1500:
          fOphittp = fOphio * fObetact
          return RuleUnitResult(
              result_variables = {
                  "fOphittp": fOphittp,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )