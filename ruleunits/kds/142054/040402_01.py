import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040402_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.2 (1)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 앵커 또는 앵커 그룹의 전단력에 대한 공칭콘크리트 브레이크아웃강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
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
    A[전단력에 대한 기본 콘크리트 브레이크아웃강도];
    B["KDS 14 20 54 4.4.2 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 기본 콘크리트 브레이크아웃강도/];
    VarIn2[/입력변수 : 앵커의 중심 간격/];
    VarIn3[/입력변수 : 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트단부까지 거리/];
    VarIn4[/입력변수 : 콘크리트 설계기준압축강도/];
    VarIn5[/입력변수 : 앵커의 전단력에 대한 지압 저항길이/];
    VarIn6[/입력변수 : 헤드스터드,헤드볼트,갈고리형 볼트의 샤프트 지름/];
    VarIn7[/입력변수 : 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수/];
    VarIn8[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];

    VarIn1~~~VarIn4 ~~~VarIn7
    VarIn2~~~VarIn5 ~~~VarIn8
    VarIn3~~~VarIn6
    end
    Python_Class~~~Variable_def
    C{"앵커 구분"};
    D{"전단력 작용 방향"};
    E{"전단력 작용 방향"};
    F["<img src='https://latex.codecogs.com/svg.image?A_{Vco}=4.5(c_{a1})^{2}'>-----------------------------"];
    G["<img src='https://latex.codecogs.com/svg.image?A_{Vc}\leq&space;nA_{Vco}'>-----------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?V_{cb}\leq\frac{A_{Vc}}{A_{Vco}}\psi&space;_{ed,V}\psi&space;_{c, V}\psi&space;_{h,V}V_{b}'>--------------------------------------------------"];
    J["<img src='https://latex.codecogs.com/svg.image?V_{cbg}\leq\frac{A_{Vc}}{A_{Vco}}\psi&space;_{ec,V}\psi&space;_{ed, V}\psi&space;_{c,V}\psi&space;_{h,V}V_{b}'>--------------------------------------------------------------------"];
    K["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,V}=1.0'>"];
    M["<img src='https://latex.codecogs.com/svg.image?\psi&space;_{ed,V}=1.0'>"];
    N["<img src='https://latex.codecogs.com/svg.image?V_{cb}\leq\2frac{A_{Vc}}{A_{Vco}}\psi&space;_{ed,V}\psi&space;_{c, V}\psi&space;_{h,V}V_{b}'>-----------------------------------------------------------------------------------"];
    O["<img src='https://latex.codecogs.com/svg.image?V_{cbg}\leq\2frac{A_{Vc}}{A_{Vco}}\psi&space;_{ec,V}\psi&space;_{ed, V}\psi&space;_{c,V}\psi&space;_{h,V}V_{b}'>---------------------------------------------------------------------------------------"];
    P(["Pass or Fail"]);
    Variable_def--->F--->G--->C--단일앵커--->D--평행--->K--->N--->P
    D--직각--->H--->P
    C--앵커그룹--->E--평행--->M--->O--->P
    E--직각--->J--->P
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_concrete_breakout_strength_for_shear_force_of_a_single_anchor_or_group_of_anchors(fIVcb,fIAvc,fIAbco,fIpsiedV,fIpsicV,fIpsihV,fIpsiecV,fIVb,fIVcbg,fIn,fIcaone,fIuserdefined) -> float:
        """단일 앵커 또는 앵커 그룹의 전단력에 대한 공칭콘크리트 브레이크아웃강도

        Args:
            fIVcb (float): 단일 앵커 또는 앵커 그룹의 전단력에 대한 공칭콘크리트 브레이크아웃강도
            fIAvc (float): 전단강도 산정을 위한 단일 앵커 또는 앵커그룹의 콘크리트 브레이크아웃 파괴면 투영면적
            fIAvco (float): 전단강도 산정을 위한 단일 앵커의 콘크리트 브레이크아웃 파괴면 투영면적
            fIpsiedV (float): 연단거리 영향에 따른 전단강도에 대한 수정계수
            fIpsicV (float): 콘크리트 균열 및 보조철근의 유무에 따른 전단강도에 대한 수정계수
            fIpsihV (float): ha< 1.5ca1인 콘크리트 부재에 설치된 앵커의전단강도에 대한 수정계수
            fIpsiecV (float): 앵커 그룹이 편심하중을 받는 경우의 전단강도에 대한 수정계수
            fIVb (float): 균열 콘크리트에서 전단을 받는 단일 앵커의 기본 콘크리트 브레이크아웃강도
            fIVcbg (float): 앵커 그룹에서 가장자리에 직각방향으로 작용하는 전단력
            fIn (float): 앵커 그룹에서 앵커의 수
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의 거리
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준 4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (1)의 통과여부
        """

        #단일 앵커에서 가장자리에 직각방향으로 작용하는 전단력: fIuserdefined = 1
        #앵커 그룹에서 가장자리에 직각방향으로 작용하는 전단력: fIuserdefined = 2
        #단일 앵커에서 가장자리에 평행방향으로 작용하는 전단력: fIuserdefined = 3
        #앵커 그룹에서 가장자리에 평행방향으로 작용하는 전단력: fIuserdefined = 4

        fIAvco = 4.5 * ((fIcaone)**2)
        if fIAvc <= fIn * fIAvco :
          if fIuserdefined == 1:
            if fIVcb <= fIAvc / fIAvco * fIpsiedV * fIpsicV * fIpsihV * fIVb :
              return "Pass"
            else:
              return "Fail"

          elif fIuserdefined == 2:
            if fIVcbg <= fIAvc / fIAvco * fIpsiecV * fIpsiedV * fIpsicV * fIpsihV * fIVb :
              return "Pass"
            else:
              return "Fail"

          elif fIuserdefined == 3:
            if fIVcb <= 2 * fIAvc / fIAvco * fIpsiedV * fIpsicV * fIpsihV * fIVb :
              return "Pass"
            else:
              return "Fail"

          elif fIuserdefined == 4:
            if fIVcbg <= 2 * fIAvc / fIAvco * fIpsiecV * fIpsiedV * fIpsicV * fIpsihV * fIVb :
              return "Pass"
            else:
              return "Fail"
        else:
          return "Fail"


