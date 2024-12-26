import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010201_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '전단보강철근이 배치된 부재의 설계전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.1 일반
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단보강철근이 배치된 부재의 설계전단강도];
    B["KDS 24 14 21 4.1.2.1 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 전단보강철근이 배치된 부재의 설계전단강도/];
		VarIn1[/입력변수: 설계전단강도/];
		VarIn2[/입력변수: 최대설계전단강도/];

		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.1 (3)"])
		C --> Variable_def

		Variable_def--->E--->D

		E["<img src='https://latex.codecogs.com/svg.image?V_{d}=V_{sd}\leq&space;V_{d,max}'>---------------------------------"]
		D(["전단보강철근이 배치된 부재의 설계전단강도"])
    """

    @rule_method
    def Design_shear_strength_of_members_with_shear_rebar(fIVsd,fIVdmax,fIVdmaxc) -> RuleUnitResult:
        """전단보강철근이 없는 부재의 설계전단강도

        Args:
            fIVsd (float): 설계전단강도
            fIVdmax (float): 최대설계전단강도
            fIVdmaxc (float): 축방향 압축력이 작용하는 경우의 최대설계전단강도

        Returns:
            fOVd (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (3)의 값 1
            fOVdmax (float): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (3)의 값 2
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.1 일반 (3)의 판단 결과
        """

        assert isinstance(fIVsd, float)
        assert isinstance(fIVdmax, float)
        assert isinstance(fIVdmaxc, float)

        fOVd = fIVsd

        if fIVdmaxc == 0 :
          fOVdmax = fIVdmax
        else:
          fOVdmax = fIVdmaxc

        if fOVd <= fOVdmax:
          return RuleUnitResult(
              result_variables = {
                  "fOVd": fOVd,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOVd": fOVd,
                  "pass_fail": False,
              }
          )