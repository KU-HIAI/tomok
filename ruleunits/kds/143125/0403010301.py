import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403010301 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.3.1' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '원형강관의 한계상태'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.3 중공단면 폭의 중심에 종방향으로 분포된 횡방향 집중하중
    4.3.1.3.1 원형강관
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
	  A[각형강관]
	  B["KDS 14 31 25 4.3.1.3.1"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/출력변수: 원형강관의 한계상태/]
	  VarIn2[/입력변수: 원형강관의 외경/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 강재의 항복강도/]
	  VarIn5[/입력변수: 집중하중이 작용하는 폭/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
	  VarIn1 ~~~ VarIn2 & VarIn3
	  VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
	  end

	  Python_Class ~~~ Variable_def --> C & D --> E --> F
	  C["T형접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;50'>--------------"]
	  D["X형접합에 대하여 <img src='https://latex.codecogs.com/svg.image?D/t\leq&space;40'>----------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?R_n=5.5F_yt^2(1&plus;0.25N/D)Q_f'>---------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------------"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Limit_State_of_Circular_Steel_Pipe(fIRn, fID, fIt, fIFy, fIN, fIQf,fIuserdefined) -> bool:
        """원형강관의 한계상태

        Args:
            fIRn (float): 원형강관의 한계상태
            fID (float): 원형 강관의 외경
            fIt (float): 주강관의 두께
            fIFy (float): 강재의 항복강도
            fIN  (float): 집중하중이 작용하는 폭
            fIQf (float): 주관-응력상관변수
            fIuserdefined (float): 사용자선택

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.3.1 원형강관의 값
        """

        #T형 접합 : fIuserdefined == 1
        #X형 접합 : fIuserdefined == 2

        fIRn = 5.5 * fIFy * fIt ** 2 * (1 + 0.25 * fIN/fID) * fIQf

        if fIuserdefined == 1 :
          if fID/fIt <= 50:
            return fIRn, "Pass"
          else:
            return fIRn, "Fail"

        if fIuserdefined == 2 :
          if fID/fIt <= 40:
            return fIRn, "Pass"
          else:
            return fIRn, "Fail"


# 

