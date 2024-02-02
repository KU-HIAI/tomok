import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020202_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (5)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '필릿용접의 유효길이'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
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
	  A([필릿용접의 유효길])
	  B["KDS 14 31 25 4.1.2.2.2(5)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 부재단부에 용접된 필릿용접의 길이/]
	  VarIn2[/입력변수: 용접치수/]
	  VarIn3[/입력변수: 실제 용접된 길이/]
	  VarIn4[/입력변수: 유효길이/]
	  VarIn5[/입력변수: 감소계수/]
	  VarIn6[/입력변수: 필릿용접의 유효길이/]
	  VarIn7[/입력변수: 용접길이/]
	  VarIn5 ~~~ VarIn1 & VarIn2
	  VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
  	end
	  Python_Class ~~~ Variable_def --> D & E & F
	  D --> H
	  E --> G
	  F --> J
	  H --> K
	  G--> I --> K
	  J --> K
	  D{"용접길이 ≤ 용접치수x100"}
	  E{"용접치수x100 < 용접길이 ≤용접치수x300"}
	  F{"용접길이 > 용접치수x300"}
	  G["<img src='https://latex.codecogs.com/svg.image?\beta=1.2-0.002\left(\frac{l}{z}\right)\leq&space;1.0'>-------------------------------------------------------"]
	  H["실제 용접된 길이= 유효길이"]
	  I["용접길이 x β =필릿용접의 유효길이"]
	  J["용접치수x180=필릿용접의 유효길이"]
  	K([필릿용접의 유효길이])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_length_of_fillet_weld(fOeflefw,fIl,fIz,fIacwele,fIbeta,fIwellen) -> bool:
        """필릿용접의 유효길이

        Args:
            fOeflefw (float): 필릿용접의 유효길이
            fIl (float): 부재 단부에 용접된 필릿용접의 길이
            fIz (float): 용접치수
            fIacwele (float): 실제 용접된 길이
            fIbeta (float): 감소계수
            fIwellen (float): 용접길이

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.2.2 제한사항 (5)의 값
        """
        fIbeta = min(1.2-0.002*(fIl/fIz), 1.0)

        if fIl <= 100*fIz :
          fOeflefw = fIacwele

        if 100*fIz < fIwellen <= 300*fIz :
          fOeflefw = fIacwele*fIbeta

        if 300*fIz < fIwellen  :
          fOeflefw = fIacwele*180

        return fOeflefw


# 

