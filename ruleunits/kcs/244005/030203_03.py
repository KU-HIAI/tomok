import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_030203_03(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 3.2.3 (3)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '시험빈도'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    3. 시공
    3.2 탄성받침
    3.2.3 시험
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### (3) 시험빈도
    ① 시험
    가. 형식시험:생산의 중대한 변화로 규격과의 일치에 영향을 미칠 때 공인된 시험기관에서 반복적으로 실시하는 일종의 선정시험
    나. 정기시험:제조자가 지속적으로 실시하는 일종의 관리시험
    ② 시료 크기
    표 3.2-3 시료형식에 따른 크기
    \begin{table}[]
    \begin{tabular}{ccccc}
    \multicolumn{5}{r}{(단위:mm)}                                                                                                                   \\
    \multicolumn{1}{l}{시료형식 (TYPE)} & \multicolumn{1}{l}{a} & \multicolumn{1}{l}{b} & \multicolumn{1}{l}{고무층수} & \multicolumn{1}{l}{고무층과 보강판의 두께} \\
    Ⅰ                               & 200                   & 300                   & 3                        & 8(te) + 3(ts)                    \\
    Ⅱ                               & 400                   & 500                   & 5                        & 12(te) + 4(ts)                   \\
    Ⅲ                               & 600                   & 700                   & 7                        & 16(te) + 5(ts)                   \\
    \multicolumn{5}{l}{주 1) 여기서, a: 가로 길이  b: 세로 길이  te: 고무층 두께  ts: 보강판 두께}
    \end{tabular}
    \end{table}
    ③ 재료특성 시험형식 및 시험빈도
    표 3.2-4 시험항목에 따른 시험형식 및 빈도수
    \begin{table}[]
    \begin{tabular}{ccc}
    \multicolumn{1}{l}{시험항목} & \multicolumn{1}{l}{시험형식} & \multicolumn{1}{l}{시험 빈도수(회)} \\
    \multirow{2}{*}{인장강도}    & 형식시험                     & 1/년                           \\
                            & 정기시험                     & 각 배치별                         \\
    신장률                      & 형식시험                     & 1/년                           \\
    \multirow{2}{*}{인열저항시험}  & 형식시험                     & 1/년                           \\
                            & 정기시험                     & 4/년                           \\
    \multirow{2}{*}{압축영구줄음률} & 형식시험                     & 1/년                           \\
                            & 정기시험                     & 4/년                           \\
    \multirow{2}{*}{노화시험}    & 형식시험                     & 1/년                           \\
                            & 정기시험                     & 4/년                           \\
    \multirow{2}{*}{오존저항시험}  & 형식시험                     & 1/년                           \\
                            & 정기시험                     & 4/년
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 시험빈도];
    B["KCS 24 40 05 3.2.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.2.3 (3)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 시료크기/];
    VarIn11[/입력변수: 시료의 가로 길이/];
    VarIn12[/입력변수: 시료의 세로 길이/];
    VarIn13[/입력변수: 고무층수/];
    VarIn14[/입력변수: 고무층과 보강판의 두께/];
    VarIn15[/입력변수: 시료형식/];
    VarIn16[/입력변수: 고무층 두께/];
    VarIn17[/입력변수: 보강판 두께/];
    end
    subgraph V2
    VarOut2[/출력변수: 재료특성 시험 빈도수/];
    VarIn21[/입력변수: 시험항목/];
    VarIn22[/입력변수: 시험형식/];
    end
    subgraph V3
    VarOut3[/출력변수: 완제품의 시료형식 및 시험빈도/];
    VarIn31[/입력변수: 시료형식/];
    VarIn32[/입력변수: 시험 빈도수/];
    VarIn33[/입력변수: 시험항목/];
    VarIn34[/입력변수: 시험형식/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> I{"시료크기\n재료특성 시험 빈도수\n완제품의 시료형식 및 시험빈도\n."}
    I --> |"시료크기"|C{시료의 가로 길이\n시료의 세로 길이\n고무층수\n고무층과 보강판의 두께\n시료형식\n고무층 두께\n보강판 두께\n.}
    C --> |표 3.2-3|D[시료크기]
    I --> |"재료특성 시험 빈도수"|E{시험항목\n시험형식\n.}
    E --> |표 3.2-4|F[재료특성 시험 빈도수]
    I --> |"완제품의 시료형식 및 시험빈도"|G{시료형식\n시험 빈도수\n시험항목\n시험형식\n.}
    G --> |표 3.2-5|H[완제품의 시료형식 및 시험빈도]
    D & F & H--> End(["시험빈도"])
    """

    @rule_method
    def sample_size(bIA,bIB,bINumLay,bIThiLay,sISamTyp,fITe,fITs)->float:
        """
        Args:
            bIA (boolean): 시료의 가로 길이
            bIB (boolean): 시료의 세로 길이
            bINumLay (boolean): 고무층수
            bIThiLay (boolean): 고무층과 보강판의 두께
            sISamTyp (string): 시료형식
            fITe (float): 고무층 두께
            fITs (float): 보강판 두께
        Returns:
            fOSamSiz (float): 시료크기
        """
        if sISamTyp == "Ⅰ":
            if bIA:
                fOSamSiz = 200
            elif bIB:
                fOSamSiz = 300
            elif bINumLay:
                fOSamSiz = 3
            elif bIThiLay:
                fOSamSiz = 8*fITe + 3*fITs
        elif sISamTyp == "Ⅱ":
            if bIA:
                fOSamSiz = 400
            elif bIB:
                fOSamSiz = 500
            elif bINumLay:
                fOSamSiz = 5
            elif bIThiLay:
                fOSamSiz = 12*fITe + 4*fITs
        elif sISamTyp == "Ⅲ":
            if bIA:
                fOSamSiz = 600
            elif bIB:
                fOSamSiz = 700
            elif bINumLay:
                fOSamSiz = 7
            elif bIThiLay:
                fOSamSiz = 16*fITe + 5*fITs
        return fOSamSiz

    def test_frequency(self,sITesIte_1,sITesTyp_1)->str:
        """
        Args:
            sITesIte_1 (string): 시험항목
            sITesTyp_1 (string): 시험형식
        Returns:
            sOTesFre (string): 재료특성 시험 빈도수
        """
        if sITesIte_1 == "인장강도":
            if sITesTyp_1 == "형식시험":
                sOTesFre ="1 회/년"
            elif sITesTyp_1 == "정기시험":
                sOTesFre = "각 배치별"
        elif sITesIte_1 == "신장률":
            sOTesFre ="1 회/년"
        elif sITesIte_1 == "인열저항시험" or sITesIte_1 == "압축영구줄음률" or sITesIte_1 == "노화시험" or sITesIte_1 == "오존저항시험" :
            if sITesTyp_1 == "형식시험":
                sOTesFre ="1 회/년"
            elif sITesTyp_1 == "정기시험":
                sOTesFre = "4 회/년"
        else:
            return "시험항목은 인장강도, 신장률, 인열저항시험, 압축영구줄음률, 노화시험, 오존저항시험 중에서 선택해주세요"
        return sOTesFre

    def sample_type_frequency(self, bISamTyp,bITesFre,sITesIte_2,sITesTyp_2)->str:
        """
        Args:
            bISamTyp (boolean): 시료형식
            bITesFre (boolean): 시험 빈도수
            sITesIte_2 (string): 시험항목
            sITesTyp_2 (string): 시험형식
        Returns:
            sOFinGoo (string): 완제품의 시료형식 및 시험빈도
        """
        if sITesIte_2 == "대기온도(상온) 전단계수" or sITesIte_2 == "압축강도":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ, Ⅱ, Ⅲ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            elif sITesTyp_2 == "정기시험":
                if bISamTyp:
                    sOFinGoo = "생산되는 전 규격"
                elif bITesFre:
                    sOFinGoo = "생산 시마다"
        elif sITesIte_2 == "저온 전단계수":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "저온 전단계수는 형식시험만 치룸"
        elif sITesIte_2 == "노화 후 전단계수":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ, Ⅱ, Ⅲ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "노화후 전단계수는 형식시험만 치룸"
        elif sITesIte_2 == "대기온도(상온) 전단부착":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ, Ⅱ, Ⅲ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            elif sITesTyp_2 == "정기시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ"
                elif bITesFre:
                    sOFinGoo = "생산 시마다"
        elif sITesIte_2 == "노화 후 전단부착":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ, Ⅱ, Ⅲ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "노화 후 전단부착는 형식시험만 치룸"
        elif sITesIte_2 == "반복압축재하":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "반복압축재하는 형식시험만 치룸"
        elif sITesIte_2 == "복원모멘트 또는 편심률재하":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ, Ⅱ, Ⅲ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "복원모멘트 또는 편심률재하는 형식시험만 치룸"
        elif sITesIte_2 == "오존저항":
            if sITesTyp_2 == "형식시험":
                if bISamTyp:
                    sOFinGoo = "Ⅰ"
                elif bITesFre:
                    sOFinGoo = "1회/년"
            else:
                return "오존저항은 형식시험만 치룸"
        else:
            return "시험항목은 대기온도(상온) 전단계수, 저온 전단계수, 노화 후 전단계수, 대기온도(상온) 전단부착, 노화 후 전단부착, 압축강도, 반복압축재하, 복원모멘트 또는 편심률재하, 오존저항 중에서 선택해주세요"
        return sOFinGoo