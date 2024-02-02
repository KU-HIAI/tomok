import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010304_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.3.4 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-10-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지압접합이 인장과 전단의 조합력을 받을 경우 볼트의 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.3 볼트
    4.1.3.4 지압접합에서 인장과 전단의 조합
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
	  A([지압접합에서 인장과 전단의 조합])
	  B["KDS 14 31 25 4.1.3.4(1)"]
	  A ~~~ B
	  end

  	subgraph Variable_def
  	VarOut1[/출력변수: 볼트의 설계강도/]
    VarOut2[/출력변수: 전단응력의 효과를 고려한 공칭 인장강도/]
  	VarIn1[/입력변수: 저항계수/]
  	VarIn2[/입력변수: 공칭인장강도/]
  	VarIn3[/입력변수: 공칭전단강도/]
    VarIn4[/입력변수: 소요전단응력/]
  	VarOut1 & VarOut2 ~~~ VarIn2 & VarIn3 & VarIn4
  	end

	  Python_Class ~~~ Variable_def --> D --> E


	  D["<img src='https://latex.codecogs.com/svg.image?F_{nt}`=1.3F_{nt}-\frac{F_{nt}}{\phi&space;F_{nv}}f_v\leq&space;F_{nt}'>-----------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?R_n=F_{nt}`A_b'>--------------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_strength_per_unit_length_of_fillet_weld(fORn,fIphi,fIFntpri,fIFnt,fIFnv,fIfv,fIAb) -> bool:
        """지압접합이 인장과 전단의 조합력을 받을 경우 볼트의 설계강도

        Args:
            fORn (float): 볼트의 설계강도
            fIphi (float): 저항계수
            fIFntpri (float): 전단응력의 효과를 고려한 공칭인장강도
            fIFnt (float): 공칭인장강도
            fIFnv (float): 공칭전단강도
            fIfv (float): 소요전단응력
            fIAb (float): 볼트, 또는 나사 강봉의 나사가 없는 부분의 공칭단면적 (mm^2)

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.3.4 지압접합에서 인장과 전단의 조합 (1)의 값
        """
        fIFntpri = min((1.3)*fIFnt-fIFnt/(fIphi*fIFnv)*fIfv, fIFnt)
        fORn = fIFntpri*fIAb
        return fORn


# 

