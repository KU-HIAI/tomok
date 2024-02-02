import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_030503_05(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 3.5.3 (5)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '지진격리받침 탄성중합체의 최대전단변형률'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    3. 시공
    3.5 지진격리받침
    3.5.3 품질기준
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    #### (5) 지진격리받침 탄성중합체의 최대전단변형률은 상시에는 70%, 지진 시에는 200% 이하이어야 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 지진격리받침 탄성중합체의 최대전단변형률];
    B["KCS 24 40 05 3.5.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.5.3 (5)"])

    subgraph Variable_def
    VarOut[/출력변수: 지진격리받침 탄성중합체의 최대전단변형률/];
    VarIn1[/입력변수: 지진격리받침 탄성중합체의 최대전단변형률/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{지진 상황}
    C --> |False|D["지진격리받침 탄성중합체의 최대전단변형률 = 70%"]
    C --> |True|E["지진격리받침 탄성중합체의 최대전단변형률 = 200%"]
    D & E --> P(["지진격리받침 탄성중합체의 최대전단변형률"])
    """

    @rule_method
    def strain_seismic_bearing(bISei):
        """
        Args:
            bISei (boolean): 지진 상황
        Returns:
            fOStrSei (float): 지진격리받침 탄성중합체의 최대전단변형률
        """
        if bISei == True:
            fOStrSei = 200
        else:
            fOStrSei = 70
        return fOStrSei