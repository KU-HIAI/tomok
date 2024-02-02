import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030102_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.1.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소 관입깊이'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.2 말뚝의 관입
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
    A[말뚝의 관입];
    B["KDS 24 14 51 3.3.1.2 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 노출된 말뚝 길이/];


			VarIn1

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C[가교 또는 단일현장타설말뚝에 사용하는 말뚝]
			D([말뚝의 설계 관입깊이])
			E[노출된 말뚝길이의 최소 1/3깊이까지관입]

			Variable_def ---> C ---> E ---> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def min_pile_length(fIExplen) -> float:
        """최소 관입깊이
        Args:
            fIExplen (float): 노출된 말뚝 길이
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.1.2 (2)의 최소 관입깊이

        """

        return fIExplen/3


# 

