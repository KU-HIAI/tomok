import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_020302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 2.3.2 (2)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-31'
    title = '폴리에테르 우레탄 디스크 설계'

    description = """
    교량받침
    2. 자재
    2.3 포트받침 및 디스크받침
    2.3.2 폴리에테르 우레탄 디스크(polyether urethane disc)
    (2)
    """
    content = """
    #### 2.3.2 폴리에테르 우레탄 디스크(polyether urethane disc)
    (2) 폴리에테르 우레탄 디스크는 다음의 사항을 만족하도록 설계되어야 한다.
        ① 총설계하중에 의한 즉시처짐이 무응력상태 디스크 두께의 10%를 넘지 않아야 하고, 크리프에 의한 추가 처짐도 무응력상태 디스크 두께의 8%를 넘지 않아야 한다.
        ② 받침의 구성부품들은 어느 위치에서도 서로 들뜨지 않아야 한다.
        ③ 디스크의 평균압축응력은 35 MPa을 넘지 않아야 한다. 만약 디스크의 외측면이 연직이 아닌 경우에는 응력계산 시 디스크의 평면 상 가장 작은 면적을 사용하여야 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 폴리에테르 우레탄 디스크 설계];
    B["KCS 24 40 05 2.3.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.3.2 (2)"])

    subgraph Variable_def
    subgraph V1
    VarOut11[/출력변수: 설계하중에 의한 최대 즉시처짐/];
    VarOut12[/출력변수: 설계하중에 의한 최대 즉시처짐/];
    VarIn11[/입력변수: 무응력상태 디스크 두께/];
    end
    subgraph V2
    VarOut2[/출력변수: 디스크의 평균압축응력/];
    VarIn22[/입력변수: 디스크의 외측면이 연직/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{설계하중에 의한 최대 즉시처짐 \n설계하중에 의한 최대 즉시처짐 \n 디스크의 평균압축응력\n.}
    D --> |"설계하중에 의한 최대 즉시처짐 \n설계하중에 의한 최대 즉시처짐"|E{설계하중에 의한 최대 즉시처짐 \n설계하중에 의한 최대 즉시처짐}
    E --> |설계하중에 의한 최대 즉시처짐|F["무응력상태 디스크 두께*0.1"]
    E --> |설계하중에 의한 최대 즉시처짐|G["무응력상태 디스크 두께*0.08"]
    D --> | 디스크의 평균압축응력|H{ 디스크의 외측면이 연직}
    H --> |True|I[35 MPa을 넘지 않아야 한다]
    H --> |False|J[응력계산 시 디스크의 평면 상 가장 작은 면적을 사용하여야 한다. \n 35 MPa을 넘지 않아야 한다.]
    F & G & I & J --> End([폴리에테르 우레탄 디스크 설계])
    """

    @rule_method

    def polyether_urethane_disk_design(fIDisThi,bIPerOut) -> RuleUnitResult:
        """
        Args:
            fIDisThi (float): 무응력상태 디스크 두께
            bIPerOut (bool): 디스크의 외측면이 연직

        Returns:
            fOImmDef (float): 설계하중에 의한 최대 즉시처짐
            fOAddDef (float): 크리프에 의한 최대 추가처짐
            sOComDis (str): 디스크의 평균압축응력
        """
        assert isinstance(fIDisThi, float)
        assert isinstance(bIPerOut, bool)

        fOImmDef = fIDisThi * 0.1
        fOAddDef = fIDisThi * 0.08

        if bIPerOut:
            sOComDis = "35 MPa을 넘지 않아야 한다"
        elif bIPerOut == False:
            sOComDis = "응력계산 시 디스크의 평면 상 가장 작은 면적을 사용해야 하며, 35 MPa을 넘지 않아야 한다"

        return RuleUnitResult(
            result_variables = {
                "fOImmDef": fOImmDef,
                "fOAddDef": fOAddDef,
                "sOComDis": sOComDis,
                })