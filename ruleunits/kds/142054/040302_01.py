import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.2 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 앵커 또는 앵커 그룹 공칭콘크리트 브레이크아웃강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
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
    A[인장력을 받는 단일 앵커 또는 앵커 그룹의 공칭콘크리트 브레이크아웃강도];
    B["KDS 14 20 54 4.3.2 (1)"];
    A ~~~ B
    end
  	subgraph Variable_def
    VarIn1[/입력변수 : 단일앵커의 공칭콘크리트 브레이크아웃강도/];
    VarIn2[/입력변수 : 앵커그룹의 공칭콘크리트 브레이크아웃강도/];
    VarIn3[/입력변수 : 앵커가 편심하중을 받는 경우의 인장강도에대한 수정계수/];
    VarIn4[/입력변수 : 연단거리 영향에 따른 인장강도에대한 수정계수/];
    VarIn5[/입력변수 : 균열 유무에 따른 인장강도에대한 수정계수/];
    VarIn6[/입력변수 : 설치 시 쪼갬인장응력을 고려하여, 후설치앵커를 보조철근없이 비균열 콘크리트에 사용하기위한 인장강도에대한 수정계수/];
    VarIn7[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn8[/입력변수 : 단일 앵커 또는 앵커 그룹 브레이크아웃 파괴면의 투영면적/];
    VarIn9[/입력변수 : 단일 앵커에 대한 콘크리트 브레이크아웃 파괴면의 투영면적/];
    VarIn10[/입력변수 : 그룹에서 인장을 받는 앵커의 수/];
    VarIn1~~~VarIn5~~~VarIn9
    VarIn2~~~VarIn6~~~VarIn8
    VarIn3~~~VarIn6
    VarIn4~~~VarIn7~~~VarIn10
    end
    Python_Class~~~Variable_def
    D["<img src='https://latex.codecogs.com/svg.image?A_{Nco}=9h_{ef}^{2}'>---------------"];
    E["<img src='https://latex.codecogs.com/svg.image?A_{Nc}\leq&space;nA_{Nco}'>----------------"];
    F{"앵커 구분"};
    G["<img src='https://latex.codecogs.com/svg.image?N_{cb}\leq\frac{A_{Nc}}{A_{Nco}}\psi&space;_{ed,N}\psi&space;_{c,N}\psi&space;_{cp,N}N_{b}'>--------------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?N_{cbg}\leq\frac{A_{Nc}}{A_{Nco}}\psi&space;_{ec,N}\psi&space;_{ed,N}\psi&space;_{c,N}\psi&space;_{cp,N}N_{b}'>--------------------------------------------"];
    I(["Pass or Fail"]);
    Variable_def--->D--->E--->F--단일 앵커--->G--->I
    F--앵커 그룹--->H--->I
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_concrete_breakout_strength_of_single_anchor_or_anchor_group(fINcb,fINcbg,fIpsiecN,fIpsiedN,fIpsicN,fIpsicpN,fIhef,fIANc,fIANco,fINb,fIn,fIuserdefined) -> float:
        """단일 앵커 또는 앵커 그룹 공칭콘크리트 브레이크아웃강도

        Args:
            fINcb (float): 단일 앵커의 공칭콘크리트 브레이크아웃강도
            fINcbg (float): 앵커 그룹의 공칭콘크리트 브레이크아웃강도
            fIpsiecN (float): 앵커가 편심하중을 받는 경우의 인장강도에 대한 수정계수
            fIpsiedN (float): 연단거리 영향에 따른 인장강도에 대한 수정계수
            fIpsicN (float): 균열 유무에 따른 인장강도에 대한 수정계수
            fIpsicpN (float): 설치 시 쪼갬인장응력을 고려하여, 후설치앵커를 보조철근 없이 비균열 콘크리트에 사용하기 위한 인장강도에 대한 수정계수
            fIhef (float): 앵커의 유효묻힘깊이
            fIANc (float): 단일 앵커 또는 앵커 그룹 브레이크아웃 파괴면의 투영면적
            fIANco (float): 단일 앵커에 대한 콘크리트 브레이크아웃 파괴면의 투영면적
            fINb (float): 균열 콘크리트에서 인장을 받는 단일앵커의 기본 콘크리트 브레이크아웃강도
            fIn (float): 그룹에서 인장을 받는 앵커의 수
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (1)의 통과 여부
        """

        #단일 앵커: fIuserdefined = 1
        #앵커 그룹: fIuserdefined = 2

        fIANco = 9*(fIhef**2)
        if fIANc <= fIn*fIANco :
          if fIuserdefined == 1:
            if fINcb <= (fIANc/fIANco)*fIpsiedN*fIpsicN*fIpsicpN*fINb :
              return "Pass"
            else:
              return "Fail"
          elif fIuserdefined == 2:
            if fINcbg <= (fIANc/fIANco)*fIpsiecN*fIpsiedN*fIpsicN*fIpsicpN*fINb :
              return "Pass"
            else:
              return "Fail"
          return "Pass"
        else:
          return "Fail"


# 

