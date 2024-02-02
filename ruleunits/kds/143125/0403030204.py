import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_0403030204 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.3.2.4' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-30'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '조합력을 받는 접합부'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.3 강관 간의 모멘트접합
    4.3.3.2 각형강관
    4.3.3.2.4 T, X형 접합에서 지강관의 휨모멘트와 압축력의 조합

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
        A[Title: T, X형 접합에서 지강관의 휨모멘트와 압축력의 조합] ;
        B["KDS 14 31 25 4.3.3.2.4"] ;
        A ~~~ B
        end

        subgraph Variable_def
          VarIn1[/입력변수: 지강관의 항복강도/] ;
          VarIn2[/입력변수: 휨축에 대한 지강관의 소성단면계수/] ;
          VarIn3[/입력변수: 주강관에 용접된 지강관 면의 유효폭/] ;
          VarIn4[/입력변수: 접합평면과 90를 이루는 각형 지강관의 폭/] ;
          VarIn5[/입력변수: 접합평면에서 측정한 각형 지강관의 높이/] ;
          VarIn6[/입력변수: 지강관의 두께/] ;
        end
        VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

        Python_Class ~~~ Variable_def
        C["<img src='https://latex.codecogs.com/svg.image?(P_{u}/\phi&space;P_{n})&plus;(M_{u-ip}/\phi&space;M_{n-ip})^{2}&plus;(M_{u-op}/\phi&space;M_{n-op})\leq&space;1.0'>------------------------------------------------------------------------------------------------------------------------------------------------"] ;
    Variable_def-->C-->D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def a_joint_that_receives_the_force_of_union(fIPu,fIphiPn,fIMuip,fIphiMnip,fIMuop,fIphiMnop) -> bool:
        """조합력을 받는 접합부

        Args:
            fIPu (float): 주강관의 소요축강도
            fIphiPn (float): 설계강도
            fIMuip (float): 지강관의 소요 면내 휨강도
            fIphiMnip (float): 면내 설계휨강도
            fIMuop (float): 지강관의 소요 면외 휨강도
            fIphiMnop (float): 면외 설계휨강도

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.3.3.2.4 T, X형 접합에서 지강관의 휨모멘트와 압축력의 조합 의 통과여부
        """

        if fIPu/fIphiPn + (fIMuip/fIphiMnip)**2 + (fIMuop/fIphiMnop) <=1.0:
          return("Pass")

        else:
          return("Fail")


# 

