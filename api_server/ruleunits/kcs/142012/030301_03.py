import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_030301_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 3.3.1 (3)'
    ref_date = '2022-09-01'
    doc_date = '2023-09-26'
    title = '기초, 보의 측면, 기둥, 벽의 거푸집널의 해체'

    description = """
    거푸집 및 동바리
    3. 시공
    3.2 동바리의 시공
    3.3.1 거푸집 및 동바리의 해체
    (3)
    """
    content = """
    #### 3.3.1 거푸집 및 동바리의 해체
    (3) 기초, 보의 측면, 기둥, 벽의 거푸집널의 해체는 시험에 의해 표 3.3-1의 값을 만족할 때 시행한다. 특히, 내구성이 중요한 구조물에서는 콘크리트의 압축강도가 10 MPa 이상일 때 거푸집널을 해체할 수 있다. 거푸집널 존치기간 중 평균기온이 10 ℃ 이상인 경우는 콘크리트 재령이 표 3.3-2의 재령이상 경과하면 압축강도시험을 하지 않고도 해체할 수 있다.

    표 3.3-1 콘크리트의 압축강도를 시험할 경우 거푸집널의 해체 시기
    \begin{table}[]
    \begin{tabular}{lll}
    \multicolumn{2}{l}{부재}                                                                   & 콘크리트 압축강도($$f_{ck}$$)                                                                                                            \\
    \multicolumn{2}{l}{\begin{tabular}[c]{@{}l@{}}기초, 보, 기둥, 벽\\ 등의 측면\end{tabular}}         & 5 MPa이상1)                                                                                                                        \\
    \multirow{2}{*}{\begin{tabular}[c]{@{}l@{}}슬래브 및 보의 밑면,\\ 아치 내면\end{tabular}} & 단층구조인 경우 & \begin{tabular}[c]{@{}l@{}}설계기준압축강도의 2/3배 이상\\ 또한, 최소강도 14MPa 이상\end{tabular}                                                    \\
                                                                                & 다층구조인 경우 & \begin{tabular}[c]{@{}l@{}}설계기준 압축강도 이상\\ (필러 동바리 구조를 이용할 경우는 구조계산에 의해 기간을 단축할 수 있음. 단, 이 경우라도 최소강도는 14 MPa 이상으로 함)\end{tabular} \\
    \multicolumn{3}{l}{주 1) 내구성이 중요한 구조물의 경우 10MPa 이상}
    \end{tabular}
    \end{table}

    표 3.3-2 콘크리트의 압축강도를 시험하지 않을 경우 거푸집널의 해체 시기 (기초, 보, 기둥 및 벽의 측면)
    \begin{table}[]
    \begin{tabular}{llll}
    \begin{tabular}[c]{@{}l@{}}시멘트의\\ 종류\\ \\ 평균기온\end{tabular} & 조강포틀랜드 시멘트 & \begin{tabular}[c]{@{}l@{}}보통포틀랜드 시멘트\\ 고로 슬래그 시멘트(1종)\\ 포틀랜드포졸란시멘트(1종)\\ 플라이 애시 시멘트(1종)\end{tabular} & \begin{tabular}[c]{@{}l@{}}고로 슬래그 시멘트(2종)\\ 포틀랜드포졸란시멘트(2종)\\ 플라이 애시 시멘트(2종)\end{tabular} \\
    20 ℃ 이상                                                     & 2일         & 4일                                                                                                    & 5일                                                                                       \\
    \begin{tabular}[c]{@{}l@{}}20 ℃ 미만\\ 10 ℃ 이상\end{tabular}   & 3일         & 6일                                                                                                    & 8일
    \end{tabular}
    \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 기초, 보의 측면, 기둥, 벽의 거푸집널의 해체 시기];
    B["KCS 14 20 12 3.3.1 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 3.3.1 (3)"])

    subgraph Variable_def
    VarOut1[/출력변수: 기초, 보의 측면, 기둥, 벽의 거푸집널의 해체 가능 여부/];
    VarIn2[/입력변수: 내구성이 중요한 구조물/];
    VarIn3[/입력변수: 시멘트의 종류/];
    VarIn4[/입력변수: 거푸집널 존치기간 중 평균기온/];
    VarIn5[/입력변수: 콘크리트 압축강도/];
    VarIn6[/입력변수: 거푸집널 존치기간/];
    end
    VarOut1 ~~~  VarIn2 & VarIn3 & VarIn4

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> E{"거푸집널 존치기간 중 평균기온 ≥ 10 ℃"}
    E --> |False|C{"내구성이 중요한 구조물"}
    C --> |True|D{콘크리트 압축강도}
    D --> |">= 10 MPa"|Po[해체 가능]
    D --> |"< 10 MPa"|Im[해체 불가능]
    C --> |False|F{콘크리트 압축강도}
    F --> |">= 5 MPa"|Po[해체 가능]
    F --> |"< 5 MPa"|G{거푸집널 존치기간 중 평균기온}
    G --> |"20 ℃ 이상"|H{시멘트 종류}
    H --> |조강포틀랜드 시멘트|I{거푸집널 존치기간}
    I --> |">= 2일 "|Po[해체 가능]
    I --> |"< 2일"|Im[해체 불가능]
    H --> |"보통포틀랜드 시멘트 \n 고로 슬래그 시멘트(1종) \n 포틀랜드포졸란시멘트(1종) \n 플라이 애시 시멘트(1종) \n ."|J{거푸집널 존치기간}
    J --> |">= 4일 "|Po[해체 가능]
    J --> |"< 4일"|Im[해체 불가능]
    H --> |"고로 슬래그 시멘트(2종) \n 포틀랜드포졸란시멘트(2종) \n 플라이 애시 시멘트(2종) \n ."|K{거푸집널 존치기간}
    K--> |">= 5일 "|Po[해체 가능]
    K --> |"< 5일"|Im[해체 불가능]
    G --> |"20 ℃ 미만 10 ℃ 이상"|HH{시멘트 종류}
    HH --> |조강포틀랜드 시멘트|II{거푸집널 존치기간}
    II --> |">= 3일 "|Po[해체 가능]
    II --> |"< 3일"|Im[해체 불가능]
    HH --> |"보통포틀랜드 시멘트 \n 고로 슬래그 시멘트(1종) \n 포틀랜드포졸란시멘트(1종) \n 플라이 애시 시멘트(1종) \n ."|JJ{거푸집널 존치기간}
    JJ --> |">= 6일 "|Po[해체 가능]
    JJ --> |"< 6일"|Im[해체 불가능]
    HH --> |"고로 슬래그 시멘트(2종) \n 포틀랜드포졸란시멘트(2종) \n 플라이 애시 시멘트(2종) \n ."|KK{거푸집널 존치기간}
    KK --> |">= 8일 "|Po[해체 가능]
    KK --> |"< 8일"|Im[해체 불가능]
    Po & Im --> End([기초, 보의 측면, 기둥, 벽의 거푸집널의 해체 시기])
    """

    @rule_method

    def dismantle_formwork_foundation_beamside_column_wall(bIDurStr,sICemTyp,fIAveTem,fIFck, nIInsPer) -> RuleUnitResult:
        """
        Args:
            bIDurStr (bool): 내구성이 중요한 구조물
            sICemTyp (str): 시멘트의 종류
            fIAveTem (float): 거푸집널 존치기간 중 평균기온
            fIFck (float): 콘크리트 압축강도
            nIInsPer (int): 거푸집널 존치기간


        Returns:
            sODisPos (str): 기초, 보의 측면, 기둥, 벽의 거푸집널의 해체 가능 여부
        """
        assert isinstance(bIDurStr, bool)
        assert isinstance(sICemTyp, str)
        assert sICemTyp in ["조강포틀랜드 시멘트", "보통포틀랜드 시멘트", "고로 슬래그 시멘트(1종)", "포틀랜드포졸란시멘트(1종)",
                            "플라이 애시 시멘트(1종)", "고로 슬래그 시멘트(2종)", "포틀랜드포졸란시멘트(2종)",  "플라이 애시 시멘트(2종)"]
        assert isinstance(fIAveTem, float)
        assert isinstance(fIFck, float)
        assert isinstance(nIInsPer, int)

        if fIAveTem < 10:
            if bIDurStr:
                if fIFck >=10:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
            else:
                if fIFck >=5:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
        elif fIAveTem < 20:
            if sICemTyp == "조강포틀랜드 시멘트":
                if nIInsPer >= 3:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
            elif sICemTyp == "보통포틀랜드 시멘트" or sICemTyp == "고로 슬래그 시멘트(1종)" or sICemTyp == "포틀랜드포졸란시멘트(1종)" or sICemTyp == "플라이 애시 시멘트(1종)":
                if nIInsPer >= 6:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
            elif sICemTyp == "고로 슬래그 시멘트(2종)" or sICemTyp == "포틀랜드포졸란시멘트(2종)" or sICemTyp == "플라이 애시 시멘트(2종)":
                if nIInsPer >= 8:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
        elif fIAveTem >=20:
            if sICemTyp == "조강포틀랜드 시멘트":
                if nIInsPer >= 2:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
            elif sICemTyp == "보통포틀랜드 시멘트" or sICemTyp == "고로 슬래그 시멘트(1종)" or sICemTyp == "포틀랜드포졸란시멘트(1종)" or sICemTyp == "플라이 애시 시멘트(1종)":
                if nIInsPer >= 4:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"
            elif sICemTyp == "고로 슬래그 시멘트(2종)" or sICemTyp == "포틀랜드포졸란시멘트(2종)" or sICemTyp == "플라이 애시 시멘트(2종)":
                if nIInsPer >= 5:
                    sODisPos = "해체 가능"
                else:
                    sODisPos = "해체 불가능"

        return RuleUnitResult(
            result_variables = {
                "sODisPos": sODisPos,
                })