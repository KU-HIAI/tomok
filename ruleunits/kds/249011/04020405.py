import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020405 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.5' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '하중 분산'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.5 하중분산
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
    A[하중분산];
    B["KDS 24 90 11 4.2.4.5"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 하중 분산각/];

		VarIn1
		end

		Python_Class ~~~ Variable_def;
		Variable_def--> C

		C{"포트받침의 구성요소 및 재료의 특징 고려 시"}

		C--Yes--->D["하중 분산각≤60°"]
		C--No--->E["하중 분산각=45°"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Load_Dispersion_Angle (fIloadsa,fIuserdefined) -> bool:
        """하중 분산
        Args:
            fIloadsa (float): 하중 분산각
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)    4.2.4.5 하중분산의 통과 여부
        """
        # fIuserdefined = 1
        # 포트받침의 구성요소 및 재료의 특징을 고려한 경우 : fIuserdefined = 2

        if fIuserdefined == 1:
          fIloadsa = 45
          return fIloadsa

        elif fIuserdefined == 2:
          if fIloadsa > 60 :
            return "Fail"
          else:
            return "Pass"


# 

