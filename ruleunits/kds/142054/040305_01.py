import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040305_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.3.5 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 부착식 앵커의 공칭부착강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
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
    A[공칭부착강도];
    B["KDS 14 20 54 4.3.5 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/출력변수 : 단일 부착식 앵커의 공칭부착강도/];
    VarIn2[/출력변수 : 부착식 앵커 그룹의 공칭부착강도/];
    VarIn3[/입력변수 : 앵커그룹의 투영영향면적/];
    VarIn4[/입력변수 : 단일 앵커의 투영영향면적/];
    VarIn5[/입력변수 : 부착식 앵커에서 연단거리 영향에 따른 인장강도에대한수정계수/];
    VarIn6[/입력변수 :비균열 콘크리트에 사용되는 부착식앵커의수정계수/];
    VarIn7[/입력변수 :인장을 받는 단일부착식 앵커의 기본부착강도/];
    VarIn8[/입력변수 : 부착식 앵커가 편심하중을 받는 경우의 인장강도에대한수정계수/];
    VarIn9[/입력변수 : 부착식 앵커의 수/];
    VarIn10[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리/];
    VarIn1~~~ VarIn5~~~VarIn8
    VarIn2 ~~~ VarIn6~~~VarIn9
    VarIn3 ~~~ VarIn7~~~VarIn10
    VarIn4~~~VarIn5

    end
    Python_Class~~~Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?A_{Na}\leq&space;nA_{Nao}'>----------------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?A_{Nao}=(2\times&space;10d_{a}(\frac{\tau&space;_{uncr}}{7.6})^{0.5})^{2}'>-------------------------------------------------"];
		F{"단일 부착식 앵커"};
    G{"부착식 앵커 그룹"};
    H["<img src='https://latex.codecogs.com/svg.image?N_{a} \leq \frac{A_{Na}}{A_{Nao}}\psi_{ed,Na}\psi_{cp,Na}N_{ba}'>---------------------------------------------------"];
    I["<img src='https://latex.codecogs.com/svg.image?N_{ag} \leq \frac{A_{Na}}{A_{Nao}}\psi_{ec,Na}\psi&space;_{ed,Na}\psi_{cp,Na}N_{ba}'>--------------------------------------------------------------"];
    J(["Pass or Fail"]);

    Variable_def--->D--->E--->F & G
    F--->H--->J
		G--->I--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def nominal_bond_strength_of_a_single_bonded_anchor(fINa,fINag,fIANa,fIANao,fIpsedNa,fIpscpNa,fINba,fIpsecNa,fIn,fIcNa,fIda,fItauncr,fIuserdefined) -> bool:
        """단일 부착식 앵커의 공칭부착강도

        Args:
            fINa (float): 단일 부착식 앵커의 공칭부착강도
            fINag (float): 부착식 앵커 그룹의 공칭부착강도
            fIANa (float): 앵커그룹의 투영영향면적
            fIANao (float): 단일 앵커의 투영영향면적
            fIpsedNa (float): 부착식 앵커에서 연단거리 영향에 따른 인장강도에 대한 수정계수
            fIpscpNa (float): 비균열 콘크리트에 사용되는 부착식앵커의 수정계수
            fINba (float): 인장을 받는 단일부착식 앵커의 기본부착강도
            fIpsecNa (float): 부착식 앵커가 편심하중을 받는 경우의 인장강도에 대한 수정계수
            fIn (float): 부착식 앵커의 수
            fIcNa (float): 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형 볼트의 샤프트 지름
            fItauncr (float): 비균열 콘크리트에 사용된 부착식 앵커의 특성 부착강도
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (1)의 통과여부
        """

        #단일 부착식 앵커 : fIuserdefined = 1
        #부착식 앵커 그룹 : fIuserdefined = 2

        fIcNa = 10*fIda*((fItauncr/7.6)**0.5)
        fIANao = (2*fIcNa)**2
        if fIANa <= fIn * fIANao:
          if fIuserdefined == 1:
           if fINa <= (fIANa / fIANao)*fIpsedNa*fIpscpNa*fINba:
             return "Pass"
           else:
             return "Fail"
          elif fIuserdefined == 2:
            if fINag <= (fIANa / fIANao)*fIpsecNa*fIpsedNa*fIpscpNa*fINba:
              return "Pass"
            else:
              return "Fail"
        else:
          return "Fail"


