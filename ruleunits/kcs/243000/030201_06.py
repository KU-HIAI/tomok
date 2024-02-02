import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS243000_030201_06(RuleUnit):
    priority = 1
    author = '서울대학교, 최정운'
    ref_code = 'KCS 24 30 00 3.2.1 (6)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '완전용입 맞대기 용접부의 피로시험'

    # 건설기준문서항목 (분류체계정보)
    description = """
    강교량공사
    3. 시공
    3.2 용접
    3.2.1 일반사항

    """

    # 건설기준문서내용(text)
    content = """
    ####(6) 완전용입 맞대기 용접부의 피로시험
    ① 완전용입 맞대기 용접부의 피로성능에 대한 평가 실적이 없는 공급원이 공급한 재료(모재, 용접봉 또는 와이어, 플럭스)를 사용하는 경우에는 용접부 인장 시험체에 대해 다음의 피로시험법에 따라 피로시험을 수행하고 그 합격 여부를 판단한다.
    ② 시험체의 용접철구제작공장 또는 공사현장 작업조건과 동일하거나 그보다 가혹한 조건에서 피로 성능평가용 시험체를 용접한다.
    ③ 판두께별 시험체의 형상
        가. 시험체의 단면 폭(W)은 판두께(T)의 1.5배 이상으로 설정한다.
        나. 그립부 폭(B)이 단면 폭(W)의 1.5배 이상으로 설정한다.
        다. 시험체의 단면 평행길이(L)는 판두께(T)의 3배 이상으로 설정한다.
        라. 변화부 반경은 단면 폭(W)의 2.5배 이상 또는 구조해석을 통해 응력집중도(=변화부 응력/시험단면 응력)가 1.1 이하가 되도록 설정한다. 표 3.2-3은 판두께별 피로시험체의 크기와 형상에 대한 예시이다.
        표 3.2-3 판두께별 피로시험체의 크기와 형상의 예시
        \begin{table}[]
        \begin{tabular}{lllllll}
        \multicolumn{7}{r}{(단위: mm)}                                     \\
        판두께(T) & 그립부폭(B) & 단면폭(W) & 평행부길이(L) & 변화부반경(R) & 그립부길이 & 시험체총길이 \\
        20     & 90      & 40     & 170      & 100      & 250   & 802    \\
        40     & 100     & 60     & 200      & 160      & 250   & 855    \\
        60     & 140     & 90     & 250      & 240      & 250   & 963    \\
        80     & 190     & 120    & 350      & 320      & 250   & 1,141
        \end{tabular}
        \end{table}
    ④ 시험체의 정합도(alignment) 평가하중 축과 편심에 의한 시험체에 발생한 휨 변형율을 축방향 변형율로 나눈 값(percent bending)이 5% 이내임을 정적 재하시험을 통해 확인 후 피로시험을 수행한다.
    ⑤ 피로 시험체의 개수 및 시험조건
        가. 피로 시험체의 개수는 최소 9개 이상으로 하며, 3개의 피로하중 응력범위에 대해 각각 3개씩 실험한다.
        나. 반복횟수 50만회 이상에서 피로파단이 일어나도록 피로하중 응력범위를 설정하되, 피로수명 200만회에 해당하는 피로강도 이하의 값이 포함되도록 한다. 표 3.2-4는 판두께별 피로하중의 크기와 응력범위에 대한 예시이다.
        다. 작용하중의 응력비는 0.05 이상으로 한다.
        표 3.2-4 판두께별 피로하중의 크기와 응력범위의 예시
        \begin{table}[]
        \begin{tabular}{llrrlll}
        \begin{tabular}[c]{@{}l@{}}판두께\\ (㎜)\end{tabular} & \begin{tabular}[c]{@{}l@{}}순단면적\\ (㎡)\end{tabular} & \multicolumn{1}{l}{\begin{tabular}[c]{@{}l@{}}최대하중 \\ (kN)\end{tabular}} & \multicolumn{1}{l}{\begin{tabular}[c]{@{}l@{}}최소하중 \\ (kN)\end{tabular}} & \begin{tabular}[c]{@{}l@{}}최대응력 \\ (MPa)\end{tabular} & \begin{tabular}[c]{@{}l@{}}최소응력 \\ (MPa)\end{tabular} & \begin{tabular}[c]{@{}l@{}}응력범위 \\ (MPa)\end{tabular} \\
        \multirow{3}{*}{20}                               & \multirow{3}{*}{0.0008}                            & 98                                                                       & 9.8                                                                      & 122                                                   & 12                                                    & 110                                                   \\
                                                        &                                                    & 123                                                                      & 12.3                                                                     & 153                                                   & 15.5                                                  & 137.5                                                 \\
                                                        &                                                    & 147                                                                      & 14.7                                                                     & 183                                                   & 18                                                    & 165                                                   \\
        \multirow{3}{*}{40}                               & \multirow{3}{*}{0.0024}                            & 293                                                                      & 29.3                                                                     & 122                                                   & 12                                                    & 110                                                   \\
                                                        &                                                    & 366                                                                      & 36.6                                                                     & 153                                                   & 15.5                                                  & 137.5                                                 \\
                                                        &                                                    & 439                                                                      & 43.9                                                                     & 183                                                   & 18                                                    & 165                                                   \\
        \multirow{3}{*}{60}                               & \multirow{3}{*}{0.0054}                            & 659                                                                      & 65.9                                                                     & 122                                                   & 12                                                    & 110                                                   \\
                                                        &                                                    & 824                                                                      & 82.4                                                                     & 153                                                   & 15.5                                                  & 137.5                                                 \\
                                                        &                                                    & 989                                                                      & 98.9                                                                     & 183                                                   & 18                                                    & 165                                                   \\
        \multirow{3}{*}{80}                               & \multirow{3}{*}{0.0096}                            & 1,167                                                                    & 116.7                                                                    & 122                                                   & 12                                                    & 110                                                   \\
                                                        &                                                    & 1,462                                                                    & 146.2                                                                    & 153                                                   & 15.5                                                  & 137.5                                                 \\
                                                        &                                                    & 1,756                                                                    & 175.6                                                                    & 183                                                   & 18                                                    & 165
        \end{tabular}
        \end{table}
    ⑥ 피로 시험결과의 판정모든 피로 시험체가 도로교설계기준에 규정된 설계 피로등급의 피로강도 이상일 경우 합격한 것으로 한다.
    ⑦ 재시험
        가. 불합격의 경우 같은 방법으로 일차로 재시험을 수행하여 모든 피로 시험체가 설계 피로등급의 피로강도 이상일 경우 합격한 것으로 한다.
        나. 일차 재시험이 불합격된 경우에는 추가적으로 이차 재시험을 수행하여, 총 27개의 시험결과를 통계 처리하여 하한 5% 피로강도 곡선이 설계 피로등급의 피로강도 이상일 경우 합격한 것으로 한다.
    ⑧ 사용하고자 하는 강재에 대한 피로 성능 평가 실적이 있더라도, 제강사(mill), 강종, 용접재료가 기존 실적자료와 다른 경우에는 해당 부재에 대한 피로성능 평가를 별도로 실시하여야 한다. 강종과 용접재료가 동일하더라도 최대 판두께, 개선형상, 용접자세, 최대 입열량, 최소 예열온도, 용접 비드 개선 등이 다른 경우에는 가혹한 조건을 기준으로 피로 성능 평가의 추가 실시 여부를 감독자가 판단한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 완전용입 맞대기 용접부의 피로시험];
    B["KCS 24 30 00 3.2.1 (6)"];
    B ~~~ A
    end

    KCS(["KCS 24 30 00 3.2.1 (6)"])

    subgraph Variable_def
    subgraph V1
    VarOut1[/출력변수: 판두께별 시험체의 형상/];
    VarIn11[/입력변수: 단면폭/];
    VarIn12[/입력변수: 판두께/];
    VarIn13[/입력변수: 그립부 폭/];
    VarIn14[/입력변수: 단면 평행길이/];
    VarIn15[/입력변수: 변화부 반경/];
    VarIn16[/입력변수: 단면 폭/];
    VarIn17[/입력변수: 응력집중도/];
    end
    subgraph V2
    VarOut2[/출력변수: 시험체의 정합도/];
    VarIn21[/입력변수: 하중 축과 편심에 의한 시험체에 발생한 \n 휨 변형율을 축방향 변형율로 나눈 값/];
    end
    subgraph V3
    VarOut3[/출력변수: 작용하중의 응력비/];
    VarIn31[/"입력변수: 작용하중의 응력비"/];
    end
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"판두께별 시험체의 형상\n시험체의 정합도\n작용하중의 응력비"}
    C --> |"판두께별 시험체의 형상"|D{"단면폭≥판두께*1.5 \n 그립부 폭 ≥ 단면 폭 * 1.5 \n 단면 평행길이 ≥ 판두께*3 \n  변화부 반경 ≥단면 폭 2.5 or 응력집중도 ≤ 1.1 \n."}
    D --> |True|Pass1([Pass])
    D --> |False|Fail1([Fail])
    C --> |시험체의 정합도|E{"percent bending < 5"}
    E --> |True|F[피로시험을 수행]
    E --> |False|Fail2([Fail])
    C --> |작용하중의 응력비|G{"작용하중의 응력비 ≥ 0.05"}
    G --> |True|Pass3([Pass])
    G--> |False|Fail3([Fail])
    F --> Q(["용접시공시험"])
    """

    @rule_method
    def shape_specimen(fIW,fIT,fIB,fIL,fIR,fIStrCon)-> str:
        """
        Args:
            fIW (float): 단면폭
            fIT (float): 판두께
            fIB (float): 그립부 폭
            fIL (float): 단면 평행길이
            fIR (float): 변화부 반경
            fIStrCon (float): 응력집중도
        Returns:
            sOShaSpe (string): 판두께별 시험체의 형상
        """
        if fIW>=fIT*1.5 and fIB>=fIW*1.5 and fIL>=fIT*3:
            if fIR>=fIW*2.5 or fIStrCon<=1.1:
                sOShaSpe = "Pass"
            else:
                sOShaSpe = "Fail"
        else:
            sOShaSpe = "Fail"
        return sOShaSpe

    def alignment_specimen(self,fIPerBen)-> str:
        """
        Args:
            fIPerBen (float): 하중 축과 편심에 의한 시험체에 발생한 휨 변형율을 축방향 변형율로 나눈 값
        Returns:
            sOAliSpe (string): 시험체의 정합도
        """
        if fIPerBen < 5:
            sOAliSpe = "Pass"
        else:
            sOAliSpe = "Fail"
        return sOAliSpe

    def stress_ratio(self,fIStrLoa):
        """
        Args:
            fIStrLoa (float): 작용하중의 응력비
        Returns:
            sOStrLoa (string): 작용하중의 응력비
        """
        if fIStrLoa >= 0.05:
            sOStrLoa = "Pass"
        else:
            sOStrLoa = "Fail"
        return sOStrLoa