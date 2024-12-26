import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244005_030103(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 05 3.1.3'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '받침 설치 검사기준'

    description = """
    교량받침
    3. 시공
    3.1 일반사항
    3.1.3 설치 시 검사기준
    """
    content = """
    #### 3.1.3 설치 시 검사기준
    (1) 설치된 받침이 표 3.1-1의 검사기준을 만족하지 못하면 교정하거나, 공사감독자의 지시에 따라야 한다.
        표 3.1-1 받침 설치 검사기준
        \begin{table}[]
        \begin{tabular}{lcll}
        \multicolumn{2}{l}{검사항목}                                                            & 콘크리트교                    & 강교                           \\
        \multicolumn{2}{l}{받침 중심간격(교축직각방향)}                                                 & ±5mm                     & 4+0.5(B-2)mm                 \\
        \multicolumn{2}{l}{가동받침의 교축방향의 이동편차 동일 받침선 상의 상대오차}                                 & \multicolumn{2}{l}{5mm}                                 \\
        \multicolumn{2}{l}{설치 높이}                                                           & \multicolumn{2}{l}{±5mm}                                \\
        \multicolumn{2}{l}{교량 전체 받침의 상대높이 오차}                                               & \multicolumn{2}{l}{6mm}                                 \\
        \multicolumn{2}{l}{단일 box를 지지하는 인접 받침의 상대높이 오차}                                     & \multicolumn{2}{l}{3mm}                                 \\
        \multirow{2}{*}{받침의 수평도 (교축 및 직각방향)}                     & 포트받침                     & \multicolumn{2}{c}{1/300}                               \\
                                                                & 기타 받침                    & \multicolumn{2}{c}{1/100}                               \\
        \multicolumn{2}{l}{앵커볼트의 연직도}                                                       & \multicolumn{2}{c}{1/100}                               \\
        \multicolumn{4}{l}{\begin{tabular}[c]{@{}l@{}}주 1) B:받침 중심간격(m)\\  2) 받침의 상ㆍ하면 사이의 수평도\\  3) 받침에 유해한 영향이 있는 경우는 공사감독자의 지시에 따른다.\end{tabular}}
        \end{tabular}
        \end{table}
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 받침 설치 검사기준];
    B["KCS 24 40 05 3.1.3"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.1.3"])

    subgraph Variable_def
    VarOut1[/출력변수: 받침 설치 검사기준/];
    VarIn1[/입력변수: 교량 종류/];
    VarIn2[/입력변수: 받침 중심간격/];
    VarIn3[/입력변수: 설계이동량/];
    VarIn4[/입력변수: 검사항목/];
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> I{"검사항목"}
    I --> |"받침 중심간격(교축직각방향)"|BB{교량 종류}
    BB --> |콘크리트교|AA["±5mm"]
    BB --> |강교|AAA["4+0.5(받침 중심간격-2)mm"]
    I --> |가동받침의 이동가능량|CC["설계이동량 + 10mm"]
    I --> |가동받침의 교축방향의 이동편차\n동일 받침선 상의 상대오차|D["5mm"]
    I --> |설치 높이|E["±5mm"]
    I --> |교량 전체 받침의 상대높이 오차|F["6mm"]
    I --> |설치 높이|G["±5mm"]
    I --> |단일 box를 지지하는 인접 받침의 상대높이 오차|H[" 3mm"]
    I --> |"받침의 수평도(교축 및 직각방향)"|J{"받침의 종류"}
    J --> |포트받침|K["1/300"]
    J --> |기타받침|L[" 1/100"]
    I --> |앵커볼트의 연직도|M["1/100"]
    AA & AAA & CC & D & E & F & G & H & K & L & M --> OO(["받침 설치 길이검사기준"])
    """

    @rule_method

    def PTFE_fiber(sIBriTyp,fIB,fIDesMov,sIRevIte) -> RuleUnitResult:
        """
        Args:
            sIBriTyp (str): 교량 종류
            fIB (float): 받침 중심간격
            fIDesMov (float): 설계이동량
            sIRevIte (str): 검사항목

        Returns:
            sOBeaIns (str): 받침 설치 검사기준
        """
        assert isinstance(sIBriTyp, str)
        assert sIBriTyp in ["콘크리트교","강교"]
        assert isinstance(fIB, float)
        assert isinstance(fIDesMov, float)
        assert isinstance(sIRevIte, str)
        assert sIRevIte in ["받침 중심간격(교축직각방향)","가동받침의 이동가능량", "가동받침의 교축방향의 이동편차 동일 받침선 상의 상대오차",
                            "설치 높이","교량 전체 받침의 상대높이 오차", "단일 box를 지지하는 인접 받침의 상대높이 오차",
                            "포트받침의 수평도(교축 및 직각방향)", "기타받침의 수평도(교축 및 직각방향)", "앵커볼트의 연직도"]

        if sIRevIte == "받침 중심간격(교축직각방향)":
            if sIBriTyp == "콘크리트교":
                sOBeaIns = "±5mm"
            elif sIBriTyp == "강교":
                sOBeaIns = str(round(4+0.5*(fIB-2),3)) + " mm"
        elif sIRevIte == "가동받침의 이동가능량":
            sOBeaIns = str(fIDesMov + 10) + " mm 이상"
        elif sIRevIte == "가동받침의 교축방향의 이동편차 동일 받침선 상의 상대오차":
            sOBeaIns = "5mm"
        elif sIRevIte == "설치 높이":
            sOBeaIns = "±5mm"
        elif sIRevIte == "교량 전체 받침의 상대높이 오차":
            sOBeaIns = "6mm"
        elif sIRevIte == "단일 box를 지지하는 인접 받침의 상대높이 오차":
            sOBeaIns = "3mm, 단 받침에 유해한 영향이 있는 경우는 공사감독자의 지시에 따른다."
        elif sIRevIte == "포트받침의 수평도(교축 및 직각방향)":
            sOBeaIns = "1/300"
        elif sIRevIte == "기타받침의 수평도(교축 및 직각방향)":
            sOBeaIns = "1/100"
        elif sIRevIte == "앵커볼트의 연직도":
            sOBeaIns = "1/100"

        return RuleUnitResult(
            result_variables = {
                "sOBeaIns": sOBeaIns,
                })