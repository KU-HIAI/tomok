import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04180504_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.5.4 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '교량파괴확률'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.5.4 파괴확률
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 교량파괴확률];
    B["KDS 24 12 21 4.18.5.4 (1)~(3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수:교량파괴확률/];
		VarIn1[/입력변수: 선박의 충격하중/];
		VarIn2[/입력변수: 교각내하력이 상부구조물의 횡방향 내하력으로 표현되는 수평하중에 대한 교량구조물의 강도/];

		VarOut1~~~VarIn1 & VarIn2

		end

		Python_Class ~~~ C(["KDS 24 12 21 4.18.5.4 (1)~(3)"])
		C --> Variable_def

		D{"P/H의 범위"}
		E["<img src='https://latex.codecogs.com/png.image?0.0 \leq H/P < 0.1'>-------------------"];
		F["<img src='https://latex.codecogs.com/png.image?0.1 \leq H/P < 1.0'>-------------------"];
		G["<img src='https://latex.codecogs.com/png.image?1.0 \leq H/P'>-------------------"];
		H["<img src='https://latex.codecogs.com/png.image?PC = 0.1+9\left ( 0.1-\frac{H}{P} \right )'>-------------------"];
		I["<img src='https://latex.codecogs.com/png.image?PC = \frac{1}{9}\left ( 1.0-\frac{H}{P} \right )'>-------------------"];
		J["<img src='https://latex.codecogs.com/png.image?PC = 0.0'>-------------------"];
		Variable_def ---> D ---> E & F & G
		E ---> H
		F ---> I
		G ---> J
		H & I & J ---> K
		K(["교량파괴확률(PC)"])
    """

    @rule_method
    def bridge_failure_probability(fIP,fIH) -> RuleUnitResult:
        """교량파괴확률

        Args:
            fIP (float): 선박의 충격하중
            fIH (float): 교각내하력이 상부구조물의 횡방향 내하력으로 표현되는 수평하중에 대한 교량구조물의 강도

        Returns:
            fOPC (float): 강교 설계기준(한계상태설계법)  4.18.5.4 파괴확률 (1)의 값
        """

        assert isinstance(fIP, float)
        assert isinstance(fIH, float)

        if 0<= fIH / fIP <=0.1:
          fOPC = 0.1 + 9 * (0.1 - fIH / fIP)

          return RuleUnitResult(
              result_variables = {
                  "fOPC": fOPC,
              }
          )