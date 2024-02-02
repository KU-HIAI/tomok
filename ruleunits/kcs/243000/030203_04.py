import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030203_04(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.2.3 (4)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '언더컷의 깊이'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.3 시공
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    ####(4) 용접 검사
    ① 비파괴검사의 적용분류는 전수검사, 부분검사 및 지정검사로 나누어 시행한다.
    ② 육안검사자는 관련분야에 5년 이상 종사한 자가 실시하는 것을 기본으로 한다.
    ③ 용접비드 표면의 요철은 비드길이 25 mm 범위에서의 고저차로 나타내고, 3 mm를 넘는 요철이 있어서는 안 된다.
    ④ 언더컷의 깊이는 표 3.2-7의 값을 초과해서는 안 된다.
    표 3.2-7 언더컷의 깊이
    \begin{table}[]
    \begin{tabular}{ll}
    언더컷의 위치                           & 허용차(mm) \\
    주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 종단부 & 0.3     \\
    주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 종단부 & 0.5     \\
    2차부재의 비드 종단부                      & 0.8
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 언더컷 깊이의 허용차];
    B["KCS 24 30 00 3.2.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.2.3 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 언더컷 깊이의 허용차/];
    VarIn1[/입력변수: 언더컷의 위치/];
    VarIn2[/입력변수: 언더컷의 깊이/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"언더컷의 깊이"}
    C --> |"주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 종단부"|D{언더컷 깊이의 허용차 < 0.3 mm}
    C --> |"주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 종단부"|E{언더컷 깊이의 허용차 < 0.5 mm}
    C --> |"2차부재의 비드 종단부"|F{언더컷 깊이의 허용차 < 0.8 mm}
    D & F & E --> |True|Pass([Pass])
    D & F & E --> |False|Fail([Fail])
    """

    @rule_method
    def undercut_depth(sIPosUnd,fIUndDep)-> str:
        """
        Args:
            sIPosUnd (string): 언더컷의 위치
            fIUndDep (float): 언더컷의 깊이
        Returns:
            sOTolUnd (string): 언더컷 깊이의 허용차
        """
        if sIPosUnd == "주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 종단부":
            if fIUndDep >0.3:
                sOTolUnd = "Fail"
            else:
                sOTolUnd = "Pass"
        elif sIPosUnd == "주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 종단부":
            if fIUndDep >0.5:
                sOTolUnd = "Fail"
            else:
                sOTolUnd = "Pass"
        elif sIPosUnd == "2차부재의 비드 종단부":
            if fIUndDep >0.8:
                sOTolUnd = "Fail"
            else:
                sOTolUnd = "Pass"
        else:
            return "주요부재의 재편에 작용하는 1차응력에 직교하는 비드의 종단부, 주요부재의 재편에 작용하는 1차응력에 평행하는 비드의 종단부, 2차부재의 비드 종단부 중에 선택해주세요"
        return sOTolUnd