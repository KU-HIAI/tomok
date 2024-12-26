import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_041103_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.11.3 (1)'
    ref_date = '2022-01-11'
    doc_date = '2024-11-13'
    title = '전단철근 배근 조건'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.11 슬래브와 기초판에 대한 전단 설계
    4.11.3 전단철근
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근 배근 조건];
    B["KDS 14 20 22 4.11.3 (1)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리/];
    VarIn2[/입력변수: 전단철근의 지름/];

    end

    Python_Class ~~~ C(["KDS 14 20 22 4.11.3 (1)"])
		C --> Variable_def

    D{"d ≥ 150 and d ≥ 전단철근의 지름 x 16"};
    E(["Pass or Fail"]);

		Variable_def --> D --> E
    """

    @rule_method
    def Shear_reinforcement_conditions(fId,fIdishre) -> RuleUnitResult:
        """전단철근 배근 조건

        Args:
            fId (float): 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리
            fIdishre (float): 전단철근의 지름

        Returns:
            pass_fail (bool): 콘크리트구조 전단 및 비틀림 설계기준  4.11.3 전단철근 (1)의 판단 결과
        """

        assert isinstance(fId, float)
        assert isinstance(fIdishre, float)


        if fId >= 150 and fId >= fIdishre * 16:
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