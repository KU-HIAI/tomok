import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_020604_04(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 2.6.4 (4)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '채움재를 넣은 PTFE판의 성질'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    2. 자재
    2.6.1 받침의 구성부품
    2.6.4 받침용 PTFE판
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### (4) 채움재를 넣은 PTFE판은 활성이 없는 채움재와 균일하게 혼합된 신생의 PTFE 수지로 만들어야 한다. 유리섬유나 탄소 등의 채움재를 넣은 PTFE판은 표 2.6-1의 요구사항을 만족하여야 한다.
    \begin{table}[]
    \begin{tabular}{ccccc}
    \multicolumn{2}{l}{구분}                                                     & \multicolumn{1}{l}{순수 불소수지판} & \multicolumn{1}{l}{15% 유리섬유} & \multicolumn{1}{l}{25% 탄소} \\
    \multirow{2}{*}{역학적} & \begin{tabular}[c]{@{}c@{}}인장강도\\ (최소)\end{tabular} & 17.2MPa                      & 14.0MPa                      & 9.0MPa                     \\
                        & 신장율(최소)                                             & 200%                         & 150%                         & 75%                        \\
    \multirow{2}{*}{물리적} & 비중(최소)                                              & 2.10 ∼ 2.23                  & 2.20 이상                      & 2.10 이상                    \\
                        & 녹는점                                                 & 327℃±10℃                     & 327℃±10℃                     & 327℃±10℃
    \end{tabular}
    \end{table}
    표 2.6-1 채움재를 넣은 PTFE판
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 채움재를 넣은 PTFE판의 성질];
    B["KCS 24 40 05 2.6.4 (4)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 2.6.4 (4)"])

    subgraph Variable_def
    VarOut[/출력변수: 채움재를 넣은 PTFE판의 성질/];
    VarIn1[/입력변수: 활성이 없는 채움재/];
    VarIn2[/입력변수: 균일하게 혼합된 신생의 PTFE 수지/];
    VarIn3[/입력변수: 채움재의 종류/];
    VarIn4[/입력변수: 인장강도/];
    VarIn5[/입력변수: 신장율/];
    VarIn6[/입력변수: 비중/];
    VarIn7[/입력변수: 녹는점/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> M{활성이 없는 채움재 \n & \n 균일하게 혼합된 신생의 PTFE 수지\n.}
    M --> |Flase|F(["Fail"])
    M --> |True|G{채움재의 종류\n 인장강도 \n 신장율, 비중, 녹는점\n .}
    G --> H{표 2.6-1}
    H --> |True|Pass(["Pass"])
    H--> |False|F(["False"])
    """

    @rule_method
    def PTFE_with_backfill(bIInaBac,bINewUni,sIBacTyp,fITenStr,fIElo,fISpeGra,fIMelPoi)->str:
        """
        Args:
            bIInaBac (boolean): 활성이 없는 채움재
            bINewUni (boolean): 균일하게 혼합된 신생의 PTFE 수지
            sIBacTyp (string): 채움재의 종류
            fITenStr (float): 인장강도
            fIElo (float): 신장율
            fISpeGra (float): 비중
            fIMelPoi (float): 녹는점
        Returns:
            sOProBac (string): 채움재를 넣은 PTFE판의 성질
        """
        if bIInaBac ==True and bINewUni == True:
            if sIBacTyp == "순수 불소수지판":
                if fITenStr >= 17.2 and fIElo >= 200:
                    if fISpeGra >=2.10 and fISpeGra <=2.23:
                        if fIMelPoi >=317 and fIMelPoi <=337:
                            sOProBac = "Pass"
                        else:
                            sOProBac = "Fail"
                    else:
                        sOProBac = "Fail"
                else:
                    sOProBac = "Fail"
            elif sIBacTyp == '15% 유리섬유':
                if fITenStr >= 14.0 and fIElo >= 150 and fISpeGra >=2.20:
                    if fIMelPoi >=317 and fIMelPoi <=337:
                        sOProBac = "Pass"
                    else:
                        sOProBac = "Fail"
                else:
                    sOProBac = "Fail"
            elif sIBacTyp == '25% 탄소':
                if fITenStr >= 9.0 and fIElo >= 75 and fISpeGra >=2.10:
                    if fIMelPoi >=317 and fIMelPoi <=337:
                        sOProBac = "Pass"
                    else:
                        sOProBac = "Fail"
                else:
                    sOProBac = "Fail"
            else:
                return "순수 불소수지판, 15% 유리섬유, 25% 탄소 중에서 선택하세요"
        else:
            sOProBac = "Fail"
        return sOProBac