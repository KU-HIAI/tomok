import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_010502_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 1.5.2 (2)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '용접업무 조정담당자의 기술관련 지식'

    description = """
    용접
    1. 적용범위
    1.5 기술인력
    1.5.2 용접업무 조정담당자
    (2)
    """

    content = """
    #### 1.5.2 용접업무 조정담당자
    (2) 품질관리 구분, 강종, 판의 두께에 따라 요구되는 용접업무 조정담당자의 기술관련 지식의 구분은 표 1.5-1에 따른다.
    표 1.5-1 용접업무 조정담당자의 기술관련 지식 구분
    \begin{table}[]
    \begin{tabular}{
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l
    >{\columncolor[HTML]{FFFFFF}}l }
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      \multicolumn{3}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 판두께 t (mm)}} \\
    \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 품질관리 구분}} &
      \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}강종\\ 항복강도 (MPa)\end{tabular}}} &
      {\color[HTML]{333333} t ≤ 25} &
      {\color[HTML]{333333} 25 \textless t ≤ 50} &
      {\color[HTML]{333333} 50 \textless t} \\
    {\color[HTML]{333333} 가} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} -} &
      {\color[HTML]{333333} -} \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 235$\sim$360} &
      {\color[HTML]{333333} B} &
      {\color[HTML]{333333} S} &
      {\color[HTML]{333333} C} \\
    \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 나}} &
      {\color[HTML]{333333} 420$\sim$460} &
      {\color[HTML]{333333} S} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} \\
    \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} } &
      {\color[HTML]{333333} 235$\sim$360} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} \\
    \multirow{-2}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 다}} &
      {\color[HTML]{333333} 420$\sim$690} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} \\
    {\color[HTML]{333333} 라} &
      {\color[HTML]{333333} 235$\sim$690} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} &
      {\color[HTML]{333333} C} \\
    \multicolumn{5}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 주 1) B(기초적인 기술관련 지식), S(세부적인 기술관련 지식), C(포괄적인 기술관련 지식)}}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접업무 조정담당자의 기술관련 지식];
    B["KCS 14 31 20 1.5.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 1.5.2 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 용접업무 조정담당자의 기술관련 지식/];
    VarIn1[/입력변수: 품질관리 구분/];
    VarIn2[/입력변수: 항복강도/];
    VarIn3[/입력변수: 판의 두께/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{품질관리 구분, 항복강도, 판 두께}
		C --> |표 1.5-1|D["용접업무 조정담당자의 기술관련 지식"]
		D --> End([용접업무 조정담당자의 기술관련 지식])
    """

    @rule_method
    def Yield_Strength(sITypQua, fIYieStr, fIThiPla) -> str:
        """ 용접업무 조정담당자의 기술관련 지식
        Args:
        sITypQua (str): 품질관리 구분
        fIYieStr (float): 항복강도
        fIThiPla (float): 판의 두께

        Returns:
        sOTecKno (str): 용접업무 조정담당자의 기술관련 지식
        """
        assert isinstance(sITypQua, str)
        assert sITypQua in["나", "다", "라"]
        assert isinstance(fIYieStr, float)
        assert 235 <= fIYieStr <= 690
        assert isinstance(fIThiPla, float)

        if sITypQua == "나":
          if 235 <= fIYieStr <= 360:
            if fIThiPla <= 25:
              sOTecKno = "B(기초적인 기술관련 지식)"
            elif 25 < fIThiPla <= 50:
              sOTecKno = "S(세부적인 기술관련 지식)"
            elif fIThiPla > 50:
              sOTecKno = "C(포괄적인 기술관련 지식)"
          elif 420 <= fIYieStr <= 460:
            if fIThiPla <= 25:
              sOTecKno = "S(세부적인 기술관련 지식)"
            elif fIThiPla >= 25:
              sOTecKno = "C(포괄적인 기술관련 지식)"

        elif sITypQua == "다":
          if 235 <= fIYieStr <= 360:
            sOTecKno = "C(포괄적인 기술관련 지식)"
          elif 420 <= fIYieStr <= 690:
            sOTecKno = "C(포괄적인 기술관련 지식)"

        elif sITypQua == "라":
          if 235 <= fIYieStr <= 690:
            sOTecKno = "C(포괄적인 기술관련 지식)"

        return RuleUnitResult(
                result_variables = {
                    "sOTecKno": sOTecKno
                }
            )