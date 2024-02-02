import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020101_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.1.1 (8)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '오버랩 접합계수'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.1 원형강관
    4.3.2.1.1 적용한계
    (8)
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
		A[적용한계] ;
		B["KDS 14 31 25 4.3.2.1.1 (8)"] ;
		A ~~~ B
		end

		subgraph Variable_def
	  VarIn1[/입력변수: 오버랩 접합계수/]
	  VarIn2[/입력변수: 주강관에 대한 겹치는 지강관의 투영길이/]
	  VarIn3[/입력변수: 주강관의 접촉면에서 측정한 겹친 길이/]
		end


		Python_Class ~~~ Variable_def



    D["<img src='https://latex.codecogs.com/svg.image?&space;25%\leq&space;O_{v}\leq&space;100%'>----------------------------------------------"] ;
    C["<img src='https://latex.codecogs.com/svg.image?O_{v}=(q/p)\times&space;100%'>----------------------------------------------"] ;
		Variable_def --> C
		C --"겹침 K접합"--> D
    D-->F(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Overlap_junction_factor(fIOv,fIp,fIq) -> bool:
        """오버랩 접합계수
        Args:
            fIOv (float): 오버랩 접합계수
            fIp (float): 주강관에 대한 겹치는 지강관의 투영길이
            fIq (float): 주강관의 접촉면에서 측정한 겹친 길이


        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.1.1 적용한계 (8)의 통과여부
        """


        fIOv = (fIq / fIp) * 100
        if 25 <= fIOv <= 100:
            return "Pass"
        else:
            return "Fail"


# 

