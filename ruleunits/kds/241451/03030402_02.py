import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030402_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.4.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '사질토의 근입 깊이'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.4 구조설계
    3.3.4.2 말뚝의 좌굴
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
    A[말뚝의 좌굴];
    B["KDS 24 14 51 3.3.4.2 (2)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:근입 깊이/]
			VarIn1[/입력변수:말뚝의 탄성계수/]
			VarIn2[/입력변수:말뚝의 관성모멘트/]
			VarIn3[/입력변수:점성토의 탄성계수/]


			VarOut1
			VarIn1
			VarIn2
			VarIn3

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			E{아래 일정한 깊이에 고정되어는 것으로 가정}
			E~~~ |"KDS 24 14 21"| E
			E~~~ |"KDS 24 14 31"| E

			C["<img src='https://latex.codecogs.com/svg.image?1.8[\frac{E_{p}I_{p}}{n_{h}}]^{0.2}'>---------------------------------"]

			D([고정점까지의 근입 깊이])
			Variable_def---> E ---> I{점성토} ---> C ---> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Penetration_depth_of_sandy_soil(fOpendep,fIEp,fIlp,fInh) -> float:
        """사질토의 근입 깊이
        Args:
            fOpendep (float): 근입 깊이
            fIEp (float): 말뚝의 탄성계수
            fIlp (float): 말뚝의 관성모멘트
            fInh (float): 사질토의 깊이에 따른 탄성계수 증가비

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.3.4.2 말뚝의 좌굴 (2)의 값

        """

        fOpendep=1.8*(fIEp*fIlp/fInh)**0.2
        return fOpendep


# 

