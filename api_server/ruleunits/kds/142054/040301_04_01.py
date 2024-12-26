import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142050_040301_04_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.1 (1) ④ 가'
    ref_date = '2021-02-18'
    doc_date = '2024-05-22'
    title = '프리스트레스하지 않는 부재의 현장치기콘크리트의 최소 피복 두께'

    description = """
    콘크리트구조 철근상세 설계기준
    4. 설계
    4.3 최소 피복 두께
    4.3.1 프리스트레스하지 않는 부재의 현장치기콘크리트
    (1)
    ④
    가
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력과 전단력의 동시 작용];
    B["KDS 14 20 54 4.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 앵커의 강도/];
    VarIn2[/입력변수 : 최대 소요강도/];
    end
    Python_Class~~~ C(["KDS 14 20 54 4.1 (2)"])--> Variable_def
    D["앵커의 강도 &ge; KDS 14 20 10(3.2)의 적용 가능한 하중조합에 의해 결정되는 최대소요강도"];
    E(["Pass or Fail"]);
    Variable_def--->D--->E
    """

    @rule_method
    def Minimum_covering_thickness_of_non_prestrictive_concrete_for_non_prestrictive_members(fIlacscA,fIlacscB,fIexsmct,fIbesmct) -> RuleUnitResult:
        """프리스트레스하지 않는 부재의 현장치기콘크리트의 최소 피복 두께

        Args:
            fIlacscA (float): D35 초과하는 철근인 경우
            fIlacscB (float): D35 이하인 철근인 경우
            fIexsmct (float):  D35 초과하는 철근인 경우 피복 두께
            fIbesmct (float):  D35 이하인 철근인 경우 피복 두께

        Returns:
            pass_fail (bool): 콘크리트구조 철근상세 설계기준 4.3.1 프리스트레스하지 않는 부재의 현장치기콘크리트 (1) ④ 가의 판단 결과
        """

        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)
        assert isinstance(fIexsmct, float)
        assert isinstance(fIbesmct, float)

        if fIlacscA != 0 and fIlacscB == 0 :
          if fIexsmct >= 40 :
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
        if fIlacscA == 0 and fIlacscB != 0 :
          if fIbesmct >= 20 :
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