import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060302_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.3.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '전단철근의 종방향 최대간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.3 슬래브
    4.6.3.2 전단철근
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근의 종방향 최대간격];
    B["KDS 24 14 21 4.6.3.2 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:단면의 유효깊이/];
		VarIn2[/입력변수:경사전단철근과 주인장철근 사이의 경사각/];
		VarOut1[/출력변수:종방향 최대 간격/];
		VarOut2[/출력변수:굽힘철근의 종방향 최대간격/];
		VarOut1 & VarOut2~~~~VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.3.2 (3)"])
		C --> Variable_def

		Variable_def--->F & E
		F["<img src='https://latex.codecogs.com/svg.image?s_{max}=0.75d(1&plus;cot\alpha)'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?s_{max}=d'>---------------------------------"]
		G(["종방향 최대간격"])
		H(["굽힘철근의 종방향 최대간격"])
		F--->G
		E--->H
    """

    @rule_method
    def Longitudinal_maximum_spacing(fId,fIalpha) -> RuleUnitResult:
        """전단철근의 종방향 최대간격

        Args:
            fId (float): 단면의 유효깊이
            fIalpha (float): 경사전단철근과 주인장철근 사이의 경사각


        Returns:
            fOsbSmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.3.2 전단철근 (3)의 값 1
            fObbSmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.6.3.2 전단철근 (3)의 값 2
        """

        assert isinstance(fId, float)
        assert isinstance(fIalpha, float)

        import math

        fOsbSmax = 0.75 * fId * (1 + 1 / math.tan(fIalpha / 180 * math.pi))
        fObbSmax = fId

        return RuleUnitResult(
            result_variables = {
                "fOsbSmax": fOsbSmax,
                "fObbSmax": fObbSmax,
            }
        )