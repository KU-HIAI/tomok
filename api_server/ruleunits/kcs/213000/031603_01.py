import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_031603_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.16.3.(1)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '계측빈도'

    description = """
    가설흙막이 공사
    3. 시공
    3.16. 계측관리
    3.16.3 계측빈도
    (1)
    """

    content = """
    #### 3.16.3 계측빈도
    (1) 계측빈도는 주변현황, 토질 및 지하수위 등의 조사결과와 흙막이 구조물의 형식에 따라 공사시방서에서 정하며, 굴착행위 단계별 계측을 수행하는 것이 원칙이어야 한다. 별도로 명시된 것이 없는 경우에는 다음을 참고할 수 있다.
    ① 굴착기간 동안은 각 항목별로 1주 2회 이상 측정하며, 굴착 완료 후에는 1주 1회 이상 측정하는 것을 원칙으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계측빈도];
    B["KCS 21 30 00 3.16.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.16.3 (1)"])

    subgraph Variable_def
    VarOut1[/출력변수: 주당 계측회수/];
    VarIn1[/입력변수: 굴착완료 여부/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"굴착완료 여부"}
    C1 --> |완료|D1["1회"]
    C1 --> |미완료|D2["2회"]

    D1 & D2 -->  E1(["주당 계측회수"])

    """

    @rule_method
    def Excavation_Status(bIExcSta) -> int:
        """ 계측빈도
        Args:
            bIExcSta (bool): 굴착 완료여부

        Returns:
            nOMeaFre (int): 주당 계측횟수
        """
        assert isinstance(bIExcSta, bool)

        if bIExcSta == True:
          nOMeaFre = 1
        elif bIExcSta == False:
          nOMeaFre = 2

        return RuleUnitResult(
                result_variables = {
                    "nOMeaFre": nOMeaFre
                }
            )