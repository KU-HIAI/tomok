import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020403_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.4.3 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '콘크리트 유효탄성계수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 유효탄성계수];
    B["KDS 24 14 21 4.2.4.3 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 탄성계수/];
		VarIn2[/입력변수: 하중과 지속 기간에 맞는 크리프계수/];
		VarOut1[/출력변수: 장기거동을 반영한 콘크리트의 유효탄성계수/];
		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.4.3 (3)"])
		C --> Variable_def

		Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?E_{ce}=\frac{E_c}{1&plus;\varphi(\infty,t_o)}'>---------------------------------"]

		F(["콘크리트 유효탄성계수"])
    """

    @rule_method
    def Concrete_effective_modulus_of_elasticity(fIEc,fIvaphit) -> RuleUnitResult:
        """콘크리트 유효탄성계수

        Args:
            fIEc (float): 콘크리트의 탄성계수
            fIvaphit (float): 하중과 지속 기간에 맞는 크리프계수

        Returns:
            fOEce (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (3)의 값
        """

        assert isinstance(fIEc, float)
        assert isinstance(fIvaphit, float)
        assert fIvaphit > 0

        fOEce = fIEc / (1 + fIvaphit)

        return RuleUnitResult(
            result_variables = {
                "fOEce": fOEce,
            }
        )