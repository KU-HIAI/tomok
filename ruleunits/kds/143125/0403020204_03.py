import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403020204_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2.4 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '겹침 K형 접합에서 지강관의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
    4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관
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
		A[Title: 겹침 K형 접합에서 압축력을 받는 지강관] ;
		B["KDS 14 31 25 4.3.2.2.4(3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
  	VarOut1[/출력변수: 지강관의 설계강도/] ;
	  VarIn1[/입력변수: 국부항복의 한계상태/] ;
		VarIn2[/입력변수: 겹치는 지강관 재료의 항복응력/] ;
	  VarIn3[/입력변수: 겹치는 지강관의 두께/] ;
  	VarIn4[/입력변수: 겹치는 지강관의 높이/] ;
  	VarIn5[/입력변수: 겹치는 지강관의 폭/] ;
    VarIn6[/입력변수: 겹친 브레이스에 용접된 지강관면의 유효폭/] ;

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

		Python_Class ~~~ Variable_def

		C{"80%≤Ov＜100%"} ;
    D["<img src='https://latex.codecogs.com/svg.image?P_{n}=F_{ybi}t_{bi}[2H_{bi}-4t_{bi}&plus;B_{bi}&plus;b_{eov}]'>------------------------------------------------------------------------------------------------------------"] ;

		Variable_def --> C--"Yes"-->D--"<img src='https://latex.codecogs.com/svg.image?\phi=0.95'>"-->Q(["<img src='https://latex.codecogs.com/svg.image?\phi&space;P_{n}'>------------------"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength_of_steel_pipe(fOphiPn,fIPn,fIFybi,fItbi,fIHbi,fIBbi,fIbeov) -> bool:
        """겹침 K형 접합에서 지강관의 설계강도
        Args:
            fOphiPn (float): 지강관의 설계강도
            fIPn (float): 국부항복의 한계상태
            fIFybi (float): 겹치는 지강관 재료의 항복응력
            fItbi (float): 겹치는 지강관의 두께
            fIHbi (float): 겹치는 지강관의 높이
            fIBbi (float): 겹치는 지강관의 폭
            fIbeov (float): 겹친 브레이스에 용접된 지강관 면의 유효폭

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.2.4 겹침 K형 접합에서 압축력을 받는 지강관 (3)의 값
        """

        fIPn = fIFybi * fItbi * (2 * fIHbi - 4 * fItbi + fIBbi + fIbeov)
        fOphiPn = fIPn * 0.95
        return fOphiPn


# 

