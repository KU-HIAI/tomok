import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020406_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.6' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-26'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '탄성패드 설계'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.6 탄성패드 설계
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
    A[탄성패드의 최소두께];
    B["KDS 24 90 11 4.2.4.6 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 설계최대 회전각/];
		VarIn2[/입력변수: 탄성패드의 직경/];
		VarOut1[/출력변수: 탄성패드의 최소두께/];

    VarOut1~~~~VarIn1 & VarIn2

    end

    Python_Class ~~~ Variable_def;
		Variable_def--->K--->L

    K["<img src='https://latex.codecogs.com/svg.image?t_{min}=3.33\alpha&space;_{dmax}d\geq\frac{15}{d}'>--------------------------------------------------------"];
		L(["탄성패드의 최소두께"])

   """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_Thickness_Of_The_Elastic_Pad(fOtmin, fIalphadmax, fIdprime) -> bool:
        """탄성패드 설계

        Args:
            fOtmin (float): 탄성패드의 최소두께
            fIalphadmax (float): 설계최대 회전각
            fIdprime (float): 탄성패드의 직경


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.4.6 탄성패드 설계 (1)의 값
        """

        fOtmin = max(3.33*fIalphadmax*fIdprime , fIdprime/15)

        return fOtmin


# 

