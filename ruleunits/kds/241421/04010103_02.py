import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010103_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.1.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-09'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '축력과 2축 휨이 작용하는 부재의 휨강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도
    (2)
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
    A["축력과 2축 휨이 작용하는 부재의 휨강도"];
    B["KDS 24 14 21 4.1.1.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 세장비 비율/];
		VarIn2[/입력변수: 단면의 등가 폭/];
    VarIn3[/입력변수: 단면의 등가 깊이/] ;
		VarIn4[/입력변수: 단면의 y축 세장비/] ;
		VarIn5[/입력변수: 단면의 z축 세장비/];
		VarIn6[/입력변수: 단면의 y축 회전반지름/];
		VarIn7[/입력변수: 단면의 z축 회전반지름/];
		VarIn8[/입력변수: Muy/Pu/];
		VarIn9[/입력변수: Muz/Pu/];
		VarIn10[/입력변수: 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트/];
		VarIn11[/입력변수: 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트/];


		VarIn1 & VarIn2 & VarIn3~~~VarIn4 & VarIn5 & VarIn6 & VarIn7
		VarIn5 ~~~VarIn8 & VarIn9 & VarIn10 & VarIn11
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C & D
		C & D-->E
		C["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{y}=\frac{l}{r_{y}}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\lambda&space;_{z}=\frac{l}{r_{z}}'>---------------------------------"]

		E["<img src='https://latex.codecogs.com/svg.image?\frac{\lambda&space;_{y}}{\lambda&space;_{z}}\leq&space;2,\frac{\lambda&space;_{z}}{\lambda&space;_{y}}\leq&space;2'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?b_{eq}=r_{y}\sqrt{12}'>---------------------------------"]
  	G["<img src='https://latex.codecogs.com/svg.image?h_{eq}=r_{z}\sqrt{12}'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?e_{z}=\frac{M_{uy}}{P_{u}}'>---------------------------------"]
	  I["<img src='https://latex.codecogs.com/svg.image?e_{z}=\frac{M_{uz}}{P_{u}}'>---------------------------------"]
	  J["<img src='https://latex.codecogs.com/svg.image?\frac{e_{y}/h_{eq}}{e_{z}/b_{eq}}\leq&space;0.2\;\,or\,\,\frac{e_{z}/b_{eq}}{e_{y}/h_{eq}}\leq&space;0.2'>---------------------------------"]
	  Variable_def---> F & G & H & I--->J
  	K(["Pass or Fail"])
    E & J--->K
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def bending_strength_of_member_subject_to_axial_force_and_biaxial_bending(fIslerat,fIbeq,fIheq,fIlambday,fIlambdaz,fIry,fIrz,fIez,fIey,fIMuy,fIMuz) -> bool:
        """축력과 2축 휨이 작용하는 부재의 휨강도

        Args:
             fIslerat (float): 세장비 비율
             fIbeq (float): 단면의 등가 폭
             fIheq (float): 단면의 등가 깊이
             fIlambday(float): 단면의 y축 세장비
             fIlambdaz(float): 단면의 z축 세장비
             fIry(float): 단면의 y축 회전반지름
             fIrz(float): 단면의 z축 회전반지름
             fIez(float): Muy/Pu
             fIey(float): Muz/Pu
             fIMuy(float): 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트
             fIMuz(float): 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트


        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (2)의 통과 여부
        """

        if fIlambday/fIlambdaz <= 2 and fIlambdaz/fIlambday <= 2:
          if (fIey/fIheq)/(fIez/fIbeq) or (fIez/fIbeq)/(fIey/fIheq):
            return("Pass")
          else:
            return("Fail")
        else:
          return("Fail")


# 

