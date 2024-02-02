import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010204_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.4 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '필릿용접의 단위길이 당 소요강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.4 설계강도
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
	  A([필릿용접의 단위길이 당 소요강])
	  B["KDS 14 31 25 4.1.2.4(2)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut[/출력변수: 필릿용접의 단위길이당 소요강도/]
  	VarIn1[/입력변수: 필릿용접의 유효면에 작용하는 수직력/]
  	VarIn2[/입력변수: 필릿용접의 유효면에서 용접축에 직각방향으로 작용하는 전단력/]
  	VarIn3[/입력변수: 필릿용접의 유효면에서 용접축에 평행으로 작용하는 전단력/]
  	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
  	end

	  Python_Class ~~~ Variable_def --> D --> E


	  D["<img src='https://latex.codecogs.com/svg.image?P_u=\sqrt{P_\perp^2&plus;V_\perp^2&plus;V_\parallel^2}'>-----------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?P_u'>----------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fOPu,fIPperp,fIVperp,fIVii) -> bool:
        """필릿용접의 단위길이 당 소요강도

        Args:
            fOPu (float): 필릿용접의 단위길이 당 소요강도
            fIPperp (float): 필릿용접의 유효면에 작용하는 수직력
            fIVperp (float): 필릿용접의 유효면에서 용접축에 직각방향으로 작용하는 전단력
            fIVii (float): 필릿용접의 유효면에서 용접축에 평행으로 작용하는 전단력

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.4 설계강도 (1)의 값
        """
        fOphiRn = ((fIPperp**2)+(fIVperp**2)+(fIVii**2))**(1/2)
        return fOphiRn


# 

