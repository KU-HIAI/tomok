import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04050701_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.7.1 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '등가지름'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.7 다발철근에 대한 추가 규정
    4.5.7.1 일반사항
    (3)
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
    A["등가지름"];
    B["KDS 24 14 21 4.5.7.1 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 다발에서의 철근의 수/];
		VarIn2[/입력변수: 철근의 지름/];
		VarOut1[/출력변수: 등가지름/];

		VarOut1~~~VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def--->D---->E

		D["<img src='https://latex.codecogs.com/svg.image?d_{b,n}=d_b\sqrt{n_b}\leq&space;55mm'>---------------------------------"]

		E(["등가지름"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def equivalent_diameter(fOdbn,fInb,fIdb,fIuserdefined) -> float:
        """등가지름

        Args:
            fOdbn (float): 등가지름
            fInb (float): 다발에서의 철근의 수
            fIdb (float): 철근의 지름
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.7.1 일반사항 (3)의 값
        """

        #압축영역의 수직철근과 겹침이음 연결부의 철근 : fIuserdefined == 1
        #그 외의 경우 : fIuserdefined == 2

        if fIuserdefined == 1:
          if fInb <= 4:
            fOdbn = min(fIdb*fInb**0.5, 55)
            return fOdbn
          else:
            return "Fail"

        if fIuserdefined == 2:
          if fInb <= 3:
            fOdbn = min(fIdb*fInb**0.5, 55)
            return fOdbn
          else:
            return "Fail"


# 

