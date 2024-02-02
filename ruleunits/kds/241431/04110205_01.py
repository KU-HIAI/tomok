import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04110205_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.2.5 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '트러스의 솟음'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.2 트러스교
    4.11.2.5 솟음
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
		A[트러스의 솟음];
		B["KDS 24 14 31 4.11.2.5(1)"];
		A ~~~ B
		end

    subgraph Variable_def
		VarIn1[/입력변수: 트러스의 솟음/] ;
		VarIn2[/입력변수: 고정하중에 의한 처짐/] ;
    end
    Python_Class ~~~ Variable_def
    Variable_def -->D
    D["트러스의 솟음 &ge; 고정하중에 의한 처짐"];
    D --> H([PASS or Fail]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Camber_of_truss(fIcamtru,fIcamddl) -> bool:
        """트러스의 솟음

        Args:
            fIcamtru (float): 트러스의 솟음
            fIcamddl (float): 고정하중에 의한 처짐

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.2.5 솟음 (1)의 통과 여부
        """

        if fIcamtru >= fIcamddl:
          return "Pass"
        else:
          return "Fail"


# 

