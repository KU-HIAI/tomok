import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04030404_01(RuleUnit): # KDS241711_04030404_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.3.4.4 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-22'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '모드의 수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.3 해석방법
    4.3.4 다중모드스펙트럼해석법
    4.3.4.4 모드 수
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
	A([모드 수])
	B["KDS 24 17 11 4.3.4.4(1)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarIn1[/입력변수: 모드의 수/]
	VarIn2[/입력변수: 지간 수/]
	VarIn3[/입력변수: 잔여모드/]
	VarIn1 & VarIn2
	end
	Python_Class ~~~ Variable_def --> D & E --> F
	D["모드의 수 ≥ 지간 수 x3"]
	E["모드의 수 + 잔여모드 < 응답 x 1.1"]
	F([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def numbers_of_modes(fInuofmo,fInuofsp,fIremmod) -> bool:
        """모드의 수

        Args:
            fInuofmo (float): 모드의 수
            fInuofsp (float): 지간 수
            fIremmod (float): 잔여모드
        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.3.4.4 모드 수 (1)의 통과 여부
        """
        if fInuofmo >= fInuofsp * 3 and (fInuofmo + fIremmod) < fInuofmo * 1.1:
          return 'Pass'
        else:
          return 'Fail'