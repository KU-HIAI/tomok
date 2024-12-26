import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_01050202_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 1.5.2.2 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '받침점의 계수 휨 모멘트 감소량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침점의 계수 휨 모멘트 감소량];
    B["KDS 24 14 21 1.5.2.2 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
    VarOut1[/출력변수: 계수 휨모멘트 변화량/] ;
    VarIn1[/입력변수: 받침점의 계수 반력/];
		VarIn2[/입력변수: 받침점 폭/];
    VarOut1 ~~~ VarIn1 & VarIn2
		end

	  Python_Class ~~~ C(["KDS 24 14 21 1.5.2.2 (5)"])
		C --> Variable_def

		Variable_def-->E
		E["<img src='https://latex.codecogs.com/svg.image?\Delta&space;M_{U}=f_{u,sup}t/8'>--------------------------------------------------------"];
		D(["계수 휨모멘트"]);

    E--->D
    """

    @rule_method
    def modulus_bending_moment_reduction(fIfusup,fIt) -> RuleUnitResult:
        """받침점의 계수 휨 모멘트 감소량

        Args:
            fIfusup (float) : 받침점의 계수 반력
            fIt (float) : 받침점 폭

        Returns:
            fOdelMu (float): 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (5)의 값
        """

        assert isinstance(fIfusup, float)
        assert isinstance(fIt, float)

        fOdelMu = fIfusup * fIt / 8

        return RuleUnitResult(
            result_variables = {
                "fOdelMu": fOdelMu,
            }
        )