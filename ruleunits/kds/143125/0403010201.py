import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403010201 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.2.1' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '국부항복 한계상태에 관한 설계강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.2 축직각방향 집중하중
    4.3.1.2.1 원형강관
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
	  A[원형강관]
	  B["KDS 14 31 25 4.3.1.2.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/입력변수: 국부항복한계상태에 관한 설계강도/]
	  VarIn2[/입력변수: 강재의 항복강도/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 판폭/]
	  VarIn5[/입력변수: 원형 강관의 외경/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
	  VarIn7[/입력변수: 원형 강관의 외경/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end
	  Python_Class ~~~ Variable_def --> C --> E & F & G --> D
	  C["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n=F_yt^2[5.5/(1-0.81B_p/D)]Q_f'>------------------------------------------------------------------------------------"]
	  D(["<img src='https://latex.codecogs.com/svg.image?\phi&space;R_n'>------------------------"])
	  E["<img src='https://latex.codecogs.com/svg.image?0.2<B_p/D\leq&space;1.0'>--------------------------------------------"]
	  F["T형 접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;50'>--------------"]
	  G["X형 접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;40'>--------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_strength_for_local_yield_limit_state(fIphiRn,fIFy,fIt,fIBp,fID,fIQf,fIuserdefined) -> bool:
        """국부항복 한계상태에 관한 설계강도
        Args:
            fIphiRn (float): 국부항복 한계상태에 관한 설계강도
            fIFy (float): 강재의 항복강도
            fIt (float): 주강관의 두께
            fIBp (float): 접합평면과 90°를 이루는 판폭
            fID (float): 원형 강관의 외경
            fIQf (float): 주관-응력상관변수
            fIuserdefined (float): 사용자선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.2.1 원형강관의 값
        """

        #T형 접합 : fIuserdefined == 1
        #X형 접합 : fIuserdefined == 2

        fIphiRn = fIFy * (fIt ** 2) * (5.5 / (1 - 0.81 * (fIBp / fID))) * fIQf
        if fIuserdefined == 1:
          if 0.2 < fIBp/fID <= 1.0 and fID/fIt <= 50 :
            return fIphiRn, "Pass"
          else:
            return fIphiRn, "Fail"

        if fIuserdefined == 2:
          if 0.2 < fIBp/fID <= 1.0 and fID/fIt <= 40 :
            return fIphiRn, "Pass"
          else:
            return fIphiRn, "Fail"


# 

