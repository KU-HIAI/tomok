import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060202_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.2 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '전단강도에 기여하는 굽힘철근의 정착길이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.2 종방향 인장 철근의 길이 방향 배치
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단강도에 기여하는 굽힘철근의 정착길이];
    B["KDS 24 14 21 4.6.2.2 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 굽힘철근의 정착길이: 인장 영역/];
		VarIn2[/입력변수: 굽힘철근의 정착길이: 압축 영역/];
		VarIn3[/입력변수: 설계정착길이/];
		VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.2 (4)"])
		C --> Variable_def

		Variable_def--->F

		F{"굽힘철근의 정착길이"}
		F--인장영역--->G
		G{"인장영역≥1.3lbd"}
		F--압축영역--->H
		H{"압축영역≥0.7lbd"}
    G & H ---> I
		I(["Pass or fail"])
    """

    @rule_method
    def Settlement_length_of_bending_rebar(fIselerA,fIselerB,fIlbd) -> RuleUnitResult:
        """전단강도에 기여하는 굽힘철근의 정착길이

        Args:
            fIselerA (float): 굽힘철근의 정착길이 (인장 영역)
            fIselerB (float): 굽힘철근의 정착길이 (압축 영역)
            fIlbd (float): 설계정착길이

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.6.2.2 종방향 인장 철근의 길이 방향 배치 (4)의 판단 결과
        """

        assert isinstance(fIselerA, float)
        assert isinstance(fIselerB, float)
        assert isinstance(fIlbd, float)

        if fIselerA != 0 and fIselerB == 0 :
          if fIselerA >= 1.3 * fIlbd:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        elif fIselerA == 0 and fIselerB != 0 :
          if fIselerB >= 0.7 * fIlbd:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )