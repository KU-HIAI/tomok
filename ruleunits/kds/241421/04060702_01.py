import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060702_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.7.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '종방향 철근의 중심간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.7 속빈 사각형 단면 압축부재의 보강철근
    4.6.7.1 철근 간격
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
    A["철근 간격"];
    B["KDS 24 14 21 4.6.7.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:종방향 철근의 중심간격/];
		VarIn2[/입력변수:벽체두께/];
		VarIn3[/입력변수:횡방향 철근의 수직방향으로의 중심간격/];

		VarIn1 & VarIn2 & VarIn3
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C & D
		C["종방향 철근의 중심간격≤ min(벽체두께 X1.5 or 450mm)"]
		D["횡방향철근의 수직방향으로의 중심간격≤min(벽체두께X1.25 or 300mm)"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Center_spacing_of_longitudinal_bars(fIcenslb, fIwalthi, fIcspvdl) ->bool:
        """종방향 철근의 중심간격
        Args:
             fIcenslb (float): 종방향 철근의 중심간격
             fIwalthi (float): 벽체두께
             fIcspvdl (float): 횡방향 철근의 수직방향으로의 중심간격
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.7.2 (1) 설계기준에 따른 종방향 철근의 중심간격 적합여부
        """
        if fIcenslb <= min(1.5*fIwalthi, 450) and fIcspvdl <= min(1.25*fIwalthi, 300):
          return "Pass"
        else:
          return "Fail"


# 

