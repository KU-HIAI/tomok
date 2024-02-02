import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403010302 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.3.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '각형강관의 한계상태'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.3 중공단면 폭의 중심에 종방향으로 분포된 횡방향 집중하중
    4.3.1.3.2 각형강관
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
	  B["KDS 14 31 25 4.3.1.3.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarIn1[/출력변수: 각형강관의 한계상태/]
	  VarIn2[/입력변수: 접합평면과 90도를 이루는 각형 강관폭/]
	  VarIn3[/입력변수: 주강관의 두께/]
	  VarIn4[/입력변수: 강재의 항복강도/]
	  VarIn5[/입력변수: 판재의 두께/]
	  VarIn6[/입력변수: 주관-응력상관변수/]
    VarIn7[/입력변수: 유요성비/]
	  VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
	  VarIn3 ~~~ VarIn5 & VarIn6 & VarIn7
	  end

	  Python_Class ~~~ Variable_def --> C & D --> E --> F
	  C["하중을 받는 관벽에 관한 <img src='https://latex.codecogs.com/svg.image?B/t\leq&space;40(\phi=1.00)'>--------------"]
	  D["<img src='https://latex.codecogs.com/svg.image?Q_f=(1-U^2)^{0.5}'>------------------------------"]
	  E["<img src=https://latex.codecogs.com/svg.image?R_n=[F_yt^2/(1-t_p/B)][2N/B&plus;4(1-t_p/B)^{0.5}Q_f]'>------------------------------------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?R_n'>---------------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Limit_State_of_Rectangular_Steel_Pipe(fORn, fIB, fIt, fIFy, fItp, fIQf, fIU, fIN,fIuserdefined) -> bool:
        """각형강관의 한계상태

        Args:
            fORn (float): 각형강관의 한계상태
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fIt (float): 주강관의 두께
            fIFy (float): 강재의 항복강도
            fItp (float): 판재의 두께
            fIQf (float): 주관-응력상관변수
            fIU (float): 유요성비
            fIN (float): 집중하중이 작용하는 폭
            fIuserdefined (float): 사용자선택


        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.3.2 각형강관
        """

        #하중을 받는 관 벽 : fIuserdefined == 1

        fIQf = (1 - fIU ** 2) ** 0.5
        fORn = (fIFy * fIt ** 2 / (1 - fItp/fIB)) * (2 * fIN/fIB + 4 * (1 - fItp / fIB) ** 0.5 * fIQf)

        if fIuserdefined == 1 :
          if fIB/fIt <= 40:
            return fORn, "Pass"
          else:
            return fORn, "Fail"
        else:
          return fORn


# 

