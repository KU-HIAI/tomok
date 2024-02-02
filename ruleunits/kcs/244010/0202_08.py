import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS244010_0202_08(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 24 40 10 2.2 (8)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2018-08-30'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '신축이음'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    신축이음
    2. 자재
    2.2 재료
    (8)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2 재료
    (8) 신축이음장치의 봉함용 고무는 양질의 흑색 프로필렌계 고무를 성형한 것으로 표 2.2-1에 적합한 것이어야 한다.
    표 2.2-1 봉함용 고무재 품질 기준
\begin{table}[]
\begin{tabular}{|ll|l|l|l|}
\hline
\multicolumn{2}{|l|}{시험항목}                           & 단위  & 규격          & 시험방법      \\ \hline
\multicolumn{2}{|l|}{인장강도}                           & MPa & 15.0 이상     & KS M 6518 \\ \hline
\multicolumn{2}{|l|}{연신율}                            & \%  & 300 이상      & 〃         \\ \hline
\multicolumn{2}{|l|}{경도시험}                           & 경도  & 45 $\sim$60 & 〃         \\ \hline
\multicolumn{1}{|l|}{\multirow{3}{*}{가열노화시험}} & 인장강도 & MPa & 13.0 이상     & 〃         \\ \cline{2-5}
\multicolumn{1}{|l|}{}                        & 연신율  & \%  & 250 이상      & 〃         \\ \cline{2-5}
\multicolumn{1}{|l|}{}                        & 경도변화 & 경도  & 10 이하       & 〃         \\ \hline
\multicolumn{2}{|l|}{압축영구변형}                         & \%  & 25 이하       & 〃         \\ \hline
\end{tabular}
\end{table}
"""

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 봉함용 고무 품질기준];
    B["KCS 24 40 10 2.2 (8)"];
    B ~~~ A
    end

    KCS(["KCS 24 40 10 2.2 (8)"])

    subgraph Variable_def
    VarOut1[/출력변수: 봉함용 고무 품질기준/];
    VarOut2[/출력변수: 시험 방법/];

    VarIn1[/입력변수: 인장강도/];
    VarIn2[/입력변수: 연신율/];
    VarIn3[/입력변수: 경도시험/];
    VarIn4[/입력변수: 가열 노화 시험/];
    VarIn7[/입력변수: 압축영구변형/];
    VarIn8[/입력변수: 경도변화/];
    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5 & VarIn6 & VarIn7 & VarIn8
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{가열 노화 시험}
    C --> |True|D{"시험항목"}
    C --> |False|E{"시험항목"}

		E --> |인장강도|F[15.0 이상]
		E --> |연신율|G[300 이상]
		E --> |경도시험|H["45~60"]
		E --> |압축영구변형|L[25 이하]

		D --> |인장강도|I[13.0 이상]
		D --> |연신율|J[250 이상]
		D --> |경도변화|K[10 이하]

		F --> m([봉함용 고무 품질기준])
		G --> m
		H --> m
		I --> m
		J --> m
		K --> m
		L --> m
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def standards_for_sealing_materials_of_joint(bIHeaAgi, bITenStr, bIElo, bIHarTes, bIComDef, bIHarVar) ->str :
        """신축이음장치의 봉함용 고무 품질기준

        Args:
            bIHeaAgi (boolean): 가열노화시험
            bITenStr (boolean): 인장강도
            bIElo (boolean): 연신율
            bIHarTes (boolean): 경도시험
            bIComDef (boolean): 압축영구변형
            bIHarVar (boolean): 경도변화

        Returns:
            sOQuaSta (string): 신축이음장치의 봉함용 고무 품질기준
            sOTesMet (string): 시험 방법
        """

        if bIHeaAgi == True:
            if bITenStr == True:
                sOQuaSta = "13.0 MPa 이상"
                sOTesMet = "KS M 6518"
            elif bIElo == True:
                sOQuaSta = "250 % 이상"
                sOTesMet = "KS M 6518"
            elif bIHarVar == True:
                sOQuaSta = "10 이하"
                sOTesMet = "KS M 6518"
            return sOQuaSta, sOTesMet
        else:
            if bITenStr == True:
                sOQuaSta = "15.0 MPa 이상"
                sOTesMet = "KS M 6518"
            elif bIElo == True:
                sOQuaSta = "300 % 이상"
                sOTesMet = "KS M 6518"
            elif bIHarTes == True:
                sOQuaSta = "45 ~ 60"
                sOTesMet = "KS M 6518"
            elif bIComDef == True:
                sOQuaSta = "25 % 이하"
                sOTesMet = "KS M 6518"
            return sOQuaSta, sOTesMet