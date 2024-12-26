import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04050701_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.7.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '가상 철근의 등가지름'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.7 다발철근에 대한 추가 규정
    4.5.7.1 일반사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 가상 철근의 등가지름];
    B["KDS 24 14 21 4.5.7.1 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 다발에서의 철근의 수/];
		VarIn2[/입력변수: 철근의 지름/];
		VarOut1[/출력변수: 등가지름/];

		VarOut1~~~VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.7.1 (3)"])
		C --> Variable_def

		Variable_def--->D---->E

		D["<img src='https://latex.codecogs.com/svg.image?d_{b,n}=d_b\sqrt{n_b}\leq&space;55mm'>---------------------------------"]

		E(["등가지름"])
    """

    @rule_method
    def Virtual_reinforcement_equivalent_diameter(fInbA,fInbB,fIdb) -> RuleUnitResult:
        """가상 철근의 등가지름

        Args:
            fInbA (float): 다발에서의 철근의 수 (압축영역의 수직철근과 겹침이음 연결부의 철근)
            fInbB (float): 다발에서의 철근의 수 (그 외의 경우)
            fIdb (float): 철근의 지름

        Returns:
            fOdbn (float): 깊은기초 설계기준(일반설계법)  4.5.7.1 일반사항 (3)의 값
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.5.7.1 일반사항 (3)의 판단 결과
        """

        assert isinstance(fInbA, float)
        assert isinstance(fInbB, float)
        assert isinstance(fIdb, float)

        if fInbA !=0 and fInbB == 0 :
          fOdbn = fIdb * fInbA**0.5
          if fInbA <= 4 and fIdb <= 55 :
            return RuleUnitResult(
                result_variables = {
                    "fOdbn": fOdbn,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        elif fInbA ==0 and fInbB != 0 :
          fOdbn = fIdb * fInbB**0.5
          if fInbA <= 3 and fIdb <= 55 :
            return RuleUnitResult(
                result_variables = {
                    "fOdbn": fOdbn,
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