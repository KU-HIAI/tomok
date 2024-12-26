import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070501_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.5.1 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '정모멘트에 요구되는 주철근량의 비'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.1 현장타설 슬래브 상부구조
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 정모멘트에 요구되는 주철근량의 비];
    B["KDS 24 14 21 4.7.5.1 (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:채움 토사의 두께/];
		VarIn2[/입력변수:주철근량의 비/];
		VarIn3[/입력변수:경간길이/];
		VarIn4[/입력변수:손실 발생 후 프리스트레스 강재의 유효 프리스트레스/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.5.1 (3)"])
		C --> Variable_def

		Variable_def--->D
		D{"채움 토사의 두께≥600mm"}
		D--철근콘크리트 슬래브--->E
		D--프리스트레스트 슬래브--->F
		E & F ---> I

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{1750}{\sqrt{L}}\leq&space;50%'>---------------------------------"]

		F["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{1750}{\sqrt{L}}\frac{f_{pe}}{410}\leq&space;50%'>---------------------------------"]
		I(["Pass or Fail"])
    """

    @rule_method
    def Ratio_of_main_reinforcement_required_for_positive_moment(fIthifis, fIramasm, fIL, fIfpe) -> RuleUnitResult:
        """정모멘트에 요구되는 주철근량의 비

        Args:
            fIthifis (float): 채움 토사의 두께
            fIramasm (float): 주철근량의 비
            fIL (float): 경간길이
            fIfpe (float): 손실 발생 후 프리스트레스 강재의 유효 프리스트레스

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.1 현장타설 슬래브 상부구조 (3)의 판단 결과 1
            sOramasm (string): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.1 현장타설 슬래브 상부구조 (3)의 판단 결과 2
        """

        assert isinstance(fIthifis, float)
        assert isinstance(fIramasm, float)
        assert isinstance(fIL, float)
        assert fIL > 0
        assert isinstance(fIfpe, float)

        if fIthifis >= 600:
          if 1750/(fIL**0.5)<=50 or 1750/(fIL**0.5)*fIfpe/410<=50:
            return RuleUnitResult(
                result_variables = {
                    "sOramasm": "암거의 상판과 교량 바닥판 제외",
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "sOramasm": "암거의 상판과 교량 바닥판 제외",
                    "pass_fail": False,
                }
            )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOramasm": "암거의 상판과 교량 바닥판 제외",
                  "pass_fail": False,
              }
          )