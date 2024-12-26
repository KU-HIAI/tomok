import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_020202(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 2.2.2'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '스터드 종류 및 치수'

    description = """
    용접
    2. 자재
    2.2 스터드형 전단연결재
    2.2.2 스터드 종류 및 치수
    """

    content = """
    #### 2.2.2 스터드 종류 및 치수
    합성 구조물에 사용되는 스터드의 지름은 16 mm, 19 mm 및 22 mm를 표준으로 하며, 합성 거더교와 같이 특별히 필요한 경우에는 25 mm를 사용할 수 있다. 형상, 치수 및 허용오차 등은 표 2.2-1을 표준으로 한다.
    표 2.2-1 스터드의 형상, 치수 및 허용오차(단위 : mm)
\begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 줄 기 지 름(d)}} &
  \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 머 리 지 름(D)}} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 호칭}} &
  {\color[HTML]{333333} 기준치수} &
  {\color[HTML]{333333} 허용오차} &
  {\color[HTML]{333333} 기준치수} &
  {\color[HTML]{333333} 허용오차} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}머리두께\\ (T)의 최소치\end{tabular}}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}헌치부\\ 반지름(r)\end{tabular}}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}표준형상 및 치수\\ 표시기호\end{tabular}}} \\
{\color[HTML]{333333} 16} &
  {\color[HTML]{333333} 16.0} &
  {\color[HTML]{333333} ±0.3} &
  {\color[HTML]{333333} 29.0} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
{\color[HTML]{333333} 19} &
  {\color[HTML]{333333} 19.0} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  {\color[HTML]{333333} 32.0} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
{\color[HTML]{333333} 22} &
  {\color[HTML]{333333} 22.0} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  {\color[HTML]{333333} 35.0} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10}} &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } \\
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
  \multirow{-4}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \#}} \\
\multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 25}} &
  \multirow{-4}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ±0.4}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 41.0}} &
  \multirow{-5}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} ±0.4}} &
  \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 12}} &
  \multirow{-5}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 2 이상}} &
  {\color[HTML]{333333} } \\
\multicolumn{8}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주 1) 스터드 길이(L)는 용접 후 스터드 베이스의 모양과 길이를 고려하여 정해야 하며, 허용오차는 ±2.0 mm를 기준으로 함.}}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 개선 절단면 검사];
    B["KCS 14 31 20 2.2.2"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 2.2.2"])

    subgraph Variable_def
    VarOut1[/출력변수: 스터드의 형상, 치수 및 허용오차/];
    VarIn1[/입력변수: 줄기지름 기준/];
    VarIn2[/입력변수: 줄기지름 허용오차/];
    VarIn3[/입력변수: 머리지름 기준/];
    VarIn4[/입력변수: 머리지름 허용오차/];
    VarIn5[/입력변수: 머리두께의 최소/];
    VarIn6[/입력변수: 헌치부 반지름/];
    VarIn7[/입력변수: 호칭/];
		VarOut1 & VarIn1 & VarIn2 & VarIn3
		~~~ VarIn4
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> G{스터드의 지름 \n 줄기지름 기준 \n 줄기지름 허용오차 \n 머리지름 기준\n 머리지름 허용오차 \n 호칭 \n 헌치부 반지름\n 머리두께의 최소 \n}
		G --> |표 2.2-1|H[스터드의 형상, 치수 및 허용오차]
		H --> End([스터드의 형상, 치수 및 허용오차])
    """

    @rule_method
    def Standard_of_Stem_Diameter(bIStdSte, bITolSte, bIStdHea, bITolHea, bIMinHea, bIRadHau, nINom) -> str:
        """ 스터드의 종류 및 치수
        Args:
        bIStdSte (bool): 줄기지름 기준
        bITolSte (bool): 줄기지름 허용오차
        bIStdHea (bool): 머리지름 기준
        bITolHea (bool): 머리지름 허용오차
        bIMinHea (bool): 머리두께의 최소
        bIRadHau (bool): 헌치부 반지름
        nINom (int): 호칭

        Returns:
        sOTolStu (str): 스터드의 형상, 치수 및 허용오차
        """
        assert isinstance(bIStdSte, bool)
        assert isinstance(bITolSte, bool)
        assert isinstance(bIStdHea, bool)
        assert isinstance(bITolHea, bool)
        assert isinstance(bIMinHea, bool)
        assert isinstance(bIRadHau, bool)
        assert (bIStdSte + bITolSte + bIStdHea + bITolHea + bIMinHea + bIRadHau) == 1
        assert isinstance(nINom, int)
        assert nINom in[16, 19, 22, 25]

        if bIStdSte == True:
          if nINom == 16:
            sOTolStu = "16.0"
          elif nINom == 19:
            sOTolStu = "19.0"
          elif nINom == 22:
            sOTolStu = "22.0"
          elif nINom == 25:
            sOTolStu = "25.0"

        elif bITolSte == True:
          if nINom == 16:
            sOTolStu = "±0.3"
          elif nINom == 19 or 22 or 25:
            sOTolStu = "±0.4"

        elif bIStdHea == True:
          if nINom == 16:
            sOTolStu = "29.0"
          elif nINom == 19:
            sOTolStu = "32.0"
          elif nINom == 22:
            sOTolStu = "35.0"
          elif nINom == 25:
            sOTolStu = "41.0"

        elif bIStdSte == bITolHea == True:
          sOTolStu = "±0.4"

        elif bIStdSte == bIMinHea == True:
          if nINom == 16 or 19 or 22:
            sOTolStu = "10"
          elif nINom == 25:
            sOTolStu = "12"

        elif bIStdSte == bIRadHau == True:
          sOTolStu = "2 이상"

        return RuleUnitResult(
                result_variables = {
                    "sOTolStu": sOTolStu
                }
            )