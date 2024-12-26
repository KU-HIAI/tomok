import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS216015_0303_07(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 60 15 3.3 (7)'
    ref_date = '2022-02-23'
    doc_date = '2023-11-15'
    title = '발판의 고정과 미끄럼막이의 설치'

    description = """
    작업발판 및 통로
    3. 시공
    3.3 경사로
    (7)
    """

    content = """
    #### 3.3. 경사로
    (7) 경사각은 30°이하이어야 하며, 미끄럼막이를 일정한 간격으로 설치하여야 한다. 미끄럼막이로 목재를 사용하는 경우의 간격은 다음 표 3.3-1에 따른다.
    \begin{table}[]
    \begin{tabular}{cccc}
    \hline
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 경사각} & {\color[HTML]{333333} 미끄럼막이 간격} & {\color[HTML]{333333} 경사각} & {\color[HTML]{333333} 미끄럼막이 간격} \\ \hline
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 30°} & {\color[HTML]{333333} 300mm}    & {\color[HTML]{333333} 22°} & {\color[HTML]{333333} 400mm}    \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 29°} & {\color[HTML]{333333} 330mm}    & {\color[HTML]{333333} 19°} & {\color[HTML]{333333} 430mm}    \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 27°} & {\color[HTML]{333333} 350mm}    & {\color[HTML]{333333} 17°} & {\color[HTML]{333333} 450mm}    \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 24°} & {\color[HTML]{333333} 370mm}    & {\color[HTML]{333333} 14°} & {\color[HTML]{333333} 470mm}    \\
    \multicolumn{1}{l}{}       & \multicolumn{1}{l}{}            & \multicolumn{1}{l}{}       & \multicolumn{1}{l}{}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 경사로 경사각과 미끄럼막이의 간격];
    B["KCS 21 60 15 3.3 (7)"];
    B ~~~ A
    end

    KCS(["KCS 21 60 15 3.3 (7)"])

    subgraph Variable_def
    VarOut[/출력변수: 미끄럼막이의 간격/];
    VarIn[/입력변수: 경사로 경사각/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"경사로 경사각 <= 30°"}
    C1 --> C2{"KCS 21 60 15 3.3 표 3.3-1"}
    C1 --> D1([Pass or Fail])
    C2 --> |경사각을 고려|D3["미끄럼막이의 간격"]
    D3 --> E2(["미끄럼막이의 간격"])
    """

    @rule_method
    def Slope_Angle_of_Ramp(fIAngRam) -> bool:
        """ 발판의 고정과 미끄럼막이의 설치
        Args:
            fIAngRam (float): 경사로 경사각

        Returns:
            pass_fail (bool): 작업 발판 및 통로 3.3 경사로 (7)의 판단 결과
            fOGapAnt (float): 미끄럼막이의 간격
        """
        assert isinstance(fIAngRam, float)
        assert fIAngRam in [30, 29, 27, 24, 22, 19, 17, 14]

        if fIAngRam <= 30:
          pass_fail = True
          if fIAngRam == 30:
            fOGapAnt = 300
          elif fIAngRam == 29:
            fOGapAnt = 330
          elif fIAngRam == 27:
            fOGapAnt = 350
          elif fIAngRam == 24:
            fOGapAnt = 370
          elif fIAngRam == 22:
            fOGapAnt = 400
          elif fIAngRam == 19:
            fOGapAnt = 430
          elif fIAngRam == 17:
            fOGapAnt = 450
          elif fIAngRam == 14:
            fOGapAnt = 470
        else:
          pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "fOGapAnt": fOGapAnt,
                    "pass_fail": pass_fail,
                }
            )