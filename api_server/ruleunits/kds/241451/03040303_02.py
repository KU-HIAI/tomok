import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03040303_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.4.3.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '공칭 단위 선단지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭 단위 선단지지력];
    B["KDS 24 14 51 3.4.3.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:공칭 단위 선단지지력/]
		VarIn1[/입력변수:말뚝의 지름/]
		VarIn2[/입력변수:말뚝의 관입깊이/]
		VarIn3[/입력변수:비배수전단강도/]
		VarIn4[/입력변수:지름/]
		VarIn5[/입력변수:현장시험결과/]
		VarIn6[/입력변수:실내시험결과/]
		VarIn7[/입력변수: Nc값/]

		VarIn1 ~~~ VarIn2 ~~~ VarIn3
		VarIn4 ~~~ VarIn5 ~~~ VarIn6 ~~~ VarIn7

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.4.3.3 (2)"])
		C --> Variable_def

		J["<img src='https://latex.codecogs.com/svg.image?q_{p}=N_{c}S_{u}\leq&space;4.0'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?N_{c}=6[1&plus;0.2(\frac{Z}{D})]\leq&space;9'>---------------------------------"]
		E{선단으로부터 지름 2배만큼 떨어진 깊이 이내의 위치에서 시행한 현장시험결과}
		F{이 깊이에서 채취한 불교란 시료를 사용한 실내시험 결과}
		H{비배수전단강도가 0.024MPa 이하라면 Nc 값에 0.67을 곱한다}

		Variable_def ---> E & F & D
		D ---> H
		E & F ---> G[비배수전단강도] ---> J
		J & H ---> I[공칭 단위 선단지지력] ---> K([Pass or Fail])
    """

    @rule_method
    def unit_nominal_end_bearing_capacity(fID,fIZ,fISu) -> RuleUnitResult:
        """공칭 단위 선단지지력

        Args:
            fID (float): 말뚝의 탄성계수
            fIZ (float): 말뚝의 관성모멘트
            fISu (float): 사질토의 깊이에 따른 탄성계수 증가비

        Returns:
            fOqp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정 (2)의 값 1
            fONc (float): 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정 (2)의 값 2
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.3 점성토에 설치한 현장타설말뚝의 지지력 산정 (2)의 판단 결과
        """

        assert isinstance(fID, float)
        assert isinstance(fIZ, float)
        assert isinstance(fISu, float)

        fONc = 6*(1 + 0.2 * (fIZ / fID))

        if fISu <= 0.024 :
          fOqp = fONc * 0.67 * fISu
        else:
          fOqp = fONc * fISu

        if fONc <= 9 and fOqp <= 4 :
          return RuleUnitResult(
              result_variables = {
                  "fONc": fONc,
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