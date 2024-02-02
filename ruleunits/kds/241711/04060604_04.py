import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060604_04(RuleUnit): # KDS241711_04060604_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.4 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '소요 변위연성도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.4 전단 설계
    (4)
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
    A[콘크리트에 의한 공칭전단강도];
    B["KDS 24 17 11 4.6.6.4 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 소요 변위연성도/] ;
    VarIn2[/입력변수: 전단 유효단면적/];
    VarIn3[/입력변수: 기둥 총 단면적/];
    VarIn4[/입력변수: 복부폭/];
    VarIn5[/입력변수: 유효깊이/];
    end

    Python_Class ~~~ Variable_def --> G
    D["<img src='https://latex.codecogs.com/svg.image?V_{c}=k\sqrt{f_{ck}}A_{e}'>------------------------------------"];
    E["<img src='https://latex.codecogs.com/svg.image?k=0.3-0.1(\mu&space;_{\triangle}-2)'>------------------------------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?V_{c}'>-------"]) ;
    G{"<img src='https://latex.codecogs.com/svg.image?\mu&space;_{\Delta}\leq&space;2.0'>------------------"};
   G--Yes--> H["K = 0.3"] --> D
   G--No--> E --> D
   D-->F
   Variable_def -->I & J
   I["원형 단면, 사각형 단면"];
   J["I형 단면, 사각형 중공단면"];
   K["<img src='https://latex.codecogs.com/svg.image?A_{e}=A_{g}\times&space;0.8'>-------------------------------"];
   L["<img src='https://latex.codecogs.com/svg.image?A_{e}=b_{w}d'>-----------------------"];
   M["<img src='https://latex.codecogs.com/svg.image?A_{e}'>--------"];
   I-->K-->M
   J-->L-->M
   M-->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def nominal_shear_strength_of_concrete(fOVc,fImudelta,fIfck,fIAg,fIabdwid,fIeffdep,fIAe,fluserdefined,fIk) -> float:
        """소요 변위연성도

        Args:
            fOVc (float): 콘크리트에 의한 공칭전단강도
            fImudelta (float): 소요 변위연성도
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIAg (float): 기둥 총 단면적
            fIabdwid (float): 복부폭
            fIeffdep (float): 유효깊이
            fIAe (float): 전단 유효단면적
            fluserdefined (float): 사용자 선택
            fIk (float): 계수

        Returns:
            float: fOVc, 콘크리트에 의한 공칭전단강도
        """

        if fImudelta <= 2.0:
          fIk = 0.3
          if fluserdefined == 1: # I형 단면, 사각형 중공단면
            fIAe = fIabdwid * fIeffdep
            fOVc = fIk * fIfck ** 0.5 * fIAe
            return fOVc
          elif fluserdefined == 2: # 원형단면, 사각형단면
            fIAe = 0.8 * fIAg
            fOVc = fIk * fIfck ** 0.5 * fIAe
            return fOVc
        else:
          fIk = 0.3 - 0.1 * (fImudelta - 2)
          if fluserdefined == 1: # I형 단면, 사각형 중공단면
            fIAe = fIabdwid * fIeffdep
            fOVc = fIk * fIfck ** 0.5 * fIAe
            return fOVc
          elif fluserdefined == 2: # 원형단면, 사각형단면
            fIAe = 0.8 * fIAg
            fOVc = fIk * fIfck ** 0.5 * fIAe
            return fOVc