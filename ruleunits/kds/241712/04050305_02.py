import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04050305_02(RuleUnit): # KDS241712_04050305_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.5.3.5 (2)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-19'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '횡방향철근의 최대수직간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.3 주탑 및 기둥
    4.5.3.5 단부구역의 횡방향철근상세
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
    A[단부구역의 횡방향철근상세];
    B["KDS 24 17 12 4.5.3.5 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 횡방향철근의 최대수직간격/];
    VarIn2[/입력변수: 부재 최소 단면치수/];
		VarIn3[/입력변수: 축방향철근지름/];


	 VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def--->E--->D




		E["횡방향철근의 최대수직간격≤부재 최소 단면치수 X 1/4, 횡방향철근의 최대수직간격≤축방향철근지름 X 6 "]
		D(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def maximum_vertical_spacing_of_transverse_steel(fImavstr,fImacsdm,fIlogrdi) -> bool:
        """횡방향철근의 최대수직간격

        Args:
            fImavstr (float): 횡방향철근의 최대수직간격
            fImacsdm (float): 부재 최소 단면치수
            fIlogrdi (float): 축방향철근지름

        Returns:
            bool: 교량내진 설계기준(케이블교량) 4.5.3.5 (2)의 통과여부
        """
        if 0.25*fImacsdm >= fImavstr and 6*fIlogrdi >= fImavstr:
          return("Pass")
        else:
          return("Fail")


