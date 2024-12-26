import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010202_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '보통콘크리트의 탄성계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.2 탄성변형
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보통콘크리트의 탄성계수];
    B["KDS 24 14 21 3.1.2.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 평균압축강도/];
    VarIn2[/입력변수: 콘크리트의 단위질량/] ;
  	VarOut1[/출력변수: 보통 콘크리트의 탄성계수/];

	  VarOut1~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.2 (1)"])
		C --> Variable_def

		Variable_def---->D-->G

		D["<img src='https://latex.codecogs.com/svg.image?&space;E_{c}=0.077m_{c}^{1.5}\sqrt[3]{f_{cm}}'>--------------------------------------------------------"]

		G(["보통콘크리트의 탄성계수"]);
    """

    @rule_method
    def Modulus_of_elasticity_of_normal_concrete(fIfcm,fImc) -> RuleUnitResult:
        """보통 콘크리트의 탄성계수

        Args:
            fIfcm (float): 콘크리트의 평균압축강도
            fImc (float): 콘크리트의 단위 질량

        Returns:
            fOEc (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.2 탄성변형 (1)의 값
        """

        assert isinstance(fIfcm, float)
        assert isinstance(fImc, float)

        fOEc = 0.077 * (fImc**1.5) * (fIfcm**(1/3))

        return RuleUnitResult(
            result_variables = {
                "fOEc": fOEc,
            }
        )