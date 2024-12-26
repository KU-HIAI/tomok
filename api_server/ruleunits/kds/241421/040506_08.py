import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040506_08(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.6 (8)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '표피철근 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.6 지름이 큰 철근에 대한 추가 규정
    (8)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표피철근 단면적];
    B["KDS 24 14 21 4.5.6 (8)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 표피철근 단면적/];
		VarIn2[/입력변수: 지름이 큰 철근에 대한 표피철근 단면적/];

		VarIn1 & VarIn2

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.6 (8)"])
		C --> Variable_def

		Variable_def--->H

		H{"큰 지름 철근의 방향"}
		H--직각 방향--->D
		H--평행한 방향--->E

		D["<img src='https://latex.codecogs.com/svg.image?0.01A_{ct,ext}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?0.02A_{ct,ext}'>---------------------------------"]
		D & E ---> G(["Pass or Fail"])
    """

    @rule_method
    def Skin_rebar_cross_sectional_area(fIsrcsve,fIsrcsho,fIActext) -> RuleUnitResult:
        """표피철근 단면적

        Args:
            fIsrcsve (float): 표피철근 단면적 (큰 지름 철근의 직각 방향)
            fIsrcsho (float): 표피철근 단면적 (큰 지름 철근의 평행 방향)
            fIActext (float): 지름이 큰 철근에 대한 표피철근 단면적

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.5.6 지름이 큰 철근에 대한 추가 규정 (8)의 판단 결과
        """

        assert isinstance(fIsrcsve, float)
        assert isinstance(fIsrcsho, float)
        assert isinstance(fIActext, float)

        if fIsrcsve >= 0.01 * fIActext and fIsrcsho >= 0.02 * fIActext :
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