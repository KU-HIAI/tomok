import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244005_030203_02(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 40 05 3.2.3 (2)'
    ref_date = '2018-08-30'
    doc_date = '2023-11-07'
    title = '탄성받침 완제품 성능'

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량받침
    3. 시공
    3.2 탄성받침
    3.2.3 시험
    (2)
    """

    # 건설기준문서내용(text)
    content = """
        #### (2) 성능시험
    ① 탄성받침의 성능시험은 KS F 4420에 규정된 완제품 성능시험 규정 및 시험방법에 따라 시험하며 그 기준을 요약하면 표 3.2-2와 같다.
    표 3.2-2 탄성받침 완제품 성능 규정
    \begin{table}[]
    \begin{tabular}{cccccc}
    \multicolumn{2}{l}{시험항목}                                                        & \multicolumn{3}{l}{품질기준}                                                                                                                          & \multicolumn{1}{l}{비고}                                                                           \\
    \multirow{3}{*}{전단 계수} & (G_k)kgf/cm2 (MPa)                                     & 7.14(0.7)                                       & 9.18(0.9)                                     & 11.73(1.15)                                     & 23℃±2℃                                                                                           \\
                        & 저온                                                     & \multicolumn{3}{c}{G(저온) ≤ 3G_k}                                                                                                                  & \begin{tabular}[c]{@{}c@{}}-25℃±2℃에서 \\ 7일간 냉각\end{tabular}                                      \\
                        & 노화후                                                    & \multicolumn{3}{c}{G(노화후)≤G_k+1.53kgf/cm2(0.15MPa)}                                                                                               & 70℃에서 3일간                                                                                        \\
    \multirow{2}{*}{전단 부착} & 대기온도                                                   & \multicolumn{3}{c}{최대 변형률에서 고무의 균열이 없어야 한다.}                                                                                                      & 23℃±5℃                                                                                           \\
                        & 노화후                                                    & \multicolumn{3}{c}{최대 변형률에서 고무의 균열이 없어야 한다.}                                                                                                      & 70℃에서 3일간                                                                                        \\
    \multicolumn{2}{c}{압축강도}                                                        & \multicolumn{3}{l}{\begin{tabular}[c]{@{}l@{}}∙최대 하중에서 고무에 균열이 없어야 하고 보강강판의 배치가 정확하여야 한다.\\ ∙정적압축 탄성계수(Ecs)는 최대하중 30% ∼ 100% 사이에 결정\end{tabular}} & 23℃±2℃                                                                                           \\
    \multicolumn{2}{c}{\begin{tabular}[c]{@{}c@{}}압축반복 재하\\ (피로시험)\end{tabular}}    & \multicolumn{3}{l}{\begin{tabular}[c]{@{}l@{}}∙압축계수 증가율이 피로시험전의 12% 이내\\ ∙부착결함, 균열이 없어야 한다.\end{tabular}}                                         & \begin{tabular}[c]{@{}c@{}}시험반복횟수: 2,000,000회\\ 주파수＜3Hz\\ 응력변화는 7.5MPa ~ 25MPa 이내\end{tabular}   \\
    \multirow{2}{*}{정적 회전} & 편심재하시험                                                 & \multicolumn{3}{c}{\begin{tabular}[c]{@{}c@{}}편심이 가해진 상태에서 \\ 최대회전각의 검증\end{tabular}}                                                             & 23℃ ± 2℃                                                                                         \\
                        & \begin{tabular}[c]{@{}c@{}}복원모멘트\\ 시험(Me)\end{tabular} & \multicolumn{3}{c}{설계값 이내}                                                                                                                        & \begin{tabular}[c]{@{}c@{}}23℃ ± 2℃  \\ 압축하중 7MPa로  \\ 회전 0.03㎐ 이하 주파수로 10회 반복재하\end{tabular}    \\
    \multicolumn{2}{c}{오존저항시험}                                                      & \multicolumn{3}{c}{균열이나 부착결함이 없어야 함.}                                                                                                             & \begin{tabular}[c]{@{}c@{}}압축응력 1.3 G․SF, \\ 전단변형률 \\ Vx = 0.7*T_0 \\ 40℃±2℃에서 72시간\end{tabular}
    \end{tabular}
    \end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 탄성받침 완제품 성능 규정];
    B["KCS 24 40 05 3.2.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 05 3.2.3 (2)"])

    subgraph Variable_def
    VarOut1[/출력변수: 탄성받침 완제품 성능/];
    VarIn1[/입력변수: 시험항목/];
    VarIn2[/입력변수: 품질기준/];
    VarIn3[/입력변수: 비고/];
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"시험항목 \n 품질기준 \n 비고"}
    C --> |"표 3.2-2"|D[탄성받침 완제품 성능]
    D --> End(["탄성받침 완제품 성능"])
    """

    @rule_method
    def elastometric_bearing(sITesIte,bIQuaSta,bIRem)->str:
        """
        Args:
            sITesIte (string): 검사항목
            bIQuaSta (boolean): 품질기준
            bIRem (boolean): 비고
        Returns:
            sOBeaPer (string): 탄성받침 완제품 성능
        """
        if sITesIte == "전단계수":
            if bIQuaSta:
                sOBeaPer = "7.14 kgf/㎠(0.7MPa) \n 9.18 kgf/㎠(0.9MPa) \n 11.73 kgf/㎠(1.15MPa)"
            elif bIRem:
                sOBeaPer = "23 ℃ ± 2 ℃"
        elif sITesIte == "저온 전단계수":
            if bIQuaSta:
                sOBeaPer = "G(저온) ≤ 3*전단계수"
            elif bIRem:
                sOBeaPer = "-25 ℃ ± 2 ℃에서 7일간 냉각"
        elif sITesIte == "노화후 전단계수":
            if bIQuaSta:
                sOBeaPer = "G(노화후) ≤ 전단계수+1.53 kgf/㎠(0.15 MPa)"
            elif bIRem:
                sOBeaPer = "70 ℃에서 3일간"
        elif sITesIte == "대기온도 전단부착":
            if bIQuaSta:
                sOBeaPer = "최대 변형률에서 고무의 균열이 없어야 한다."
            elif bIRem:
                sOBeaPer = "23 ℃ ±5 ℃"
        elif sITesIte == "노화후 전단부착":
            if bIQuaSta:
                sOBeaPer = "최대 변형률에서 고무의 균열이 없어야 한다."
            elif bIRem:
                sOBeaPer = "70 ℃에서 3일간"
        elif sITesIte == "압축강도":
            if bIQuaSta:
                sOBeaPer = "∙최대 하중에서 고무에 균열이 없어야 하고 보강강판의 배치가 정확하여야 한다.\n ∙정적압축 탄성계수(E_{cs}))는 최대하중 30% ~ 100% 사이에 결정"
            elif bIRem:
                sOBeaPer = "23 ℃ ±2 ℃"
        elif sITesIte == "압축반복 재하(피로시험)":
            if bIQuaSta:
                sOBeaPer = "압축계수 증가율이 피로시험전의 12% 이내\n ∙부착결함, 균열이 없어야 한다."
            elif bIRem:
                sOBeaPer = "시험반복횟수: 2,000,000회 \n 주파수 ＜ 3 ㎐ \n 응력변화는 7.5 MPa ~ 25 MPa 이내"
        elif sITesIte == "편심재하시험":
            if bIQuaSta:
                sOBeaPer = "편심이 가해진 상태에서 최대회전각의 검증"
            elif bIRem:
                sOBeaPer = "23 ℃ ± 2 ℃"
        elif sITesIte == "복원모멘트시험":
            if bIQuaSta:
                sOBeaPer = "설계값 이내"
            elif bIRem:
                sOBeaPer = "23 ℃ ± 2 ℃ \n 압축하중 7 MPa \n 회전 0.03 ㎐ 이하 \n 주파수로 10회 반복재하"
        elif sITesIte == "오존저항시험":
            if bIQuaSta:
                sOBeaPer = "균열이나 부착결함이 없어야 함."
            elif bIRem:
                sOBeaPer = "압축응력 1.3 G*SF, 전단변형률 = 0.7*T_{0}, 40 ℃ ± 2 ℃에서 72시간"
        else:
            return "검사항목은 전단계수, 저온 전단계수, 노화후 전단계수, 대기온도 전단부착, 노화후 전단부착, 압축강도, 압축반복 재하(피로시험), 편심재하시험, 복원모멘트시험, 오존저항시험 중에서 선택해주세요."
        return sOBeaPer