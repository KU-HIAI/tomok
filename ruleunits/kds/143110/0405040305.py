import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040305 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.3.5' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '이음부 강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.5 이음부 강도
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
		A[Title: 이음부 강도] ;
		B["KDS 14 31 10 4.5.4.3.5"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 이음부 강도/] ;
      VarIn1[/입력변수: 휨에 대해서만 설계하는 경우 이음부 강도/] ;
      VarIn2[/입력변수: 파형강판의 소성모멘트강도/] ;
      VarIn3[/입력변수: 압축력과 휨을 동시에 고려할 경우 이음부 강도/] ;
      VarIn4[/입력변수: 설계압축력/] ;
      VarIn5[/입력변수: 이음부의 휨모멘트/] ;
      VarIn6[/입력변수: 파형강판의 소성모멘트 강도/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

		Python_Class ~~~ Variable_def
		C["휨에 대해서만 설계하는 경우"]
		D["압축력과 휨을 동시에 고려하는 경우"]
		E["이음부 설계 시"]

		Q["<img src=https://latex.codecogs.com/svg.image?\phi&space;_{j}S_{m}\geq&space;M_{pf}>-----------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?\phi&space;_{j}S_{s}\geq&space;T_{f}>--------------------------------"]
		R(["Max(이음부의 휨모멘트, <img src=https://latex.codecogs.com/svg.image?0.75M_{pf})>---------------------------------"])

		Variable_def --> C & D & E
		C --> Q
		D --> W
 		E --> R

		Q & W --> S(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def joint_strength(fISs,fIphijSm,fIMpf,fIphijSs,fITf,fIbemojo,fIuserdefined) -> bool:
        """이음부 강도
        Args:
            fISs (float): 이음부 강도
            fIphijSm (float): 휨에 대해서만 설계하는 경우 이음부 강도
            fIMpf (float): 파형강판의 소성모멘트강도
            fIphijSs (float): 압축력과 휨을 동시에 고려할 경우 이음부 강도
            fITf (float): 설계압축력
            fIbemojo (float): 이음부의 휨모멘트
            fIuserdefined (float): 사용자 선택



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.3.5 이음부 강도의 값
        """


        # fIuserdefined == 1 : 휨에 대해서만 설계하는 경우
        # fIuserdefined == 2 : 압축력과 휨을 동시에 고려할 경우




        fISs = max(fIbemojo, 0.75 * fIMpf)
        if  fIuserdefined == 1:
            if fIphijSm >= fIMpf:
                return "Pass", fISs
            else:
                return "Fail"
        elif fIuserdefined == 2:
             if fIphijSs >= fITf:
                return "Pass", fISs
             else:
                return "Fail"


# 

