import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041807_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.18.7 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '선박충돌에너지'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.7 선박충돌에너지
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
        A[선박의 충돌에너지];
        B["KDS 24 12 21 4.18.7 (1)"];
        A ~~~ B
        end
    subgraph Variable_def
    VarOut[/출력변수 : 선박의 충돌에너지/];
    VarIn1[/입력변수 : 선박의 용적톤수/];
    VarIn2[/입력변수 : 수리동적질량계수/];
    VarIn3[/입력변수 : 선박충돌속도/];
    end
    Python_Class~~~Variable_def

    D{"적재선박의 경우"};
    E["선박의 용적톤수 = 비적재선박질량 + 화물질량"];
    F["선박의 용적톤수 = 비적재선박질량 + 선박의 수송을 위한 water ballast의 질량"];
    G{"견인되는 바지선의 경우"};
    H["선박의 용적 = 예인선의 질량 + 예인되는 바지선들의 질량"];
    I["<img src ='https://latex.codecogs.com/svg.image?KE=500C_{H}MV^2'>---------------------------------"];
    J(["선박의 충돌에너지"]);

    Variable_def--->D--Yes--->E--->I--->J
    D--No--->F--->I
    Variable_def--->G--->H--->I
        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def the_collision_energy_of_a_ship(fOKE,fIM,fICH,fIV) -> float:
        """선박충돌에너지

        Args:
            fOKE (float): 선박충돌에너지
            fIM (float): 선박의 용적 톤수
            fICH (float): 수리동적질량계수
            fIV (float): 선박충돌속도
        Returns:
            float: 강교 설계기준(한계상태설계법) 4.18.7 선박충돌에너지 (1) 의 값
        """

        fOKE = 500*fICH*fIM*fIV**2
        return(fOKE)


# 

