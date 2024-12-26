import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03020301_05(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3.1 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '편심하중을 받는 기초의 감소된 유효면적'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.1 지지력
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 편심하중을 받는 기초의 감소된 유효면적];
    B["KDS 24 14 51 3.2.3.1 (5)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수:유효면적/];
		VarIn2[/입력변수:수정된 B방향 길이/];
		VarIn3[/입력변수:수정된 L방향 길이/];
		VarIn4[/입력변수:B방향의 편심거리/];
		VarIn5[/입력변수:L방향의 편심거리/];
		VarIn6[/입력변수:감가된 지지력/];
		VarIn7[/입력변수:설계하중/];
		VarIn8[/입력변수:기초의 편심/];
		VarIn9[/입력변수:기초의 크기/];


		VarIn1
		VarIn2 ~~~ VarIn3 ~~~ VarIn4
		VarIn5 ~~~ VarIn6 ~~~ VarIn7
		VarIn8 ~~~ VarIn9
    end

    Python_Class ~~~ C(["KDS 24 14 51 3.2.3.1 (5)"])
		C --> Variable_def;

		Variable_def--->K
		K["감가된 지지력 ≥ 설계하중"]
		K--->D & F
		D["지진하중을 고려하는 극단상황한계상태"]
		D--->E
		E["B or L < 4/10"]
		F["B or L < 1/4"]
		E & F ---> G
		G["<img src='https://latex.codecogs.com/svg.image?B^\prime=B-2e_B'>---------------------------------"]
		G-->H
		H["<img src='https://latex.codecogs.com/svg.image?L^\prime=L-2e_L'>---------------------------------"]
		H-->I
		I["<img src='https://latex.codecogs.com/svg.image?B^\prime\times&space;L^\prime'>---------------------------------"]
		I--->J
		J["편심하중을 받는 기초의 감소된 유효면적"]
    """

    @rule_method
    def Reduced_effectiv_area_of_foundation_under_eccentric_load(fIEb,fIEl,fIdimsup,fIDgnlod,fIB,fIL) -> RuleUnitResult:
        """편심하중을 받는 기초의 감소된 유효면적

        Args:
            fIEb (float): B방향의 편심거리
            fIEl (float): L방향의 편심거리
            fIdimsup (float): 감가된 지지력
            fIDgnlod (float): 설계하중
            fIB (float): 기초의 B 크기
            fIL (float): 기초의 L 크기

        Returns:
            fOEffare (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (5)의 값 1
            fOBp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (5)의 값 2
            fOLp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (5)의 값 3
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (5)의 판단 결과
        """

        assert isinstance(fIEb, float)
        assert isinstance(fIEl, float)
        assert isinstance(fIdimsup, float)
        assert isinstance(fIDgnlod, float)
        assert isinstance(fIB, float)
        assert isinstance(fIL, float)

        if fIEb < fIB/4 and fIEl < fIL/4 :
          fOBp = fIB - 2*fIEb
          fOLp = fIL - 2*fIEl
          fOEffare = fOBp * fOLp
          return RuleUnitResult(
              result_variables = {
                  "fOEffare": fOEffare,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOEffare": fOEffare,
                  "pass_fail": False,
              }
          )