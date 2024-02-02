import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040304 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.3.4' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-13'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '한계상태에서 정점부 설계휨모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.4 휨강도 검토
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
		A[Title: 휨강도 검토] ;
		B["KDS 14 31 10 4.5.4.3.4"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 한계상태에서 정점부 설계휨모멘트/] ;
      VarOut2[/출력변수: 한계상태에서 어깨부 설계휨모멘트/] ;
      VarOut3[/출력변수: 소성설계모멘트/] ;
      VarIn1[/입력변수: 소성힌지 저항계수/] ;
      VarIn2[/입력변수: 파형강판의 소성단면계수/] ;
      VarIn3[/입력변수: 파형강판의 항복강도/] ;
			end

		VarOut1 & VarOut2 & VarOut3 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?M_{pf}=\phi&space;_{h}ZF_{y}>-----------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{cf}\leq&space;M_{pf}>--------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?M_{hf}\leq&space;M_{pf}>---------------------------------"]

		Variable_def --> Q --> W & R
		W & R --> S(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Vertex_Design_Bending_Moment_in_Limit_State(fIMcf,fIMhf,fIMpf,fIphih,fIZ,fIFy) -> bool:
        """한계상태에서 정점부 설계휨모멘트
        Args:
            fIMcf (float): 한계상태에서 정점부 설계휨모멘트
            fIMhf (float): 한계상태에서 어깨부 설계휨모멘트
            fIMpf (float): 소성설계모멘트
            fIphih (float): 소성힌지 저항계수
            fIZ (float): 파형강판의 소성단면계수
            fIFy (float): 파형강판의 항복강도



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.3.4 휨강도 검토의 값
        """

        fIMpf = fIphih * fIZ * fIFy
        if fIMcf <= fIMpf and fIMhf <= fIMpf:
          return "Pass"
        else:
          return "Fail"


# 

