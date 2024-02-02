import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040504 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.5.4' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최대 골재치수'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.5 현장타설말뚝의 구조세목
    3.4.5.4 콘크리트
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
    A[일반사항];
    B["KDS 24 14 51 3.4.5.4"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수:최대 골재치수/]
			VarIn2[/입력변수:철근 간격/]

			VarIn1 ~~~ VarIn2

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[최대 골재치수 < 철근간격 X 1/5]
			E([Pass or Fail])

			Variable_def ---> C --->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_aggregate_dimensions(fImaxdim,fIbarspa) -> float:
        """최대 골재치수
        Args:
            fImaxdim (float): 최대 골재치수
            fIbarspa (float): 철근간격

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.4 콘크리트의 부합 여부

        """

        if fImaxdim <= fIbarspa*1/5:
          return "Pass"
        else:
          return "Fail"


# 

