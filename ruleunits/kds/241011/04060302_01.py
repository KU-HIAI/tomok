import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060302_01(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.3.2 (1)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '모멘트 및 전단 분배계수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.3 보-슬래브 교량의 근사적 해석방법
    4.6.3.2 모멘트 및 전단 분배계수
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
     A[콘크리트 바닥판을 지지하는 내측거더];
     B["KDS 24 10 11 4.6.3.2 (1)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : I/J/];
    VarIn2[/입력변수 : 종방향 강성도 변수/];
    VarIn3[/입력변수 : 지간/];
    VarIn4[/입력변수 : 콘크리트 슬래브의 두께/];
    end
    Python_Class~~~Variable_def
    D{"기본설계의 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?K_{g}/()Lt_{s}^{3})=1.0&space;and&space;I/J=1.0'>-------------------------------------------"];
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def fIratIJ_04060302_01(fIratIJ,fIKg,fIL,fIts) -> float:
        """기본 설계 시 적용 값
        Args:
            fIratIJ (float): I/J.
            fIKg (float): 종방향 강성도 변수.
            fIL(float): 지간.
            fIts (float): 콘크리트 슬래브의 두께.

        Returns:
            float: 기본 설계 시 적용 값
        """
        A=fIKg/(fIL*fIts**3)
        if A==1.0:
          if fIratIJ==1.0:
            return "Pass"
          else:
            return "Fail"
        else:
          return "Fail"


