import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04010301_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.1.3.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '신축이음 노면 최대 틈새 간격'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.3 설계
    4.1.3.1 설계 이동량 계산 및 허용 틈새 간격
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 신축이음 노면 최대 틈새 간격];
    B["KDS 24 90 11 4.1.3.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 노면 틈새 간격/];

		end
		Python_Class ~~~ C(["KDS 24 90 11 4.1.3.1 (2)"])
		C --> Variable_def--->E
		Variable_def--->H
		E---->F
		H---->G

		E{"신축이음 노면 최대 틈새 간격 (틈새가 하나인 경우)"}
		F{"100mm≤신축이음 노면 최대 틈새 간격"}
		H{"신축이음 노면 최대 틈새 간격 (틈새가 여러 개인 모듈 형식인 경우"}
		G{"신축이음 노면 최대 틈새 간격≤80mm"}
    I(["Pass or Fail"])
    F & G ---->I
    """

    @rule_method
    def Maximum_Pavement_Gap_Spacing_For_Expansion_Joint (fIW, fIlacscA, fIlacscB) -> RuleUnitResult:
        """신축이음 노면 최대 틈새 간격
        Args:
            fIW (float): 신축이음 노면 최대 틈새 간격
            fIlacscA (float): 신축이음 노면 최대 틈새 간격 (틈새가 하나인 경우)
            fIlacscB (float): 신축이음 노면 최대 틈새 간격 (틈새가 여러 개인 모듈 형식인 경우)

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.1.3.1 설계 이동량 계산 및 허용 틈새 간격의 판단 결과
        """

        assert isinstance(fIW, float)
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)


        if fIlacscA == 0 and fIlacscB != 0 :
          if fIW <= 100 :
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

        elif fIlacscA != 0 and fIlacscB == 0 :
          if fIW <= 80 :
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