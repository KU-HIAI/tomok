import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060504_11(RuleUnit): # KDS241711_04060504_11

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.5.4 (11)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '보강 띠철근간의 수평간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.5 중공원형 교각
    4.6.5.4 소성힌지구역에서의 심부구속 방향
    (11)
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
    A[중공원형 교각에서의 보강 띠철근간의 수평간격];
    B["KDS 24 17 11 4.6.5.4 (11)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 보강 띠철근간의 수평간격/] ;
    VarIn2[/입력변수: 심부구속 후프철근 호칭지름/];
    end

    Python_Class ~~~ Variable_def -->H
    H["심부구속 후프철근 호칭지름 x30 &ge; 보강 띠철근간의 수평간격"]
   	I([Pass or Fail])

		H -->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def horizontal_rebar_spacing(fIhosprb,fInddrhr) -> bool:
        """보강 띠철근간의 수평간격

        Args:
            fIhosprb (flaot): 보강 띠철근간의 수평간격
            fInddrhr (flaot): 심부구속 후프철근 호칭지름

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.6.5.4 중공원형 교각 (11)의 통과 여부
        """

        if fIhosprb <= 30 * fInddrhr:
          return "Pass"
        else:
          return "Fail"