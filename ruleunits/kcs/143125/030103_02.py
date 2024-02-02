import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_030103_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.3 (2)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.3 접합부 단차 수정
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.3 접합부 단차 수정
    (2) 품질관리 구분 ‘라’는 우천에 노출되어 있어 부식의 우려가 있는 교량의 경우에는 접합부 표면 높이 차이의 정도에 따라 표 3.1-3과 같이 처리한다.
    표 3.1-3 접합부 표면의 높이 차이 처리방법(교량)

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 높이 차이}           & {\color[HTML]{333333} 처리 방법}                 \\ \hline
{\color[HTML]{333333} 1 mm 이하}         & {\color[HTML]{333333} 별도 처리 불필요}             \\ \hline
{\color[HTML]{333333} 1 mm 초과 3 mm 미만} & {\color[HTML]{333333} 모재 접합면 높이 차이을 경사지게 가공} \\ \hline
{\color[HTML]{333333} 3 mm 이상}         & {\color[HTML]{333333} 끼움재 사용}                \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 접합부 표면의 높이 차이 처리방법_교량];
    B["KCS 14 31 25 3.1.3 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.3 (2)"])

    subgraph Variable_def
    VarOut[/출력변수: 접합부 표면의 높이 차이 처이 방법_교량/];
    VarIn1[/입력변수: 높이 차이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"높이 차이"}
    C --> |1 mm 이하|E["별도 처리 불필요"]
    C --> |1 mm 초과 3 mm 미만|F["모재 접합면 높이 차이를 경사지게 가공"]
    C --> |3 mm 이상|G["끼움재 사용"]
    E --> H(["접합부 표면의 높이 차이 처리방법_교량"])
    F --> H(["접합부 표면의 높이 차이 처리방법_교량"])
    G --> H(["접합부 표면의 높이 차이 처리방법_교량"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def method_for_joint_surface_difference_in_bridge(fIDifJoi) ->str :
        """접합부 표면의 높이 차이 처리 방법(교량)

        Args:
            fIDifJoi (float): 높이 차이

        Returns:
            sOJoiSur (string): 접합부 표면의 높이 차이 처리 방법(교량)


        """

        if fIDifJoi <= 1:
            sOJoiSur = "별도 처리 불필요"
            return sOJoiSur
        elif 1 < fIDifJoi < 3:
            sOJoiSur = "모재 접합면 높이 차이을 경사지게 가공"
            return sOJoiSur
        else:
            sOJoiSur = "끼움재 사용"
            return sOJoiSur