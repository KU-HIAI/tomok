import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_04010110_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.1.10 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-14'
    title = '고장력볼트의 구멍중심간 거리'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.1 일반사항
    4.1.1.10 이음부 설계세칙
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
  	subgraph Python_Class
	  A[Title: 고장력볼트의 구멍중심간 거리]
  	B["KDS 14 31 25 4.1.1.10(4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut1[/출력변수: 최소거리/]
	  VarOut2[/출력변수: 표준거리/]
	  VarIn[/입력변수: 공칭직경/]
	  end

    Python_Class ~~~ C(["KDS 14 31 25 4.1.1.10(4)"])
		C --> Variable_def

	  Variable_def --> D --최소거리--> E
	  D--표준거리-->F
	  E --> G
	  F --> H
  	D["고장력볼트의 구멍중심간의 거리"]
	  E["공칭직경 X 2.5"]
	  F["공칭직경 X 3"]
    G([최소거리])
	  H([표준거리])
    """

    @rule_method
    def Distance_between_hole_center_of_high_strength_bolt(fInomdim) -> RuleUnitResult:
        """고장력볼트의 구멍중심간 거리

        Args:
            fInomdim (float): 공칭직경

        Returns:
            fOmindis (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.1.10 이음부 설계세칙 (4)의 값 1
            fOstadis (float): 강구조 연결 설계기준(하중저항계수설계법)   4.1.1.10 이음부 설계세칙 (4)의 값 2
        """

        assert isinstance(fInomdim, float)

        fOmindis = fInomdim*2.5
        fOstadis = fInomdim*3

        return RuleUnitResult(
            result_variables = {
                "fOmindis": fOmindis,
                "fOstadis": fOstadis,
            }
        )