import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.3.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단철근을 사용하는 경우의 슬래브의 최소두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.3 슬래브
    4.6.3.2 전단철근
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
    A["전단철근"];
    B["KDS 24 14 21 4.6.3.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:슬래브의 최소두께/];

		VarIn1
		end

		Python_Class ~~~ Variable_def--->F

		F["슬래브의 최소두께≥200mm"]
		F --->G(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def minimum_slab_thickness(fIminslt) ->bool:
        """전단철근을 사용하는 경우의 슬래브의 최소두께
        Args:
             fIminslt (float): 주철근의 최대간격

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 슬래브의 최소두께가 건설기준 4.6.3.2(1)을 만족하는지 여부
        """
        # fIuserdefined = 1
        # 집중하중 또는 최대 휨모멘트가 작용하는 영역: fIuserdefined = 2

        if fIminslt>=200:
          return "Pass"
        else:
          return "Fail"


# 

