import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS243000_030201_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 30 00 3.2.1 (5)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '용접시공시험'

    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.1 일반사항
    (5)
    """
    content = """
    #### 3.2.1 일반사항
    (5) 용접시공시험
    ① 다음의 각 항의 어느 것에 해당될 경우에는 용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다. 그러나 동일 조건 또는 그 이상의 조건에서 용접시공시험을 실시하고, 또 시공 경험이 있는 공장에서는 그 당시의 시험보고서를 제출하여 감독자의 승인을 받는 경우는 용접시공시험을 생략할 수 있다.
        가. 강판두께가 50 mm를 초과하는 용접구조용 압연강재(KS D 3515)나 강판두께가 40 mm를 초과하는 내후성 열간압연강재(KS D 3259)의 경우
        나. 강종별로 용접법에 따라 한 패스의 입열량이 표 3.2-2의 최대 입열량을 초과할 경우
        다. 피복아크용접(수용접의 경우만), 가스메탈 아크용접(CO2 가스 혹은 Ar과 CO2의 혼합가스), 서브머지드 아크용접, FCAW 이외의 용접을 할 경우
        라. 이 기준의 요건을 충족시킬 수 있음을 보여주는 사용실적이 없는 공급원이 공급한 재료(모재, 용접봉 또는 와이어, 플럭스)를 사용하는 경우
    ② 용접시공시험을 할 경우에 시험강판의 선정, 용접조건의 선정 등에 대해서는 다음을 고려한다.
        가. 시험강판으로는 같은 용접조건으로 취급하는 강판 중 가장 조건이 나쁜 것을 사용한다.
        나. 용접은 실제의 시공에 사용하는 용접조건으로 하고 용접자세는 실제로 행하는 자세 중 가장 불리한 것으로 한다.
        다. 서로 다른 강재의 그루브 용접시험은 실제의 시공과 동등한 조합의 강재로 실시하며 용접재료는 낮은 강도의 강재 규격을 따른다. 같은 강종으로 판두께가 다른 이음에 대하여는 판두께가 얇은 쪽의 강재로 시험하여도 좋다.
        라. 재시험은 처음 개수의 2배로 한다.
        표 3.2-1 용접시공시험
        \begin{table}[]
        \begin{tabular}{llllll}
        \begin{tabular}[c]{@{}l@{}}시험의\\ 종류\end{tabular}                        & 시험항목                                                      & 시험편의 형상      & \begin{tabular}[c]{@{}l@{}}시험편\\ 개수\end{tabular}   & 시험방법      & 판정기준                                                                              \\
        \multirow{5}{*}{\begin{tabular}[c]{@{}l@{}}그루브 \\ 용접\\ 시험\end{tabular}} & 인장시험                                                      & KS B 0801 1호 & 2                                                  & KS B 0833 & \begin{tabular}[c]{@{}l@{}}인장강도가 모재의 \\ 규격치 이상\end{tabular}                       \\
                                                                                & \begin{tabular}[c]{@{}l@{}}파괴시험\\ (굽힘시험)\end{tabular}     & KS B 0832    & 2                                                  & KS B 0832 & 결함길이 3 ㎜ 이하                                                                       \\
                                                                                & 충격시험주1)                                                   & KS B 0809    & 3                                                  & KS B 0810 & \begin{tabular}[c]{@{}l@{}}용착금속으로 모재의 규격치 이상\\ (3개의 평균치)\end{tabular}             \\
                                                                                & 마크로시험주2)                                                  &              & 2                                                  & KS D 0210 & \begin{tabular}[c]{@{}l@{}}균열 없음. \\ 언더컷 1 ㎜ 이하 \\ 용접치수 확보\end{tabular}           \\
                                                                                & 방사선 투과시험                                                  &              & \begin{tabular}[c]{@{}l@{}}시험편\\ 이음전장\end{tabular} & KS B 0845 & \begin{tabular}[c]{@{}l@{}}2류 이상(인장측)\\ 3류 이상(압축측)\end{tabular}                   \\
        \begin{tabular}[c]{@{}l@{}}필릿용접\\ 시험\end{tabular}                       & 마크로시험                                                     & KS D 0210    & 1                                                  & KS D 0210 & \begin{tabular}[c]{@{}l@{}}균열 없음. \\ 언더컷 1 ㎜ 이하 \\ 용접치수 확보 \\ 루트부 용융\end{tabular} \\
        Y형 용접 균열 시험                                                             & \begin{tabular}[c]{@{}l@{}}Y형 용접 \\ 균열 시험주3)\end{tabular} & KS B 0870    & 1                                                  & KS B 0870 & 균열 없음.                                                                            \\
        \begin{tabular}[c]{@{}l@{}}최고경도\\ 시험\end{tabular}                       & 최고경도시험주4)                                                 & KS B 0811    & 1                                                  & KS B 0811 & Hv ≤ 370                                                                          \\
        \begin{tabular}[c]{@{}l@{}}스터드\\ 용접시험\end{tabular}                      & \begin{tabular}[c]{@{}l@{}}스터드굽힘\\ 시험\end{tabular}        & KS B 0529    & 3                                                  & KS B 0529 & \begin{tabular}[c]{@{}l@{}}용접부에 균열이 \\ 생겨서는 안 된다.\end{tabular}
        \end{tabular}
        \end{table}
        표 3.2-2 강종별 용접법에 따른 한 패스의 최대 입열량
        \begin{table}[]
        \begin{tabular}{lll}
        강종                                                                             & 서브머지드 아크용접     & 가스메탈 아크용접 또는 플럭스코어드 아크용접 \\
        SM490, SM490Y, SMA490, SM520, SM570, SMA570, HSB500W, HSB600W, HSB800, HSB800L & 7,000 Joule/㎜  & 2,500 Joule/㎜            \\
        HSB500, HSB500L, HSB600, HSB600L                                               & 10,000 Joule/㎜ & 3,000 Joule/㎜            \\
        HSB800W                                                                        & 5,000 Joule/㎜  & 2,500 Joule/㎜
        \end{tabular}
        \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 용접시공시험];
    B["KCS 24 30 00 3.2.1 (5)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.2.1 (5)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 용접시공시험/];
    VarIn11[/입력변수: 강판두께/];
    VarIn12[/입력변수: 용접구조용 압연강재/];
    VarIn13[/입력변수: 내후성 열간압연강재/];
    end
    subgraph V2
    VarOut2[/출력변수: 용접시공시험/];
    VarIn21[/입력변수: 패스의 입열량/];
    VarIn22[/입력변수: 강종/];
    VarIn23[/입력변수: 용접법/];
    end
    subgraph V3
    VarOut3[/출력변수: 용접시공시험/];
    VarIn31[/"입력변수: 피복아크용접(수용접의 경우만)"/];
    VarIn32[/"입력변수: 가스메탈 아크용접\n(CO2 가스 혹은 Ar과 CO2의 혼합가스)"/];
    VarIn33[/입력변수: 서브머지드 아크용접/];
    VarIn34[/입력변수: FCAW/];
    end
    subgraph V4
    VarOut4[/출력변수: 용접시공시험/];
    VarIn41[/"입력변수: 기준의 요건을 충족"/];
    VarIn42[/"입력변수: 사용실적이 없는 공급원이 공급한 재료"/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"용접구조용 압연강재\n용접구조용 압연강재"}
    C --> |"용접구조용 압연강재"|D{강판두께 > 50 mm}
    C --> |"용접구조용 압연강재"|E{강판두께 > 40 mm}
    Variable_def --> F{"강종\n용접법\n패스의 입열량"}
    F --> |표 3.2-2|G{최대 입열량 > 패스의 입열량}
    Variable_def --> H{"피복아크용접(수용접의 경우만)\n가스메탈 아크용접\n(CO2 가스 혹은 Ar과 CO2의 혼합가스)\n서브머지드 아크용접\FCAW"}
    Variable_def --> I{"기준의 요건을 충족\n사용실적이 없는 공급원이 공급한 재료"}
    D & E & G & I--> |True|P["용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. \n 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다. \n 그러나 동일 조건 또는 그 이상의 조건에서 용접시공시험을 실시하고,\n 또 시공 경험이 있는 공장에서는 그 당시의 시험보고서를 제출하여 \n 감독자의 승인을 받는 경우는 용접시공시험을 생략할 수 있다."]
    H-->|False|P["용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. \n 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."]
    P --> Q(["용접시공시험"])
    """

    @rule_method

    def welding_test(fISteThi,bIRolWel,bIWeaHot,bIShiArc,bIGasMet,bISubArc,bIFCA,sISteTyp,fIHeaPas,bIMeeReq,bIHisUse) -> RuleUnitResult:
        """
        Args:
            fISteThi (float): 강판두께
            bIRolWel (bool): 용접구조용 압연강재
            bIWeaHot (bool): 내후성 열간압연강재
            bIShiArc (bool): 수용접의 경우 피복아크용접
            bIGasMet (bool): 가스메탈 아크용접
            bISubArc (bool): 서브머지드 아크용접
            bIFCA (bool): 플럭스코어드 아크용접
            sISteTyp (str): 강종
            fIHeaPas (float): 패스의 입열량
            bIMeeReq (bool): 기준의 요건을 충족
            bIHisUse (bool): 사용실적이 없는 공급원이 공급한 재료

        Returns:
            sOWelTes (str): 용접시공시험
        """
        assert isinstance(fISteThi, float)
        assert isinstance(bIRolWel, bool)
        assert isinstance(bIWeaHot, bool)
        assert isinstance(bIShiArc, bool)
        assert isinstance(bIGasMet, bool)
        assert isinstance(bISubArc, bool)
        assert isinstance(bIFCA, bool)
        assert (bIShiArc+bIGasMet+bISubArc+bIFCA) <= 1
        assert isinstance(sISteTyp, str)
        assert sISteTyp in ["SM490", "SM490Y","SMA490", "SM520", "SM570", "SMA570", "HSB500W", "HSB600W", "HSB800", "HSB800L","HSB500", "HSB500L", "HSB600", "HSB600L","HSB800W"]
        assert isinstance(fIHeaPas, float)
        assert isinstance(bIMeeReq, bool)
        assert isinstance(bIHisUse, bool)


        if bIRolWel == True and fISteThi > 50:
            sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
        elif bIWeaHot == True and fISteThi > 40:
            sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."

        elif bISubArc:
            if sISteTyp == "SM490" or sISteTyp == "SM490Y" or sISteTyp == "SMA490" or sISteTyp == "SM520" or sISteTyp == "SM570" or "SMA570" or sISteTyp == "HSB500W" or sISteTyp =="HSB600W" or sISteTyp =="HSB800" or sISteTyp == "HSB800L":
                if fIHeaPas > 7000:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
            elif sISteTyp == "HSB500" or sISteTyp == "HSB500L" or sISteTyp == "HSB600" or sISteTyp == "HSB600L":
                if fIHeaPas > 10000:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
            elif sISteTyp == "HSB800W":
                if fIHeaPas > 5000:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
        elif bIGasMet == True or bIFCA == True:
            if sISteTyp == "SM490" or sISteTyp == "SM490Y" or sISteTyp == "SMA490" or sISteTyp == "SM520" or sISteTyp == "SM570" or "SMA570" or sISteTyp == "HSB500W" or sISteTyp =="HSB600W" or sISteTyp =="HSB800" or sISteTyp == "HSB800L":
                if fIHeaPas > 2500:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
            elif sISteTyp == "HSB500" or sISteTyp == "HSB500L" or sISteTyp == "HSB600" or sISteTyp == "HSB600L":
                if fIHeaPas > 3000:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
            elif sISteTyp == "HSB800W":
                if fIHeaPas > 2500:
                    sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
                else:
                    sOWelTes = None
        elif bIShiArc == False:
            sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
        elif bIHisUse == True and bIMeeReq == True:
            sOWelTes = "용접시공시험을 하고 그 결과를 사전에 감독자에게 승인을 받는다. 용접시공시험은 표 3.2-1에 따르되, 필요에 따라 추가 용접성 시험을 실시할 수 있다."
        else:
            sOWelTes = None

        return RuleUnitResult(
            result_variables = {
                "sOWelTes": sOWelTes,
                })