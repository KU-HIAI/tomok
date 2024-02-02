import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_01040501_03(RuleUnit): # KDS241711_01040501_03

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 1.4.5.1 (3)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '지진의 재현주기'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    1. 일반사항
    1.4 내진설계의 기본방침
    1.4.5 철도 중요구조물의 내진설계 검토사항
    1.4.5.1 열차 주행의 안전성 검증
    (3)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    #### 1.4.5.1 열차 주행의 안전성 검증
    \n (3) 열차 주행의 안전성 검증에는 지진의 재현주기는 100년을 기준으로 한다.
    """

    # 플로우차트(mermaid)
    flowchart = """
  flowchart TD
		subgraph Python_Class
		A[지진의 재현주기] ;
		B["KDS 24 17 11 1.4.5.1 (3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 지진의 재현주기/] ;
		end

		Python_Class ~~~ Variable_def

		C["지진의 재현주기"] ;

		D([100년])

		Variable_def --> C --> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def earthquake_cycle(fOEarcyc) -> float:
        """지진의 재현주기

        Args:
            fOEarcyc (float): 지진의 재현주기

        Returns:
            float: 교량내진설계기준(한계상태설계법) 1.4.5.1 열차 주행의 안전성 검증 (3)의 값
        """

        fOEarcyc = 100
        return fOEarcyc




