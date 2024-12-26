import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0403020203_04(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.3.2.2.3 (4)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-25'
    title = '간격'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[Title: 간격]
	  B["KDS 14 31 25 4.3.2.2.3 (4)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 간격/] ;
		VarIn2[/입력변수: 지강관 벽두께의 총합/] ;
		end

    Python_Class ~~~ C(["KDS 14 31 25 4.3.2.2.3 (4)"])
		C --> Variable_def

	  E{"g ≥ 지강관 벽두께의 총합"} ;

		Variable_def --> E --> D(["PASS or Fail"])
    """

    @rule_method
    def spacing(fIg,fIbmwthi) -> RuleUnitResult:
        """간격

        Args:
            fIg (float): 간격
            fIbmwthi (float): 지강관 벽두께

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)  4.3.2.2.3 간격 K형 접합에서 압축력을 받는 지강관 (4)의 판단 결과
        """

        assert isinstance(fIg, float)
        assert isinstance(fIbmwthi, float)

        temp = sum(fIbmwthi[j] for j in range(i))

        if fIg >= temp:
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