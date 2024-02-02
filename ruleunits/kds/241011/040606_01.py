import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_040606_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.6 (1)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '슬래브교에 대한 등가 스트립 폭'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.6 유효길이계수, K
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
     A[설계시 유효계수길이];
     B["KDS 24 10 11 4.6.6 (1)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 유효길이계수/];
   end
     Python_Class~~~Variable_def
    C{"이상화된 구속 조건이 실제 구속조건을 완전히 충족시키지 못하는 경우"};
    D{"지지 조건"};
    E["K 설계치=0.65"];
    F["K 설계치=0.80"];
    G["K 설계치=1.2"];
    H["K 설계치=1.0"];
    I["K 설계치=2.1"];
    J["K 설계치=2.0"];
    K["양단 회전변위,수평이동 구속"];
    N{"일단 회전변위,수평이동 구속"};
    M["양단 수평이동 구속, 회전변위 자유"];
    O{"일단 수평이동 구속, 회전변위 자유"};
    P(["유효계수길이"]);
    Variable_def--->C--->D--->K--->E--->P
    D--->N--다른 단 수평이동 구속, 회전변위 자유--->F--->P
    N--다른 단 수평이동 자유, 회전변위 구속--->G--->P
    D--->M--->H--->P
    N--다른 단 수평이동 자유, 회전변위 자유--->I--->P
    D--->O--다른 단 수평이동 자유, 회전변위 구속--->J--->P
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def fOK_040606_01(fOK,fIuserdefined) -> float:
        """슬래브교에 대한 등가 스트립 폭
        Args:
            fOK (float): 유효길이계수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 두 차로 이상 재하 된 경우 차로 당 전단력과 모멘트에 대한 교축방향 스트립의 등가폭
        """
        if fIuserdefined == 1: #양단 회전변위,수평이동 구속
          fOK=0.65
          return fOK
        if fIuserdefined == 2: #일단 회전변위,수평이동 구속/다른단 수평이동 구속, 회전변위 자유
          fOK=0.80
          return fOK
        if fIuserdefined == 3: #일단 회전변위,수평이동 구속/다른단 수평이동 자유, 회전변위 구속
          fOK=1.2
          return fOK
        if fIuserdefined == 4: #일단 회전변위,수평이동 구속/다른단 수평이동 구속, 회전변위 구속
          fOK=2.1
          return fOK
        if fIuserdefined == 5: #양단 수평이동 구속,회전변위 자유
          fOK=1.0
          return fOK
        if fIuserdefined == 6: #일단 수평이동 구속,회전변위 자유
          fOK=2.0
          return fOK


