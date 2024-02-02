import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040506 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.5.6' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '확대선단부'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.5 현장타설말뚝의 구조세목
    3.4.5.6 확대선단부
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
    A[확대선단부];
    B["KDS 24 14 51 3.4.5.6"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarIn1[/입력변수:각도/]
			VarIn2[/입력변수:바닥면의 지름/]
			VarIn3[/입력변수:말뚝지름/]
			VarIn4[/입력변수:확대선단부의 바닥 가장자리 두께/]


			VarIn1 ~~~ VarIn2
			VarIn3 ~~~ VarIn4

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[30° 이하의 각도]
			D[바닥면의 지름 ≤ 말뚝지름의 3배]
			F[확대 선단부의 바닥 가장자리 두께 ≥ 150mm]
			E([Pass or Fail])



			Variable_def ---> C & D & F ---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Enlarged_Shear(fIangle,fIdiaflo,fIdiasta,fIbotthi) -> float:
        """확대선단부
        Args:
            fIangle (float): 각도
            fIdiaflo (float): 바닥면의 지름
            fIdiasta (float): 말뚝지름
            fIbotthi (float): 확대선단부의 바닥 가장자리 두께

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.6 확대선단부의 부합 여부

        """

        if fIangle <= 30 and fIdiaflo<= 3*fIdiasta and fIbotthi >= 150:
          return "Pass"
        else:
          return "Fail"


# 

