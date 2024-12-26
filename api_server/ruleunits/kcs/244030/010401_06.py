import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244030_010401_06(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 1.4.1 (6)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '점검계단 및 점검통로의 규격'

    description = """
    교량점검시설
    1. 일반사항
    1.4 시스템 설명
    1.4.1 설치기준 및 규격
    (6)
    """

    content = """
    #### 1.4.1 설치기준 및 규격
    (6) 점검계단 및 점검통로의 규격은 표 1.4-1에서 규정한 이상으로 하여야 한다.
\begin{table}[]
\begin{tabular}{lll}
\cline{1-2}
\multicolumn{1}{|l|}{구분}                                               & \multicolumn{1}{l|}{}               & 규격                                                                \\ \cline{1-2}
\rowcolor[HTML]{FFFFFF}
\multicolumn{2}{l}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 점검계단}}                                      & {\color[HTML]{333333} 유효폭: 0.60 m}                                \\
\rowcolor[HTML]{FFFFFF}
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                        & {\color[HTML]{333333} 통로}           & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                   \\
\rowcolor[HTML]{FFFFFF}
\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                        & {\color[HTML]{333333} 난간}           & \cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }                   \\
\rowcolor[HTML]{FFFFFF}
\multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 출입 통로}} & {\color[HTML]{333333} 출입사다리 및 출입계단} & \multirow{-3}{*}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} }}
\end{tabular}
\end{table}
"""

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 점검계단 및 점검통로의 규격"];
    B["KCS 24 40 30 1.4.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 30 1.4.1 (6)"])

    subgraph Variable_def
    VarOut[/"출력변수: 점검계단 및 점검통로의 규격"/];
    VarIn1[/"입력변수: 점검계단"/];
    VarIn2[/입력변수: 통로/];
    VarIn3[/입력변수: 난간/];
    VarIn4[/입력변수: 출입사다리/];
    VarIn5[/입력변수: 출입계단/];

    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"구분"}
		D --> |점검계단|E["유효폭: 0.60 m"]
		D --> |통로|F["유효폭: 0.80 m"]
		D --> |난간|G["유효높이: 1.1 m \n 난간 레일: 3단 \n레일수직간격: 0.3 m"]
		D --> |출입사다리|H["발판폭: 0.50 m, 원형 지지대 내경: 0.60 m \n 경사형 출입계단 발판의 깊이: 130 mm 이상\n경사형 출입계단 발판의 높이: 250 mm 이하\n경사형 출입계단의 각도: 45°내외\n발판과 손잡이에 미끄럼방지 시설 설치\n"]
		D --> |출입계단|H

		E --> I([점검계단 및 점검통로의 규격])
		F --> I
		G --> I
		H --> I

    """

    @rule_method
    def specifications_of_inspection_stairs_and_passage(bIInsSta, bIPas, bIHan, bIAccLad, bIAccSta) -> str :
        """점검계단 및 점검통로의 규격

        Args:
            bIInsSta (bool): 점검계단
            bIPas (bool): 통로
            bIHan (bool): 난간
            bIAccLad (bool): 출입사다리
            bIAccSta (bool): 출입계단

        Returns:
            sOSpeSta (str) : 점검계단 및 점검통로의 규격
        """
        assert isinstance(bIInsSta, bool)
        assert isinstance(bIPas, bool)
        assert isinstance(bIHan, bool)
        assert isinstance(bIAccLad, bool)
        assert isinstance(bIAccSta, bool)
        assert (bIInsSta + bIPas + bIHan + bIAccLad + bIAccSta) == 1

        if bIInsSta == True:
            sOSpeSta = "유효폭: 0.60 m"
        elif bIPas == True:
            sOSpeSta = "유효폭: 0.80 m"
        elif bIHan == True:
            sOSpeSta = "유효높이: 1.1 m / 난간 레일: 3단 / 레일수직간격: 0.3 m"
        elif (bIAccLad == True) or (bIAccSta == True):
            sOSpeSta = "발판폭: 0.50 m / 원형 지지대 내경: 0.60 m / 경사형 출입계단 발판의 깊이: 130 mm 이상 / 경사형 출입계단 발판의 높이: 250 mm 이하 / 경사형 출입계단의 각도: 45°내외 / 발판과 손잡이에 미끄럼방지 시설 설치"

        return RuleUnitResult(
                result_variables = {
                    "sOSpeSta": sOSpeSta,
                }
            )