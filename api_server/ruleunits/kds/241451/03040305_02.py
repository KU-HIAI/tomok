import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03040305_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.4.3.5 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '주면마찰력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.5 암반에 설치한 현장타설말뚝의 지지력 산정
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 암반에 설치한 현장타설말뚝의 지지력 산정];
    B["KDS 24 14 51 3.4.3.5 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:주면마찰력/]
		VarIn1[/입력변수:암의 일축압축강도/]
		VarIn2[/입력변수:대기압/]
		VarIn3[/입력변수:암반절리를 고려한 감소계수/]
		VarIn4[/입력변수:콘크리트 압축강도/]
		VarOut1
		VarIn1 ~~~ VarIn2
		VarIn3 ~~~ VarIn4

    end
		Python_Class ~~~ C(["KDS 24 14 51 3.4.3.5 (2)"])
		C --> Variable_def

		E{"<img src='https://latex.codecogs.com/svg.image?0.65\alpha&space;_{E}p_{a}(\frac{q_{u}}{p_{a}})^{0.5}<7.8p_{a}(\frac{f_{c}^{\prime}}{P_{a}})^{0.5}'>---------------------------------"}
		D([주면 마찰력])

		Variable_def ---> E ---> D
    """

    @rule_method
    def skin_friction(fIqu,fIPa,fIredjoi,fIfc) -> RuleUnitResult:
        """주면마찰력

        Args:
            fIqu (float): 암의 일축압축강도
            fIPa (float): 대기압
            fIredjoi (float): 암반절리를 고려한 감소계수
            fIfc (float): 콘크리트 압축강도

        Returns:
            fOqs (float): 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.5 암반에 설치한 현장타설말뚝의 지지력 산정 (2)의 값
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.5 암반에 설치한 현장타설말뚝의 지지력 산정 (2)의 판단 결과
        """

        assert isinstance(fIqu, float)
        assert fIqu > 0
        assert isinstance(fIPa, float)
        assert fIPa > 0
        assert isinstance(fIredjoi, float)
        assert isinstance(fIfc, float)
        assert fIfc > 0

        if 0.65 * fIredjoi * fIPa * (fIqu / fIPa) ** 0.5 < 7.8 * fIPa * (fIfc / fIPa) ** 0.5:
          fOqs = 0.65 * fIredjoi * fIPa * (fIqu / fIPa) ** 0.5
          return RuleUnitResult(
              result_variables = {
                  "fOqs": fOqs,
                  "pass_fail": True,
                  }
              )
        else :
          return RuleUnitResult(
              result_variables = {
                  "fOqs": fOqs,
                  "pass_fail": False,
                  }
              )