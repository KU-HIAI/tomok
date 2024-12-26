import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0303_04(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.3.(4)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '발판지지 장선의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.3 경사로
    (4)
    """

    content = """
    #### 3.3 경사로
    (4) 발판을 지지하는 장선은 1.8m 이하의 간격으로 발판에 3점 이상 지지하도록 하여 경사로 보에 연결한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 발판지지 장선의 설치];
    B["KCS 21 60 15 3.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.3 (4)"])

    subgraph Variable_def
    VarIn1[/입력변수: 발판지지 장선의 간격/];
    VarIn2[/입력변수: 장선의 지지점 개수/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"발판지지 장선의 간격 <= 1.8m & <br/> 장선의 지지점 개수 >= 3점"}
    C --> D([Pass or Fail])
    """

    @rule_method
    def Spacing_of_Tread_Support_Beams(fISpaBea, nINumPoi) -> bool:
        """ 발판지지 장선의 설치
        Args:
            fISpaBea (float): 발판지지 장선의 간격
            nINumPoi (int): 장선의 지지점 개수

        Returns:
            pass_fail (bool): 작업발판 및 통로 3.3 경사로 (4)의 판단 결과
        """
        assert isinstance(fISpaBea, float)
        assert isinstance(nINumPoi, int)

        if fISpaBea <= 1.8 and nINumPoi >= 3:
          pass_fail = True
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )