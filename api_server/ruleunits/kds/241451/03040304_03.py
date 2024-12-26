import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03040304_03(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.4.3.4 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '공칭 단위 선단지지력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.4 사질토에 설치한 현장타설말뚝의 지지력 산정
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 공칭 단위 선단지지력];
    B["KDS 24 14 51 3.4.3.4 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:공칭 선단지지력/]
		VarIn1[/입력변수:설계구역지층의 평균 N값으로서, 해머효율에 대해서 보정한 /]
		VarIn2[/입력변수:대상층 중간에서 연직유효응력/]
		VarIn3[/입력변수:대기압/]

		VarOut1
		VarIn1 ~~~ VarIn2 ~~~ VarIn3

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.4.3.4 (3)"])
		C --> Variable_def

		H[N60 > 50]
		D["<img src='https://latex.codecogs.com/svg.image?q_{p}=0.59[N_{60}(\frac{p_{a}}{\sigma&space;_{v}^{\prime}})]\sigma&space;_{v}^{\prime}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?0.057N_{60}\leq&space;50'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?q_{p}=1.2N_{60}'>---------------------------------"]
		G[재하시험을 실시한 경우 외, 공친선단지지력 < 3.0MPa]
		I[N_60값이 50보다 큰 지층에 대해서 중간지반으로 간주]
		K([공칭선단지지력])

		Variable_def ---> E ---> F ---> G ---> K
		Variable_def ---> I ---> H ---> D ---> K
    """

    @rule_method
    def unit_nominal_end_bearing_capacity(fIN,fIverstr,fIPa) -> RuleUnitResult:
        """공칭 단위 선단지지력

        Args:
            fIN (float): 설계구역 지층의 평균 N값으로서, 해머효율에 대해서 보정한 값
            fIverstr (float): 대상층 중간에서 연직유효응력
            fIPa (float): 대기압

        Returns:
            fOqp (float): 교량 하부구조 설계기준 (한계상태설계법)  3.4.3.4 사질토에 설치한 현장타설말뚝의 지지력 산정 (3)의 값
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법)  3.4.3.4 사질토에 설치한 현장타설말뚝의 지지력 산정 (3)의 판단 결과
        """

        assert isinstance(fIN, float)
        assert isinstance(fIverstr, float)
        assert isinstance(fIPa, float)

        if fIN * 0.057 <= 50:
          fOqp = 1.2*fIN
          if fOqp <= 3 :
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

        if fIN > 50:
          fOqp = 0.59 * ((fIN * (fIPa / fIverstr))**0.8) * fIverstr
          if fIN <= 100 :
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