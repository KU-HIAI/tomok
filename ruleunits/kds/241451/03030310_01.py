import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030310_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.3.10 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '감가된 지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.10 무리말뚝의 축방향 지지력
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
    A[무리말뚝의 축방향 지지력];
    B["KDS 24 14 51 3.3.3.10 (1)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:감가된 지지력/]
			VarIn1[/입력변수:무리말뚝의 공칭 지지력/]
			VarIn2[/입력변수:무리말뚝의 저항계수/]



			VarOut1
			VarIn1 ~~~ VarIn2


      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?Q_{R}=\phi&space;Q_{n}=\phi&space;_{g}Q_{g}'>---------------------------------"]
			D([무리말뚝의 감가된 지지력])
			Variable_def ---> C ---> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def diminished_support(fOQr,fIQg,fIresbul) -> float:
        """감가된 지지력
        Args:
            fOQr (float): 감가된 지지력
            fIQg (float): 무리말뚝의 공칭 지지력
            fIresbul (float): 무리말뚝의 저항계수

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.10 무리말뚝의 축방향 지지력 (1)의 값

        """

        fOQr=fIresbul*fIQg
        return fOQr


# 

