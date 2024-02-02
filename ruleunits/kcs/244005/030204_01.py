import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_030204_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 3.2.4 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '탄성받침의 외부판 용접'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    3. 시공
    3.2 탄성받침
    3.2.4 설치
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 탄성받침 외부판은 용접부와 고무사이에 적어도 38 mm의 이격이 존재하지 않는다면 용접을 해서는 안 된다. 어떠한 경우라도 고무와 부착부는 200 ℃ 이상으로 가열되어서는 안 된다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성받침의 외부판 용접];
    B["KCS 24 40 05 3.2.4 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.2.4 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 탄성받침의 외부판 용접/];
    VarIn1[/입력변수: 용접부와 고무사이 이격/];
    VarIn2[/입력변수: 고무와 부착부 가열 온도/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용접부와 고무사이 이격 ≥ 38 mm"}
    C --> |True|D{"고무와 부착부 가열 온도 < 200 ℃"}
    C --> |False|E(["Fail"])
    D --> |False|E(["Fail"])
    D --> |True|F(["Pass"])
    """

    @rule_method
    def weld_bearing(fIDisWel,fITemWel)->str:
        """
        Args:
            fIDisWel (float): 용접부와 고무사이 이격
            fITemWel (float): 고무와 부착부 가열 온도
        Returns:
            sOWelBea (string): 탄성받침의 용접
        """
        if fIDisWel >= 38 and fITemWel < 200:
            sOWelBea = "Pass"
        else:
            sOWelBea = "Fail"
        return sOWelBea