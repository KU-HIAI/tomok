import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS244010_0202_08(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 24 40 10 2.2 (8)'
    ref_date = '2023-09-11'
    doc_date = '2018-08-30'
    title = '신축이음장치의 봉함용 고무 품질기준'

    description = """
    신축이음
    2. 자재
    2.2 재료
    (8)
    """

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

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 신축이음장치의 봉함용 고무 품질기준];
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

    @rule_method
    def standards_for_sealing_materials_of_joint(bIHeaAgi, bITenStr, bIElo, bIHarTes, bIComDef, bIHarVar) -> str :
        """신축이음장치의 봉함용 고무 품질기준

        Args:
            bIHeaAgi (bool): 가열노화시험
            bITenStr (bool): 인장강도
            bIElo (bool): 연신율
            bIHarTes (bool): 경도시험
            bIComDef (bool): 압축영구변형
            bIHarVar (bool): 경도변화

        Returns:
            sOQuaSta (str): 신축이음장치의 봉함용 고무 품질기준
            sOTesMet (str): 시험 방법
        """
        assert isinstance(bIHeaAgi, bool)
        assert isinstance(bITenStr, bool)
        assert isinstance(bIElo, bool)
        assert isinstance(bIHarTes, bool)
        assert isinstance(bIComDef, bool)
        assert isinstance(bIHarVar, bool)
        assert (bITenStr + bIElo + bIHarVar + bIHarTes + bIComDef) == 1

        sOQuaSta = ""
        sOTesMet = ""

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

        return RuleUnitResult(
                result_variables = {
                    "sOTesMet": sOTesMet,
                    "sOQuaSta": sOQuaSta,
                }
            )