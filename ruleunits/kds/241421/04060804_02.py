import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060804_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.8.4 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '횡방향 철근 배치'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.8 벽체
    4.6.8.4 횡방향 철근
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
    A["횡방향 철근"];
    B["KDS 24 14 21 4.6.8.4 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:횡방향 철근/];
		VarIn2[/입력변수:지름/];
		VarIn3[/입력변수:용접강선망/];
		VarIn4[/입력변수:피복두께/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C
		Variable_def--->D--->E

		C["횡방향 철근≥단위면적당 4개 이상"]
		D{"용접강선망 지름 ≤16mm"}
		E["피복두께=지름x2"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Transverse_reinforcement(fItrarei, fIdiamet, fIwelwir, fIcovthi) ->bool:
        """횡방향 철근 배치
        Args:
             fItrarei (float): 횡방향 철근
             fIdiamet (float): 지름
             fIwelwir (float): 용접강선망
             fIcovthi (float): 피복두께
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.8.4 (2) 설계기준에 따른 횡방향 철근 배치 적합여부
        """
        if fIdiamet <= 16 and fIcovthi >= fIdiamet*2 :
          return "Pass"
        else:
          if fItrarei >= 4:
            return "Pass"
          else:
            return "Fail"


# 

