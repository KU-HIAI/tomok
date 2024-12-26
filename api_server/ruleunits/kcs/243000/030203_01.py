import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030203_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.2.3 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '보호가스를 사용하는 일렉트로가스 용접 시 풍속'

    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.3 시공
    (1)
    """
    content = """
    #### 3.2.3 시공
    (1) 일렉트로 슬래그 용접법(ESW)과 일렉트로 가스 용접법(EGW)
    ① 일렉트로슬래그용접과 일렉트로가스 용접은 열처리 고장력강에 사용해서는 안 되며, 또한 인장응력이나 교번응력을 받기 쉬운 부재의 용접에도 사용해서는 안 된다.
    ② 보호가스를 사용하는 일렉트로가스 용접은 풍속이 2.2 m/s 이상일 경우 용접을 해서는 안 된다.
    부득이 용접을 실시할 경우에는 용접부 주변의 최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 적절한 방풍시설을 갖추어야 한다.
    동일하더라도 최대 판두께, 개선형상, 용접자세, 최대 입열량, 최소 예열온도, 용접 비드 개선 등이 다른 경우에는 가혹한 조건을 기준으로 피로 성능 평가의 추가 실시 여부를 감독자가 판단한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 보호가스를 사용하는 일렉트로가스 용접 풍속];
    B["KCS 24 30 00 3.2.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.2.3 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 보호가스를 사용하는 일렉트로가스 용접/];
    VarIn1[/입력변수: 풍속/];
    VarIn2[/입력변수: 부득이 용접을 실시/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"풍속 ≥ 2.2 m/s"}
    C --> |"True"|D{부득이 용접을 실시}
    D --> |"False"|F[용접을 해서는 안된다]
    D --> |"True"|G["최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 \n 적절한 방풍시설을 갖추어야 한다"]
    F & G --> H([보호가스를 사용하는 일렉트로가스 용접])
    """

    @rule_method

    def electrogas_welding_wind(fIWinSpe,bINecWel) -> RuleUnitResult:
        """
        Args:
            fIWinSpe (float): 풍속
            bINecWel (bool): 부득이 용접을 실시

        Returns:
            sOEleWel (str): 보호가스를 사용하는 일렉트로가스 용접
        """
        assert isinstance(fIWinSpe, float)
        assert isinstance(bINecWel, bool)
        assert fIWinSpe >=2.2


        if fIWinSpe >=2.2:
            if bINecWel:
                sOEleWel = "주변의 최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 적절한 방풍시설을 갖추어야 한다"
            else:
                sOEleWel = "용접을 해서는 안 된다"

        return RuleUnitResult(
            result_variables = {
                "sOEleWel": sOEleWel,
                })