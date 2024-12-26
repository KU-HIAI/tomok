import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010204_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.4 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-05-14'
    title = '횡방향 철근'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 철근];
    B["KDS 24 14 21 4.1.2.4 (5)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 종방향 전단응력/];
		VarIn2[/입력변수: 콘크리트의 재료계수/];
		VarIn3[/입력변수: 콘크리트 하위 0.05 분위 기준인장강도/];
		VarIn1 & VarIn2 & VarIn3

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.4 (5)"])
		C --> Variable_def

		Variable_def--->D--->E
		D{"<img src='https://latex.codecogs.com/svg.image?&space;v_{uf}\leq&space;0.4\phi&space;_{c}f_{ctk}'>---------------------------------"}
		E(["휨철근량 이상의 추가적인 횡방향 철근은 배치할 필요 없음"])
    """

    @rule_method
    def transverse_reinforcement(fIvuf,fIphic,fIfctk) -> RuleUnitResult:
        """횡방향 철근

        Args:
            fIvuf (float): 종방향 전단응력
            fIphic (float): 콘크리트의 재료계수
            fIfctk (float): 콘크리트 하위 0.05 분위 기준인장강도

        Returns:
            sOvuf (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (5)의 판단 결과 1
            sOnone (string): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (5)의 판단 결과 2
        """

        assert isinstance(fIvuf, float)
        assert isinstance(fIphic, float)
        assert isinstance(fIfctk, float)

        if fIvuf <= 0.4 * fIphic * fIfctk :
          return RuleUnitResult(
              result_variables = {
                  "sOvuf": "휨철근량 이상의 추가적인 횡방향 철근은 배치할 필요 없음",
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )