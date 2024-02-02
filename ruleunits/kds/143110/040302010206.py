import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302010206 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.1.2.6' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '원형강관의 공칭전단강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.2 전단강도
    4.3.2.1.2.6 원형강관
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
	  B["KDS 14 31 10 4.3.2.1.2.6"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 공칭전단강도/]
	  VarIn1[/입력변수: 국부좌굴강도/]
	  VarIn2[/입력변수: 강판의 전단면적/]
	  VarIn3[/입력변수: 강재의 탄성계수/]
	  VarIn4[/입력변수: 항복강도/]
	  VarIn5[/입력변수: 최대전단력의 작용점과 전단력이 0인 점 사이의 거리/]
	  VarIn6[/입력변수: 강관의 외경/]
	  VarIn7[/입력변수: 강관의 두께/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7
	  end
	  Python_Class ~~~ Variable_def --> C --> D --> E --> F
	  C["원형강관의 공칭전단강도 Vn"]
	  D["max(<img src='https://latex.codecogs.com/svg.image?F_{cr}=\frac{1.60E}{\sqrt{\frac{L_v}{D}}\left(\frac{D}{t}\right)^\frac{5}{4}}'> , <img src='https://latex.codecogs.com/svg.image?F_{cr}=\frac{0.78E}{(\frac{D}{t})^\frac{3}{2}}'>)------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?V_n=F_{cr}A_g/2'>----------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?V_n'>---------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def niominal_shear_strength(fOVn,fIFcr,fIAg,fIE,fIFy,fILv,fID,fIt) -> bool:
        """원형강관의 공칭전단강도
        Args:
            fOVn (float): 공칭전단강도
            fIFcr (float): 국부좌굴강도
            fIAg (float): 강관의 전단면적
            fIE (float): 강재의 탄성계수
            fIFy (float): 항복강도
            fILv (float): 최대전단력 작용점과 전단력이 0인 점 사이의 거리
            fID (float): 강관의 외경
            fIt (float): 강관의 두께


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.2.6 원형강관의 값
        """


        fIFcr = max((1.60 * fIE) / ((fILv / fID) ** 0.5) * (fID / fIt) ** (5 / 4), (0.78 * fIE) / (fID / fIt) ** 1.5)
        if fIFcr >= 0.6* fIFy:
            return "Fail"
        else:
            fOVn = fIFcr * fIAg / 2
            return fOVn


# 

