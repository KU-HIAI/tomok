import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03020302_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.2.3.2 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '편심량'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.2 암반 지지력
    (5)
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
    A[암반지지력];
    B["KDS 24 14 51 3.2.3.2 (5)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 편심량/];
			VarIn2[/입력변수: 기초의 크기 B/];
			VarIn3[/입력변수: 기초의 크기 L/];


			VarIn1
			VarIn2
			VarIn3

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C[기초크기 B or L 의 3/8 > 편심량]
			D[기초크기 B or L 의 4/10 > 편심량]

			Variable_def --하중에대한 편심량 ---> C
			Variable_def --지진하중을 고려하는 극단상황한계상태 ---> D

			E([Pass or Fail])

			C & D ---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def eccentricity(fIeccent,fIb,fIl,fIuserdefined) -> bool:
        """편심량
        Args:
            fIeccent (float): 편심량
            fIb (float): 기초의 크기
            fIl (float): 기초의 크기
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.2 암반 지지력 (5)의 통과 여부

        """

        #극단상황한계상태 : fIuserdefined == 1
        #그 외 : fIuserdefined == 2

        if fIuserdefined==1:
          if fIeccent <= 4/10*fIb and fIeccent <= 4/10*fIl:
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined==2:
          if fIeccent <= 3/8*fIb and fIeccent <= 3/8*fIl:
            return "Pass"
          else:
            return "Fail"


# 

