import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS241000_030301(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 10 00 3.3.1'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '철근 배치의 시공 허용오차'


    description = """
    콘크리트교량공사
    3. 시공
    3.3 가설 및 시공 허용오차
    3.3.1 철근 배치의 시공 허용오차
    """
    content = """
    #### 3.3.1 철근 배치의 시공 허용오차
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} 항목}   & {\color[HTML]{333333} 시공허용오차}                                                                                                                                                              \\
    {\color[HTML]{333333} 유효높이} & \cellcolor[HTML]{FFFFFF}{\color[HTML]{000000} \begin{tabular}[c]{@{}l@{}}설계치수의 ±3 % 또는 ±30 mm 중에서 작은 값. 다만, 최소 피복두께는 확보하여야 한다.\\ 바닥판의 경우 설계치수의 ±10 mm로 하고 소요 피복두께를 확보하여야 한다.\end{tabular}}
    \end{tabular}
    \end{table}
    """

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
    VarIn1[/입력변수: 철근배치의 설계값/];
    VarIn2[/입력변수: 철근배치의 시공값/];
    VarIn4[/입력변수: 최소 피복두께/];
    VarIn5[/입력변수: 소요 피복두께/];
    VarIn6[/입력변수: 바닥판의 경우/]
    VarOut ~~~ VarIn1 & VarIn2
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{바닥판의 경우}
    C --> |False|D{"|철근배치의 설계값-철근배치의 시공값| \n <= min(철근배치의 설계값*0.03, 30 mm)"}
    D --> |True|E{"철근배치의 시공값 > = 최소 피복두께"}
    C --> |True|F{"|철근배치의 설계값-철근배치의 시공값| \n <=10 mm"}
    F --> |True|G{"철근배치의 시공값>= 소요 피복두께"}
    E & G--> End([Pass or Fail])
    """

    @rule_method

    def tolerance_reinforcement_layout(fIDesLay, fIConLay, fIMinCle, fIReqCle, bIDec) -> RuleUnitResult:
        """
        Args:
            fIDesLay (float): 철근배치의 설계값
            fIConLay (float): 철근배치의 시공값
            fIMinCle (float): 최소 피복두께
            fIReqCle (float): 소요 피복두께
            bIDec (bool): 바닥판의 경우

        Returns:
            pass_fail (bool): 콘크리트교량공사 3.3.1 철근 배치의 시공 허용오차의 판단 결과
        """
        assert isinstance(fIDesLay, float)
        assert isinstance(fIConLay, float)
        assert isinstance(fIMinCle, float)
        assert isinstance(fIReqCle, float)
        assert isinstance(bIDec, bool)

        if bIDec == False:
            if abs(fIConLay-fIDesLay) <= min(fIDesLay * 0.03, 30) and fIConLay >= fIMinCle:
                pass_fail = True
            else:
                pass_fail = False
        else:
            if abs(fIConLay-fIDesLay) <= 10 and fIConLay >= fIReqCle:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })