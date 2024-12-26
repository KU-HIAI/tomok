import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030803_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.8.3 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '볼트구멍의 관통률 및 정지율'

    description = """
    제작
    3. 시공
    3.8 토목구조물의 가조립(품질관리 구분'라')
    3.8.3 가조립 부재 연결
    (2)
    """

    content = """
    #### 3.8.3 가조립 부재 연결
    (2) 볼트구멍의 관통률 및 정지율은 표 3.8-1에 따르며 가조립용 볼트시공은 KCS 14 31 25의 해당요건에 따른다.
    표 3.8-1 볼트구멍의 관통률 및 정지율
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} 구분} &
      {\color[HTML]{333333} 볼트의 지름} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}관통게이지\\ (mm)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}관통률 \\ (\%)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}정지게이지\\ (mm)\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}정지율\\ (\%)\end{tabular}} \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 16} &
      {\color[HTML]{333333} 17.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 19.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 20} &
      {\color[HTML]{333333} 21.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 23.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 22} &
      {\color[HTML]{333333} 23.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 25.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 24} &
      {\color[HTML]{333333} 25.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 27.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 27} &
      {\color[HTML]{333333} 27.7} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 30.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \multirow{-6}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}마찰\\ 접합\end{tabular}}} &
      {\color[HTML]{333333} M 30} &
      {\color[HTML]{333333} 30.7} &
      \multirow{-6}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}} &
      {\color[HTML]{333333} 33.3} &
      \multirow{-6}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 80 이상}} \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 8} &
      {\color[HTML]{333333} 9.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 11.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 10} &
      {\color[HTML]{333333} 11.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 13.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 12} &
      {\color[HTML]{333333} 13.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 15.0} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 16} &
      {\color[HTML]{333333} 17.0 (16.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 19.0 (18.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 20} &
      {\color[HTML]{333333} 21.0 (20.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 23.0 (22.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 22} &
      {\color[HTML]{333333} 23.0 (22.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 25.0 (24.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 24} &
      {\color[HTML]{333333} 25.0 (24.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 27.0 (26.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} M 27} &
      {\color[HTML]{333333} 27.7(27.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 30.0 (29.0)1)} &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
    \multirow{-9}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}지압\\ 접합\end{tabular}}} &
      {\color[HTML]{333333} M 30} &
      {\color[HTML]{333333} 30.7(30.0)1)} &
      \multirow{-9}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 100}} &
      {\color[HTML]{333333} 33.0 (32.0)1)} &
      \multirow{-9}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 80 이상}} \\
    \multicolumn{6}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) (  ) 안의 수치는 공사용 거더 등 주요부재에 일반볼트를 지압접합으로 사용한 경우다. 이 경우 일반볼트의 볼트품질은 KS B 5221에 따르며, 8g/7H로 한다.\\    2) 마찰접합과 지압접합에는 고장력볼트를 사용할 수 있다. 이 경우 고장력볼트의 볼트품질은 KS B 5221에 따르며, 6g/6H로 한다.\end{tabular}}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 볼트구멍의 관통률 및 정지율];
    B["KCS 14 31 10 3.8.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.8.3 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 볼트구멍의 관통률 및 정지율/];
    VarIn1[/입력변수: 관통률/];
    VarIn2[/입력변수: 정지율/];
		VarOut1 ~~~ VarIn1 & VarIn2
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"관통률\n정지율"}
    C --> |"관통률"|D["100%"]
    C --> |"정지율"|E["80%"]
		D & E --> End([볼트구멍의 관통률 및 정지율])
    """

    @rule_method
    def Through_Rate(bIThrRat, bIStoRat) -> str:
        """ 볼트구멍의 관통률 및 정지율
        Args:
        bIThrRat (bool): 관통률
        bIStoRat (bool): 정지율

        Returns:
        sOThrRat (str): 볼트구멍의 관통률 및 정지율
        """
        assert isinstance(bIThrRat, bool)
        assert isinstance(bIStoRat, bool)
        assert bIThrRat != bIStoRat

        if bIThrRat == True and bIStoRat == False:
          sOThrRat = "100%"
        elif bIThrRat == False and bIStoRat == True:
          sOThrRat = "80% 이상"

        return RuleUnitResult(
            result_variables={
                "sOThrRat": sOThrRat
            }
        )