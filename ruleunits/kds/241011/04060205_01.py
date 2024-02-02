import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060205_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.2.5 (1)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-06'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '캔틸레버 바닥판의 휨모멘트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.5 캔틸레버 바닥판
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
   # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
     subgraph Python_Class
     A[캔틸레버 바닥판에 작용하는 윤하중으로 발생되는 휨모멘트];
     B["KDS 24 10 11 4.6.2.5 (1)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 폭 1m당의 휨모멘트/];
    VarIn1[/입력변수 : 하중점에서 지지점까지의 거리/];
    VarIn2[/입력변수 : 설계차량활하중의1후륜하중/];
    end
    Python_Class~~~Variable_def
    D{"주철근이 차량진행방향에 직각인 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?E=0.8X+1.14'>------------------------"];
    F["<img src='https://latex.codecogs.com/svg.image?M=\frac{P}{E}X'>"];
    G(["휨모멘트"]);
    Variable_def--->D--->E--->F--->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def bending_moment(fIX,fIP,fOM) -> str:
        """주철근이 차량진행방향에 직각인 경우 캔틸레버 바닥판의 휨모멘트
        Args:
            fIX (float): 하중점에서 지지점까지의 거리
            fIP (float): 설계차량활하중의 1후륜하중
            fOM (float): 폭 1m당의 휨모멘트

        Returns:
            float: fOM ,주철근이 차량진행방향에 직각인 경우 캔틸레버 바닥판의 휨모멘트
        """

        fOM=fIP*fIX/(0.8*fIX+1.14)

        return fOM


