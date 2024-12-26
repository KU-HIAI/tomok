import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS241000_030303(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 24 10 00 3.3.3'
    ref_date = '2018-08-30'
    doc_date = '2023-09-25'
    title = '부재치수의 시공 허용오차'

    description = """
    콘크리트교량공사
    3. 시공
    3.3 가설 및 시공 허용오차
    3.3.3 부재치수의 시공 허용오차
    """
    content = """
    #### 3.3.3 부재치수의 시공 허용오차
    부재치수의 시공 허용오차는 표 3.3-3의 값을 표준으로 한다.
    \begin{table}[]
    \begin{tabular}{ll}
    항목           & 시공허용오차                                              \\
    수직부재의 길이치수   & {\color[HTML]{333333} 설계치수의 ±1% 또는 ±30 mm 중에서 작은 값} \\
    수평부재의 길이치수   & {\color[HTML]{333333} 설계치수의 ±1% 또는 ±30 mm 중에서 작은 값} \\
    기둥 및 보의 단면치수 & {\color[HTML]{333333} 설계치수의 ±2% 또는 ±20 mm 중에서 작은 값} \\
    바닥판의 두께      & {\color[HTML]{333333} +20 mm ~ -10 mm}
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 부재치수의 시공 허용오차];
    B["KCS 24 10 00 3.3.3"];
    B ~~~ A
    end

    KCS(["KCS 24 10 00 3.3.3"])

    subgraph Variable_def
    VarIn0[/입력변수: 부재 종류/]
    VarIn1[/입력변수: 수직부재의 길이 설계치수/];
    VarIn2[/입력변수: 수평부재의 길이 설계치수/];
    VarIn3[/입력변수: 기둥의 단면 설계치수/];
    VarIn4[/입력변수: 보의 단면 설계치수/]
    VarIn5[/입력변수: 바닥판의 두께 설계치수/]
    VarIn6[/입력변수: 수직부재의 길이 시공값/];
    VarIn7[/입력변수: 수평부재의 길이 시공값/];
    VarIn8[/입력변수: 기둥의 단면 시공값/];
    VarIn9[/입력변수: 보의 단면 시공값/]
    VarIn10[/입력변수: 바닥판의 두께 시공값/]
    VarIn0 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~  VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9 & VarIn10

    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{부재 종류}
    C --> |수직부재|D{"|수직부재의 길이 설계치수
    -수직부재의 길이 시공값|\n<=min(수직부재의 길이 설계치수*0.01, 30 mm)"}
    C --> |수평부재|E{"|수평부재의 길이 설계치수
    -수직부재의 길이 시공값| \n<= min(수평부재의 길이 설계치수*0.01, 30 mm)"}
    C --> |기둥|F{"|기둥의 단면 설계치수
    -기둥의 단면 시공값| \n <= min(기둥의 단면 설계치수*0.02, 20 mm)"}
    C --> |보|G{"|보의 단면 설계치수
    -보의 단면 시공값| \n <= min(보의 단면 설계치수*0.02, 20 mm)"}

    C --> |바닥판|H{"-10 mm<=바닥판의 두께 설계치수
    -바닥판의 두께 시공값 <= +20 mm"}
    D & E & F & G & H --> I([Pass or Fail])
    """

    @rule_method

    def tolerance_member_dimension(sIMemTyp, fIDesVer, fIDesHor, fIDesCol, fIDesWei,fIDesDec, fIConVer, fIConHor, fIConCol, fIConWei,fIConDec) -> RuleUnitResult:
        """
        Args:
            sIMemTyp (str): 부재 종류
            fIDesVer (float): 수직부재의 길이 설계치수
            fIDesHor (float): 수평부재의 길이 설계치수
            fIDesCol (float): 기둥의 단면 설계치수
            fIDesWei (float): 보의 단면 설계치수
            fIDesDec (float): 바닥판의 두께 설계치수
            fIConVer (float): 수직부재의 길이 시공값
            fIConHor (float): 수평부재의 길이 시공값
            fIConCol (float): 기둥의 단면 시공값
            fIConWei (float): 보의 단면 시공값
            fIConDec (float): 바닥판의 두께 시공값


        Returns:
            pass_fail (bool): 콘크리트교량공사 3.3.3 부재치수의 시공 허용오차의 시공 허용오차의 판단 결과
        """
        assert isinstance(sIMemTyp, str)
        assert sIMemTyp in ["수직부재", "수평부재", "기둥", "보", "바닥판"]
        assert isinstance(fIDesVer, float)
        assert isinstance(fIDesHor, float)
        assert isinstance(fIDesCol, float)
        assert isinstance(fIDesWei, float)
        assert isinstance(fIDesDec, float)
        assert isinstance(fIConVer, float)
        assert isinstance(fIConHor, float)
        assert isinstance(fIConCol, float)
        assert isinstance(fIConWei, float)
        assert isinstance(fIConDec, float)

        if sIMemTyp == "수직부재":
            if abs(fIDesVer-fIConVer) <= min(fIDesVer*0.01, 30):
                pass_fail = True
            else:
                pass_fail = False
        elif sIMemTyp =="수평부재":
            if abs(fIDesHor-fIConHor) <= min(fIDesHor*0.01, 30):
                pass_fail = True
            else:
                pass_fail = False
        elif sIMemTyp =="기둥":
            if abs(fIDesCol-fIConCol) <= min(fIDesCol*0.02, 20):
                pass_fail = True
            else:
                pass_fail = False
        elif sIMemTyp =="보":
            if abs(fIDesWei-fIConWei) <= min(fIDesWei*0.02, 20):
                pass_fail = True
            else:
                pass_fail = False
        elif sIMemTyp == "바닥판":
            if (fIConDec- fIDesDec) < 20 and (fIConDec- fIDesDec) > -10:
                pass_fail = True
            else:
                pass_fail = False

        return RuleUnitResult(
            result_variables = {
                "pass_fail": pass_fail,
                })