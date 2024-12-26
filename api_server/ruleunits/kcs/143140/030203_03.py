import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143140_030203_03(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 40 3.2.3 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-12-21'
    title = '표면조도 만족 여부'

    description = """
    도장
    3. 시공
    3.2 표면처리 작업
    3.2.3 2차 표면처리 기준
    """

    content = """
    #### 3.2.3 2차 표면처리 기준
    (3) 표면조도는 별도의 언급이 없으면 25~75μ을 기준으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 표면조도];
    B["KCS 14 31 40 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 40 3.2.3 (3)"])

    subgraph Variable_def
    VarIn1[/입력변수: 별도의 언급/];
    VarIn2[/입력변수: 표면조도/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"별도의 언급"}

		C --> |true|F["표면조도 = Pass"]
		C --> |False|E{25μ <= 표면조도 <= 75μ}

		E --> |true|H["표면조도 = Pass"]
  	E --> |False|I["표면조도 = Fail"]

		F & H & I --> End([Pass or Fail])
    """

    @rule_method
    def Surface_Roughness(fISurRou, bISpeVal) -> bool:
        """ 표면조도 만족 여부
        Args:
        fISurRou (float): 표면조도
        bISpeVal (bool): 별도의 언급

        Returns:
        pass_fail (bool): 도장 3.2.3 2차 표면처리 기준 (3)의 판단 결과
        """
        assert isinstance(fISurRou, float)
        assert isinstance(bISpeVal, bool)

        if bISpeVal == True:
          pass_fail = True
        elif bISpeVal == False:
          if 25 <= fISurRou <=75:
            pass_fail = True
          else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )