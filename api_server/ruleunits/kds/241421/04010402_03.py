import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010402_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '계수하중에 의한 최대 전단응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.2 뚫림전단 설계
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계수하중에 의한 최대 전단응력];
    B["KDS 24 14 21 4.1.4.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 슬래브의 평균 유효깊이/];
    VarOut2[/출력변수: 계수하중에 의한 최대 전단응력/];
		VarIn1[/입력변수: 위험단면에서 y-방향 유효깊이/];
		VarIn2[/입력변수: 위험단면에서 z-방향 유효깊이/];
		VarIn3[/입력변수: 검토하는 위험단면의 둘레길이/];
    VarIn4[/입력변수: 전단력/];

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.2 (3)"])
		C --> Variable_def

		Variable_def--->F--->D--->E
		F["<img src='https://latex.codecogs.com/svg.image?d=(d_y&plus;d_z)/2'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?v&space;_u=\frac{V_u}{u_id}'>---------------------------------"]
		E(["계수하중에 의한 최대 전단응력"])
    """

    @rule_method
    def maximum_shear_stress_by_factored_load(fIVu,fIdy,fIdz,fIui) -> RuleUnitResult:
        """계수하중에 의한 최대 전단응력

        Args:
            fIVu (float): 전단력
            fIdy (float): 위험단면에서 y-방향 유효깊이
            fIdz (float): 위험단면에서 z-방향 유효깊이
            fIui (float): 검토하는 위험단면의 둘레길이

        Returns:
            fOvu (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.2 뚫림전단 설계 (3)의 값 1
            fOd (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.2 뚫림전단 설계 (3)의 값 2
        """

        assert isinstance(fIVu, float)
        assert isinstance(fIdy, float)
        assert isinstance(fIdz, float)
        assert isinstance(fIui, float)

        fOd = (fIdy + fIdz) / 2
        fOvu = fIVu / (fIui * fOd)

        return RuleUnitResult(
            result_variables = {
                "fOvu": fOvu,
            }
        )