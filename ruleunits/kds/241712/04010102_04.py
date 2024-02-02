import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04010102_04(RuleUnit): # KDS241712_04010102_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.1.1.2 (4)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '유효수평지반가속도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.1 설계일반사항
    4.1.1 설계지반운동
    4.1.1.2 지진위험도 및 유효수평지반가속도
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
    A[평균압축강도];
    B["KDS 24 17 21 4.1.1.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지진구역계수/];
    VarIn2[/입력변수: 위험도계수/] ;
 	VarOut1[/출력변수: 유효수평지반가속도/];


	 VarOut1~~~VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def;


		D["유효수평지반가속도=지진구역계수X위험도계수"]

		Variable_def--->D--->J
		J(["유효수평지반가속도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def effective_horizontal_ground_acceleration(fIZ,fII,fOS) -> float:
        """유효수평지반가속도

        Args:
            fIZ (float): 지진구역계수
            fII (float): 위험도계수
            fOS (float): 유효수평지반가속도

        Returns:
            float: 교량내진 설계기준(케이블교량) 4.1.1.2 (4) 유효수평지반가속도
        """
        fOS = fIZ * fII
        return(fOS)


