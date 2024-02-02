import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010501 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.5.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-06'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '핀접합부재의 설계인장강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.5 핀접합부재
    4.1.5.1 인장강도
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
		A[핀접합부재] ;
		B["KDS 14 31 10 4.1.5.1"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 핀접합부재의 설계인장강도/]
    VarIn1[/입력변수: 인장파단/]
    VarIn2[/입력변수: 전단파단/]
    VarIn3[/입력변수: 지압 및 항복의 한계상태/]
		end

		Python_Class ~~~ Variable_def
  	D(["핀접합부재의 설계인장강도=min(인장파단, 전단파단, 지압 및 항복의 한계상태)"])
	Variable_def-->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_tensil_strength_of_pin_joint_member(fOphitPn,fItenrup,fIsherup,fIlsoaas) -> float:
        """핀접합부재의 설계인장강도

        Args:
            fOphitPn (float): 핀접합부재의 설계인장강도
            fItenrup (float): 인장파단
            fIsherup (float): 전단파단
            fIlsoaas (float): 지압 및 항복의 한계상태

        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.1.5.1 인장강도의 값
        """

        fOphitPn = min(fItenrup,fIsherup,fIlsoaas)
        return fOphitPn


# 

