import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143130_030303_03(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 30 3.3.3 (3)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '조립 및 설치'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    조립 및 설치
    3. 시공
    3.3 부재조립 및 설치
    3.3.3 토목구조물의 현장조립(품질관리 구분 ‘라’)
    (3)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.3.3 토목구조물의 현장조립(품질관리 구분 ‘라’)
    (3) 부재의 현장조립
    ⑧ 조립의 정밀도는 표 3.3-1을 따르되, 기타 내용은 KCS 14 31 10(부록 1)의 부표 1.1 을 준수한다.
\begin{table}[]
\begin{tabular}{|l|l|}
\hline
항목                                                                  & 규격                                                                                        \\ \hline
\multirow{2}{*}{현장이음부의 간격}                                          & δ ≤ 10 (mm)                                                                               \\ \cline{2-2}
                                                                    & δ : 가조립 간격으로 부터의 조립오차                                                                     \\ \hline
\multirow{7}{*}{\begin{tabular}[c]{@{}l@{}}솟음\\ (치올림)\end{tabular}} & L ≤ 20 : -10 -$\sim$+15mm                                                                 \\ \cline{2-2}
                                                                    & 20 ＜ L ≤ 40 : -10 -$\sim$+20mm                                                            \\ \cline{2-2}
                                                                    & 40 ＜ L ≤ 200 : -{[}(L/2)-10{]} -$\sim$+(L/2)mm                                            \\ \cline{2-2}
                                                                    & 여기서 L은 교량받침이 있는 경우는 지간장(m)으로 하고 그 이외의 경우에는 경간장(m)으로 정의한다.                                 \\ \cline{2-2}
                                                                    & ① 상기값은 최대 솟음(치올림)위치에서의 허용값이며 지점에서의 허용값은 0                                                 \\ \cline{2-2}
                                                                    & ② 기타 위치에서의 허용값은 최대점 위치의 허용값을 꼭지점으로 하고 지점에서는 0이 되는 2차 또는 3차 포물선(솟음형상에 따라 결정)으로 보간한다.       \\ \cline{2-2}
                                                                    & ③강교 가설 후 최종 솟음(치올림)을 만족시키기 위해서는 강구조물의 자중에 의한 처짐과 콘크리트 슬래브 등 부가되는 자중에 의한 처짐을 분리하여 관리해야 한다. \\ \hline
\end{tabular}
\end{table}
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 토목구조물 부재의 조립 정밀도"];
    B["KCS 14 31 30 3.3.3 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 3.3.3 (3)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 현장 이음부 간격의 조립 오차"/];
    VarOut2[/"출력변수: 치올림의 허용값"/];

		VarIn1[/"입력변수: 지간장 혹은 경간장"/];
		VarIn2[/"입력변수: 현장 이음부 간격의 조립 오차"/];
		VarIn3[/"입력변수: 치올림의 허용값"/];

    VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
    end


Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"현장 이음부"}
    Variable_def --> E{"지간장 혹은 경간장 (L)"}


		D --> F[δ <= 10mm]
		F --> |True|G([PASS])
		F --> |False|K([FAIL])

		E --> |L <= 20|H["-10 <= 치올림의 허용값 <= +15"]
		E --> |20 < L <= 40|I["-10 <= 치올림의 허용값 <= +25"]
		E --> |40 < L <= 200|J["-[(L/2)-10] <= 치올림의 허용값 <= +(L/2)"]


		H --> |True|L([PASS])
		I --> |True|L([PASS])
		J --> |True|L([PASS])


		H --> |False|M([FAIL])
		I --> |False|M
		J --> |False|M



    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def assembly_precifion_of_civil_structure_components(fIAssDif, fIL, fITolDef) ->str :
        """토목구조물 부재의 조립 정밀도

        Args:
            fIAssDif (float) : 현장 이음부 간격의 조립 오차
            fIL (float): 지간장 혹은 경간장
            fITolDef (float): 치올림의 허용값

        Returns:
            sOAssDif (string) : 현장 이음부 간격의 조립 오차
            sOTolDef (string): 치올림의 허용값
        """

        if fIAssDif <= 10:
            sOAssDif = "PASS"
            if fIL <= 20:
                if -10 <= fITolDef <= 15:
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef

            elif 20 < fIL <= 40:
                if -10 <= fITolDef <= 20:
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef

            elif 40 < fIL <= 200:
                if -((fIL/2)-10) <= fITolDef <= (fIL/2):
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef


        else:
            sOAssDif = "FAIL"
            if fIL <= 20:
                if -10 <= fITolDef <= 15:
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef

            elif 20 < fIL <= 40:
                if -10 <= fITolDef <= 20:
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef

            elif 40 < fIL <= 200:
                if -((fIL/2)-10) <= fITolDef <= (fIL/2):
                    sOTolDef = "PASS"
                    return sOAssDif, sOTolDef
                else:
                    sOTolDef = "FAIL"
                    return sOAssDif, sOTolDef