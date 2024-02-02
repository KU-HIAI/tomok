import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030203_01(RuleUnit): #KCS243000_030203_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 최정운'  # 작성자명
    ref_code = 'KCS 24 30 00 3.2.3 (1)' # 건설기준문서
    ref_date = '2019-05-20'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '보호가스를 사용하는 일렉트로가스 용접 시 풍속'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.3 시공
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    ####(1) 일렉트로 슬래그 용접법(ESW)과 일렉트로 가스 용접법(EGW)
    ① 일렉트로슬래그용접과 일렉트로가스 용접은 열처리 고장력강에 사용해서는 안 되며, 또한 인장응력이나 교번응력을 받기 쉬운 부재의 용접에도 사용해서는 안 된다.
    ② 보호가스를 사용하는 일렉트로가스 용접은 풍속이 2.2 m/s 이상일 경우 용접을 해서는 안 된다. 부득이 용접을 실시할 경우에는 용접부 주변의 최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 적절한 방풍시설을 갖추어야 한다.
    """

    # 플로우차트(mermaid)
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
    C --> |"False"|Pass([Pass])
    D --> |"False"|F[용접을 해서는 안된다]
    D --> |"True"|G["최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 \n 적절한 방풍시설을 갖추어야 한다"]
    F & G --> H([보호가스를 사용하는 일렉트로가스 용접])
    """

    @rule_method
    def electrogas_welding_wind(fIWinSpe,bINecWel)-> str:
        """
        Args:
            fIWinSpe (float): 풍속
            bINecWel (boolean): 부득이 용접을 실시
        Returns:
            sOEleWel (string): 보호가스를 사용하는 일렉트로가스 용접
        """
        if fIWinSpe >=2.2:
            if bINecWel:
                sOEleWel = "주변의 최대풍속을 2.2 m/s 이하까지 감소시킬 수 있는 적절한 방풍시설을 갖추어야 한다"
            else:
                sOEleWel = "용접을 해서는 안 된다"
        else:
            sOEleWel = "Pass"
        return sOEleWel