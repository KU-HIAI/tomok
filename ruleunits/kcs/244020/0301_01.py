import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244020_0301_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 20 3.1 (1)'
    ref_date = '2016-06-30'
    doc_date = '2023-10-12'
    title = '콘크리트 바닥판면 방수층 시공'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량방수
    3. 시공
    3.1 시공 전 준비사항
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 콘크리트 바닥판면의 시공에 보통시멘트를 사용할 경우, 콘크리트 타설 후, 2주 이내에 방수층 시공을 해서는 안 된다. 그러나 조강 및 초속경시멘트를 사용할 경우는 고주파 수분계로 건조상태를 확인한 후, 그 값이 10% 이하일 때에는 2주 이내에 방수층을 시공하여도 무방하다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트 바닥판면 방수층 시공];
    B["KCS 24 40 20 3.1 (1))"];
    B ~~~ A
    end

    KCS(["KCS 24 40 20 3.1 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 콘크리트 바닥판면 방수층 시공/];
    VarIn1[/입력변수: 시멘트 종류/];
    VarIn2[/입력변수: 고주파 수분계로 측정한 수분/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{시멘트 종류}
    C --> |보통시멘트|D["콘크리트 타설 후 \n 2주 이내에 방수층 시공을 해서는 안 된다"]
    C --> |조강시멘트, 초속경시멘트|E{"고주파 수분계로 측정한 수분"}
    E --> |"고주파 수분계로 측정한 수분 ≤ 10%"|F["콘크리트 타설 후 \n 2주 이내에 방수층을 시공하여도 무방"]
    E --> |"고주파 수분계로 측정한 수분 > 10%"|D["콘크리트 타설 후 \n 2주 이내에 방수층 시공을 해서는 안 된다"]
    D & F --> End([콘크리트 바닥판면 방수층 시공])
    """

    @rule_method
    def waterproofing_concrete_slab(sICemTyp,fIMoiHig)->str:
        """
        Args:
            sICemTyp (string): 시멘트 종류
            fIMoiHig (float): 고주파 수분계로 측정한 수분
        Returns:
            sOWatCon (string): 콘크리트 바닥판면 방수층 시공
        """
        if sICemTyp =="보통시멘트":
            sOWatCon = "콘크리트 타설 후, 2주 이내에 방수층 시공을 해서는 안 된다"
        elif sICemTyp =="조강 시멘트" or "초속경시멘트":
            if fIMoiHig <= 10:
                sOWatCon = "콘크리트 타설 후 2주 이내에 방수층을 시공하여도 무방하다"
            else:
                sOWatCon = "콘크리트 타설 후, 2주 이내에 방수층 시공을 해서는 안 된다"
        return sOWatCon