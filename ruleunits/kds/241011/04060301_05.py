import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241011_04060301_05(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 10 11 4.6.3.1 (5)' # 건설기준문서
    ref_date = '2021-04-15'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-16'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '보-슬래브 교량의 근사적 해석방법의 적용'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량 설계 일반사항(한계상태설계법)
    4. 구조해석
    4.6 정적 해석
    4.6.3 보-슬래브 교량의 근사적 해석방법
    4.6.3.1 적용
    (5)
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
     A[보-슬래브 교량의 근사적 해석 적용];
     B["KDS 24 10 11 4.6.3.1 (5)"];
     A ~~~ B
     end
    subgraph Variable_def
    VarIn1[/입력변수 : 차도의 내민부분/];
    VarIn2[/입력변수 : 면내 곡률/];
    VarIn3[/입력변수 : 4.6.1.2의 한계값/];
    end
    Python_Class~~~Variable_def
    D["910mm &ge; 차도의 내민부분"];
    E["면내 곡률< 4.6.1.2의 한계값"];
    F(["Pass or Fail"]);
    Variable_def--->D--Yes--->E--->F
    D--No--->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def indented_part_of_driveway(fIde,fIcurvpl,fIlimmit) -> bool:
        """4.6.2.8(5)의 내용 부합 여부
        Args:
            fIde (float): 차도의 내민부분.
            fIcurvpl (float): 면내 곡률.
            fIlimmit (float): 4.6.1.2의 한계값.

        Returns:
            bool: 4.6.2.8(5)의 내용 부합 여부
        """
        if fIde<=910:
          if fIcurvpl<fIlimmit:
            return "Pass"
          else:
            return "Fail"
        else:
            return "Fail"


