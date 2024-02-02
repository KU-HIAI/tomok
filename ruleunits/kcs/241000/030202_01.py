import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS241000_030202_01(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 10 00 3.2.2 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-09-24'
    title = '프리스트레싱 도입시 부재에 발생하는 최대 압축응력'

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트교량공사
    3. 시공
    3.2 프리스트레스트 콘크리트
    3.2.2 프리스트레싱 시의 콘크리트의 압축강도
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### (1) 프리스트레싱 도입시 부재에 발생하는 최대 압축응력은 도입시 콘크리트 압축강도의 60%를 넘지 말아야 한다.
    또는 특별한 규정이 없으면 포스트텐션 방식에서는 28 MPa, 프리텐션 방식에서는 30 MPa를 도입시 압축강도로 적용할 수 있다.
    이때 압축강도의 확인은 구조물과 동일한 양생조건의 공시체를 사용한다.
    """

    # 플로우차트(mermaid)
    flowchart ="""
    flowchart TD
    subgraph Python_Class
    A[Title: 프리스트레싱 도입시 부재에 발생하는 최대 압축응력];
    B["KCS 24 10 00 3.2.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.2.2 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 프리스트레싱도입시 최대 압축응력/];
    VarIn1[/입력변수: 특별한 규정 값/];
    VarIn2[/입력변수: 프리스트레싱 방식/];
    VarIn3[/입력변수: 콘크리트 압축강도/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"특별한 규정 값"}
    C --> |True|D[콘크리트 압축강도*0.6]
    C --> |False|E{프리스트레싱 방식}
    E --> |포스트텐션|F[28 MPa]
    E --> |프리텐션|G[30 MPa]
    D & F & G --> End([프리스트레싱 도입시 부재에 발생하는 최대 압축응력])
    """

    @rule_method
    def compressive_stress_prestressing(fIFck, bISpeVal,sIPreMet):
        """
        Args:
            fIFck (float): 콘크리트 압축강도
            bISpeVal (boolean): 특별한 규정 값
            sIPreMet (string): 프리스트레싱 방식
        Returns
            fOMaxCom (float): 프리스트레싱도입시 최대 압축응력
        """
        if bISpeVal:
            fOMaxCom = fIFck*0.6
        else:
            if sIPreMet == "포스트텐션":
                fOMaxCom = 28
            elif sIPreMet == "프리텐션":
                fOMaxCom = 30
        return fOMaxCom