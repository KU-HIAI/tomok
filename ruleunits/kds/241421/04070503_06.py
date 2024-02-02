import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070503_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.5.3 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '횡방향 포스트텐션 긴장재 이음부의 압축깊이'  # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.3 프리캐스트 슬래브교
    (6)
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
    A["프리캐스트 슬래브교"];
    B["KDS 24 14 21 4.7.5.3 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:이음부의 압축깊이/];
		VarIn2[/입력변수:손실 후의 프리스트레스/];

		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def
		Variable_def--->D
		Variable_def--->E
		D["이음부의 압축깊이≥175mm"]
		E["손실 후의 프리스트레스≤1.7MPa"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Compression_depth_of_joint (fIcomdjo, fIprealo) ->bool:
        """횡방향 포스트텐션 긴장재 이음부의 압축깊이
        Args:
             fIcomdjo (float): 콘크리트의 최소두께
             fIprealo (float): 손실 후의 프리스트레스
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.5.3 (6) 설계기준에 따른 횡방향 포스트텐션 긴장재 이음부의 압축깊이 적합여부
        """
        if fIcomdjo >= 175 and fIprealo >= 1.7:
          return "Pass"
        else:
          return "Fail"


# 

