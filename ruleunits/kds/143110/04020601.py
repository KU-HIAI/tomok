import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04020601 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.2.6.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '조립부재의 수정된 기둥세장비'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.2 압축부재
    4.2.6 조립 압축재
    4.2.6.1 압축강도
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
		A[압축강도] ;
		B["KDS 14 31 10 4.2.6.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 조립부재의 수정된 기둥세장비/]
    VarIn1[/입력변수: 고려하는 좌굴방향으로 단일부재로 거동하는 조립부재의 세장비/]
    VarIn2[/입력변수: Ki/]
    VarIn3[/입력변수: 접합재 사이의 길이/]
    VarIn4[/입력변수: 개별부재의 최소단면 2차반경/]
		end

		Python_Class ~~~ Variable_def
	  C["1차조임의 볼트로 접합된 경우"] ;
    D["용접이나 볼트로 접합된 경우"] ;
    E(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{KL}{r}\right)_{m}=\sqrt{\left(\frac{KL}{r}\right)_{0}^{2}&plus;\left(\frac{a}{r_{i}}\right)^{2}}'>---------------------------------------------------------------"]) ;
    F(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{KL}{r}\right)_{m}=\left(\frac{KL}{r}\right)_{o}'>-----------------------------------------------------------------------"]) ;
    G(["<img src='https://latex.codecogs.com/svg.image?\left(\frac{KL}{r}\right)_{m}=\sqrt{\left(\frac{KL}{r}\right)_{0}^{2}&plus;\left(\frac{K_{i}a}{r_{i}}\right)^{2}}'>-------------------------------------------------------------------------------"]) ;
    H["<img src='https://latex.codecogs.com/svg.image?\frac{a}{r_{i}}\leq&space;40'>---------------------------"] ;
    I["<img src='https://latex.codecogs.com/svg.image?\frac{a}{r_{i}}>40'>-----------------------------"] ;

	  Variable_def-->C & D
    C-->E
    D-->H & I
    H-->F
    I-->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Modified_Column_Slender_Ratio_of_Assemblies(fOKLrm,fIKLro,fIKi,fIa,fIri,fIuserdefined1,fIuserdefined2) -> float:
        """조립부재의 수정된 기둥세장비

        Args:
            fOKLrm (float): 조립부재의 수정된 기둥세장비
            fIKLro (float): 고려하는 좌굴방향으로 단일부재로 거동하는 조립부재의세장비
            fIKi (float): 부재 종류에 따른 좌굴길이 보정상수
            fIa (float): 접합재 사이의 길이
            fIri (float): 개별부재의 최소 단면2차반경
            fIuserdefined1 (float): 사용자 선택1
            fIuserdefined2 (float): 사용자 선택2

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.2.6.1 압축강도의 값
        """

        # 1차조임의 볼트로 접합된 경우 : fIuserdefined1 == 1
        # 용접이나 볼트로 접합된 경우 : fIuserdefined1 == 2

        # 서로 맞닿은 ㄱ형강일 경우 : fIuserdefined2 == 1
        # 서로 맞닿은 ㄷ형강일 경우 : fIuserdefined2 == 2
        # 다른 모든 경우 : fIuserdefined2 == 3


        if fIuserdefined1 == 1:
          fOKLrm = (fIKLro ** 2 + (fIa / fIri) ** 2) ** 0.5
          return fOKLrm
        elif fIuserdefined1 == 2:
          if fIa / fIri <= 40:
            fOKLrm = fIKLro
            return fOKLrm
          else:
            if fIuserdefined2 == 1:
              fIKi = 0.5
              fOKLrm = (fIKLro ** 2 + (fIKi * fIa / fIri) ** 2) ** 0.5
              return fOKLrm
            elif fIuserdefined2 == 2:
              fIKi = 0.75
              fOKLrm = (fIKLro ** 2 + (fIKi * fIa / fIri) ** 2) ** 0.5
              return fOKLrm
            elif fIuserdefined2 == 3:
              fIKi = 0.86
              fOKLrm = (fIKLro ** 2 + (fIKi * fIa / fIri) ** 2) ** 0.5
              return fOKLrm


# 

