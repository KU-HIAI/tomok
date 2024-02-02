import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060605_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.6.5 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '띠철근 배치'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.5 띠철근 상세
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
    A["띠철근 상세"];
    B["KDS 24 14 21 4.6.6.5 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:중심간격/];
		VarIn2[/입력변수:축방향 철근과의 순간격/];


		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C
		C{기둥에 소성힌지가 형성되도록 설계하는 경우}
		C--Yes---> G
		C--NO--->F
		G["축방향 철근과의 순간격≤150mm"]
		F["중심간격≤60mm"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Spacing_of_tie(fIcenspa, fIinsgai, fIuserdefined) ->bool:
        """나선철근의 순간격
        Args:
             fIcenspa (float): 중심간격
             fIinsgai (float): 축방향 철근과의 순간격
             fIuserdefined (float): 사용자 선택
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.6.5 (4) 설계기준에 따른
        """
        #기둥에 소성힌지가 형성되도록 설계하는 경우: fIuserdefined = 1
        if fIuserdefined == 1:
          if fIinsgai <= 150:
            return "Pass"
          else:
            return "Fail"
        else:
          if fIcenspa <= 600:
            return "Pass"
          else:
            return "Fail"


# 

