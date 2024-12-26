import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_041103_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.11.3 (2)'
    ref_date = '2022-01-11'
    doc_date = '2024-08-02'
    title = '전단철근에 의한 공칭전단강도'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.11 슬래브와 기초판에 대한 전단 설계
    4.11.3 전단철근
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단철근에 의한 공칭전단강도];
    B["KDS 14 20 22 4.11.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 전단철근에 의한 공칭전단강도/];
    VarOut2[/출력변수: 뚫림전단파괴시 전단철근에 작용하는 응력/];
    VarIn1[/입력변수: 종방향 철근에 평행한 방향으로 전단 또는 비틀림철근의 간격 내의 전단철근의 단면적/];
    VarIn2[/입력변수: 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리/];
    VarIn3[/입력변수: 종방향 철근에 평행한 방향으로 전단 또는 비틀림철근의 간격/];
    VarIn4[/입력변수: 횡방향 철근의 설계기준항복강도/];
    end

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
    VarIn1 ~~~ VarIn3 & VarIn4

    Python_Class ~~~ C(["KDS 14 20 22 4.11.3 (2)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image? f_{s}=0.5f_{yt}'>--------------------------"];
    E["<img src='https://latex.codecogs.com/svg.image? V_{s}=\frac{A_{v}f_{s}d}{s}'>----------------------------"];

		Variable_def --> D --> E --> F(["전단철근에 의한 공칭전단강도"])
    """

    @rule_method
    def Nominal_shear_strength_by_shear_reinforcement(fIAv,fId,fIs,fIfyt) -> RuleUnitResult:
        """전단철근에 의한 공칭전단강도

        Args:
            fIAv (float): 종방향 철근에 평행한 방향으로 전단 또는 비틀림철근의 간격 내의 전단철근의 단면적
            fId (float): 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리
            fIs (float): 종방향 철근에 평행한 방향으로 전단 또는 비틀림철근의 간격
            fIfyt (float): 횡방향 철근의 설계기준항복강도


        Returns:
            fOVs (float): 전단철근에 의한 공칭전단강도
            fOfs (float): 뚫림전단파괴시 전단철근에 작용하는 응력
        """

        assert isinstance(fIAv, float)
        assert isinstance(fId, float)
        assert isinstance(fIs, float)
        assert isinstance(fIfyt, float)




        if fIAv == 0:
          fOVs = 0
          return RuleUnitResult(
              result_variables = {
                  "fOVs": fOVs,
              }
          )
        else:
          assert fIs > 0
          assert fId > 0
          fOfs = 0.5 * fIfyt
          fOVs = fIAv * fOfs * fId / fIs
          return RuleUnitResult(
              result_variables = {
                  "fOVs": fOVs,
              }
          )