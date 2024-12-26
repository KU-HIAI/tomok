import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010205_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.5 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '콘크리트의 응력-변형률 곡선'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.5 응력-변형률 관계
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 응력-변형률 곡선];
    B["KDS 24 14 21 3.1.2.5 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 응력/];
		VarIn2[/입력변수: 콘크리트 탄성계수/];
    VarIn3[/입력변수: 콘크리트 압축강도의 평균값/] ;
		VarIn4[/입력변수: 최대 응력에 도달하였을 때의 정점 변형률/] ;
		VarIn5[/입력변수: 극한한계변형률/] ;
	 	VarIn6[/입력변수: 28일 콘크리트 공시체의 기준압축강도/];
    VarOut1[/출력변수: 콘크리트의 응력/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.5 (1)"])
		C --> Variable_def

		Variable_def--->E--->D

		E["<img src='https://latex.codecogs.com/svg.image?k=1.1\frac{E_c\varepsilon&space;_{co,r}}{f_{cm}}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?f_{c}=f_{cm}[\frac{k(\varepsilon&space;_c/\varepsilon_{co,r})-(\varepsilon&space;_c/\varepsilon&space;_{co,r})^{2}}{1&plus;(k-2)(\varepsilon&space;_{c}/\varepsilon&space;_{co,r})}]'>---------------------------------"]
		D--->K
		K(["콘크리트의 응력"])
    """

    @rule_method
    def stress_strain_curve_of_concrete(fIEc,fIfcm,fIepscor,fIepsc,fIfck) -> RuleUnitResult:
        """콘크리트의 응력-변형률 곡선

        Args:
            fIEc (float): 콘크리트 탄성계수
            fIfcm (float): 콘크리트 압축강도의 평균값
            fIepscor (float): 최대 응력에 도달하였을 때의 정점 변형률
            fIepsc (float): 콘크리트의 압축 변형률
            fIfck (float): 28일 콘크리트 공시체의 기준압축강도

        Returns:
            fOfc (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (1)의 값 1
            fOk (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.5 응력-변형률 관계 (1)의 값 2
        """

        assert isinstance(fIEc, float)
        assert isinstance(fIfcm, float)
        assert fIfcm != 0
        assert isinstance(fIepscor, float)
        assert fIepscor != 0
        assert isinstance(fIfck, float)

        fOk = 1.1 * fIEc * fIepscor / fIfcm
        fOfc = fIfcm * (fOk*fIepsc/fIepscor - (fIepsc/fIepscor)**2)/(1 + (fOk-2)*(fIepsc/fIepscor))

        return RuleUnitResult(
            result_variables = {
                "fOfc": fOfc,
            }
        )