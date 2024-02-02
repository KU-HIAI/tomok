import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS171000_0201_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 17 10 00 2.1 (2)' # 건설기준문서
    ref_date = '2018-12-06'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-12-26'  # 건설기준문서 -> 디지털 건설기준 변환 기준일 (작성 년월)
    title = '기반암 전단파 속도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    내진설계 일반
    2. 조사 및 계획
    2.1 지반조사
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
    A["기반암 전단파 속도"];
    B["KDS 17 10 00 2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:전단파 속도/];

		VarIn1
		end

		Python_Class ~~~ Variable_def
		Variable_def--->D
		D["전단파속도≥760m/s"]
		D --->E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Bedrock_shear_wave_velocity(fIVs) -> bool:
        """기반암 전단파 속도
        Args:
            fIVs (float): 전단파속도

        Returns:
            bool: 내진설계 일반  2.1 지반조사 (2)의 통과 여부
        """

        if fIVs >= 760:
            return 'Pass'
        else:
            return 'Fail'


