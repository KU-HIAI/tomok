import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04030306(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.3.3.6'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '지진격리받침에 작용하는 부반력에 의한 인장응력'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.3 적층고무형 지진격리받침
    4.3.3 설계 요구조건
    4.3.3.6 부반력으로 인한 안정성 검토
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지진격리받침에 작용하는 부반력에 의한 인장응력];
    B["KDS 24 90 11 4.3.3.6"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 전단력/];
		VarIn2[/입력변수: 자가격리받침면적/];
		VarIn3[/입력변수: 허용인장응력/];
		VarOut1[/출력변수: 지진격리받침에 작용하는 부반력에 의한 인장응력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.3.3.6"])
		C --> Variable_def
;
		Variable_def-->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\sigma&space;_{t}=\frac{V}{A}\leq\sigma&space;_{te}'>--------------------------------------------------------"];
		D~~~ |"Table 24 90 11 4.3-3"| D
		E(["인장응력"])
    """

    @rule_method
    def Tensile_Stresses_Due_To_Negative_Reaction_Forces_Acting_On_Seismic_Isolation_Bracing(fIV, fIAe, fIsigmte) -> RuleUnitResult:
        """지진격리받침에 작용하는 부반력에 의한 인장응력

        Args:
            fIV (float): 전단력
            fIAe (float): 자가격리받침면적
            fIsigmte (float): 허용인장응력

        Returns:
            fOsigmat (float): 교량 기타시설설계기준 (한계상태설계법)  4.3.3.6 부반력으로 인한 안정성 검토의 값
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.3.3.6 부반력으로 인한 안정성 검토의 판단 결과
        """

        assert isinstance(fIV, float)
        assert isinstance(fIAe, float)
        assert fIAe > 0
        assert isinstance(fIsigmte, float)

        fOsigmat = fIV / fIAe

        if fIV / fIAe <= fIsigmte:
          return RuleUnitResult(
                result_variables = {
                    "fOsigmat": fOsigmat,
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
                result_variables = {
                    "fOsigmat": fOsigmat,
                    "pass_fail": False,
                }
            )