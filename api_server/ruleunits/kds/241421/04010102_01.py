import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010102_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.2 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '콘크리트 압축 연단의 변형률 및 강재의 극한한계변형'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 압축 연단의 변형률 및 강재의 극한한계변형];
    B["KDS 24 14 21 4.1.1.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 압축 연단의 변형률/];
		VarIn2[/입력변수: 한계변형률/];
    VarIn3[/입력변수: 강재의 극한한계변형률/] ;
    VarIn4[/입력변수: 설계한계변형률/];
		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.2 (1)"])
		C --> Variable_def

		Variable_def--->D
		Variable_def--->F

		D{"콘크리트 압축 연단의 변형률≤한계변형률"}
		F{"강재의 극한한계변형률≤설계한계변형률"}
		D~~~ |"KDS 24 14 21 3.1.2.5"| D
		F~~~ |"KDS 24 14 21 3.2"| F
		D & F--->E
		E(["Pass or Fail"])
    """

    @rule_method
    def Strain_of_concrete_compression_brittle_and_Ultimate_limit_strain_of_steel(fIstrcon,fIepscu,fIultsts,fIepsud) -> RuleUnitResult:
        """콘크리트 압축 연단의 변형률 및 강재의 극한한계변형

        Args:
            fIstrcon (float): 콘크리트 압축 연단의 변형률
            fIepscu (float): 한계변형률
            fIultsts (float): 강재의 극한한계변형률
            fIepsud (float): 설계한계변형률

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (1)의 판단 결과
        """

        assert isinstance(fIstrcon, float)
        assert isinstance(fIepscu, float)
        assert isinstance(fIultsts, float)
        assert isinstance(fIepsud, float)

        if fIstrcon <= fIepscu and fIultsts <= fIepsud:
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