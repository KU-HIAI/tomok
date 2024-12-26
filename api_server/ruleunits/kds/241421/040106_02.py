import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040106_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.6 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '설계지압강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.6 지압부 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 설계지압강도];
    B["KDS 24 14 21 4.1.6 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 재료계수/];
		VarIn2[/입력변수: 콘크리트 기준압축강도/];
		VarIn3[/입력변수: 지압력 재하 면적/];
		VarIn4[/입력변수: Ac0와 같은 형상을 가지는 최대설계분포면적/];
		VarOut1[/출력변수: 설계지압강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.6 (2)"])
		C --> Variable_def

		Variable_def-->D--->E

		D["<img src='https://latex.codecogs.com/svg.image?F_d=\phi&space;_c(0.85f_{ck})A_{c0}\sqrt{\frac{A_{c1}}{A_{c0}}}\leq&space;3.0\phi&space;_c(0.85f_{ck})A_{c0}'>---------------------------------"]
		E(["설계지압강도"])
    """

    @rule_method
    def design_bearing_strength(fIphic,fIfck,fIAC0,fIAC1) -> RuleUnitResult:
        """설계지압강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIfck (float): 콘크리트 기준압축강도
            fIAC0 (float): 지압력 재하면적
            fIAC1 (float): AC0와 같은 형상을 가지는 최대설계분포면적

        Returns:
            fOFd (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.6 지압부 설계 (2)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.6 지압부 설계 (2)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIAC0, float)
        assert isinstance(fIAC1, float)

        fOFd = fIphic * (0.85 * fIfck) * fIAC0 * (fIAC1/fIAC0)**0.5

        if fOFd <= 3.0 * fIphic * (0.85  *fIfck) * fIAC0 :
          return RuleUnitResult(
              result_variables = {
                  "fOFd": fOFd,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )