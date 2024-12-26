import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060605_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.6.5 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '띠철근의 간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.5 띠철근 상세
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 띠철근의 간격];
    B["KDS 24 14 21 4.6.6.5 (3)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:띠철근의 간격/];
		VarIn2[/입력변수:축방향 철근 최소 지름/];
		VarIn3[/입력변수:압축부재의 최소치수/];
		VarIn4[/입력변수:띠철근의 간격/];
		VarIn5[/입력변수:부재 최소치수/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.6.5 (3)"])
		C --> Variable_def

		Variable_def--->D
		D{D32보다 큰 철근을 다발로 한경우}
		D--yes---> G
		D--NO--->F
		F{"띠철근의 간격≤부재 최소 치수 X1/2, 150mm"}

		G{"띠철근의 간격≤압축부재의 최소치수, 400mm, 방향 철근 최소 지름X20"}
		F & G ---> H(["Pass or Fail"])
    """

    @rule_method
    def Spacing_of_tie(fIsptieA,fIsptieB,fImidiar,fImidicm,fImidime) -> RuleUnitResult:
        """띠철근의 간격

        Args:
            fIsptieA (float): 띠철근의 간격
            fIsptieB (float): 띠철근의 간격 (D32보다 큰 철근을 다발로 한 경우)
            fImidiar (float): 축방향 철근 최소 지름
            fImidicm (float): 압축부재의 최소치수
            fImidime (float): 부재 최소치수

        Returns:
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법)  4.6.6.5 띠철근 상세 (3)의 판단 결과
        """

        assert isinstance(fIsptieA, float)
        assert isinstance(fIsptieB, float)
        assert isinstance(fImidiar, float)
        assert isinstance(fImidicm, float)
        assert isinstance(fImidime, float)

        if fIsptieA != 0 and fIsptieB == 0 :
          if fIsptieA <= fImidiar * 20 and fIsptieA <= fImidicm and fIsptieA <= 400 :
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

        if fIsptieA == 0 and fIsptieB != 0 :
          if fIsptieB <= fImidime/2 and fIsptieB <= 150 :
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