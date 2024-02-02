import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060603_04(RuleUnit): # KDS241711_04060603_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.6.3 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-17'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '총 소요 단면적'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.6 철근콘크리트 기둥의 연성도 내진설계
    4.6.6.3 심부구속 횡방향철근량
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
    A[심부구속 횡방향철근의 총 소요 단면적];
    B["KDS 24 17 11 4.6.6.3 (4)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 총 소요 단면적/] ;
    VarIn1[/입력변수: 띠철근의 수직간격/] ;
    VarIn2[/입력변수: 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로한 심부의 단면치수/];
		VarOut1 ~~~ VarIn1 & VarIn2
    end

    Python_Class ~~~ Variable_def -->D -->F
    D["<img src='https://latex.codecogs.com/svg.image?&space;A_{sb}=0.9ah_{c}(0.008\alpha\beta\frac{f_{ck}}{f_{yh}}&plus;\gamma)'>------------------------------------------------------------"];
    F(["<img src='https://latex.codecogs.com/svg.image?&space;A_{sb}'>----------------"]) ;
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def total_required_cross_sectional_area(fOAsh,fIa,fIhc,fIfck,fIfyh,fIalpha,fIbeta,fIgamma) -> float:
        """총 소요 단면적

        Args:
            fOAsh (float): 총 소요 단면적
            fIa (float): 띠철근의 수직간격
            fIhc (float): 띠철근 기둥의 고려하는 방향으로의, 띠철근 외측표면을 기준으로 한 심부의 단면 치수
            fIfck (float): 콘크리트의 설계기준 압축강도
            fIfyh (float): 횡방향철근의 설계기준 항복강도
            fIalpha (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량 (2)의 식 (4.6-16)의 계수
            fIbeta (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량 (2)의 식 (4.6-17)의 계수
            fIgamma (float): 교량내진설계기준(한계상태설계법) 4.6.6.3 심부구속 횡방향철근량 (2)의 식 (4.6-18)의 계수

        Returns:
            float: fOAsh, 총 소요 단면적
        """

        fOAsh = 0.9 * fIa * fIhc * (0.008 * fIalpha * fIbeta * fIfck / fIfyh + fIgamma)
        return fOAsh