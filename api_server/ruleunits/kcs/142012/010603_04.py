import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (4)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '콘크리트의 측압'

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
    ① 콘크리트의 측압은 사용재료, 배합, 타설 속도, 타설 높이, 다짐 방법 및 타설할 때의 콘크리트 온도, 사용하는 혼화제의 종류, 부재의 단면 치수, 철근량 등에 의한 영향을 고려하여 산정한다.
    ② 일반 콘크리트용 측압은 아래 ③의 경우를 제외하고는 식 (1.6-1)에 의해 산정한다.

	    $$p = WH$$ (1.6-1)
       여기서,  $$p$$:콘크리트의 측압(kN/㎡)
	            $$W$$:굳지 않은 콘크리트의 단위 중량(kN/㎥)
	            $$H$$:콘크리트의 타설 높이(m)

    ③ 콘크리트 슬럼프가 175 mm 이하이고, 1.2 m 깊이 이하의 일반적인 내부진동다짐으로 타설되는 기둥 및 벽체의 콘크리트의 측압은 다음 식으로 산정 할 수 있다. 다만,  값은 최소 30 이상이고, 최대  이하이다.
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


        (나) 벽체의 측압은 콘크리트 타설 속도에 따라 식 (1.6-3)과 식 (1.6-4)과 같이 구분한다.
            ㉠ 타설 속도가 2.1m/h 이하이고, 타설 높이가 4.2m 미만인 벽체

                $$p= C_{w}C_{c}[7.2 + \frac{790R}{T+18}$$    (1.6-3)

            ㉡ 타설 속도가 2.1m/h 이하이면서 타설 높이가 4.2m 초과하는 벽체 및 타설 속도가 (2.1~4.5)m/h인 모든 벽체

		        $$p= C_{w}C_{c}[7.2 + \frac{1160+240R}{T+18}$$(1.6-4)

    ④ 재진동을 하거나 거푸집 진동기를 사용할 경우, 묽은 반죽의 콘크리트를 타설하는 경우 또는 응결이 지연되는 콘크리트를 사용할 경우에는 전문가의 권장 값에 따라 측압을 증가시킨다.
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 콘크리트의 측압];
    B["KCS 14 20 12 1.6.3 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (4)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 일반 콘크리트 측압/];
    VarIn1[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn2[/입력변수: 콘크리트의 타설 높이/];
    end
    subgraph V2
    VarOut2[/출력변수: 기둥의 측압/];
    VarIn3[/입력변수: 콘크리트 슬럼프/];
    VarIn4[/입력변수: 타설깊이/];
    VarIn5[/입력변수: 일반적인 내부 진동다짐/];
    VarIn6[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn7[/입력변수: 시멘트 종류 및 첨가물/];
    VarIn8[/입력변수: 콘크리트 타설 속도/];
    VarIn9[/입력변수: 콘크리트의 온도/];
    end
    subgraph V3
    VarOut3[/출력변수: 벽체의 측압/];
    VarIn10[/입력변수: 콘크리트 슬럼프/];
    VarIn11[/입력변수: 타설깊이/];
    VarIn12[/입력변수: 일반적인 내부 진동다짐/];
    VarIn13[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn14[/입력변수: 시멘트 종류 및 첨가물/];
    VarIn15[/입력변수: 콘크리트 타설 속도/];
    VarIn16[/입력변수: 콘크리트의 온도/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트 슬럼프 ≤ 175mm, \n 타설 깊이 ≤ 1.2m \n 일반적인 내부 진동다짐"}
    C --> |"False"| D["<img src='https://latex.codecogs.com/png.image?\dpi{500} p = WH'>"];
    C --> |"False"|E{"기둥의 측압 \n 벽체의 측압"}
    E --> |"기둥의 측압"|EE{콘크리트 단위 중량}
    EE --> |"KCS 14 20 12 table 1.6-1"|EEE["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>------"]
    EEE --> EEEE{시멘트 종류 및 첨가물}
    EEEE --> |"KCS 14 20 12 table 1.6-2"|EEEEE["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>-----"]
    EEEEE --> F["<img src='https://latex.codecogs.com/png.image?\dpi{500} p= C_{w}C_{c}[7.2 + \frac{790R}{T+18}]'>----------------------------------------"];
    F --> J["min(max(p, 30*Cw), WH) \n ."]
    E --> |"벽체의 측압"|ee{콘크리트 단위 중량}
    ee --> |"KCS 14 20 12 table 1.6-1"|eee["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>-----"]
    eee --> eeee{시멘트 종류 및 첨가물}
    eeee --> |"KCS 14 20 12 table 1.6-2"|eeeee["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{w}'>-----"]
    eeeee --> G{"타설 속도  \n 타설 높이"}
    G --> |"타설 속도 ≤ 2.1m/h & 타설 높이 < 4.2 m"|H["<img src='https://latex.codecogs.com/png.image?\dpi{500} p= C_{w}C_{c}[7.2 + \frac{790R}{T+18}]'>----------------------------------------"];
    G --> |"타설 속도 ≤ 2.1m/h & 타설 높이 > 4.2 m \n 2.1<타설 속도<4.5"|I["<img src='https://latex.codecogs.com/png.image?\dpi{500} p= C_{w}C_{c}[7.2 + \frac{1160+240R}{T+18}]'>---------------------------------------------"];
    H & I --> J["min(max(p, 30*Cw), WH) \n ."]
    D & J --> End([콘크리트의 측압])
    """

    @rule_method

    def concrete_pressure(fIConSlu, fIPouDep, bIVibCom, bICol, bIWal, fIW, fIH, sICemAdm, fIR, fIT) -> RuleUnitResult:
        """
        Args:
            fIConSlu (float): 콘크리트 슬럼프
            fIPouDep (float): 타설깊이
            bIVibCom (bool): 일반적인 내부 진동다짐
            bICol (bool): 기둥
            bIWal (bool): 벽체
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
        assert isinstance(bIWal, bool)
        assert (bICol+bIWal) !=2
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
            if fIR <= 2.1 and fIH < 4.2:
                fOConPre = min(max(C_w * C_c * (7.2 + (790 * fIR) / (fIT + 18)), 30 * C_w), fIW * fIH)
            else:
                fOConPre = min(max(C_w * C_c * (7.2 + (1160 + 240 * fIR) / (fIT + 18)), 30 * C_w), fIW * fIH)
        elif fIConSlu <= 175 and fIPouDep <= 1.2 and bIVibCom and bIWal:
            if fIW <= 22.5:
                C_w = max(0.5 * (1 + fIW / 23), 0.8)
            elif fIW < 24:
                C_w = 1.0
            else:
                C_w = fIW / 23
            if sICemAdm == "지연제를 사용하지 않은 KS L 5201의 1, 2, 3종 시멘트":
                C_c = 1.0
            elif (
                sICemAdm == "지연제를 사용한 KS L 5201의 1, 2, 3종 시멘트"
                or sICemAdm == "다른 타입의 시멘트 또는 지연제 없이 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트"
            ):
                C_c = 1.2
            elif (
                sICemAdm == "다른 타입의 시멘트 또는 지연제를 사용한 40 % 이하의 플라이 애시 또는 70 % 이하의 슬래그가 혼합된 시멘트"
                or sICemAdm == "70 % 이상의 슬래그 또는 40 % 이상의 플라이 애시가 혼합된 시멘트"
            ):
                C_c = 1.4
            if fIR <= 2.1 and fIH < 4.2:
                fOConPre = min(max(C_w * C_c * (7.2 + (790 * fIR) / (fIT + 18)), 30 * C_w), fIW * fIH)
            else:
                fOConPre = min(max(C_w * C_c * (7.2 + (1160 + 240 * fIR) / (fIT + 18)), 30 * C_w), fIW * fIH)
        else:
            fOConPre = fIW * fIH
        return RuleUnitResult(
            result_variables = {
                "fOConPre": fOConPre,
                })