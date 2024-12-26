import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142011_03010304_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 11 3.1.3.4 (5)'
    ref_date = '2022-01-11'
    doc_date = '2024-05-17'
    title = '철근 용접이음 시 풍속'

    description = """
    철근공사
    3. 시공
    3.1 철근
    3.1.3 철근의 이음
    3.1.3.4 용접 이음
    (5)
    """
    content = """
    #### 3.1.3.4 용접 이음
    (5) 철근의 용접부에 순간최대풍속 2.7 m/s 이상의 바람이 불 때는 철근을 용접할 수 없으며, 풍속을 2.7 m/s 이하로 저감시킬 수 있는 방풍시설을 설치하는 경우에만 용접할 수 있다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 용접이음 시 풍속];
    B["KCS 14 20 11 3.1.3.4 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 11 3.1.3.4 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 철근 용접이음 시 풍속/];
    VarIn1[/입력변수: 순간최대풍속/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"순간최대풍속 ≥ 2.7"}
    C --> |"True"|D["철근을 용접할 수 없으며, \n 풍속을 2.7 m/s 이하로 저감시킬 수 있는 방풍시설을 설치하는 경우에만 \n용접할 수 있다."]
    D  --> H(["철근 용접이음 시 풍속"])
    C --> |False|Pass([Pass])
    """

    @rule_method
    def wind_weld_joint(fIMaxWin)-> RuleUnitResult:
        """
        Args:
           fIMaxWin (float): 순간최대풍속

        Returns:
            sOWelJoi (str): 철근 용접이음 시공
            pass_fail (bool): 철근공사 3.1.3.4 용접 이음 (5)의 판단 결과

        """
        assert isinstance(fIMaxWin, float)

        if fIMaxWin >=2.7:
            sOWelJoi = "철근을 용접할 수 없으며, 풍속을 2.7 m/s 이하로 저감시킬 수 있는 방풍시설을 설치하는 경우에만 용접할 수 있다"
            pass_fail = None
        else:
            sOWelJoi = None
            pass_fail = True
        return RuleUnitResult(
            result_variables = {
                "sOWelJoi": sOWelJoi,
                "pass_fail": pass_fail,
                })