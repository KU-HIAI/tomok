import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04010404_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.4.4' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '접합부재의 압축강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.4 접합부재의 설계강도
    4.1.4.4 설계압축강도
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
	  A([접합부재의 압축강도])
	  B["KDS 14 31 25 4.1.4.4(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 압축강도/]
	  VarIn1[/입력변수: 유효좌굴길이계수/]
	  VarIn2[/입력변수: 지간길이/]
	  VarIn3[/입력변수: 좌굴축에 대한 단면2차반경/]
	  VarIn4[/입력변수: 핀의 항복강도/]
	  VarIn5[/입력변수: 부재의 총단면적/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  VarIn2 ~~~ VarIn4 & VarIn5

	  end

	  Python_Class ~~~ Variable_def --> C --Yes--> E --> F
	  C["<img src='https://latex.codecogs.com/svg.image?KL/r\leq&space;25'>----------------------"]
	  E["<img src='https://latex.codecogs.com/svg.image?P_n=F_yA_g'>------------------------------------------"]
	  F(["<img src='https://latex.codecogs.com/svg.image?P_n'>-----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Compressive_strength_of_the_joint(fOPn,fIK,fIL,fIr,fIFy,fIAg) -> bool:
        """접합부재의 압축강도

        Args:
            fOPn (float): 압축강도
            fIK (float): 유효좌굴길이계수
            fIL (float): 지간길이
            fIr (float): 좌굴축에 대한 단면2차반경
            fIFy (float): 핀의 항복강도
            fIAg (float): 부재의 총단면적

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.4.4 접합부재의 압축강도 (1)의 값
        """

        if fIK * fIL / fIr <= 25 :
          fOPn = fIFy*fIAg
          return fOPn
        else:
          return "Fail"


# 

