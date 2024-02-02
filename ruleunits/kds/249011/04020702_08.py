import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020702_08 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.7.2 (8)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '볼트구멍 중심으로부터 연단까지의 최대거리'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.7 연결 이음부 설계
    4.2.7.2 볼트 이음부 설계
    (8)
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
    A[볼트구멍 중심으로부터 연단까지의 최대거리];
    B["KDS 24 90 11 4.2.7.2 (8)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 볼트구멍 중심으로부터 연단까지의 최대거리/];
		VarIn2[/입력변수: 표면의 판 두께/];

		VarIn1 & VarIn2

		end

		Python_Class ~~~ Variable_def;
		Variable_def---> C---->D--->E
		C["볼트구멍 중심으로부터 연단까지의 최대거리=표면의 판 두께x8"]
		D["볼트구멍 중심으로부터 연단까지의 최대거리≤150mm"]
		E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Maximum_Distance_From_The_Center_Of_The_Bolt_Hole_To_The_Podium(fImdfcbp,fIplthos) -> bool:
        """볼트구멍 중심으로부터 연단까지의 최대거리

        Args:
             fImdfcbp (float): 볼트구멍 중심으로부터 연단까지의 최대거리
             fIplthos (float): 표면의 판 두께


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.7.2 볼트 이음부 설계 (8)의 통과 여부
        """

        if fImdfcbp == 8*fIplthos and fImdfcbp <= 150:
           return "Pass"
        else:
           return "Fail"


# 

