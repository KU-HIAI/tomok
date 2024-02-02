import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020307 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.7' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '형상계수'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.7 형상계수
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
    A[형상계수];
    B["KDS 24 90 11 4.2.3.7"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 내부강판과 접촉하는 받침의 유효 면적/];
		VarIn2[/입력변수: 탄성받침의 힘이 0인 둘레길이/];
		VarIn3[/입력변수: 압축상태에서 개별 탄성중합체 층의 유효두께/];
		VarIn4[/입력변수: 개별 탄성중합체 층의 두께/];
		VarOut1[/출력변수: 형상계수/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3  & VarIn4

		end

		Python_Class ~~~ Variable_def;
		Variable_def-->E
		E{"압축상태에서 개별 탄성중합체 층의 유효두께"}
		E--적층받침의 경우--->F
		E--3mm이상 외부층의 경우--->G
		F & G--->H--->I

		F["<img src='https://latex.codecogs.com/svg.image?t_{e}=t_{i}'>--------------------------------------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?t_{e}=1.4t_{i}'>--------------------------------------------------------"];
		H["<img src='https://latex.codecogs.com/svg.image?S=\frac{A_{1}}{l_{p}t_{e}}'>--------------------------------------------------------"];
		I(["형상계수"]))

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Shape_Factor(fOS, fIA1, fIlp, fIte, fIti,fIuserdefined) -> float:
        """형상계수

        Args:
            fOS (float): 형상계수률
            fIA1 (float): 내부강판과 접촉하는 받침의 유효 면적
            fIlp (float): 탄성받침의 힘이 0인 둘레길이률
            fIte (float): 압축상태에서 개별 탄성중합체 층의 유효두께
            fIti (float): 개별 탄성중합체 층의 두께
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법) 4.2.3.7 형상계수의 값
        """
        #적층받침의 경우 내부 층> fIuserdefined == 1
        #3mm 이상인 외부 층 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIte = fIti
        if fIuserdefined == 2:
          fIte = 1.4 * fIti

        fOS = fIA1/(fIlp*fIte)
        return fOS


# 

