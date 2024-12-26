import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS116000_030302_02(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 11 60 00 3.3.2 (2)'
    ref_date = '2020-12-03'
    doc_date = '2023-08-14'
    title = '중심결정구 부착 간격'

    description = """
    앵커
    3. 시공
    3.3 시공기준
    3.3.2 앵커의 삽입
    (2)
    """

    content = """
    #### 3.3.2. 앵커의 삽입
    (2) 앵커 삽입 시 앵커가 천공 구멍의 중앙에 위치하도록 앵커에 중심결정구(센트럴라이저)를 1m ~ 3m 간격으로 부착하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 중심결정구 부착 간격];
    B["KCS 11 60 00 3.3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 11 60 00 3.3.2 (2)"])

    subgraph Variable_def
    VarIn[/입력변수: 중심결정구 부착 간격/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"1m <= 중심결정구 부착 간격 <= 3m"}
    C--> D(["Pass or Fail"])
    """

    @rule_method
    def Spcacing_between_Centralizer(fISpaCen) -> bool:
        """중심결정구 부착간격
        Args:
          fISpaCen (float): 중심결정구 부착간격

        Returns:
          pass_fail (bool): 앵커 3.3.2 앵커의 삽입 (2)의 판단 결과
        """
        assert isinstance(fISpaCen, float)

        if 1 <= fISpaCen <= 3:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )