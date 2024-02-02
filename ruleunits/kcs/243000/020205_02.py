import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_020205_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 2.2.5 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-08'
    title = '스터드의 기계적 성질'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    2. 자재
    2.2 사용재료
    2.2.5 스터드형 전단연결재
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    ####(2) 강도는 표 2.2-4에 따른다.
    표 2.2-4 스터드의 기계적 성질
    \begin{table}[]
    \begin{tabular}{lll}
    인장강도(MPa) & 항복점 또는 0.2 % 내력(MPa) & 연신율(%) \\
    400∼550   & 235 이상               & 20 이상
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스터드의 기계적 성질];
    B["KCS 24 30 00 2.2.5 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 2.2.5 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 스터드의 기계적 성질/];
    VarIn1[/입력변수: 인장강도/];
    VarIn2[/입력변수: 항복점 또는 0.2% 내력/];
    VarIn3[/입력변수: 연신율/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"400<인장강도<550 \n 항복점 또는 0.2% 내력 >=235 \n 연신율>=20 \n."}
    C --> |True|Pass([Pass])
    C -->|False|Fail([Fail])
    """

    @rule_method
    def mechanical_stud(fITenStr, fIYieBea,fIEloRat)-> str:
        """
        Args:
            fITenStr (float): 인장강도
            fIYieBea (float): 항복점 또는 0.2% 내력
            fIEloRat (float): 연신율
        Returns:
            sOMecStu (string): 스터드의 기계적 성질
        """
        if fITenStr >400 and fITenStr<550 and fIYieBea >=235 and fIEloRat >=20:
            sOMecStu = "Pass"
        else:
            sOMecStu = "Fail"
        return sOMecStu