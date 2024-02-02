import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_010703_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 1.7.3 (2)' # 건설기준문서
    ref_date = '2023-09-25'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    1. 일반사항
    1.7 레디믹스트 콘크리트 품질에 대한 지정
    1.7.3 슬럼프 및 슬럼프 플로
    (2)

    """

    # 건설기준문서내용(text)
    content = """
    #### 1.7.3 슬럼프 및 슬럼프 플로
    (2) 슬럼프 플로로 품질을 지정하는 경우 KS F 2594의 규정에 따라 시험하고 슬럼프 플로의 허용오차는 표 1.7-3에 따라야 한다.

표 1.7-3 슬럼프 플로의 허용오차(mm)2)

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 슬럼프 플로}}                                          & {\color[HTML]{333333} 슬럼프 플로의 허용오차}                                          \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 500}}                                             & {\color[HTML]{333333} ± 75}                                                  \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 600}}                                             & {\color[HTML]{333333} ± 100}                                                 \\ \hline
\multicolumn{1}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} 700 1)}}                                          & {\color[HTML]{333333} ± 100}                                                 \\ \hline
\multicolumn{2}{|l|}{\cellcolor[HTML]{FFFFFF}{\color[HTML]{333333} \begin{tabular}[c]{@{}l@{}}주 1) 굵은 골재의 최대 치수가 13 mm인 경우에 한하여 적용한다.\\ 2) 이 기준은 설계기준압축강도 40 MPa 미만의 콘크리트에 한하여 적용한다.\end{tabular}}} \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 슬럼프 플로의 허용오차"];
    B["KCS 14 31 30 1.7.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 1.7.3 (2)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 슬럼프 플로의 허용오차"/];

		VarIn1[/"입력변수: 슬럼프 플로"/];
		VarIn2[/"입력변수: 굵은골재 최대 치수"/];
		VarIn3[/"입력변수: 설계기준압축강도"/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"설계기준강도 < 40 MPa"}


		D --> |True|E{"굵은골재 최대 치수 = 13 mm"}

		E --> |ALL|F{슬럼프 플로}
		E --> |True|G{슬럼프 플로}


		F --> |500|H["±75"]
		F --> |600|I["±100"]
		G --> |700|J["±100"]

		H --> K([슬럼프 플로의 허용오차])
		I --> K([슬럼프 플로의 허용오차])
		J --> K([슬럼프 플로의 허용오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def slump_flow_tolerance(fISluFlo, fIMaxAgg, fIComStr) ->str :
        """슬럼프 플로의 허용오차

        Args:
            fISluFlo (float): 슬럼프 플로
            fIMaxAgg (float): 굵은골재 최대 치수
            fIComStr (float): 설계기준압축강도

        Returns:
            sOTolSlu (string): 슬럼프 플로의 허용오차

        """

        if fIComStr < 40:
            if fISluFlo == 500:
                sOTolSlu = "±75 mm"
                return sOTolSlu
            elif fISluFlo == 600:
                sOTolSlu = "±100 mm"
                return sOTolSlu
            elif (fIMaxAgg == 13) and (fISluFlo == 700):
                sOTolSlu = "±100 mm"
                return sOTolSlu