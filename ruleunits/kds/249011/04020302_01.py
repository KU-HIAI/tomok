import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020302_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축특성'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.2 압축특성과 전단특성
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
    A[탄성받침의 수직 압축강성];
    B["KDS 24 90 11 4.2.3.2 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 탄성받침의 압축탄성계수/];
		VarIn2[/입력변수: 탄성받침의 단면적/];
		VarIn3[/입력변수: 탄성중합체층의 총두께/];
		VarOut1[/출력변수: 탄성받침의 수직 압축강성/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		end

    Python_Class ~~~ Variable_def;
		Variable_def--->D-->E


    E(["탄성받침의 수직 압축강성"])
    D["<img src='https://latex.codecogs.com/svg.image?K_{V}=\frac{E_{c}A}{T_{r}}'>--------------------------------------------------------"];

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Vertical_Compressive_Stiffness_Of_Elastic_Support(fOKv, fIA, fIEc, fITr) -> float:
        """압축특성

        Args:
            fOKv (float): 탄성받침의 수직 압축강성
            fIA (float): 탄성받침의 단면적
            fIEc (float): 탄성받침의 압축탄성계수
            fITr (float): 탄성중합체층의 총두께

        Returns:
            float:

            교량 기타시설설계기준 (한계상태설계법)  4.2.3.2 압축특성 (1)의 값
        """

        fOKv = fIA*fIEc/fITr
        return fOKv


# 

