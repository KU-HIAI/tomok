import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030305_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '말뚝의 공칭 단위선단지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.5 암반 지지 말뚝
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝의 공칭 단위선단지지력];
    B["KDS 24 14 51 3.3.3.5 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:말뚝의 공칭 단위선단지지력/]
		VarIn1[/입력변수:불연속면 간격/]
		VarIn2[/입력변수:암석시편의 평균 일축압축강도/]
		VarIn3[/입력변수:무차원 깊이계수/]
		VarIn4[/입력변수:무차원 지지력계수/]
		VarIn5[/입력변수:불연속면 간격/]
		VarIn6[/입력변수:불연속면 폭/]
		VarIn7[/입력변수:말뚝 폭/]
		VarIn8[/입력변수:암반에 근입된 말뚝의 근입깊이/]
		VarIn9[/입력변수:암반 근입부 말뚝 폭/]

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~ VarIn3
		VarIn4 ~~~ VarIn5 ~~~ VarIn6
		VarIn7 ~~~ VarIn8 ~~~ VarIn9

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.5 (1)"])
		C --> Variable_def;

		J[말뚝 폭 또는 직경, 암반의 불연속면 간격 > 300mm ]
		D[속이 차있지 않은 불연속면의 폭이 < 6.4mm]
		E[흙 또는 암편으로 차있는 불연속면의 폭 < 25mm]
		F["<img src='https://latex.codecogs.com/svg.image?K_{sp}=\frac{3&plus;\frac{s_{d}}{D}}{10\sqrt{1&plus;300\frac{t_{d}}{s_{d}}}}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?&space;q_{p}=3q_{u}K_{sp}d'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?d=1&plus;0.4H_{s}/D_{s}\leq&space;3.4'>---------------------------------"]
		K([공친 단위 선단지지력])

		Variable_def ---> J & D & E
		J & D & E ---> I{만족} ---> F & H ---> G ---> K
    """

    @rule_method
    def Nominal_unit_end_support(fIqu,fIsd,fItd,fID,fIHs,fIDs) -> RuleUnitResult:
        """말뚝의 공칭 단위선단지지력

        Args:
            fIqu (float): 암석시편의 평균 일축압축강도
            fIsd (float): 불연속면 간격
            fItd (float): 불연속면 폭
            fID (float): 말뚝 폭
            fIHs (float): 암반에 근입된 말뚝의 근입깊이
            fIDs (float): 암반 근입부 말뚝 폭

        Returns:
            fOqp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.5 암반 지지 말뚝 (1)의 값 1
            fOd (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.5 암반 지지 말뚝 (1)의 값 2
            fOksp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.5 암반 지지 말뚝 (1)의 값 3
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.5 암반 지지 말뚝 (1)의 판단 결과
        """

        assert isinstance(fIqu, float)
        assert isinstance(fIsd, float)
        assert fIsd > 0
        assert isinstance(fItd, float)
        assert fItd > 0
        assert isinstance(fID, float)
        assert fID > 0
        assert isinstance(fIHs, float)
        assert isinstance(fIDs, float)
        assert fIDs > 0

        fOksp = (3 + fIsd / fID) / (1 + 300 * fItd / fIsd)**0.5 / 10
        fOd = 1 + 0.4 * fIHs / fIDs
        fOqp = 3 * fIqu * fOksp * fOd

        if fOd <= 3.4:
          return RuleUnitResult(
              result_variables = {
                  "fOqp": fOqp,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )