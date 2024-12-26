import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040103_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.1.3 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '계수하중에 의한 스트럿과 타이의 단면력 검토'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.1 스트럿-타이 모델 설계 절차
    4.1.3 설계 원칙
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스트럿, 타이 그리고 절점영역의 설계];
    B["KDS 14 20 24 4.1.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수 : 계수하중에 의한 스트럿과 타이의 단면력/];
		VarIn2[/입력변수 : 절점영역의 한 면에 작용하는 단면력/];
		VarIn3[/입력변수 : 스트럿, 타이 그리고 절점영역의 공칭축강도/];
		VarIn1 ~~~ VarIn3
		VarIn2
    end

		Python_Class ~~~ C(["KDS 14 20 24 4.1.3 (1)"])
		C --> Variable_def

		D{"강도감소계수"};
		E["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{c} = 0.75'>"];
		F["<img src='https://latex.codecogs.com/svg.image?\phi&space;_{t} = 0.85'>"];
		Variable_def --->D
		D--스트럿--->E
		D--타이--->F

		G{"<img src='https://latex.codecogs.com/svg.image?\phi&space;F_{n}\geq&space;F_{u}'>"};
		E--->G
		F--->G
		G--->H([Pass or Fail])
    """

    @rule_method
    def examine_the_sectional_forces_in_struts_and_ties_under_counting_loads(fIFus, fIFut, fIFn) -> RuleUnitResult:
        """계수하중에 의한 스트럿과 타이의 단면력 검토

        Args:
            fIFus (float): 계수하중에 의한 스트럿과  타이의 단면력
            fIFut (float): 절점영역의 한 면에 작용하는단면력
            fIFn (float): 공칭축강도

        Returns:
            pass_fail (bool): 콘크리트구조 스트럿-타이모델 기준  4.1.3 설계원칙 (1)의 판단 결과
        """

        assert isinstance(fIFus, float)
        assert isinstance(fIFut, float)
        assert isinstance(fIFn, float)

        if 0.75 * fIFn >= fIFus and 0.85 * fIFn >= fIFut :
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