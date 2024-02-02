import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04010102_05(RuleUnit): # KDS241711_04010102_05

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.1.1.2 (5)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-19'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '유효수평지반가속도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.1 설계일반사항
    4.1.1 설계지반운동
    4.1.1.2 지진위험도 및 유효수평지반가속도
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
		A[지진위험도 및 유효수평지반가속도] ;
		B["KDS 24 17 11 4.1.1.2 (5)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 유효수평지반가속도/] ;
		VarIn1[/입력변수: 지진구역계수/] ;
		VarIn2[/입력변수: 평균재현주기의 위험도계수/] ;
		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		end

		Python_Class ~~~ Variable_def

		C{국가지진위험지도를 이용하여 결정하는 경우}

		F["<img src='https://latex.codecogs.com/svg.image?&space;S\geq&space;0.8\times&space;Z\times&space;I'>--------------------------"]

		E([PASS or Fail]) ;

		Variable_def --> C --> F --> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def effective_horizontal_ground_acceleration(fOS,fIZ,fII) -> bool:
        """유효수평지반가속도

        Args:
            fOS (float): 유효수평지반가속도
            fIZ (float): 지진구역계수
            fII (float): 평균재현주기의 위험도계수

        Returns:
            bool: 국가지진위험지도를 이용하여 결정한 유효수평지반가속도가 행정구역에 의해 결정한 값의 80%보다 작지 않은지 여부
        """
        fIZ = fIZ
        if fOS >= 0.8 * fIZ * fII:
          return("Pass")
        else:
          return("Fail")


