import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241221_041501_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 12 21 4.15.1 (1)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-11-23'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '원심하중'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.15 원심하중 및 제동하중, 시제동하중: CF, BR, SB
    4.15.1 원심하중
    (1)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """

    # 플로우차트(mermaid)
    flowchart = """

        """
    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def centrifugal_load(fOLcent,fILtruck,fIC,fIv,fIR,fIN,fIm) -> float:
        """원심하중

        Args:
            fOLcent (float): 원심하중
            fILtruck (float): 표준트럭하중의 축중량
            fIC (float): 계수 C
            fIv (float): 도로설계속도
            fIR (float): 통행차선의 회전반경
            fIN (float): 재하차로의 수
            fIm (float): 다차로 재하계수

        Returns:
            float: 강교 설계기준(한계상태설계법) 4.15.1 원심하중 의 값
        """
        flC = (4/3)*(fIv**2)/9.8/fIR

        if fIN == 1:
          fIm = 1.0
        if fIN == 2:
          fIm = 0.9
        if fIN == 3:
         fIm = 0.8
        if fIN == 4:
          fIm = 0.7
        if fIN == 5:
         fIm = 0.65

        fOLcent = fILtruck*flC*fIm
        return(fOLcent)


# 

