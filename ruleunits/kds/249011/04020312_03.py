import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020312_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.12 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '미끄럼 안정성'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
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
    A[적층탄성받침의 보강판 최소두께];
    B["KDS 24 90 11 4.2.3.11"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 모든 수평력의 합/];
		VarIn2[/입력변수: Fxy,d가 적용될 때 최소 수직설계하중/];
		VarIn3[/입력변수: 마찰계수/];
		VarIn4[/입력변수: 평균압축응력/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4

    end

    Python_Class ~~~ Variable_def;
		Variable_def--->K--->L
		K["<img src='https://latex.codecogs.com/svg.image?\mu&space;_{e}=0.1&plus;\frac{1.5K_{f}}{\sigma&space;_{m}}'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?F_{xy,d}\leq\mu&space;_{e}F_{z,dmin}'>--------------------------------------------------------"];

    Variable_def--->I
    I["<img src='https://latex.codecogs.com/svg.image?\sigma&space;_{cdmin}=\frac{F_{z,dmin}}{A_{r}}\geq&space;3(MPa)'>--------------------------------------------------------"];
		I & L--->J
		J(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Sum_Of_Horizontal_Force(fIFxyd, fIzdmin, fImue, fIKf, fIsigmam,fIuserdefined) -> bool:
        """미끄럼 안정성

        Args:
            fIFxyd (float): 모든 수평력의 합
            fIzdmin (float): Fxy,d가 적용될 때 최소 수직설계하중
            fImue (float): 마찰계수
            fIKf (float):
            fIsigmam (float): 평균압축응력
            fIuserdefined (float): 사용자 선택


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.12 안정성 (3)의 통과 여부
        """

        #콘크리트 표면 > fIuserdefined == 1
        #기타 표면 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIKf = 0.6
        if fIuserdefined == 2:
          fIKf = 0.2

        fImue = 0.1 + 1.5*fIKf/fIsigmam

        if fIFxyd <=fImue*fIzdmin :
           return "Pass"
        else:
           return "Fail"


# 

