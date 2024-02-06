import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040504030303 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.3.3.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지진하중에 의한 정점부 휨모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.3 설계휨모멘트
    4.5.4.3.3.3 지진하중에 의한 휨모멘트
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
		A[Title: 지진하중에 의한 휨모멘트] ;
		B["KDS 14 31 10 4.5.4.3.3.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 지진하중에 의한 정점부 휨모멘트/] ;
      VarOut2[/출력변수: 지진하중에 의한 어깨부 휨모멘트/] ;
      VarIn1[/입력변수: 지진하중에 의한 휨모멘트/] ;
      VarIn2[/입력변수: 수직가속도계수/] ;
      VarIn3[/입력변수: 수평가속도계수/] ;
			end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?A_{V}=\frac{2}{3}A_{H}>---------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{E}=M_{D}A_{V}>---------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?M_{cE}=\kappa&space;M_{E}>--------------------------"]
		S["<img src=https://latex.codecogs.com/svg.image?M_{hE}=(1-\kappa)M_{E}>-------------------------------------"]

		Variable_def --> Q --> W --> R & S
		R --> D(["<img src=https://latex.codecogs.com/svg.image?M_{cE}>-----------"])
		S --> H(["<img src=https://latex.codecogs.com/svg.image?M_{hE}>-----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Peak_bending_moment_due_to_seismic_load(fOMcE,fOMhE,fIME,fIAV,fIAH,fIk) -> bool:
        """지진하중에 의한 정점부 휨모멘트
        Args:
            fOMcE (float): 지진하중에 의한 정점부 휨모멘트
            fOMhE (float): 지진하중에 의한 어깨부 휨모멘트
            fIME (float): 지진하중에 의한 휨모멘트
            fIAV (float): 수직가속도계수
            fIAH (float): 수평가속도계수
            fIk (float): 정점부 휨모멘트 분배계수




        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.3.3.3 지진하중에 의한 휨모멘트의 값
        """


        fOMcE = fIk * fIME
        fOMhE = (1 - fIk) * fIME
        fIAV = 2 / 3 * fIAH
        return fOMcE, fOMhE


# 
