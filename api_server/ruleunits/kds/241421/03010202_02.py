import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '경량콘크리트의 탄성계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.2 탄성변형
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경량콘크리트의 탄성계수];
    B["KDS 24 14 21 3.1.2.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 경량콘크리트 탄성계수/];
    VarOut2[/출력변수: 경량콘크리트 계수/];
    VarIn1[/입력변수: 보통 콘크리트의 탄성계수/] ;
		VarIn2[/입력변수: 절대건조 밀도의 상한값/] ;

	  VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.2 (2)"])
		C --> Variable_def

		Variable_def---->D-->E--->G

		D["<img src='https://latex.codecogs.com/svg.image?&space;\eta_{E}=(\gamma_{g}/2200)^2'>--------------------------------------------------------"]

		E["경량콘크리트 탄성계수=<img src='https://latex.codecogs.com/svg.image?&space;\eta_{E}E_{c}'>--------------------------------------------------------"]
    G(["경량콘크리트의 탄성계수"]);
    """

    @rule_method
    def Modulus_of_elasticity_of_light_concrete(fIEc,fIgammag) -> RuleUnitResult:
        """경량콘크리트의 탄성계수

        Args:
            fIEc (float): 보통 콘크리트의 탄성계수
            fIgammag (float): 절대건조 밀도의 상한값

        Returns:
            fOmodelc (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.2 탄성변형 (2)의 값 1
            fOetaE (float): 콘크리트교 설계기준(한계상태설계법) 3.1.2.2 탄성변형 (2)의 값 2
        """

        assert isinstance(fIEc, float)
        assert isinstance(fIgammag, float)

        fOetaE = (fIgammag / 2200)**2
        fOmodelc = fIEc * fOetaE

        return RuleUnitResult(
            result_variables = {
                "fOmodelc": fOmodelc,
            }
        )