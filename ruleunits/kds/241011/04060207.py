import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060207 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.2.7' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '등분포 고정하중에 의한 휨모멘트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.7 등분포 고정하중에 의한 휨모멘트
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
     A[등분포 고정하중에 의한 바닥판의 단위폭당 설계휨모멘트];
     B["KDS 24 10 11 4.6.2.7"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 설계휨모멘트/];
    VarIn1[/입력변수 : 등분포 고정하중/];
    VarIn2[/입력변수 : 고정하중에 대한 바닥판의 지간/];
    end
    Python_Class~~~Variable_def
    D{"판의 구분"};
    E{"휨모멘트의 종류"};
    K{"휨모멘트의 종류"};
    N{"휨모멘트의 종류"};
    F["<img src='https://latex.codecogs.com/svg.image?+wl_{d}^{2}/8'>"];
    G["<img src='https://latex.codecogs.com/svg.image?-wl_{d}^{2}/2'>"];
    H["<img src='https://latex.codecogs.com/svg.image?+wl_{d}^{2}/10'>"];
    I["<img src='https://latex.codecogs.com/svg.image?-wl_{d}^{2}/10'>"];
    J(["바닥판 지간방향의 단위폭당 설계휨모멘트"]);
    Variable_def--->D--단순판--->E--지간 휨모멘트--->F--->J
    D--캔틸레버판--->K--지점 휨모멘트--->G--->J
    D--연속판--->N--지간 휨모멘트--->H--->J
    N--지점 휨모멘트--->I--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def fOM(fIw,fIld,fOM,fIuserdefined) -> float:
        """등분포 고정하중에 의한 휨모멘트
        Args:
            fIw (float): 등분포 고정하중
            fIld (float): 고정하중에 대한 바닥판의 지간
            fOM (float): 단위폭당 바닥판 지간방향의 휨모멘트
            fIuserdefined (float): 사용자 선택

        Returns:
            float: fOM,등분포 고정하중에 의한 휨모멘트
        """
        if fIuserdefined == 1: #단순판, 지간 휨모멘트
            fOM=fIw*fIld**2/8
            return fOM
        if fIuserdefined == 2: #캔틸레버판, 지점 휨모멘트
            fOM=-fIw*fIld**2/2
            return fOM
        if fIuserdefined == 3: #연속판, 지간 휨모멘트
            fOM=fIw*fIld**2/10
            return fOM
        if fIuserdefined == 4: #연속판, 지점 휨모멘트
            fOM=-fIw*fIld**2/10
            return fOM


