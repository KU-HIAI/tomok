import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (7)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '경우에 따른 앵커의 수정계수'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (7)
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
    A[콘크리트 균열 및 보조철근의 유무에 따른 전단강도에 대한 수정계수];
    B["KDS 14 20 54 4.4.2 (7)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 콘크리트 균열 및 보조철근의 유무에 따른 전단강도에 대한 수정계수/];
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지 최소연단거리/];
    VarIn2[/입력변수 : 위험 연단거리/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end
    Python_Class~~~Variable_def
    D{"부재가 사용하중을 받을 때 콘크리트에 균열이 발생하는 부분에 위치한 앵커"};
    E["앵커와 가장자리 사이에 D13이상의 보조철근이 있는 균열 콘크리트에 설치된 앵커"];
    F["보조철근이 없고 D13 미만의 가장자리 보강근이 배치된 균열 콘크리트에 설치된 앵커"];
    G["앵커와 가장자리 사이에 D13 이상의 보조철근이 있고 이 보조철근이 100mm이하 간격의 스터럽으로 둘러싸인 균열 콘크리트에 설치된 앵커"]
    H["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,V}=1.0'>"];
    I["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,V}=1.2'>"];
    J["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,V}=1.4'>"];
    K(["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{c,V}'>"]);
    Variable_def --->D
    D--No--->J---->K
    D--Yes--->E--->I--->K
    D--Yes--->F--->H--->K
    D—Yes--->G--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def correction_factor_for_anchors_of_uncracked_or_cracked_concrete(fOpsicV,fIstigap,fIuserdefined) -> float:
        """경우에 따른 앵커의 수정계수

        Args:
            fOpsicV (float): 경우에 따른 앵커의 수정계수
            fIstigap (float): 간격의 스터럽
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (7)의 값
        """

        #콘크리트 균열이 발생하지 않는다고 해석된 위치에 설치된 앵커 : fIuserdefined = 1
        #해석상 균열이 발생하고 보조철근이 없거나 D13 미만의 가장자리 보강근이 배치된 균열 콘크리트에 설치된 앵커 : fIuserdefined = 2
        #해석상 균열이 발생하고 앵커와 가장자리 사이에 D13 이상의 보조철근이 있는 균열 콘크리트에 설치된 앵커 : fIuserdefined = 3
        #해석상 균열이 발생하고 앵커와 가장자리 사이에 D13 이상의 보조철근이 있고, 이 보조철근이 100mm 이하 간격의 스터럽으로 둘러싸인 균열 콘크리트에 설치된 앵커 : fIuserdefined = 4

        if fIuserdefined == 1:
          fOpsicV = 1.4
          return fOpsicV

        if fIuserdefined == 2:
          fOpsicV = 1.0
          return fOpsicV

        if fIuserdefined == 3:
          fOpsicV = 1.2
          return fOpsicV

        if fIuserdefined == 4 and fIstigap <= 100:
          fOpsicV = 1.4
          return fOpsicV


