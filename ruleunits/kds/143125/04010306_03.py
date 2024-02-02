import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010306_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.6 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-10-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '미끄럼 한계상태에 대한 마찰접합의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.6 마찰접합의 미끄럼강도
    (3)
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
	  A([마찰접합의 설계강도])
	  B["KDS 14 31 25 4.1.3.6(3)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 마찰접합의 설계강도/]
    VarIn1[/출력변수: 미끄럼계수/]
    VarIn2[/입력변수: 끼움재계수/]
    VarIn3[/입력변수: 고장력볼트의 설계볼트장력/]
    VarIn4[/입력변수: 전단면의 수/]
  	end

	  Python_Class ~~~ Variable_def --> C & D & E --> F --> G



	  C["표준구멍 또는 하중방향에 수직인 단슬롯, Φ=1.00"]
	  D["과대구멍 또는 하중방향에 평행한 단슬롯, Φ=0.85"]
    E["장슬롯, Φ=0.70"]
    F["<img src='https://latex.codecogs.com/svg.image?R_n=\mu&space;h_fT_oN_s'>---------------------------------------------"]
    G(["<img src='https://latex.codecogs.com/svg.image?R_n'>------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fORn,fImu,fIhf,fITo,fINs,flphi) -> bool:
        """미끄럼 한계상태에 대한 마찰접합의 설계강도

        Args:
            fORn (float): 마찰접합의 설계강도
            fImu (float): 미끄럼계수
            fIhf (float): 끼움재계수
            fITo (float): 고장력볼트의 설계볼트장력
            fINs (float): 전단면의 수
            fIphi (float): 저항계수

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.6 미끄럼 한계상태에 대한 마찰접합의 설계강도 (3)의 값
        """

        fORn = fImu*fIhf*fITo*fINs
        return fORn


# 

