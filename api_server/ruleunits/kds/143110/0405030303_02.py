import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405030303_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '고정점까지의 깊이'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.3 말뚝
    4.5.3.3 압축저항
    4.5.3.3.3 좌굴
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[고정점까지의 깊이] ;
		B["KDS 14 31 10 4.5.3.3.3 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 고정점까지의 깊이/] ;
      VarIn1[/입력변수: 말뚝의 변형계수/] ;
      VarIn2[/입력변수: 말뚝의 단면2차 모멘트/] ;
      VarIn3[/입력변수: 깊이에 따른 사질토의 변형계수 증가율/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		Python_Class ~~~ C1(["KDS 14 31 10 4.5.3.3.3 (2)"]) --> Variable_def

		F["<img src=https://latex.codecogs.com/svg.image?1.8\left|\frac{E_{p}I_{p}}{E_{h}}\right|^{0.25}>------------------------------------------"]
		T["사질토"]

		Variable_def --> T
		T --> F
		F --> Q(["고정점까지의 깊이"])
    """

    @rule_method
    def depth_to_anchor_point(fIEp,fIIp,fInh) -> RuleUnitResult:
        """고정점까지의 깊이

        Args:
            fIEp (float): 말뚝의 변형계수
            fIIp (float): 말뚝의 단면2차모멘트
            fInh (float): 깊이에 따른 사질토의 변형계수 증가율

        Returns:
            fOdeanpo (float): 강구조부재설계기준(하중저항계수설계법) 4.5.3.3.3 좌굴 (2)의 값
        """

        assert isinstance(fIEp, float) and fIEp != 0
        assert isinstance(fIIp, float) and fIIp != 0
        assert isinstance(fIEs, float)
        assert isinstance(fInh, float) and fInh != 0

        fOdeanpo = 1.8 * abs(fIEp * fIIp / fInh) ** 0.25

        return RuleUnitResult(
            result_variables = {
                "fOdeanpo": fOdeanpo,
            }
        )