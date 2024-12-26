import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030402_05(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.4.2 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-06'
    title = '건축구조물의 철근 관통구멍의 지름'

    description = """
    제작
    3. 시공
    3.4 구멍뚫기
    3.4.2 볼트 구멍의 치수 및 정밀도
    (5)
    """

    content = """
    #### 3.4.2 볼트 구멍의 치수 및 정밀도
    (5) 건축구조물의 철근 관통구멍의 지름은 해당 공사시방서에 따른다. 해당 공사시방서에 정한 바가 없는 경우에는 표 3.4-2에 명시한 값을 표준으로 한다.
    (단위: mm)
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 호칭} &
      {\color[HTML]{333333} D10} &
      {\color[HTML]{333333} D13} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} D16}} &
      {\color[HTML]{333333} D19} &
      {\color[HTML]{333333} D22} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} D25}} &
      {\color[HTML]{333333} D29} &
      {\color[HTML]{333333} D32} \\
    \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 이형철근}} &
      {\color[HTML]{333333} 구멍직경} &
      {\color[HTML]{333333} 21} &
      {\co  lor[HTML]{333333} 24} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 28}} &
      {\color[HTML]{333333} 31} &
      {\color[HTML]{333333} 35} &
      \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 38}} &
      {\color[HTML]{333333} 43} &
      {\color[HTML]{333333} 46} \\
    {\color[HTML]{333333} 원형철근} &
      {\color[HTML]{333333} 구멍직경} &
      \multicolumn{10}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 철근 직경 + 10 mm}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 건축구조물의 철근 관통구멍의 지름];
    B["KCS 14 31 10 3.4.2 (5)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.4.2 (5)"])

    subgraph Variable_def
    VarOut1[/출력변수: 철근 관통구멍의 지름/];
		VarIn1[/공사시방서/]
    VarIn2[/입력변수: 이형철근/];
    VarIn3[/입력변수: 원형철근/];
    VarIn4[/입력변수: 철근의 호칭/];
    VarIn5[/입력변수: 철근 직경/];
		end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 ~~~ VarIn5 & VarIn4

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> E{"공사시방서"}
		E --> |False|C{"이형철근, 원형철근"}
		C --> |이형철근|D{호칭}
		C --> |원형철근|F[철근직경 + 10]
		D --> |표 3.4-2|G[구멍직경]
		F & G --> End([철근 관통구멍의 지름])
    """

    @rule_method
    def Project_Specification(bIProSpe, bIDefBar, bIPlaBar, sINomBar, fIReiDia) -> float:
        """ 건축구조물의 철근 관통구멍의 지름
        Args:
        bIProSpe (bool): 공사시방서
        bIDefBar (bool): 이형철근
        bIPlaBar (bool): 원형철근
        sINomBar (str): 철근의 호칭
        fIReiDia (float): 철근의 직경

        Returns:
        fODiaThr (float): 철근 관통구멍의 구멍 직경
        """
        assert isinstance(bIProSpe, bool)
        assert isinstance(bIDefBar, bool)
        assert isinstance(bIPlaBar, bool)
        assert bIDefBar != bIPlaBar
        assert isinstance(sINomBar, str)
        assert sINomBar in ["D10", "D13", "D16", "D19", "D22", "D25", "D29", "D32"]
        assert isinstance(fIReiDia, float)

        if bIProSpe == False:
          if bIDefBar == True and bIPlaBar == False:
            if sINomBar == "D10":
              fODiaThr = 21
            elif sINomBar == "D13":
              fODiaThr = 24
            elif sINomBar == "D16":
              fODiaThr = 28
            elif sINomBar == "D19":
              fODiaThr = 31
            elif sINomBar == "D22":
              fODiaThr = 35
            elif sINomBar == "D25":
              fODiaThr = 38
            elif sINomBar == "D29":
              fODiaThr = 43
            elif sINomBar == "D32":
              fODiaThr = 46
              print("호칭을 D10, D13, D16, D19, D22, D25, D29, D32 중 하나로 입력하시오")
          elif bIDefBar == False and bIPlaBar == True:
            fODiaThr = fIReiDia + 10

        return RuleUnitResult(
            result_variables={
                "fODiaThr": fODiaThr
            }
        )