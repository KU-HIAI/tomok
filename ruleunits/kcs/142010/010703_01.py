import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_010703_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 1.7.3 (1)' # 건설기준문서
    ref_date = '2023-09-25'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    1. 일반사항
    1.7 레디믹스트 콘크리트 품질에 대한 지정
    1.7.3 슬럼프 및 슬럼프 플로
    (1)

    """

    # 건설기준문서내용(text)
    content = """
    #### 1.7.3 슬럼프 및 슬럼프 플로
    (1) 슬럼프는 KS F 2402의 규정에 따라 시험한 후 그 결과값과 호칭 슬럼프의 허용오차는 표 1.7-2에 따라야 한다.
 1.7-2 슬럼프의 허용오차(mm)
 \begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 슬럼프}     & {\color[HTML]{333333} 슬럼프 허용오차} \\ \hline
{\color[HTML]{333333} 25}      & {\color[HTML]{333333} ± 10}     \\ \hline
{\color[HTML]{333333} 50 및 65} & {\color[HTML]{333333} ± 15}     \\ \hline
{\color[HTML]{333333} 80 이상}   & {\color[HTML]{333333} ± 25}     \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 슬럼프의 허용오차"];
    B["KCS 14 31 30 1.7.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 1.7.3 (1)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 슬럼프의 허용오차"/];

		VarIn1[/"입력변수: 슬럼프"/];


    VarOut1 ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"슬럼프"}


		D --> |슬럼프 = 25|G["±10"]
		D --> |슬럼프 = 50 or 65|H["±15"]
		D --> |슬럼프 => 80|K["±25"]

		G --> E([슬럼프의 허용오차])
		H --> E([슬럼프의 허용오차])
		K --> E([슬럼프의 허용오차])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def slump_tolerance(fISlump) ->str :
        """슬럼프의 허용오차

        Args:
            fISlump (float): 슬럼프

        Returns:
            sOTolSlu (string): 슬럼프의 허용오차

        """

        if fISlump == 25:
            sOTolSlu = "±10 mm"
            return sOTolSlu
        elif (fISlump == 50) or (fISlump == 65):
            sOTolSlu = "±15 mm"
            return sOTolSlu
        elif fISlump >= 80:
            sOTolSlu = "±25 mm"
            return sOTolSlu