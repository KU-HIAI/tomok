import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_04_03_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (4) ③ (가)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '기둥의 측압'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (4)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (4) 거푸집 설계에서는 굳지 않은 콘크리트의 측압을 고려하여야 한다.
    ③ 콘크리트 슬럼프가 175 mm 이하이고, 1.2 m 깊이 이하의 일반적인 내부진동다짐으로 타설되는 기둥 및 벽체의 콘크리트의 측압은 다음 식으로 산정 할 수 있다. 다만, $p$ 값은 최소 $30 C_{\text {W}}$ 이상이고, 최대 $W H$ 이하이다.
        (가) 기둥의 측압은 식 (1.6-2)에 의해 산정한다.

            $$p= C_{w}C_{c}[7.2 + \frac{790R}{T+18}$$ (1.6-2)
            여기서, $$C_{w}$$:단위 중량 계수, 표 1.6-1
                    $$C_{c}$$:화학첨가물 계수, 표 1.6-2
                    $$R$$:콘크리트 타설 속도(m/h)
                    $$T$$:타설되는 콘크리트의 온도(℃)

            표 1.6-1 단위 중량 계수($$C_{w}$$)
            \begin{table}[]
            \begin{tabular}{ll}
            \begin{tabular}[c]{@{}l@{}}콘크리트 단위 중량\\ (kN/m3)\end{tabular} & $$C_{w}$$                                                             \\
            22.5이하인 경우                                                   & \begin{tabular}[c]{@{}l@{}}$$C_{w}=0.5(1+\frac{W}{23}$$\\ 다만, 0.8 이상이어야 한다.\end{tabular} \\
            22.5~24인 경우                                                  & 1.0                                                           \\
            24이상인 경우                                                     & $$C_{w}=\frac{W}{23}$$
            \end{tabular}
            \end{table}

            표 1.6-2 화학첨가물 계수($$C_{c}$$)
            \begin{table}[]
            \begin{tabular}{ll}
            시멘트 타입종류 및 첨가물                                                                                            & $$C_{c}$$    \\
            지연제를 사용하지 않은 KS L 5201의 1, 2, 3종 시멘트                                                                      & 1.0 \\
            지연제를 사용한 KS L 5201의 1, 2, 3종 시멘트                                                                          & 1.2 \\
            \begin{tabular}[c]{@{}l@{}}다른 타입의 시멘트 또는 지연제 없이 40 % 이하의 플라이 애시\\ 또는 70 % 이하의 슬래그가 혼합된 시멘트\end{tabular}   & 1.2 \\
            \begin{tabular}[c]{@{}l@{}}다른 타입의 시멘트 또는 지연제를 사용한 40 % 이하의 플라이 애시\\ 또는 70 % 이하의 슬래그가 혼합된 시멘트\end{tabular} & 1.4 \\
            70 % 이상의 슬래그 또는 40 % 이상의 플라이 애시가 혼합된 시멘트                                                                  & 1.4
            \end{tabular}
            \end{table}
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기둥의 측압];
    B["KCS 14 20 12 1.6.3 (4) ③ (가)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (4) ③ (가)"])

    subgraph Variable_def
    VarOut[/출력변수: 콘크리트 측압/];
    VarIn1[/출력변수: 기둥/];
    VarIn2[/입력변수: 콘크리트의 타설 높이/];
    VarIn3[/입력변수: 콘크리트 슬럼프/];
    VarIn4[/입력변수: 타설깊이/];
    VarIn5[/입력변수: 일반적인 내부 진동다짐/];
    VarIn6[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn7[/입력변수: 시멘트 종류 및 첨가물/];
    VarIn8[/입력변수: 콘크리트 타설 속도/];
    VarIn9[/입력변수: 콘크리트의 온도/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트 슬럼프 ≤ 175mm, \n 타설 깊이 ≤ 1.2m \n 일반적인 내부 진동다짐"}
    C --> |True|EE{콘크리트 단위 중량}
    EE --> |"표 1.6-1"|EEE["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>------"]
    EEE --> EEEE{시멘트 종류 및 첨가물}
    EEEE --> |"표 1.6-2"|EEEEE["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>-----"]
    EEEEE --> F["<img src='https://latex.codecogs.com/png.image?\dpi{500} p= C_{w}C_{c}[7.2 + \frac{790R}{T+18}]'>----------------------------------------"];
    F --> J["콘크리트 측압 = min(max(p, 30*Cw), WH) \n ."]
    J --> End([기둥의 측압])
    """

    @rule_method

    def column_concrete_pressure(fIConSlu, fIPouDep, bIVibCom, bICol, fIW, fIH, sICemAdm, fIR, fIT) -> RuleUnitResult:
        """
        Args:
            fIConSlu (float): 콘크리트 슬럼프
            fIPouDep (float): 타설깊이
            bIVibCom (bool): 일반적인 내부 진동다짐
            bICol (bool): 기둥
            fIW (float): 굳지 않은 콘크리트의 단위 중량
            fIH (float): 콘크리트의 타설 높이
            sICemAdm (str): 시멘트 종류 및 첨가물
            fIR (float): 콘크리트 타설 속도
            fIT (float): 콘크리트의 온도

        Returns:
            fOConPre (float): 콘크리트 측압
        """
        assert isinstance(fIConSlu, float)
        assert isinstance(fIPouDep, float)
        assert isinstance(bIVibCom, bool)
        assert isinstance(bICol, bool)
        assert bICol == True
        assert isinstance(fIW, float)
        assert isinstance(fIH, float)
        assert isinstance(sICemAdm, str)
        assert sICemAdm in ["지연제를 사용하지 않은 KS L 5201의 1, 2, 3종 시멘트", "지연제를 사용한 KS L 5201의 1, 2, 3종 시멘트", "다른 타입의 시멘트 또는 지연제 없이 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트",
                            "다른 타입의 시멘트 또는 지연제를 사용한 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트", "70 % 이상의 슬래그 또는 40 % 이상의 플라이 애시가 혼합된 시멘트"]
        assert isinstance(fIR, float)
        assert isinstance(fIT, float)


        if fIConSlu <= 175 and fIPouDep <= 1.2 and bIVibCom and bICol:
            if fIW <= 22.5:
                C_w = max(0.5 * (1 + fIW / 23), 0.8)
            elif fIW < 24:
                C_w = 1.0
            else:
                C_w = fIW / 23
            if sICemAdm == "지연제를 사용하지 않은 KS L 5201의 1, 2, 3종 시멘트":
                C_c = 1.0
            elif (sICemAdm == "지연제를 사용한 KS L 5201의 1, 2, 3종 시멘트"
                or sICemAdm == "다른 타입의 시멘트 또는 지연제 없이 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트"
            ):
                C_c = 1.2
            elif (
                sICemAdm == "다른 타입의 시멘트 또는 지연제를 사용한 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트"
                or sICemAdm == "70 % 이상의 슬래그 또는 40 % 이상의 플라이 애시가 혼합된 시멘트"
            ):
                C_c = 1.4
            fOConPre = min(max(C_w * C_c * (7.2 + (790 * fIR) / (fIT + 18)), 30 * C_w), fIW * fIH)
        else:
            fOConPre = None
        return RuleUnitResult(
            result_variables = {
                "fOConPre": fOConPre,
                })