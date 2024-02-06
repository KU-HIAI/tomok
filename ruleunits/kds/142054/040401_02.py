import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_040401_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 20 54 4.4.1 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-29'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전단력을 받는 앵커의 공칭강도'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.1 전단력을 받는 앵커의 강재강도
    (2)
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
    A[전단력을 받는 앵커의 공칭강도];
    B["KDS 14 20 54 4.4.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 전단력을 받는 앵커의 공칭강도/];
    VarIn2[/입력변수 : 전단에 대한 단일 앵커의 유효단면적/];
    VarIn3[/입력변수 : 앵커 강재의 설계기준인장강도/];
    VarIn4[/입력변수 : 앵커 강재의 설계기준항복강도/];
    VarIn1~~~VarIn3
    VarIn2~~~VarIn4
    end
    Python_Class~~~Variable_def
    D{"부속물 구분"};
    E["선설치 헤드스터드"];
    F["선설치 헤드볼트와 갈고리볼트 그리고 슬리브가 전단 파괴면까지 연장되어 있지 않은 후설치 앵커"];
    G["슬리브가 전단 파괴면까지 연장되어 있는 후 설치 앵커의 경우"];
    H{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    I{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    J{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    K["<img src='https://latex.codecogs.com/svg.image?f_{uta}\leq&space;Min(1.9f_{ya},860MPa)'>---------------------------------------"];
    O["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;A_{se,V}f_{uta}'>-----------------------------"];
    P["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.8A_{se,V}f_{uta}'>---------------------------------"];
    Q["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.6A_{se,V}f_{uta}'>---------------------------------"];
    R["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.48A_{se,V}f_{uta}'>---------------------------------"];
    W{"실험결과가 있는 경우"};
    S["전단력을 받는 앵커의 공칭강도=실험결과에 기초하여 산정"];
    T["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.6A_{se,V}f_{uta}'>---------------------------------"];
    V["<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.48A_{se,V}f_{uta}'>---------------------------------"];
    X(["Pass or Fail"]);
    Variable_def--->K--->D--->E--->H--Yes--->P--->X
    H--No--->O--->X
    D--->F--->I--Yes--->R--->X
    I--No--->Q--->X
    D--->G--->W--Yes--->S--->X
    W--No--->J--Yes--->T--->X
    J--No--->V--->X
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_strength_of_anchor_subjected_to_shear_force(fIVsa,fIAseV,fIfuta,fIfya,fIuserdefined) -> float:
        """전단력을 받는 앵커의 공칭강도

        Args:
            fIVsa (float): 전단력을 받는 앵커의 공칭강도
            fIAseV (float): 전단에 대한 단일 앵커의 유효단면적
            fIfuta (float): 앵커 강재의 설계기준인장강도
            fIfya (float): 앵커 강재의 설계기준항복강도
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준 4.4.1 전단력을 받는 앵커의 강재강도 (2) 값
        """

        #선설치 헤드스터드: fIuserdefined = 1
        #선설치 헤드볼트와 갈고리볼트 그리고 슬리브가 전단 파괴면까지 연장되어 있지 않은 후설치앵커: fIuserdefined = 2
        #선설치 헤드스터드 (그라우트로 채워 높인 부위에 사용되는 앵커): fIuserdefined = 3
        #선설치 헤드볼트와 갈고리볼트 그리고 슬리브가 전단 파괴면까지 연장되어 있지 않은 후설치앵커 (그라우트로 채워 높인 부위에 사용되는 앵커): fIuserdefined = 4

        fIfuta = min(1.9 * fIfya, 860)
        if fIuserdefined == 1:
          if fIVsa <= fIAseV * fIfuta :
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 2:
          if fIVsa <= 0.6 * fIAseV * fIfuta :
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 3:
          if fIVsa <= 0.8 * fIAseV * fIfuta :
            return "Pass"
          else:
            return "Fail"

        elif fIuserdefined == 4:
          if fIVsa <= 0.8 * 0.6 * fIAseV * fIfuta :
            return "Pass"
          else:
            return "Fail"


