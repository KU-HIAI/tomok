import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_040604_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.4 (4)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '감소계수 r'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.4 슬래브교에 대한 등가 스트립 폭
    (4)
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
     A[사교에서의 종방향 부재단면력의 감소계수];
     B["KDS 24 10 11 4.6.4 (4)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarOut[/출력변수 : 감소계수/];
    VarIn1[/입력변수 : 사각/];
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?r=1.05-0.25tan\theta(\leq&space;1.00)'>-------------------------------"];
    E(["감소계수"]);
    Variable_def--->D--->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def fOr_040604_04(fIskeang,fOr) -> float:
        """감소계수 r

        Args:
            fIskeang (float): 실제 지간장
            fOr (float): 감소계수

        Returns:
            float: 4.6.4(4)의 감소계수 r
        """
        fOr=1.05-0.25*math.tan(math.radians(fIskeang))
        if fOr <=1.00:
          return fOr
        else:
          return "Fail"


