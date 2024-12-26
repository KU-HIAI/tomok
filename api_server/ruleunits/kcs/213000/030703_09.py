import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030703_09(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.7.3 (9)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '굴착구멍의 연직도'

    description = """
    가설흙막이 공사
    3. 시공
    3.7 흙막이 벽 공법
    3.7.3 지하연속벽 공법
    (9)
    """

    content = """
    #### 3.7.3. 지하연속벽 공법
    (9) 안내벽은 다음에 적합하여야 한다.
    ① 굴착 구멍은 연직으로 하고, 연직도의 허용오차는 1％ 이하이어야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 굴착구멍의 연직도];
    B["KCS 21 30 00 3.7.3 (9)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.7.3 (9)"])

    subgraph Variable_def
    VarIn[/입력변수: 굴착구멍의 연직도/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"99% <= 굴착구멍의 연직도 <= 101%"}

    C --> D([Pass or Fail])
    """

    @rule_method
    def Verticality_Torlerance_of_Excavation_Hole(fIVerExc) -> bool:
        """ 굴착구멍의 연직도
        Args:
            fIVerExc (float): 굴착 구멍의 연직도 오차

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.7.3 지하연속벽 공법 (9)의 판단 결과
        """
        assert isinstance(fIVerExc, float)

        if -1 <= fIVerExc <= 1:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )