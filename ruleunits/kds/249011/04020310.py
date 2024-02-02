import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020310 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.10' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '각회전으로 인한 설계변형률'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.10 각회전으로 인한 설계변형률
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
    A[각회전으로 인한 설계변형률];
    B["KDS 24 90 11 4.2.3.10"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 탄성받침의 너비 a를 가로지르는 회전각/];
		VarIn2[/입력변수: 탄성받침의 길이 b를 가로지르는 회전각/];
		VarIn3[/입력변수: 탄성중합체 각 층의 두께/];
		VarIn4[/입력변수: 탄성중합체 각 층의 가장 작은 두께/];
		VarOut1[/출력변수: 각회전으로 인한 설계변형률/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

    Python_Class ~~~ Variable_def;
		Variable_def-->F--->I



    F["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{\alpha,d}=\frac{(a^{\prime2}\alpha&space;_{a,d}&plus;b^{\prime2}\alpha&space;_{b,d})t_{i}^{\prime}}{2\sum(t_{i}^{3})}'>--------------------------------------------------------"];

     I(["각회전으로 인한 설계변형률"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Strain_Due_To_Angular_Rotation(fOepsilonqd, fIalphaad, fIalphabd, fIti, fItiprime) -> float:
        """각회전으로 인한 설계변형률

        Args:
           fOepsilonqd (float): 각회전으로 인한 설계변형률
            fIalphaad (float): 탄성받침의 너비 a를 가로지르는 회전각
            fIalphabd (float): 탄성받침의 길이 b를 가로지르는 회전각
            fIti (float): 탄성중합체 각 층의 두께
            fItiprime (float): 탄성중합체 각 층의 가장 작은 두께

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.9 각회전으로 인한 설계변형률의 값
        """

        fOepsilonqd = (fIalphaad+fIalphabd)*fItiprime/(2*fIti^3)
        return fOepsilonqd


# 

