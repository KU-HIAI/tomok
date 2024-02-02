import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070307_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.3.7 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '연속압출공법 시공 중의 인장응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.3 세그멘탈 공법 교량
    4.7.3.7 연속압출공법 교량
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
    A["연속압출공법 교량"];
    B["KDS 24 14 21 4.7.3.7 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:인장응력/];
		VarIn2[/입력변수:설계기준강도/];

		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def
		Variable_def--->D
		D["인장응력≤<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;0.58\sqrt{f_{ck}}'>---------------------------------"]
		D --->E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def tensile_stress(fItenstr, fIfck) ->bool:
        """연속압출공법 시공 중의 인장응력
        Args:
             fItenstr (float): 인장응력
             fIfck (float): 설계기준강도
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.3.7 (6) 설계기준에 따른 연속압출공법 시공 중의 인장응력 적합여부
        """
        if fItenstr <= 0.58*math.sqrt(fIfck):
          return "Pass"
        else:
          return "Fail"


# 

