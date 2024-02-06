import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS142054_0406_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 20 54 4.6 (2)' # 건설기준문서
    ref_date = '2021-02-18'  # 디지털 건설문서 작성일
    doc_date = '2023-11-29'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소 중심 간격'    # 건설기준명

    #
    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.6 쪼갬파괴를 방지하기 위한 연단거리, 앵커 간격, 두께
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
    A[앵커의 최소 중심 간격];
    B["KDS 14 20 54 4.6 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 앵커의 최소 중심 간격/];
    VarIn1[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트 지름/];
    VarIn2[/입력변수 : 선설치 앵커/];
    VarIn3[/입력변수 : 후설치 앵커/];
    VarOut ~~~ VarIn1
    end
    Python_Class~~~Variable_def
    D{"(5)에 의해 결정되지 않는 경우"};
    E{"비틀림이 가해지는 경우"};
    F["선설치 앵커"];
    G["선설치 앵커 and 후설치 앵커"];
    H["앵커의 최소 중심 간격 = 4da"];
    I["앵커의 최소 중심 간격 = 6da"];
    J(["앵커의 최소 중심 간격"]);
    Variable_def --->D--->E
    E--Yes--->G--->I--->J
    E—No--->F--->H--->J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def minimum_center_spacing(fOmincen,fIda,fIuserdefined) -> float:
        """최소 중심 간격

        Args:
            fOmincen (float): 최소 중심 간격
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의샤프트지름
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 콘크리트용 앵커 설계기준 4.6 쪼갬파괴를 방지하기 위한 연단거리, 앵커 간격, 두께 (2)의 값

        """

        #비틀림이 가해지지 않는 선설치앵커: fIuserdefined = 1
        #비틀림이 가해지는 선설치앵커 및 후설치앵커: fIuserdefined = 2

        if fIuserdefined == 1 :
          fOmincen = 4 * fIda
        elif fIuserdefined == 2 :
          fOmincen = 6 * fIda

        return fOmincen


# 

