import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143110_030304_02_04(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 10 3.3.4 (2) ④'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '절단면 검사 및 결함보수'

    description = """
    제작
    3. 시공
    3.3 절단 및 개선(그루브)가공
    3.3.4 절단면 검사 및 결함보수
    (2)
    ④
    """

    content = """
    #### 3.3.4 절단면 검사 및 결함보수
    (2) 절단면 검사 및 결함보수
    ④ 절단면의 결함 허용오차 및 보수는 표 3.3-2에 준한다.
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    {\color[HTML]{333333} 결함의 길이1)} &
      {\color[HTML]{333333} 보수 방법2)} \\
    {\color[HTML]{333333} 길이 25 mm 이하의 결함} &
      {\color[HTML]{333333} 불필요, 조사 불필요} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 최대깊이 3 mm 이하의 결함\end{tabular}} &
      {\color[HTML]{333333} 불필요, 깊이는 조사} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 3 mm$\sim$6 mm 결함\end{tabular}} &
      {\color[HTML]{333333} 제거, 용접할 필요는 없음} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 6 mm$\sim$25 mm인 결함\end{tabular}} &
      {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}완전하게 제거후 용접\\  용접부의 총길이는 보수하는 부재단부 길이의 20\% 이하\end{tabular}} \\
    {\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}길이 25 mm 초과\\ 깊이 25 mm 초과하는 결함\end{tabular}} &
     {\color[HTML]{333333} 4.3.4의 ⑧에 의하여 보수} \\
    \multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 결함의 길이는 강재 절단면의 긴 변(주된 응력 방향)의 치수이며 결함의 깊이는 절단면에서 강재방향으로 연장된 불연속거리이다.\\ 2) 품질저하가 우려되는 산소절단면의 불연속 10\%에 대해 깊이를 결정하기 위해서 절단면을 그라인딩하여 무작위 추출조사를 실시해야 한다. 이때 조사된 결함 중 하나라도그 깊이가 3 mm를 초과하면 절단면의 나머지 부분도 깊이를 결정하기 위해 절단면을 그라인딩한 후 조사해야 한다. 만약 10\% 무작위 추출조사 때 어떠한 결함도 그 깊이가 3 mm를 초과하지 않을 경우 절단면의 나머지 부분은 조사할 필요가 없다.\end{tabular}}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 절단면 검사 및 결함보수];
    B["KCS 14 31 10 3.3.4 (2) ④"];
    B ~~~ A
    end

    KCS(["KCS 14 31 10 3.3.4 (2) ④"])

    subgraph Variable_def
    VarOut4[/출력변수: 절단면의 결함 허용오차 및 보수방법/];
    VarIn41[/입력변수: 결함 길이/];
    VarIn42[/입력변수: 결함 깊이/];
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> E{결함의 깊이, 결함의 길이}
		E --> |"결함의 길이 ≤ 25 mm"|Ea[불필요, 조사 불필요]
		E --> |"결함의 길이 > 25 mm \n 결함깊이 ≤ 3 mm"|Eb[불필요, 깊이는 조사]
		E --> |"결함의 길이 > 25 mm \n 3 < 결함깊이 ≤ 6 mm"|Ec[제거, 용접할 필요는 없음]
		E --> |"결함의 길이 > 25 mm \n 6 < 결함깊이 ≤ 25 mm"|Ed[완전하게 제거후 용접 \n  용접부의 총길이는 보수하는 부재단부 길이의 20% 이하]
		E --> |"결함의 길이 > 25 mm \n  결함깊이 > 25 mm"|H[불연속 보수]
		Ea & Eb & Ec & Ed & H  --> End3([절단면의 결함 허용오차 및 보수방법])
    """

    @rule_method
    def Secondory_Member_of_Bridge(fILenDef, fIDepDef) -> str:
        """ 절단면 검사 및 결함보수
        Args:
        fILenDef (float): 결함 길이
        fIDepDef (float): 결함 깊이

        Returns:
        sORepCut (str): 절단면의 결함 허용오차 및 보수방법
        """

        assert isinstance(fILenDef, float)
        assert isinstance(fIDepDef, float)


        if fILenDef <= 25:
          sORepCut = "불필요, 조사 불필요"
        else:
          if fIDepDef <= 3:
            sORepCut = "불필요, 깊이는 조사"
          elif 3 < fIDepDef <= 6:
            sORepCut = "제거, 용접할 필요는 없음"
          elif 6 < fIDepDef <= 25:
            sORepCut = "완전하게 제거후 용접, 용접부의 총길이는 보수하는 부재단부 길이의 20% 이하"
          elif fIDepDef > 25:
            sORepCut = "4.3.4의 ⑧에 의하여 보수"

        return RuleUnitResult(
           result_variables={
               "sORepCut": sORepCut
           }
        )