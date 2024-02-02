import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS143125_030103_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 31 25 3.1.3 (1)' # 건설기준문서
    ref_date = '2023-09-11'  # 디지털 건설문서 작성일
    doc_date = '2019-05-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '볼트 접합 및 핀 연결'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    볼트 접합 및 핀 연결
    3. 시공
    3.1.3 접합부 단차 수정
    (1)
    """

    # 건설기준문서내용(text)
    content = """
    #### 3.1.3 접합부 단차 수정
    (1) 품질관리 구분 ‘나’, ‘다’에서 접합되는 부재의 표면 높이가 서로 차이가 있는 경우 표 3.1-2와 같이 처리한다.
    표 3.1-2 접합부 표면의 높이 차이 처리방법(건물)

\begin{table}[]
\begin{tabular}{|
>{\columncolor[HTML]{FFFFFF}}l |
>{\columncolor[HTML]{FFFFFF}}l |}
\hline
{\color[HTML]{333333} 높이 차이}   & {\color[HTML]{333333} 처리 방법}     \\ \hline
{\color[HTML]{333333} 1 mm 이하} & {\color[HTML]{333333} 별도 처리 불필요} \\ \hline
{\color[HTML]{333333} 1 mm 초과} & {\color[HTML]{333333} 끼움재 사용}    \\ \hline
\end{tabular}
\end{table}

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A[Title: 접합부 표면의 높이 차이 처리방법_건물];
    B["KCS 14 31 25 3.1.3 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 25 3.1.3 (1)"])

    subgraph Variable_def
    VarOut[/출력변수: 접합부 표면의 높이 차이 처이 방법_건물/];
    VarIn1[/입력변수: 높이 차이/];
    VarOut ~~~ VarIn1
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"높이 차이"}
    C --> |1 mm 이하|E["별도 처리 불필요"]
    C --> |1 mm 초과|F["끼움재 사용"]
    E --> G(["접합부 표면의 높이 차이 처리방법_건물"])
    F --> G(["접합부 표면의 높이 차이 처리방법_건물"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def method_for_joint_surface_difference_in_building(fIDifJoi) ->str :
        """접합부 표면의 높이 차이 처리 방법(건물)

        Args:
            fIDifJoi (float): 높이 차이

        Returns:
            sOJoiSur (string): 접합부 표면의 높이 차이 처리 방법(건물)


        """

        if fIDifJoi <= 1:
            sOJoiSur = "별도 처리 불필요"
            return sOJoiSur
        else:
            sOJoiSur = "끼움재 사용"
            return sOJoiSur