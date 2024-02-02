import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060301_13(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.3.1 (13)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '종방향 강성도 변수의 크기'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.3 보-슬래브 교량의 근사적 해석방법
    4.6.3.1 적용
    (13)
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
     A[종방향 강성도 변수];
     B["KDS 24 10 11 4.6.3.1 (13)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 종방향 강성도 변수/];
    VarIn1[/입력변수 : 보재료의 탄성계수/];
    VarIn2[/입력변수 : 바단판재료의 탄성계수/];
    VarIn3[/입력변수 : 보의 단면2차모멘트/];
    VarIn4[/입력변수 : 보의 중심과 바닥판의 중심사이의 거리/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn2
    end
    Python_Class~~~Variable_def
    C["<img src='https://latex.codecogs.com/svg.image?n=\frac{E_{B}}{E_{D}}'>"];
    D["<img src='https://latex.codecogs.com/svg.image?K_{g}=n(I+Ae_{g}^{2})'>-------------------------------------"];
    E(["종방향 강성도 변수"]);
    Variable_def--->C--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Longitudinal_stiffness_parameters(fIED,fII,fIEB,fIeg,fIA,fOKg) -> float:
        """종방향 강성도 변수의 크기
        Args:
            fIED (float): 바닥판재료의 탄성계수
            fII (float): 보의  단면 2차 모멘트
            fIEB (float): 보재료의 탄성계수
            fIeg (float): 보의 중심과 바닥판의중심사이의 거리
            fIA (float): 보의 단면적
            fOKg (float): 종방향 강성도 변수

        Returns:
            float: 종방향 강성도 변수의 크기
        """
        n=fIEB/fIED
        fOKg=n*(fII+fIA*fIeg**2)
        return("%.1e"%fOKg)


