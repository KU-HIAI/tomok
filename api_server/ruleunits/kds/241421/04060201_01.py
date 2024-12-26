import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04060201_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.6.2.1 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-05-14'
    title = '주철근 최소 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 주철근 최소 단면적];
    B["KDS 24 14 21 4.6.2.1 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수:설계기준 압축강도/];
		VarIn2[/입력변수:철근의 기준항복강도/];
		VarIn3[/입력변수:단면의 유효깊이/];
		VarIn4[/입력변수:단면의 복부폭/];
		VarIn5[/입력변수:주철근 단면적/];

		VarOut1[/출력변수:주철근 최소 단면적/];

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.6.2.1 (1)"])
		C --> Variable_def

		Variable_def--->D--->E

		D{"<img src='https://latex.codecogs.com/svg.image?A_{s}\geq&space;max\left[\frac{0.25\sqrt{f_{ck}}}{f_{y}}b_{w}d,\frac{1.4}{f_{y}}b_{w}d\right]'>---------------------------------"}

		E(["Pass or Fail"])
    """

    @rule_method
    def minimum_area_of_main_reinforcement(fIfck,fIfy,fIbw,fId,fIAs) -> RuleUnitResult:
        """주철근 최소 단면적

        Args:
            fIfck (float): 설계기준 압축강도
            fIfy (float): 철근의 기준항복강도
            fIbw (float): 단면의 복부폭
            fId (float): 단면의 유효깊이
            fIAs (float): 주철근 단면적

        Returns:
            fOAsmin (float): 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이 (1)의 값
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.6.2.1 극한한계상태에서의 중립축의 깊이 (1)의 판단 결과
        """

        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert isinstance(fIbw, float)
        assert isinstance(fId, float)
        assert isinstance(fIAs, float)

        fOAsmin = max(0.25 * (fIfck**0.5) * fIbw * fId / fIfy, 1.4 * fIbw * fId / fIfy)

        if fIAs >= fOAsmin:
          return RuleUnitResult(
              result_variables = {
                  "fOAsmin": fOAsmin,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOAsmin": fOAsmin,
                  "pass_fail": False,
              }
          )