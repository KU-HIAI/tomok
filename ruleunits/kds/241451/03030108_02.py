import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030108_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.1.8 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '부식 방지'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.8 부식 방지
    (2)
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
    A[부식 방지];
    B["KDS 24 14 51 3.3.1.8 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 염화물 함량/];
			VarIn2[/입력변수: 황산염 농축율/];
			VarIn3[/입력변수: pH/];

			VarIn1
			VarIn2
			VarIn3

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C([염화물 함량 ≥ 500ppm])
			F([황산염 농축율 ≥ 500ppm])
			D([pH ≤ 5.5])

			Variable_def ---> C & F & D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def corrosion_prevention(fIchlcon,fIsulcon,fIpH) -> bool:
        """부식 방지
        Args:
            fIchlcon (float): 염화물 함량
            fIsulcon (float): 황산염 농축율
            fIpH (float): pH

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.3.1.8(2)의 건설기준을 통과하는지 여부

        """

        if fIchlcon>=500 and fIsulcon>=500 and fIpH<=5.5:
          return "Pass"
        else:
          return "Fail"


# 

