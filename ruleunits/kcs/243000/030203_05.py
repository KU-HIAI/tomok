import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030203_05(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.2.3 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-14'
    title = '그루브용접의 더돋기'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.3 시공
    (5)
    """

    # 건설기준문서내용(text)
    content = """
    ####(5) 결함부의 보수설계에서 마무리를 지정하지 않은 그루브용접을 하는 경우는 표 3.2-8에 표시한 범위 내의 더돋기는 용접한 대로 두어도 좋다. 다만, 더돋기가 표 3.2-8의 값을 초과 할 때는 비드 형상의 끝부분(지단)을 매끄럽게 마무리 하여야 한다.
    표 3.2-8 그루브용접의 더돋기(mm)
    \begin{table}[]
    \begin{tabular}{ll}
    비드폭(B)                                                                & 더돋기 높이(h)                                                         \\
    \begin{tabular}[c]{@{}l@{}}B ＜ 15\\ 15 ≤ B ＜ 25\\ B ≥ 25\end{tabular} & \begin{tabular}[c]{@{}l@{}}h ≤ 3\\ h ≤ 4\\ h ≤ 4B/25\end{tabular}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 그루브용접의 더돋기];
    B["KCS 24 30 00 3.2.3 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.2.3 (45)"])

    subgraph Variable_def
    VarOut[/출력변수: 그루브용접의 더돋기/];
    VarIn0[/입력변수: 설계에서 마무리를 지정/];
    VarIn1[/입력변수: 비드폭/];
    VarIn2[/입력변수: 더돋기 높이/];
    VarOut ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> CC{설계에서 마무리를 지정}
    CC --> |False|C{"비드폭"}
    C --> |"비드폭 ＜ 15"|D{"더돋기 높이 ≤ 3"}
    C --> |"15 ≤ 비드폭 ＜ 25"|E{"더돋기 높이 ≤ 4"}
    C --> |"비드폭 ≥ 25"|F{"더돋기 높이 ≤ 4*비드폭/25"}
    D & F & E --> |True|H[용접한 대로 두어도 좋다]
    D & F & E --> |False|I["비드 형상의 끝부분(지단)을 \n 매끄럽게 마무리 하여야 한다"]
    CC --> |True|J["설계에서 지정한 마무대로 시공한다"]
    H & I & J --> End([그루브용접의 더돋기])
    """

    @rule_method
    def groove_weld(bIFinDes,fIB,fIH)-> str:
        """
        Args:
            bIFinDes (boolean): 설계에서 마무리를 지정
            fIB (float): 비드폭
            fIH (float): 더돋기 높이
        Returns:
            sOReiGro (string): 그루브용접의 더돋기
        """
        if bIFinDes == False:
            if fIB <15:
                if fIH <=3:
                    sOReiGro = "Pass"
                else:
                    sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리 하여야 한다."
            elif fIB <25:
                if fIH <=4:
                    sOReiGro = "Pass"
                else:
                    sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리 하여야 한다."
            else:
                if fIH <= fIB*4/25:
                    sOReiGro = "Pass"
                else:
                    sOReiGro = "비드 형상의 끝부분(지단)을 매끄럽게 마무리 하여야 한다."
        else:
            sOReiGro = "설계에서 지정한대로 마무리 시공한다"
        return sOReiGro