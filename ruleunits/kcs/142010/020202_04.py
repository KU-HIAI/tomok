import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KCS142010_020202_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = '서울대학교, 김정연'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (4)' # 건설기준문서
    ref_date = '2023-10-04'  # 디지털 건설문서 작성일
    doc_date = '2022-09-01'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.2 배합강도
    (4)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.2 배합강도
    (4) 배합강도(f_{cr})는 호칭강도(f_{cn}) 범위를 35MPa 기준으로 분류한 식 (2.2-3) 및 (2.2-4) 중 각 두 식 (①② 및 ①′②′)에 의한 값 중 큰 값으로 정하여야 한다.

f_{cn} ≤ 35 MPa인 경우     (2.2-3)
① f_{cr} = f_{cn} + 1.34s (MPa)
② f_{cr} = (f_{cn} - 3.5) + 2.33s (MPa)

f_{cn} > 35 MPa인 경우     (2.2-4)
①′f_{cr} = f_{cn} + 1.34s (MPa)
②′f_{cr} = 0.9f_{cn} + 2.33s (MPa)
여기서, s ;압축강도의 표준편차(MPa)

    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 콘크리트 배합강도"];
    B["KCS 14 31 30 2.2.2 (4)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.2 (4)"])

    subgraph Variable_def
    VarOut1[/"출력변수: 콘크리트 배합강도"/];


		VarIn1[/"입력변수: 콘크리트 호칭강도"/];
		VarIn2[/"입력변수: 압축강도의 표준편차"/];

    VarOut1  ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D{"<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cn}\leq&space;35&space;MPa'>----------------------"};

		D --> |True|E["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cr}=max((f{cn}&plus;1.34s),((f{cn}-3.5)&plus;2.33s))'>------------------------------------------------------------------------------------"];
		D --> |False|F["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cr}=max((f{cn}&plus;1.34s),(0.9f{cn}&plus;2.33s))'>------------------------------------------------------------------------------"];

		E --> G(["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cr}'>-------"]);
		F --> G(["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cr}'>-------"]);


    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def concrete_mix_strength(fIFcn, fIS) -> float:
        """콘크리트 배합강도

        Args:
            fIFcn (float): 콘크리트 호칭강도
            fIS (float): 압축강도의 표준편차

        Returns:
            fOFcr (float): 콘크리트 배합강도

        """

        if fIFcn <= 35:
            fOFcr = max((fIFcn + 1.34*fIS), ((fIFcn-3.5)+2.33*fIS))
            return fOFcr
        else:
            fOFcr = max((fIFcn + 1.34*fIS), (0.9*fIFcn + 2.33*fIS))
            return fOFcr