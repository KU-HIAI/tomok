import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060301_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.3.1 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근 최대간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.3 슬래브
    4.6.3.1 휨철근
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
    A["철근의 최대간격"];
    B["KDS 24 14 21 4.6.3.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:주철근의 최대간격/];
		VarIn2[/입력변수:슬래브 깊이/];
		VarIn3[/입력변수:배력철근의 최대간격/]

		VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ Variable_def--->E

		E{"철근 최대간격"}
		E--주철근--->D["3h≤400mm"]
		E--배력철근--->F["3.5h≤450mm"]
		D & F ---> K(["Pass or Fail"])

		Variable_def--"집중하중 또는 최대 휨모멘트가 작용하는 영역"-->H
		H{"철근 최대간격"}
		H--주철근--->I["2h≤250mm"]
		H--배력철근--->J["3h≤400mm"]
		I & J ---> L(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_spacing_between_reinforcing_bars(fImaspmr,fIh,fImasprr,fIuserdefined) ->float:
        """철근 최대간격
        Args:
             fImaspmr (float): 주철근의 최대간격
             fIh (float): 슬래브 깊이
             fImasprr (float): 배력철근의 최대간격
             fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.3.1 휨철근의 철근 최대간격(1)의 값
        """
        # fIuserdefined = 1
        # 집중하중 또는 최대 휨모멘트가 작용하는 영역: fIuserdefined = 2

        if fIuserdefined == 1:
          fImaspmr = 3*fIh
          fImasprr = 3.5*fIh
          if fImaspmr <= 400 and fImasprr <= 450 :
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined == 2:
          fImaspmr = 2*fIh
          fImasprr = 3*fIh
          if fImaspmr <= 250 and fImasprr <= 400 :
            return "Pass"
          else:
            return "Fail"


# 

