import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011103_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.3 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '수직보강재 양쪽 웨브에서 전단력'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.3 수평보강재
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
		A[Title: 수평보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.3 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
      VarIn1[/입력변수: 수평보강재의 휨응력/] ;
      VarIn2[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn3[/입력변수: 보강재의 최소항복강도/] ;
      VarIn4[/입력변수: 하이브리드 단면의 응력감소계수/] ;
    end
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4

    Python_Class ~~~ Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?f_{s}\leq\phi&space;_{f}R_{h}F_{ys}>------------------------"]
    Variable_def --> C --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shear_force_in_both_webs(fIfs,fIphif,fIFys,fIRh) -> bool:
        """수직보강재 양쪽 웨브에서 전단력
        Args:
            fIfs (float): 수평보강재의 휨응력
            fIphif (float): 휨에 대한 강도저항계수
            fIFys (float): 보강재의 최소항복강도
            fIRh (float): 하이브리드 단면의 응력감소계수

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.11.3 수평보강재 (1)의 통과여부
        """


        if fIfs <= fIphif * fIRh * fIFys:
            return "Pass"
        else:
            return "Fail"


# 

