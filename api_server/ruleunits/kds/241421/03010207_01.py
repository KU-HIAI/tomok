import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_03010207_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.1.2.7 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '증기양생한 콘크리트의 강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.7 증기양생한 콘크리트 재료
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 증기양생한 콘크리트의 강도];
    B["KDS 24 14 21 3.1.2.7 (1)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 강도 보정 계수/];
		VarIn2[/입력변수: 증기양생 후 평균압축강도/];
    VarIn3[/입력변수: 콘크리트 압축강도의 평균값/] ;
    VarIn4[/입력변수: 증기양생을 수행한 시간/] ;
		VarOut1[/출력변수: t일의 콘크리트 압축강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.1.2.7 (1)"])
		C --> Variable_def

		Variable_def--->D--->F

		D["<img src='https://latex.codecogs.com/svg.image?f_{cm}(t)=f_{cmp}&plus;\frac{f_{cm}-f{cmp}}{log(28-t_{p}&plus;1)}log(t-t_{p}&plus;1)'>---------------------------------"]
		F(["t일의 콘크리트 압축강도"])
    """

    @rule_method
    def Concrete_compressive_strength_at_day_t(fIbetacct,fIfcmp,fIfcm,fItp,fIt) -> RuleUnitResult:
        """증기양생한 콘크리트의 강도

        Args:
            fIbetacct (float): 강도 보정 계수
            fIfcmp (float): 증기양생 후 평균압축강도
            fIfcm (float): 콘크리트 압축강도의 평균값
            fItp (float): 증기양생을 수행한 시간
            fIt (float): 온도에 따라 조정한 콘크리트 재령

        Returns:
            fOfcmt (float): 콘크리트교 설계기준(한계상태설계법)  3.1.2.7 증기양생한 콘크리트 재료 (1)의 값
            pass_fail (bool): 콘크리트교 설계기준(한계상태설계법)  3.1.2.7 증기양생한 콘크리트 재료 (1)의 판단 결과
        """

        assert isinstance(fIbetacct, float)
        assert isinstance(fIfcmp, float)
        assert isinstance(fIfcm, float)
        assert isinstance(fItp, float)
        assert fItp < 28
        assert isinstance(fIt, float)
        assert fIt < 28

        import math

        if 0 < fIt - fItp < 28 and fIbetacct <=1.0 :
          fOfcmt = min(fIfcm * fIbetacct, fIfcmp + (fIfcm - fIfcmp) / (math.log10(28 - fItp + 1)) * math.log10(fIt - fItp + 1))
          return RuleUnitResult(
              result_variables = {
                  "fOfcmt": fOfcmt,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )