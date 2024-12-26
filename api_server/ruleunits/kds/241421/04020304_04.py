import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020304_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.4 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '최대균열간격'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 최대균열간격];
    B["KDS 24 14 21 4.2.3.4 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 종방향 철근과 압축 주응력 방향 사잇각/];
		VarIn2[/입력변수: 종방향에서 계산한 균열 간격/];
		VarIn3[/입력변수: 횡방향에서 계산한 균열 간격/];

		VarOut1[/출력변수: 최대균열간격/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.4 (4)"])
		C --> Variable_def

		Variable_def--->E--->D
		E{"주응력 축과 철근 방향 사이의 각이 15°보다 클 때"}
		D["<img src='https://latex.codecogs.com/svg.image?l_{r,max}=\frac{1}{(cos\theta/l_{rl,max})&plus;(sin\theta/l_{rt,max})}'>---------------------------------"]


		D--->G
		G(["최대균열간격"])
    """

    @rule_method
    def maximum_crack_spacing(fItheta,fIlrlmax,fIlrtmax) -> RuleUnitResult:
        """최대균열간격

        Args:
            fItheta (float): 종방향 철근과 압축 주응력 방향 사잇각
            fIlrlmax (float): 종방향에서 계산한 균열 간격
            fIlrtmax (float): 횡방향에서 계산한 균열 간격

        Returns:
            fOlrmax (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (4)의 값
            sOnone (string): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (4)의 판단 결과
        """

        assert isinstance(fItheta, float)
        assert isinstance(fIlrlmax, float)
        assert fIlrlmax != 0
        assert isinstance(fIlrtmax, float)
        assert fIlrtmax != 0

        import math

        if fItheta > 15:
          fOlrmax = 1 / ((math.cos(fItheta * math.pi / 180) / fIlrlmax) + (math.sin(fItheta * math.pi / 180) / fIlrtmax))

          return RuleUnitResult(
              result_variables = {
                  "fOlrmax": fOlrmax,
              }
          )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )