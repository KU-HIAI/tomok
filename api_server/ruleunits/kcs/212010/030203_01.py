import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS212010_030203_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 21 20 10 3.2.3 (1)'
    ref_date = '2022-02-23'
    doc_date = '2023-08-16'
    title = '고압선 인근 작업 시 이격거리'

    description = """
    건설지원장비
    3. 시공
    3.2 양중장비
    3.2.3 이동식 크레인
    (1)
    """

    content = """
    #### 3.2.3. 이동식 크레인
    (1) 이동식 크레인의 사용 중 다음 사항을 준수하여야 한다.
    ⑨ 고압선 인근 작업 시 다음 표 3.2-1과 같이 이격거리를 준수하고 작업지휘자를 배치하여야 한다.
    표 3.2-1
    \begin{table}[]
    \begin{tabular}{clll}
    \hline
    \rowcolor[HTML]{FFFFFF}
    \multicolumn{4}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고압선 인근 작업 시 이격거리}}                                                                                                                                                                                                 \\ \hline
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 0kV ∼ 50kV}    & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 3.0m 이상}} & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 350kV ∼ 500kV}}  & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 7.5m 이상}}  \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 50kV ∼ 200kV}  & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 4.5m 이상}} & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 500kV ∼ 750kV}}  & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 10.0m 이상}} \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 200kV ∼ 350kV} & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 6.0m 이상}} & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 750kV ∼ 1000kV}} & \multicolumn{1}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 12.5m 이상}} \\
    \rowcolor[HTML]{FFFFFF}
    \multicolumn{4}{c}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 고압선 하부 통과 시 이격거리}}                                                                                                                                                                                                 \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 0kV ∼ 50kV}    & {\color[HTML]{333333} 1.2m 이상}                                             & {\color[HTML]{333333} 350kV ∼ 500kV}                                              & {\color[HTML]{333333} 5.7m 이상}                                              \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 50kV ∼ 200kV}  & {\color[HTML]{333333} 2.7m 이상}                                             & {\color[HTML]{333333} 500kV ∼ 750kV}                                              & {\color[HTML]{333333} 8.2m 이상}                                              \\
    \rowcolor[HTML]{FFFFFF}
    {\color[HTML]{333333} 200kV ∼ 350kV} & {\color[HTML]{333333} 4.2m 이상}                                             & {\color[HTML]{333333} 750kV ∼ 1000kV}                                             & {\color[HTML]{333333} 10.7m 이상}                                             \\ \hline
    \multicolumn{1}{l}{}                 &                                                                            &                                                                                   &
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 고압선 인근 작업 시 이격거리];
    B["KCS 21 20 10 3.2.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 21 20 10 3.2.3 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 이격거리/];
    VarIn1[/입력변수: 고압선 전압/];
    VarIn2[/입력변수: 작업 종류/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"고압선 작업 형태"}
    D--> |고압선 인근 작업 시|E1{"고압선 전압"};
    D--> |고압선 하부 통과 시|E2{"고압선 전압"};

    E1--> |"0kV~50kV"|F1["3.0m 이상"];
    E1--> |"50kV~200kV"|F2["4.5m 이상"];
    E1--> |"200kV~350kV"|F3["6.0m 이상"];
    E1--> |"350kV~500kV"|F4["7.5m 이상"];
    E1--> |"500kV~750kV"|F5["10.0m 이상"];
    E1--> |"7500kV~1000kV"|F6["12.5m 이상"];
    E2--> |"0kV~50kV"|F7["1.2m 이상"];
    E2--> |"50kV~200kV"|F8["2.7m 이상"];
    E2--> |"200kV~350kV"|F9["4.2m 이상"];
    E2--> |"350kV~500kV"|F10["5.7m 이상"];
    E2--> |"500kV~750kV"|F11["8.2m 이상"];
    E2--> |"7500kV~1000kV"|F12["10.7m 이상"];
    F1 & F2 & F3  & F4  & F5  & F6 & F7 & F8  & F9  & F10  & F11  & F12--> G(["이격거리"])

    """

    @rule_method
    def Safe_Distance_from_High_voltage_Lines(nIVolHig, sITypTas) -> float:
        """ 고압선 인근 작업 시 이격거리
        Args:
            nIVolHig (int): 고압선 전압
            sITypTas (str): 작업 종류

        Returns:
            fODisHig (float): 이격거리
        """
        assert isinstance(nIVolHig, int)
        assert isinstance(sITypTas, str)
        assert sITypTas in ["고압선 인근 작업", "고압선 하부 통과 작업"]

        if sITypTas == "고압선 인근 작업":
            if 0 <= nIVolHig < 50:
                fODisHig = 3
            elif 50 <= nIVolHig < 200:
                fODisHig = 4.5
            elif 200 <= nIVolHig < 350:
                fODisHig = 6
            elif 350 <= nIVolHig < 500:
                fODisHig = 7.5
            elif 500 <= nIVolHig < 750:
                fODisHig = 10
            elif nIVolHig >= 750:
                fODisHig = 12.5

        elif sITypTas == "고압선 하부 통과 작업":
            if 0 <= nIVolHig < 50:
                fODisHig = 1.2
            elif 50 <= nIVolHig < 200:
                fODisHig = 2.7
            elif 200 <= nIVolHig < 350:
                fODisHig = 4.2
            elif 350 <= nIVolHig < 500:
                fODisHig = 5.7
            elif 500 <= nIVolHig < 750:
                fODisHig = 8.2
            elif nIVolHig >= 750:
                fODisHig = 10.7

        return RuleUnitResult(
                result_variables = {
                    "fODisHig": fODisHig
                }
            )