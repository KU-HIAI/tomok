import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_040506_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.6 (8)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '표피철근 단면적'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.6 지름이 큰 철근에 대한 추가 규정
    (8)
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
    A["지름이 큰 철근에 대한 추가 규정"];
    B["KDS 24 14 21 4.5.6 (8)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 표피철근 단면적/];
		VarIn2[/입력변수: 지름이 큰 철근에 대한 표피철근 단면적/];

		VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def--->C

		C{"큰 지름 철근의 방향"}
		C--직각 방향--->D
		C--평행한 방향--->E

		D["<img src='https://latex.codecogs.com/svg.image?0.01A_{ct,ext}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?0.02A_{ct,ext}'>---------------------------------"]
		D & E ---> G(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Skin_rebar_cross_sectional_area(fIskrcse,fIActext,fIuserdefined) -> float:
        """표피철근 단면적

        Args:
            fIskrcse (float): 표피철근 단면적
            fIActext (float): 지름이 큰 철근에 대한 표피철근 단면적
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.6 지름이 큰 철근에 대한 추가 규정 (8)의 값
        """

        #직각 방향 : fIuserdefined == 1
        #평행한 방향 : fIuserdefined == 2

        if fIuserdefined == 1:
          if fIskrcse >= 0.01*fIActext:
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          if fIskrcse >= 0.02*fIActext:
            return "Pass"
          else:
            return "Fail"


# 

