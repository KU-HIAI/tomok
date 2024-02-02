import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03050304_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.5.3.4 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '동수경사'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.5 교대와 중력식 및 반중력식 옹벽
    3.5.3 극한한계상태의 지지력과 안정성
    3.5.3.4 지중 침식
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
    A[지중 침식];
    B["KDS 24 14 51 3.5.3.4 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수:동수경사/]

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[실트나 점성토]
			D[사질토]
			E([동수경사])
			F[0.2]
			G[0.3]

			Variable_def ---> C & D
			C ---> F ---> E
			D ---> G---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_same_number_of_slopes(fIsamslo,fIuserdefined) -> float:
        """동수경사
        Args:
            fIsamslo (float): 동수경사
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.5.3.4 지중 침식 (2)의 부합 여부

        """

        #실트나 점성토 : fIuserdefined == 1
        #사질토 : fIuserdefined == 2

        if fIuserdefined == 1:
          if fIsamslo <= 0.2:
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          if fIsamslo <= 0.3:
            return "Pass"
          else:
            return "Fail"


# 

