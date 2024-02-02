import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS241000_030301(RuleUnit):

    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 10 00 3.3.1'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '철근 배치의 시공 허용오차'

    # 건설기준문서항목 (분류체계정보)
    description = """
    콘크리트교량공사
    3. 시공
    3.3 가설 및 시공 허용오차
    3.3.1 철근 배치의 시공 허용오차
    """

    # 건설기준문서내용(text)
    content = """
    #### 철근 배치에 관한 시공 허용오차는 표 3.3-1의 값으로 하여야 한다.
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} 항목}   & {\color[HTML]{333333} 시공허용오차}                                                                                                                                                              \\
    {\color[HTML]{333333} 유효높이} & \cellcolor[HTML]{FFFFFF}{\color[HTML]{000000} \begin{tabular}[c]{@{}l@{}}설계치수의 ±3 % 또는 ±30 mm 중에서 작은 값. 다만, 최소 피복두께는 확보하여야 한다.\\ 바닥판의 경우 설계치수의 ±10 mm로 하고 소요 피복두께를 확보하여야 한다.\end{tabular}}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근 배치의 시공 허용오차];
    B["KCS 24 10 00 3.3.1"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.3.1"])

    subgraph Variable_def
    VarOut[/출력변수: 철근 배치의 시공 허용오차/];
    VarIn1[/입력변수: 설계치수의 유효높이/];
    VarIn2[/입력변수: 최소 피복두께/];
    VarIn20[/입력변수: 바닥판/]
    VarIn3[/입력변수: 소요 피복두께/];
    VarOut ~~~ VarIn1 & VarIn2
    VarIn1 ~~~ VarIn20 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{바닥판}
    C --> |False|D["철근 배치의 시공 허용오차 \n = max(min(유효높이의 설계치수*0.03, 30 mm),최소 피복두께)"]
    C --> |True|E["철근 배치의 시공 허용오차 \n = max(10 mm, 소요 피복두께)"]
    D --> F([철근 배치의 시공 허용오차])
    E --> F([철근 배치의 시공 허용오차])
    """

    @rule_method
    def tolerance_reinforcement_layout(fIEffHei, fIMinCle, fIReqCle, bIDec) -> str:
        """
        Args:
            fIEffHei (float): 유효높이의 설계치수
            fIMinCle (float): 최소 피복두께
            fIReqCle (float): 소요 피복두께
            bIDec (boolean): 바닥판
        Returns:
            sOTolLay (string): 철근 배치의 시공 허용오차
        """
        if bIDec == False:
            sOTolLay =  "±" + str(round(max(min(fIEffHei * 0.03, 30),fIMinCle), 5)) + " mm"
        else:
            sOTolLay =  "±" + str(max(10,fIMinCle)) + " mm"
        return sOTolLay