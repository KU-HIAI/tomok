import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0401020102_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.2.1.2 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-09-08'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부분용입 그루브용접의 유효면적'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.1 그루브용접
    4.1.2.1.2 부분용입 그루브용접
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
	  A([부분용입 그루브용접])
  	B["KDS 14 31 25 4.1.2.1.2(3)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 부분용입그루브용접의 유효면적/]
	  VarIn1[/입력변수: 용접의 유효길이/]
	  VarIn2[/입력변수: 유효목두께/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end

	  Python_Class ~~~ Variable_def --> D --> E
	  D["부분용입 그루브용접의 유효면적=용접의 유효두께 x 유효목두께"]
	  E([부분용입 그루브용접의 유효면적])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_area_of_partial_joint_penetration_groove_weld(fOefaPJP,fIeflewe,fIefthth) -> bool:
        """부분용입 그루브용접의 유효면적

        Args:
            fOefaPJP (float): 부분용입 그루브용접의 유효면적
            fIeflewe (float): 용접의 유효길이
            fIefthth (float): 유효목두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.2.1.2 부분용입 그루브용접 (3)의 값
        """

        fOefaPJP = fIeflewe*fIefthth
        return fOefaPJP


# 

