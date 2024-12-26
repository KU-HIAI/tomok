import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050202_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.2.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '받침점 면의 모멘트'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침점 면의 모멘트];
    B["KDS 24 14 21 1.5.2.2 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def
	  VarIn1[/입력변수: 설계 모멘트/];
    VarIn2[/입력변수: 고정단모멘트/] ;

    end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.2.2 (3)"])
		C --> Variable_def

		Variable_def-->E
		E{"설계 모멘트≥고정단모멘트X0.65"};
		E--->D
		D(["Pass or Fail"]);
    """

    @rule_method
    def Moment_of_the_support_plane(fIdesmom,fIfixmom) -> RuleUnitResult:
        """받침점 면의 모멘트

        Args:
            fIdesmom (float) : 설계모멘트
            fIfixmom (float) : 고정단모멘트

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (3)의 판단 결과
        """

        assert isinstance(fIdesmom, float)
        assert isinstance(fIfixmom, float)

        if fIdesmom >= 0.65 * fIfixmom :
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