import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010205_02_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.5 (2) ①'
    ref_date = '2021-04-12'
    doc_date = '2024-07-08'
    title = '콘크리트 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.5 응력-변형률 관계
    (2)
    ①
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 응력];
    B["KDS 24 14 21 3.1.2.5 (2) ①"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 압축 변형률/];
		VarIn2[/입력변수: 설계기준 압축강도/];
	 	VarIn3[/입력변수: 콘크리트의 재료계수/];

    VarOut1[/출력변수: 콘크리트 정점변형률/];
    VarOut2[/출력변수: 콘크리트 강도에 따라 규정된 한계변형률/];
    VarOut3[/출력변수: 콘크리트의 응력/];
    VarOut4[/출력변수: 상승 곡선부의 형상을 나타내는 지수/];

		VarOut3 ~~~ VarIn4 & VarIn5 & VarIn1 & VarIn2 & VarIn6
		VarOut3 ~~~ VarIn4 & VarIn5
		VarOut4 ~~~ VarIn5
		VarOut1 ~~~ VarIn5
		VarOut1 ~~~ VarIn5

		VarIn1 ~~~ VarIn2
		VarIn2 ~~~ VarIn1 ~~~ VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.5 (2) ①"])
		C --> Variable_def

    P{"콘크리트 강도가 50 MPa 미만인 경우"};
    L{"콘크리트 강도가 50 MPa 이상일 경우"};

		Variable_def--->P & L
		P--->Q
		Q["<img src='https://latex.codecogs.com/svg.image?n=2.0,\varepsilon _{c0} = 0.002,\varepsilon _{cu}=0.0033'>---------------------------------"];

		L---> W & X & Y
		W["<img src='https://latex.codecogs.com/svg.image?n = 1.2+1.5(\frac{100-f_{ck}}{60})^{4}\leq 2.0'>---------------------------------"];
		X["<img src='https://latex.codecogs.com/svg.image?\varepsilon _{co} = 0.002+(\frac{f_{ck}-40}{100,000})\geq 0.002'>---------------------------------"];
		Y["<img src='https://latex.codecogs.com/svg.image?\varepsilon _{cu} = 0.0033+(\frac{f_{ck}-40}{100,000})\geq 0.0033'>---------------------------------"];
		Q & W & X & Y ---> GA ---> G & D
		GA["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_c'>---------------------------------"]
		G{"<img src='https://latex.codecogs.com/svg.image?0\leq\varepsilon&space;_c\leq\varepsilon&space;_{co}'>---------------------------------"}
		D{"<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{co}<\varepsilon&space;_c\leq\varepsilon&space;_{cu}'>---------------------------------"}
		G--->K
		K["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})[1-(1-\frac{\varepsilon&space;_c}{\varepsilon&space;_{co}})^{n}]'>---------------------------------"]
		D--->E
		E["<img src='https://latex.codecogs.com/svg.image?f_c=\phi&space;_c(0.85f_{ck})'>---------------------------------"]
		F(["콘크리트 강도"])
		K & E--->F
    """

    @rule_method
    def stress_of_concrete(fIepsc,fIfck,fIphic) -> RuleUnitResult:
        """콘크리트 응력

        Args:
            fIepsc (float): 콘크리트의 압축변형률
            fIfck (float): 설계기준 압축강도
            fIphic (float): 콘크리트의 재료계수

        Returns:
            fOfc (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2) ①의 값 1
            fOn (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2) ①의 값 2
            fOepsco (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2) ①의 값 3
            fOepscu (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (2) ①의 값 4
        """

        assert isinstance(fIepsc, float)
        assert fIepsc >= 0
        assert isinstance(fIfck, float)
        assert isinstance(fIphic, float)

        if fIfck < 50:
          fOn = 2.0
          fOepsco = 0.002
          fOepscu = 0.0033
        else:
          fOn = 1.2 + 1.5 * ((100-fIfck)/60)**4
          fOepsco = 0.002 + (fIfck-40)/100000
          fOepscu = 0.0033 - (fIfck-40)/100000

        if 0 <= fIepsc <= fOepsco:
          fOfc = fIphic * 0.85 * fIfck * (1 - (1 - fIepsc / fOepsco)**fOn)
        else:
          fOfc = fIphic * 0.85 * fIfck

        return RuleUnitResult(
            result_variables = {
                "fOfc": fOfc,
                "fOn": fOn,
                "fOepsco": fOepsco,
                "fOepscu": fOepscu,
            }
        )