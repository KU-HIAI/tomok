import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_040506_06(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.5.6 (6)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '보강철근의 단면적'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.6 지름이 큰 철근에 대한 추가 규정
    (6)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보강철근의 단면적];
    B["KDS 24 14 21 4.5.6 (6)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 공칭지름/];
		VarIn2[/입력변수: 콘크리트 설계압축강도/];
		VarIn3[/입력변수: 최대 지름/];
		VarIn4[/입력변수: 철근 단면적/];
		VarIn5[/입력변수: 용접의 설계전단강도/];

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.5.6 (6)"])
		C --> Variable_def

		Variable_def--->H & D

		H["<img src='https://latex.codecogs.com/svg.image?A_{sh}=0.25A_sn_1'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?A_{sv}=0.25A_sn_2'>---------------------------------"]

		E(["인장면에 평행한 정착철근의 단면적"])

		F(["인장면에 수직인 정착철근의 단면적"])
		H--->E
		D--->F
		E & F ---> G(["Pass or Fail"])
    """

    @rule_method
    def Cross_sectional_area_of_rebar(fIAsh,fIAsv,fIAs,fIn1,fIn2) -> RuleUnitResult:
        """보강철근의 단면적

        Args:
            fIAsh (float): 공칭지름
            fIAsv (float): 콘크리트 설계압축강도
            fIAs (float): 최대 지름
            fIn1 (float): 철근 단면적
            fIn2 (float): 용접의 설계전단강도

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.5.6 지름이 큰 철근에 대한 추가 규정 (6)의 판단 결과
        """

        assert isinstance(fIAsh, float)
        assert isinstance(fIAsv, float)
        assert isinstance(fIAs, float)
        assert isinstance(fIn1, float)
        assert isinstance(fIn2, float)

        if fIAsh >= 0.25*fIAs*fIn1 and fIAsv >= 0.25*fIAs*fIn2:
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