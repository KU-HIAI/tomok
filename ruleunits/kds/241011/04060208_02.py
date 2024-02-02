import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060208_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.2.8 (2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-13'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '단부보의 설계에 사용되는 활하중 휨모멘트의 크기'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.2 바닥판의 해석방법
    4.6.2.8 종방향 단부보
    (2)
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
     A[단부보의 설계에 사용되는 활하중 휨모멘트];
     B["KDS 24 10 11 4.6.2.8 (2)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 활하중 휨모멘트/];
    VarIn1[/입력변수 : 윤하중/];
    VarIn2[/입력변수 : 종방향 단부보의 지간/];
    end
    Python_Class~~~Variable_def
    E{"바닥판 구분"};
    F["활하중 휨모멘트=0.10PL"];
    G["활하중 휨모멘트=0.08PL"];
    H(["활하중 휨모멘트"]);
    Variable_def--->E--단순판--->F--->H
    E--연속판--->G--->H
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Live_load_bending_moment(fIP,fIL,fOMloadl,fIuserdefined) -> float:
        """단부보의 설계에 사용되는 활하중 휨모멘트의 크기
        Args:
            fIP (float): 윤하중
            fIL (float): 종방향 단부보의 지간
            fOMloadl (float): 활하중 휨모멘트
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 단부보의 설계에 사용되는 활하중 휨모멘트의 크기
        """

        if fIuserdefined == 1: #단순판
            fOMloadl=0.10*fIP*fIL
            return fOMloadl
        if fIuserdefined == 2: #연속판
            fOMloadl=0.08*fIP*fIL
            return fOMloadl


