import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020409_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.4.9 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '피스톤과 포트 접촉부 검토'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.9 피스톤과 포트 접촉부 검토
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 피스톤과 포트 접촉부 검토];
    B["KDS 24 90 11 4.2.4.9 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 피스톤의 폭/];
		VarIn2[/입력변수: 접촉면의 반경/];
		VarIn3[/입력변수: 직경/];


    VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.4.9 (1)"])
		C --> Variable_def;
		Variable_def--->K--평면--->L--->N
		K--곡면--->M--->N
		K{"접촉면의 상태"}
		L{"W<15mm"};
		M{"접촉면의 반경 <img src='https://latex.codecogs.com/svg.image?\leq Max(0.5D, 100mm)'>---------------"};
    N(["Pass or Fail"])
    """

    @rule_method
    def Width_Of_Piston(fIw, fID, fIr, fIlacscA, fIlacscB) -> RuleUnitResult:
        """피스톤과 포트 접촉부 검토

        Args:
            fIw (float): 피스톤의 폭
            fID (float): 직경
            fIr (float): 접촉면의 반경
            fIlacscA (float): 피스톤의 폭 (접촉면이 평면인 경우)
            fIlacscB (float): 피스톤의 폭 (접촉면이 곡면인 경우)

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (1)의 판단 결과
        """

        assert isinstance(fIw, float)
        assert isinstance(fID, float)
        assert isinstance(fIr, float)
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)

        if fIlacscA == 0 and fIlacscB != 0 :
          if fIw < 15:
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
          if fIr >= max(0.5 * fID, 100):
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