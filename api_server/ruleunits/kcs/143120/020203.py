import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_020203(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 2.2.3'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '스터드의 기계적 성질'

    description = """
    용접
    2. 재료
    2.2 스터드형 전단연결재
    2.2.3 스터드 기계적 성질
    """

    content = """
    #### 2.2.3 스터드 기계적 성질
    스터드의 재질 요구사항 중 기계적 성질은 표 2.2-2에 따른다.
    표 2.2-2 스터드의 기계적 성질
\begin{table}[]
\begin{tabular}{
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l }
{\color[HTML]{333333} 종류}  & {\color[HTML]{333333} 항복강도 또는 0.2\% 내력(MPa)} & {\color[HTML]{333333} 인장강도(MPa)}    & {\color[HTML]{333333} 연신율 (\%)} \\
{\color[HTML]{333333} HS1} & {\color[HTML]{333333} 235 이상}                & {\color[HTML]{333333} 400$\sim$550} & {\color[HTML]{333333} 20 이상}    \\
{\color[HTML]{333333} HS2} & {\color[HTML]{333333} 350 이상}                & {\color[HTML]{333333} 500$\sim$650} & {\color[HTML]{333333} 17 이상}
\end{tabular}
\end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스터드의 기계적 성질];
    B["KCS 14 31 20 2.2.3"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 2.2.3"])

    subgraph Variable_def
    VarOut1[/출력변수: 스터드의 기계적 성질/];
    VarIn1[/입력변수: 항복강도 또는 0.2% 내력/];
    VarIn2[/입력변수: 인장강도/];
    VarIn3[/입력변수: 연신율/];
    VarIn4[/입력변수: 스터드의 종류/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end


    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{항복강도 또는 0.2% 내력 \n 인장강도 \n 연신율 \n 스터드의 종류 \n.}
		C --> |표 2.2-2|D[스터드의 기계적 성질]
		D --> End([스터드의 기계적 성질])
    """

    @rule_method
    def Tensile_Strength(bIYieBea, bITenStr, bIEloRat, bITypStu) -> RuleUnitResult:
        """ 스터드의 기계적 성질
        Args:
        bIYieBea (bool): 항복강도 또는 0.2% 내력
        bITenStr (bool): 인장강도
        bIEloRat (bool): 연신율
        bITypStu (bool): 스터드의 종류

        Returns:
        sOProStu (str): 스터드의 기계적 성질
        """
        assert isinstance(bIYieBea, bool)
        assert isinstance(bITenStr, bool)
        assert isinstance(bIEloRat, bool)
        assert isinstance(bITypStu, bool)
        assert (bITenStr + bIEloRat + bIYieBea) == 1

        if bITypStu == True:
          if bIYieBea == True:
            sOProStu = "항복강도 또는 0.2% 내력(MPA)은 235 이상"
          elif bITenStr == True:
            sOProStu = "인장강도(MPa)는 400~550"
          elif bIEloRat == True:
            sOProStu = "연신율(%)은 20 이상"

        elif bITypStu == False:
          if bIYieBea == True:
            sOProStu = "항복강도 또는 0.2% 내력(MPA)은 350 이상"
          elif bITenStr == True:
            sOProStu = "인장강도(MPa)는 500~650"
          elif bIEloRat == True:
            sOProStu = "연신율(%)은 17 이상"

        return RuleUnitResult(
                result_variables = {
                    "sOProStu": sOProStu
                }
            )