import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040403_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.3 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-07'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 앵커의 공칭콘크리트 프라이아웃강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.3 전단력을 받는 앵커의 콘크리트프라이아웃강도
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
    A[공칭콘크리트 프라이아웃강도];
    B["KDS 14 20 54 4.4.3 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 단일 앵커의 공칭콘크리트 프라이아웃강도/];
    VarIn2[/입력변수 : 앵커 그룹의 공칭콘크리트 프라이아웃강도/];
    VarIn3[/입력변수 : 전단을 받는 단일 앵커의 공칭콘크리트 프라이아웃강도/];
    VarIn4[/입력변수 : 전단을 받는 앵커 그룹의 공칭콘크리트 프라이아웃강도/];
    VarIn5[/입력변수 : 프라이아웃강도 계수/];
    VarIn6[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn1 ~~~ VarIn4
    VarIn2 ~~~ VarIn5
    VarIn3~~~ VarIn6
    end
    Python_Class~~~Variable_def
    D{"<img src='https://latex.codecogs.com/svg.image?h_{ef}<65mm'>---------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?k_{cp}=1.0'>"];
    F["<img src='https://latex.codecogs.com/svg.image?k_{cp}=2.0'>"];
    G["선설치 앵커, 확장앵커,언더컷앵커"];
    H["<img src='https://latex.codecogs.com/svg.image?N_{cp}=N_{cb}(4.3-2)'>-----------------------------"];
    I["<img src='https://latex.codecogs.com/svg.image?N_{cpg}=N_{cbg}(4.3-3)'>----------------------------------"];
    J["부착식 앵커"];
    M["<img src='https://latex.codecogs.com/svg.image?N_{cp}=min[N_{cb}(4.3-2),N_{a}(4.3-18)]'>-------------------------------------------------"];
    N["<img src='https://latex.codecogs.com/svg.image?N_{cpg}=min[N_{cbg}(4.3-3),N_{ag}(4.3-19)]'>-------------------------------------------------"];
    P["<img src='https://latex.codecogs.com/svg.image?V_{cp}\leq\kappa&space;_{cp}N_{cp}'>-----------------------------"];
    Y{"앵커의 종류"};
    S["<img src='https://latex.codecogs.com/svg.image?V_{cpg}\leq\kappa&space;_{cp}N_{cpg}'>-----------------------------"];
    W(["Pass or Fail"]);
    Variable_def--->D
    D--Yes--->E--->Y--->G
    D--No--->F--->Y--->J
    G--단일 앵커--->H--->P--->W
    G--앵커 그룹--->I--->S--->W
    J--단일 앵커--->M--->P--->W
    J--앵커 그룹--->N--->S--->W
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_concrete_pryout_strength(fIVcp,fIVcpg,fINcp,fINcb,fINa,fINcpg,fINcbg,fINag,fIhef,fIkcp,fIuserdefined1,fIuserdefined2) -> bool:
        """단일 앵커의 공칭콘크리트 프라이아웃강도

        Args:
            fIVcp (float): 단일 앵커의 공칭콘크리트프라이아웃강도
            fIVcpg (float): 앵커 그룹의 공칭콘크리트프라이아웃강도
            fINcp (float): 전단을 받는 단일 앵커의 공칭콘크리트프라이아웃강도
            fINcb (float): 인장을 받는 단일 앵커의 공칭콘크리트브레이크아웃강도
            fINa (float): 인장을 받는 단일 앵커의 공칭부착강도
            fINcpg (float): 전단을 받는 앵커그룹의 공칭콘크리트프라이아웃강도
            fINcbg (float): 인장을 받는 앵커그룹의 공칭콘크리트브레이크아웃강도
            fINag (float): 인장을 받는 그룹부착식 앵커의공칭부착강도
            fIhef (float): 앵커의 유효묻힘 깊이
            fIkcp (float): 프라이 아웃강도계수
            fIuserdefined1 (float): 사용자 선택 1
            fIuserdefined2 (float): 사용자 선택 2

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.4.3 전단력을 받는 앵커의 콘크리트프라이아웃강도 (1)의 통과여부
        """
        #단일 앵커 fIuserdefined1 == 1
        #앵커 그룹 fIuserdefined1 == 2
        #선설치앵커, 확장앵커, 그리고 언더컷앵커 fIuserdefined2 == 1
        #부착식 앵커 fIuserdefined2 == 2

        if fIuserdefined2 == 1:
          fINcp = fINcb
          fINcpg = fINcbg
        elif fIuserdefined2 == 2:
          fINcp = min(fINa, fINcb)
          fINcpg = min(fINag, fINcbg)

        if fIhef < 65:
          fIkcp = 1.0
        elif fIhef >= 65:
          fIkcp = 2.0

        if fIuserdefined1 == 1:
          if fIVcp <= fIkcp * fINcp:
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined1 == 2:
          if fIVcpg <= fIkcp * fINcpg:
            return "Pass"
          else:
            return "Fail"


