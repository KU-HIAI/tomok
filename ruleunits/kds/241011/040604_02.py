import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_040604_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.4 (2)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '한 차로에만 재하 된 경우 차로 당 전단력과 모멘트에 대한 교축방향 스트립의 등가폭'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.4 슬래브교에 대한 등가 스트립 폭
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
     A[차로 당 전단력과 모멘트에 대한 교축방향 스트립의 등가폭];
     B["KDS 24 10 11 4.6.4 (2)~(3)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 등가폭/];
    VarIn1[/입력변수 : 실제 지간장/];
    VarIn2[/입력변수 : 실제교폭/];
    VarIn3[/입력변수 : KDS 24 12 21 4.3.1.1에 규정된 재하차로 수/];
    end
    Python_Class~~~Variable_def
    D["L1=Min(실제 지간장,18,000mm)"];
    E{"재하된 차로 수"};
    F["W1=Min(실제 교폭, 9,000mm)"];
    G["W1=Min(실제 교폭, 18,000mm)"];
    H["<img src='https://latex.codecogs.com/svg.image?E=1.2(250+0.42\sqrt{L_{1}W_{1}})'>------------------------------------"];
    I["<img src='https://latex.codecogs.com/svg.image?E=1.1(2100+0.12\sqrt{L_{1}W_{1}})(\leq\frac{W}{N_{L}}'>----------------------------------------------"];
    J(["교축방향 스트립의 등가폭"]);
    Variable_def--->D--->E--1--->F--->H--->J
    E-->2이상--->G--->I--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def fOE_040604_02(fOE,fILactsp,fIW,fINL) -> float:
        """한 차로에만 재하 된 경우 차로 당 전단력과 모멘트에 대한 교축방향 스트립의 등가폭

        Args:
            fOE (float): 등가폭
            fILactsp (float): 실제 지간장
            fIW (float): 실제 교폭
            fINL (float): KDS 24 12 21 4.3.1.1에 규정된 재하차로 수
        Returns:
            float: foE, 차로 이상 재하 된 경우 차로 당 전단력과 모멘트에 대한 교축방향 스트립의 등가폭
        """
        L1=min(fILactsp,18000)
        W1=min(fIW,9000)
        fOE=1.2*(250+0.42*(L1*W1)**0.5)
        return(fOE)


