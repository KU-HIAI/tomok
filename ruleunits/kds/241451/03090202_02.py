import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03090202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 51 3.9.2.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '벽체의 근입깊이'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.9 보강토 옹벽
    3.9.2 구조물 구성요소
    3.9.2.2 전면부 최소 근입깊이
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
    A[전면부 최소 근입깊이];
    B["KDS 24 14 51 3.9.2.2 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/력변수:벽체의 근입깊이/]
			VarIn1[/입력변수:예상 세굴깊이/]
			VarIn2[/입력변수:동결심도/]



			VarOut1 ~~~ VarIn1 & VarIn2

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[벽체의 근입깊이 ≥ 예상 세굴깊이 + 600mm]
			D[동결심도 킨으로 벽체 근입]

			Variable_def ---> C
			Variable_def -- 동상에 민감한 흙 ---> D
			C & D ---> E([벽체의 근입깊이])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Approximate_depth_of_the_wall(fOappwal,fIestdep,fIfrzdep) -> bool:
        """벽체의 근입깊이
        Args:
            fOappwal (float): 벽체의 근입깊이
            fIestdep (float): 예상 세굴깊이
            fIfrzdep (float): 동결심도


        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.9.2.2 (2) 전면부 최소 근입깊이의 통과여부


        """

        if fOappwal >= fIestdep + 600:
          return "Pass"
        else:
          return "Fail"


# 

