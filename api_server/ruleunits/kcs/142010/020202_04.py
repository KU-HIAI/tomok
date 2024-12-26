import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020202_04(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (4)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
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
		VarIn1[/"입력변수: 콘크리트 호칭강도"/];
		VarIn2[/"입력변수: 압축강도의 표준편차"/];
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
    def concrete_mix_strength(fINomStr, fIStaDev) -> RuleUnitResult:
        """콘크리트 배합강도

        Args:
            fINomStr (float): 콘크리트 호칭강도
            fIStaDev (float): 압축강도의 표준편차

        Returns:
            fOStrPro (float): 콘크리트 배합강도  
        """
        assert isinstance(fINomStr, float)
        assert isinstance(fIStaDev, float)
        assert 0 <= fINomStr
        assert 0 <= fIStaDev

        if fINomStr <= 35:
            fOStrPro = max((fINomStr + 1.34*fIStaDev), ((fINomStr-3.5)+2.33*fIStaDev))
            return RuleUnitResult(
                result_variables = {
                    "fOStrPro": fOStrPro
                }
            )
        else:
            fOStrPro = max((fINomStr + 1.34*fIStaDev), (0.9*fINomStr + 2.33*fIStaDev))
            return RuleUnitResult(
                result_variables = {
                    "fOStrPro": fOStrPro
                }
            )