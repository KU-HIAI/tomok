import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_020302_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 2.3.2 (1)'
    ref_date = '2018-08-30'
    doc_date = '2023-10-31'
    title = '폴리에테르 우레탄의 물리적 성질'

    description = """
    교량받침
    2. 자재
    2.3 포트받침 및 디스크받침
    2.3.2 폴리에테르 우레탄 디스크(polyether urethane disc)
    (1)
    """
    content = """
    #### 2.3.2 폴리에테르 우레탄 디스크(polyether urethane disc)
    (1) 디스크받침에 사용되는 폴리에테르 우레탄 디스크는 폴리에테르 우레탄 혼합물을 성형하여 일체로 제조하여야 한다. 폴리에테르 우레탄의 물리적 성질은 표 2.3-1의 필요조건 중 한 가지를 만족하여야 한다.
    표 2.3-1. 폴리에테르 우레탄
    \begin{table}[]
    \begin{tabular}{cccccc}
    \multicolumn{2}{l}{\multirow{3}{*}{물리적 성질}} & \multicolumn{4}{l}{필요조건}                                                                          \\
    \multicolumn{2}{l}{}                        & \multicolumn{2}{l}{화합물 A}                       & \multicolumn{2}{l}{화합물 B}                       \\
    \multicolumn{2}{l}{}                        & \multicolumn{1}{l}{최소} & \multicolumn{1}{l}{최대} & \multicolumn{1}{l}{최소} & \multicolumn{1}{l}{최대} \\
    \multicolumn{2}{c}{경도(D형 경도)}               & 46                     & 50                     & 60                     & 64                     \\
    \multirow{2}{*}{인장응력(MPa)}    & 신장률 100%    & 10.3                   & -                      & 13.8                   & -                      \\
                                & 신장률 200%    & 19.3                   & -                      & 25.5                   & -                      \\
    \multicolumn{2}{c}{인장강도(MPa)}               & 27.6                   & -                      & 34.5                   & -                      \\
    \multicolumn{2}{c}{극한신장률(%)}                & 350                    & -                      & 220                    & -                      \\
    \multicolumn{2}{c}{영구압축률(%)(70℃에서 22시간)}    & -                      & 40                     & -                      & 40
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 폴리에테르 우레탄의 물리적 성질];
    B["KCS 24 40 05 2.3.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.3.2 (1)"])

    subgraph Variable_def
    VarIn1[/입력변수: D형 경도/];
    VarIn2[/입력변수: 신장률 100%에서 인장응력/];
    VarIn3[/입력변수: 신장률 200%에서 인장응력/];
    VarIn4[/입력변수: 인장강도/];
    VarIn5[/입력변수: 극한신장률/];
    VarIn6[/입력변수: 영구압축률/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~  VarIn4 & VarIn5 & VarIn6
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{D형 경도 \n 신장률 100%에서 인장응력 \n신장률 200%에서 인장응력 \n 인장강도, 극한신장률, 영구압축률\n.}
    D --> E{표 2.3-1}
    E--> End([Pass or Fail])
    """

    @rule_method

    def polyether_urethane(fIHar,fITenElo_1,fITenElo_2,fITenStr,fIUltElo,fIPerCom) -> RuleUnitResult:
        """
        Args:
            fIHar (float): D형 경도
            fITenElo_1 (float): 신장률 100%에서 인장응력
            fITenElo_2 (float): 신장률 200%에서 인장응력
            fITenStr (float): 인장강도
            fIUltElo (float): 극한신장률
            fIPerCom (float): 영구압축률

        Returns:
            pass_fail (bool): 교량받침 2.3.2 폴리에테르 우레탄 디스크(polyether urethane disc) (1)의 판단 결과
        """
        assert isinstance(fIHar, float)
        assert isinstance(fITenElo_1, float)
        assert isinstance(fITenElo_2, float)
        assert isinstance(fITenStr, float)
        assert isinstance(fIUltElo, float)
        assert isinstance(fIPerCom, float)

        if fIHar>=46 and fIHar <=50:
            if fITenElo_1 >=10.3 and fITenElo_2 >=19.3 and fITenStr >=27.6 and fIUltElo >=350 and fIPerCom <=40:
                pass_fail = True
            else:
                pass_fail = False

        elif fIHar >=60 and fIHar<=64:
            if fITenElo_1 >=13.8 and  fITenElo_2 >=25.5 and fITenStr >=34.5 and fIUltElo >=220 and fIPerCom <=40:
                pass_fail = True
            else:
                pass_fail = False
        else:
            pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })