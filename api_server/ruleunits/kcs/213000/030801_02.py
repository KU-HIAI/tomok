import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS213000_030801_02(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 21 30 00 3.8.1 (2)'
    ref_date = '2022-02-23'
    doc_date = '2023-09-25'
    title = '천공 및 주입 제원'

    description = """
    가설흙막이 공사
    3. 시공
    3.8 그라우팅
    3.8.1 JSP(Jumno Special Pile) 공법
    (2)
    """

    content = """
    #### 3.8.1. JSP(Jumno Special Pile) 공법
    (2) 천공 및 주입
    ① 천공 및 주입의 지층별 제원은 표 3.8-1을 기준으로 실시한다.
    표 3.8-1
    \begin{table}[]
    \begin{tabular}{llllllll}
    \multirow{2}{*}{구분} & \multicolumn{2}{l}{점토층} & \multicolumn{3}{l}{모래층}     & \multirow{2}{*}{자갈층} & \multirow{2}{*}{호박돌층} \\
                        & N=0∼2      & N=3∼5      & N=0∼4   & N=5∼15  & N=16∼30 &                      &                       \\
    유효지름(m)             & 1.0        & 0.8        & 1.2     & 1.0     & 0.8     & 0.8                  & 0.8                   \\
    롯드인발속도(분/m)         & 7          & 8          & 7       & 8       & 9       & 9                    & 9                     \\
    단위분사량(ℓ/min)        & 60         & 60         & 60      & 60      & 60      & 60                   & 60                    \\
    분사량(ℓ/m)            & 462        & 528        & 462     & 528     & 594     & 594                  & 594                   \\
    시멘트량(kg)            & 351        & 401        & 351     & 401     & 451     & 451                  & 451                   \\
    물(ℓ)                & 351        & 401        & 351     & 401     & 451     & 451                  & 451                   \\
    굴착공 간격(m)           & 0.8∼0.9    & 0.6∼0.7    & 1.0∼1.1 & 0.8∼0.9 & 0.6∼0.7 & 0.6∼0.7              & 0.6∼0.7
    \end{tabular}
    \end{table}
    ② 공삭공에 사용하는 공사용수는 청수 또는 이수에 관계없이 압력이 4MPa 이하이어야 한다.
    ⑤ 시멘트 밀크의 분사량은 (60±5)/min를 기준으로 한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 천공 및 주입 제원];
    B["KCS 21 30 00 3.8.1 (2)"];
    B ~~~ A
    end

    KCS(["KCS 21 30 00 3.8.1 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 유효지름/]; VarOut2[/출력변수: 롯드인발속도/];
    VarOut3[/출력변수: 단위분사량/]; VarOut4[/출력변수: 분사량/];
    VarOut5[/출력변수: 시멘트량/]; VarOut6[/출력변수: 물/];
    VarOut7[/출력변수: 굴착공 간격/]; VarIn1[/입력변수: 지층의 종류/];
    VarIn2[/입력변수: N치/]; VarIn3[/입력변수: 공사용수의 압력/];
		VarIn4[/입력변수: 시멘트 밀크의 분사량/]; VarIn5[/입력변수: 토출압/];
    end
		VarOut1 & VarOut2 & VarOut3 & VarOut4 ~~~
		VarOut5 & VarOut6 & VarOut7 & VarIn1 ~~~ VarIn2

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C1{"KCS 21 30 00 3.8 표 3.8-1"}
    Variable_def --> C2{"공사용수의 압력 >= 4MPa"}
    Variable_def --> C3{"55l/min <= 시멘트 밀크의 분사량 <= 65l/min"}
    Variable_def --> C4{"19MPa <= 토출압 <= 21MPa"}
    C1 --> |지층의 종류, N치 고려|D1["유효지름"]
    C1 --> |지층의 종류, N치 고려|D2["롯드인발속도"]
    C1 --> |지층의 종류, N치 고려|D3["단위분사량"]
    C1 --> |지층의 종류, N치 고려|D4["분사량"]
    C1 --> |지층의 종류, N치 고려|D5["시멘트량"]
    C1 --> |지층의 종류, N치 고려|D6["물"]
    C1 --> |지층의 종류, N치 고려|D7["굴착공 간격"]

    D1 & D2 & D3 & D4 & D5 & D6 & D7--> E1(["천공 및 주입의 지층별 제원"])
    C2 & C3 & C4 --> E2([Pass or Fail])
    """

    @rule_method
    def Type_of_Soil(sITypSoi, nINVal, fIPreWat, fIInjMil, fIDisPre) -> str:
        """ 천공 및 주입 제원
        Args:
            sITypSoi (str): 지층의 종류
            nINVal (int): N치
            fIPreWat (float): 공사용수의 압력
            fIInjMil (float): 시멘트 밀크의 분사량
            fIDisPre (float): 토출압

        Returns:
            pass_fail (bool): 가설흙막이 공사 3.8.1 JSP(Jumno Special Pile) 공법 (2)의 판단 결과
            fOEffDia (float): 유효지름
            fODraSpe (float): 롯드인발속도
            fOUniInj (float): 단위분사량
            fOInjRat (float): 분사량
            fOAmoCem (float): 시멘트량
            fOWat (float): 물
            sOSpaExc (str): 굴착공 간격
        """
        assert isinstance(sITypSoi, str)
        assert sITypSoi in["점토층", "모래층", "자갈층", "호박돌층"]
        assert isinstance(nINVal, int)
        assert 0 <= nINVal <= 30
        assert isinstance(fIPreWat, float)
        assert isinstance(fIInjMil, float)
        assert isinstance(fIDisPre, float)

        if fIPreWat <= 4 and 55 <= fIInjMil <= 65 and 19 <= fIDisPre <= 21:
          pass_fail = True
        else:
          pass_fail = False

        if sITypSoi == "점토층":
          if 0 <= nINVal <= 2:
            fOEffDia = 1; fODraSpe = 7; fOUniInj = 60; fOInjRat = 462; fOAmoCem = 351; fOWat = 351; sOSpaExc = "0.8~0.9m"
          elif 3 <= nINVal <= 5:
            fOEffDia = 0.8; fODraSpe = 8; fOUniInj = 60; fOInjRat = 528; fOAmoCem = 401; fOWat = 401; sOSpaExc = "0.6~0.7m"

        elif sITypSoi == "모래층":
          if 0 <= nINVal <= 4:
            fOEffDia = 1.2; fODraSpe = 7; fOUniInj = 60; fOInjRat = 462; fOAmoCem = 351; fOWat = 351; sOSpaExc = "1.0~1.1m"
          elif 5 <= nINVal <= 15:
            fOEffDia = 1; fODraSpe = 8; fOUniInj = 60; fOInjRat = 528; fOAmoCem = 401; fOWat = 401; sOSpaExc = "0.8~0.9m"
          elif 16 <= nINVal <= 30:
            fOEffDia = 0.8; fODraSpe = 9; fOUniInj = 60; fOInjRat = 594; fOAmoCem = 451; fOWat = 451; sOSpaExc = "0.6~0.7m"

        elif sITypSoi == "자갈층":
          fOEffDia = 0.8; fODraSpe = 9; fOUniInj = 60; fOInjRat = 594; fOAmoCem = 451; fOWat = 451; sOSpaExc = "0.6~0.7m"

        elif sITypSoi == "호박돌층":
          fOEffDia = 0.8; fODraSpe = 9; fOUniInj = 60; fOInjRat = 594; fOAmoCem = 451; fOWat = 451; sOSpaExc = "0.6~0.7m"

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "fOEffDia": fOEffDia,
                    "fODraSpe": fODraSpe,
                    "fOUniInj": fOUniInj,
                    "fOInjRat": fOInjRat,
                    "fOAmoCem": fOAmoCem,
                    "fOWat": fOWat,
                    "sOSpaExc": sOSpaExc,
                }
            )