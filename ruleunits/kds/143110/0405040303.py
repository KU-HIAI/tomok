import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040303 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.3.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '박스형 파형강판 구조물의 정점부 설계휨모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.3 설계휨모멘트
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
		A[Title: 설계휨모멘트] ;
		B["KDS 14 31 10 4.5.4.3.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 박스형 파형강판 구조물의 정점부 설계휨모멘트/] ;
      VarOut2[/출력변수: 박스형 파형강판 구조물의 어깨부 설계휨모멘트/] ;
      VarIn1[/입력변수: 고정하중 하중계수/] ;
      VarIn2[/입력변수: 고정하중에 의한 정점부 휨모멘트/] ;
      VarIn3[/입력변수: 활하중 하중계수/] ;
      VarIn4[/입력변수: 활하중에 의한 정점부 휨모멘트/] ;
      VarIn5[/입력변수: 충격계수/] ;
      VarIn6[/입력변수: 지진하중 하중계수/] ;
      VarIn7[/입력변수: 지진하중에 의한 정점부 휨모멘트/] ;
      VarIn8[/입력변수: 고정하중 하중계수/] ;
      VarIn9[/입력변수: 고정하중에 의한 어깨부 휨모멘트/] ;
      VarIn10[/입력변수: 활하중 하중계수/] ;
      VarIn11[/입력변수: 활하중에 의한 어깨부 휨모멘트/] ;
      VarIn12[/입력변수: 충격계수/] ;
      VarIn13[/입력변수: 지진하중 하중계수/] ;
      VarIn14[/입력변수: 지진하중에 의한 어깨부 휨모멘트/] ;
		end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?M_{cf}=\alpha&space;_{D}M_{cD}&plus;max\left\{\alpha&space;_{L}M_{cL}(1&plus;i),\alpha&space;_{E}M_{cE}\right\}>------------------------------------------------------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{hf}=\alpha&space;_{D}M_{hD}&plus;max\left\{\alpha&space;_{L}M_{hL}(1&plus;i),\alpha&space;_{E}M_{hE}\right\}>------------------------------------------------------------------------------------"]
		R(["<img src=https://latex.codecogs.com/svg.image?M_{cf}>---------"])
		S(["<img src=https://latex.codecogs.com/svg.image?M_{hf}>---------"])

		Variable_def --> Q & W
		Q --> R
		W --> S
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_bending_moment_at_the_apex_of_a_box_type_corrugated_steel_plate_structure(fOMcf,fIalphaD,fIMcD,fIalphaL,fIMcL,fIi,fIalphaE,fIMcE,fOMhf,fIMhD,fIMhL,fIMhE) -> bool:
        """박스형 파형강판 구조물의 정점부 설계휨모멘트
        Args:
            fOMcf (float): 박스형 파형강판 구조물의 정점부 설계휨모멘트
            fIalphaD (float): 고정하중 하중계수
            fIMcD (float): 고정하중에 의한 정점부 휨모멘트
            fIalphaL (float): 활하중 하중계수
            fIMcL (float): 활하중에 의한 정점부 휨모멘트
            fIi (float): 충격계수
            fIalphaE (float): 지진하중 하중계수
            fIMcE (float): 지진하중에 의한 정점부 휨모멘트
            fOMhf (float): 박스형 파형강판 구조물의 어깨부 설계휨모멘트
            fIMhD (float): 고정하중에 의한 어깨부 휨모멘트
            fIMhL (float): 활하중에 의한 어깨부 휨모멘트
            fIMhE (float): 지진하중에 의한 어깨부 휨모멘트


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.3.3 설계휨모멘트의 값
        """


        fOMcf = fIalphaD * fIMcD + max(fIalphaL * fIMcL * (1 + fIi), fIalphaE * fIMcE)
        fOMhf = fIalphaD * fIMhD + max(fIalphaL * fIMhL * (1 + fIi), fIalphaE * fIMhE)
        return fOMcf, fOMhf


# 

