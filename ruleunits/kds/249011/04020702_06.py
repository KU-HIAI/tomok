import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020702_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.7.2 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트의 최대 중심간격'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.7 연결 이음부 설계
    4.2.7.2 볼트 이음부 설계
    (6)
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
    A[볼트의 최대 중심 간격];
    B["KDS 24 90 11 4.2.7.2 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 볼트의 최대 중심간격/];
		VarIn2[/입력변수: 외측의 판 또는 형강의 두께/];
		VarIn3[/입력변수: 볼트의 응력방향의 간격/];
		VarIn4[/입력변수: 볼트의 응력에 직각방향의 간격/];


	  VarIn1 & VarIn2 & VarIn3 & VarIn4


		end

		Python_Class ~~~ Variable_def;
		Variable_def---> L
		L(["볼트의 최대 중심간격"])
		L~~~ |"Table 24 90 11 4.2-22"| L
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Center_Spacing_For_Bolts(fImaxcsp,fIt,fIp,fIg) -> bool:
        """볼트의 최대 중심간격

        Args:
             fImaxcsp (float): 볼트의 최대 중심간격
             fIt (float): 외측의 판 또는 형강의 두께
             fIp (float): 볼트의 응력방향의 간격
             fIg (float): 볼트의 응력에 직각방향의 간격

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.7.2 볼트 이음부 설계 (6)의 통과 여부
        """

        if 15*fIt-(3*fIg)/8 < 24 and fIp <= 12*fIt:
           return "Pass"
        else:
           return "Fail"


# 

