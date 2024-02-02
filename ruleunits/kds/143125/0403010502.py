import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403010502 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.1.5.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '한 개의 벽체에 대한 국부 크리플링 한계상태'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.1 강관구조의 집중하중
    4.3.1.5 각형강관의 단부 마구리판에 작용하는 축방향 집중하중
    4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태
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
	  A[한 개의 벽체에 대한 국부 크리플링 한계상태]
	  B["KDS 14 31 25 4.3.1.3.5.2"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 국부크리플링 한계상태/]
	  VarIn1[/입력변수: 저항계수/]
	  VarIn2[/입력변수: 벽체의 두께/]
	  VarIn3[/입력변수: 집중하중이 작용하는 폭/]
	  VarIn4[/입력변수: 접합평면과 90도를 이루는 각형 강관폭/]
	  VarIn5[/입력변수: 판재의 두께/]
	  VarIn6[/입력변수: 강재의 탄성계수/]
	  VarIn7[/입력변수: 강재의 항복강도/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
	  end
  	Python_Class ~~~ Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?R_n=0.8t^2\left[1&plus;(6N/B)(t/t_p)^{1.5}\right]\left[EF_yt_p/t\right]^{0.5}'>-----------------------------------------------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Local_Crippling_Limit_State(fORn,fIphi,fIt,fIN,fIB,fItp,fIE,fIFy) -> bool:
        """한 개의 벽체에 대한 국부 크리플링 한계상태

        Args:
            fORn (float): 국부 크리플링 한계상태
            fIphi (float): 저항계수
            fIt (float): 벽체의 두께
            fIN (float): 집중하중이 작용하는 폭
            fIB (float): 접합평면과 90°를 이루는 각형 강관폭
            fItp (float): 판재의 두께
            fIE (float): 강재의 탄성계수
            fIFy (float): 강재의 항복강도

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.1.5.2 한 개의 벽체에 대한 국부 크리플링 한계상태의 값
        """

        fIphi = 0.75
        fORn = 0.8 * fIt ** 2 * (1 + (6 * fIN / fIB) * (fIt / fItp) ** 1.5) * (fIE * fIFy * fItp / fIt) ** 0.5
        return fORn


# 

