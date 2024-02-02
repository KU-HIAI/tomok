import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020311 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.11' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '적층탄성받침의 보강판 최소두께'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.11 보강판 규정
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
    A[적층탄성받침의 보강판 최소두께];
    B["KDS 24 90 11 4.2.3.11"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 수직설계하중/];
		VarIn2[/입력변수: 하중효과로 감소된 유효 면적/];
		VarIn3[/입력변수: 내부보강판 양면에서의 탄성중합체의 두께/];
		VarIn4[/입력변수: 내부보강판 양면에서의 탄성중합체의 두께/];
		VarIn5[/입력변수: 보강판의 항복 응력/];
		VarIn6[/입력변수: 보강판의 인장응력을 고려하기 위한 계수/];
    VarOut1[/출력변수: 적층탄성받침의 보강판 최소두께/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

		Python_Class ~~~ Variable_def;
		Variable_def--->G
		G{구멍이 없는 경우}
		G--yes--->K
		G--NO--->L
		K["<img src='https://latex.codecogs.com/svg.image?K_{h}=1'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?K_{h}=2'>--------------------------------------------------------"];

    K & L--->F--->I
    F["<img src='https://latex.codecogs.com/svg.image?t_{s}=\frac{1.3F_{z,d}(t_{1}&plus;t_{2})K_{h}}{A_{r}f_{y}},t_{s}\geq&space;2mm'>--------------------------------------------------------"];

		I(["적층탄성받침의 보강판 최소두께"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_Thickness_Of_Stiffeners_For_Laminated_Elastic_Supports(fOts, fIFzd, fIAr, fIt1, fIt2, fIfy, fIKh, fIuserdefined) -> float:
        """적층탄성받침의 보강판 최소두께

        Args:
            fOts (float): 적층탄성받침의 보강판 최소두께
            fIFzd (float): 수직설계하중
            fIAr (float): 하중효과로 감소된 유효 면적
            fIt1 (float): 내부보강판 양면에서의 탄성중합체의 두께
            fIt2 (float): 내부보강판 양면에서의 탄성중합체의 두께
            fIfy (float): 보강판의 항복 응력
            fIKh (float): 보강판의 인장응력을 고려하기 위한 계수
            fIuserdefined (float): 사용자 선택


        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.11 보강판 규정의 값
        """
        #구멍이 없는 경우 > fIuserdefined == 1
        #구멍이 있는 경우 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIKh = 1
        if fIuserdefined == 2:
          fIKh = 2

        fOts = (1.3*fIFzd*(fIt1+fIt2)*fIKh)/(fIAr*fIfy)
        if fOts < 2:
          fOts = 2
        return fOts


# 

