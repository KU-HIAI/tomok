import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060605_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.6.5 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '띠철근의 간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.5 띠철근 상세
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
    A["띠철근 상세"];
    B["KDS 24 14 21 4.6.6.5 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:띠철근의 간격/];
		VarIn2[/입력변수:축방향 철근 최소 지름/];
		VarIn3[/입력변수:압축부재의 최소치수/];
		VarIn4[/입력변수:띠철근의 간격/];
		VarIn5[/입력변수:부재 최소치수/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C
		C{D32보다 큰 철근을 다발로 한경우}
		C--yes---> G
		C--NO--->F
		F["띠철근의 간격≤부재 최소 치수 X1/2, 150mm"]

		G["띠철근의 간격≤압축부재의 최소치수, 400mm, 방향 철근 최소 지름X20"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Spacing_of_tie(fIspatie, fImidiaa, fImdimcm, fImemmdi, fIuserdefined) ->bool:
        """나선철근의 순간격
        Args:
             fIspatie (float): 띠철근의 간격
             fImidiaa (float): 축방향 철근 최소 지름
             fImdimcm (float): 압축부재의 최소치수
             fImemmdi (float): 부재 최소치수
             fIuserdefined (float): 사용자 선택
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.6.5 (3) 설계기준에 따른 띠철근의 간격 적합여부
        """
        # D32보다 큰 철근을 다발로 한 경우: fIuserdefined = 1

        if fIuserdefined == 1:
          if fIspatie <= fImidiaa*20 and fIspatie<=fImdimcm and fIspatie <= 400:
            return "Pass"
          else:
            return "Fail"
        else:
          if fIspatie <= fImemmdi/2 and fIspatie <= 150:
            return "Pass"
          else:
            return "Fail"


# 

