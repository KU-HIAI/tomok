import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040205_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.5 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-11-30'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '유효세장비'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.5 단일ㄱ형강 압축부재
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
		A[단일ㄱ형강 압축부재] ;
		B["KDS 14 31 10 4.2.5(1)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 유효세장비/]
    VarIn1[/입력변수: 부재길이/]
    VarIn2[/입력변수: 접합된 다리와 평행한 축에 대한 단면2차반경/]
    VarIn3[/입력변수: 다리길이의 비/]
    VarIn4[/입력변수: ㄱ형강의 긴 쪽 다리의 길이/]
    VarIn5[/입력변수: ㄱ형강의 짧은 쪽 다리의 길이/]
    VarIn6[/입력변수: 약축에 대한 단면2차반경/]
    VarIn1~~~ VarIn4
    VarOut1~~~ VarIn2~~~ VarIn5
    VarIn3~~~ VarIn6

		end

		Python_Class ~~~ Variable_def
    C["등변ㄱ형강 또는 긴 다리로 접합된 부등변ㄱ형강이 단일 부재이거나 또는 평면트러스의 웨브재로 인접한 웨브재와 거셋플레이트 또는 현재의 동일면에 접합된 경우"] ;
    D["<img src='https://latex.codecogs.com/svg.image?0\leq\frac{L}{r_{x}}\leq&space;80'>---------------------------------------------------------"] ;
    E["<img src='https://latex.codecogs.com/svg.image?\frac{L}{r_{x}}>80'>-----------------------------------------"] ;
    F(["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=72&plus;0.75\frac{L}{r_{x}}'>-----------------------------------------------------------------------"]) ;
    G(["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=32&plus;1.25\frac{L}{r_{x}}\leq&space;200'>-------------------------------------------------------------------------------"]) ;
    H{"부등변ㄱ형강에서 다리길이의 비가 1.7이하이고 ㄱ형가의 짧은 다리가 접합된 경우"} ;
    I(["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=72&plus;0.75\frac{L}{r_{x}}&plus;4[(b_{1}/b_{2})^{2}-1]\geq&space;0.95\frac{L}{r_{z}}'>-----------------------------------------------------------------------"]) ;
    J(["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}=32&plus;1.25\frac{L}{r_{x}}&plus;4[(b_{1}/b_{2})^{2}-1]\geq&space;0.95\frac{L}{r_{z}}'>-----------------------------------------------------------------------"]) ;
    K["<img src='https://latex.codecogs.com/svg.image?0\leq\frac{L}{r_{x}}\leq&space;80'>---------------------------------------------------------"] ;
    L["<img src='https://latex.codecogs.com/svg.image?\frac{L}{r_{x}}>80'>-----------------------------------------"] ;
		M["<img src='https://latex.codecogs.com/svg.image?\frac{KL}{r}'>---------------------------------------------------------"] ;
    Variable_def-->C
    C-->H-->NO
    H-->YES
    NO-->D-->F
    NO-->E-->G
    YES-->K-->I
    YES-->L-->J
		F & G & I & J --> M
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def effective_slender_ratio(fOKLr,fIL,fIrx,fIlelera,fIbI,fIbs,fIrz,fIuserdefined) -> float:
        """유효세장비

        Args:
            fOKLr (float): 유효세장비
            fIL (float): 부재길이
            fIrx (float): 접합된 다리와 평행한 축에 대한 단면2차반경
            fIlelera (float): 다리길이의 비
            fIbI (float): ㄱ형강의 긴 쪽 다리의 길이
            fIbs (float): ㄱ형강의 짧은 쪽 다리의 길이
            fIrz (float): 약축에 대한 단면2차반경
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.2.5 단일ㄱ형강 압축부재 (1)의 값
        """
        #등변ㄱ형강 또는 긴 다리로 접합된 부등변ㄱ형강이 단일 부재이거나 또는 평면트러스의 웨브재로 인접한 웨브재와 거셋플레이트 또는 현재의 동일면에 접합된 경우 : fIuserdefined == 1
        #부등변ㄱ형강에서 다리길이의 비가 1.7이하이고 ㄱ형가의 짧은 다리가 접합된 경우 : fIuserdefined == 2

        if fIuserdefined == 1:
          if 0 <= fIL/fIrx <= 80:
            fOKLr = 72 + 0.75*fIL/fIrx
          elif fIL/fIrx > 80:
            fOKLr = min(32 + 1.25*fIL/fIrx, 200)

        if fIuserdefined == 2:
          if 0 <= fIL/fIrx <= 80:
            fOKLr = max(72 + 0.75*fIL/fIrx + 4*((fIbI/fIbs)**2 - 1), 0.95*fIL/fIrx)
          elif fIL/fIrx > 80:
            fOKLr = max(32 + 1.25*fIL/fIrx + 4*((fIbI/fIbs)**2 - 1), 0.95*fIL/fIrx)

        return fOKLr


# 

