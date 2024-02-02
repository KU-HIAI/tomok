import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060202_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단강도에 기여하는 굽힘철근의 정착길이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.2 종방향 인장 철근의 길이 방향 배치
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
    A["종방향 인장 철근의 길이 방향 배치"];
    B["KDS 24 14 21 4.6.2.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:굽힘철근의 정착길이/];
		VarIn2[/입력변수: 설계정착길이/];
		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def--->F

		F{"굽힘철근의 정착길이"}
		F--인장영역--->G
		G["인장영역≥1.3lbd"]
		F--압축영역--->H
		H["압축영역≥0.7lbd"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Settlement_length_of_bending_rebar(fIsetlnr,fIlbd,fIuserdefined) ->bool:
        """전단강도에 기여하는 굽힘철근의 정착길이
        Args:
             fIsetlnr (float): 굽힘철근의 정착길이
             fIlbd (float): 설계정착길이
             fIuserdefined (float): 사용자 선택

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 전단강도에 기여하는 굽힘철근의 정착길이가 4.6.2.2(4)의 건설기준을 만족하는지 여부
        """
        if fIuserdefined==1: #인장영역
          if fIsetlnr>=1.3*fIlbd:
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined==2: #압축영역
          if fIsetlnr>=0.7*fIlbd:
            return "Pass"
          else:
            return "Fail"


# 

