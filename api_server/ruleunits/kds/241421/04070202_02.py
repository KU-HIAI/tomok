import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.2.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '콘크리트 거더의 구성 요소 두께'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.2 거더 교량
    4.7.2.2 프리캐스트 거더 교량
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 거더의 구성 요소 두께];
    B["KDS 24 14 21 4.7.2.2 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:콘크리트 거더의 구성 요소 두께/];
		VarIn2[/입력변수:상부 플랜지/];
		VarIn3[/입력변수:복부, 포스트텐션 아닌 경우/];
		VarIn4[/입력변수:복부, 포스트텐션/];
		VarIn5[/입력변수:하부 플랜지/];

		VarOut1[/출력변수:단순 받침부의 공칭길이/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~~VarIn4 & VarIn5

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.2.2 (2)"])
		C --> Variable_def

		Variable_def--->D---> E & F & G & H---> I

		D{"콘크리트 거더의 구성 요소 두께"}
		E{"상부플렌지≥50mm"}
		F{"복부,포스트텐션 아닌경우≥125mm"}
		G{"복부,포스트텐션인 경우≥165mm"}
		H{"하부플랜지≥125mm"}
		I(["Pass or Fail"])
    """

    @rule_method
    def Component_thickness_of_concrete_girder(fIupflth, fIabdnpos, fIabdpos, fIloflth) -> RuleUnitResult:
        """콘크리트 거더의 구성 요소 두께

        Args:
            fIupflth (float): 상부 플랜지 두께
            fIabdnpos (float): 복부, 포스트텐션 아닌 경우
            fIabdpos (float): 복부, 포스트텐션
            fIloflth (float): 하부 플랜지 두께

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.2.2 프리캐스트 거더 교량 (2)의 판단 결과
        """

        assert isinstance(fIupflth, float)
        assert isinstance(fIabdnpos, float)
        assert isinstance(fIabdpos, float)
        assert isinstance(fIloflth, float)

        if fIabdnpos != 0 and fIabdpos == 0 :
          if fIupflth >= 50 and fIabdnpos >= 125 and fIloflth >= 125 :
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

        elif fIabdnpos == 0 and fIabdpos != 0 :
          if fIupflth >= 50 and fIabdpos >= 165 and fIloflth >= 125 :
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