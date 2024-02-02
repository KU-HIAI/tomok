import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030105 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.1.5' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝 중심 간의 거리'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.5 말뚝 간격, 여유 거리, 관입 깊이
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
    A[말뚝의 관입];
    B["KDS 24 14 51 3.3.1.5"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 말뚝 중심 간의 거리/];
			VarIn2[/입력변수: 말뚝 직경/];
			VarIn3[/입력변수: 말뚝 폭/];
			VarIn4[/입력변수: 확대기초의 모서리 면까지의 여유거리/];



			VarIn1

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C([말뚝의 중심간의 거리 > 750mm, 말뚝직경 또는 폭의 2.5배 중 큰 값])
			D([확대기초의 모서리 면까지 여유거리 > 225mm])

			Variable_def ---> C & D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def distance_between_center_of_pile(fIbetcen,fIdispil,fIwidsta,fIFrefou) -> bool:
        """말뚝 중심 간의 거리
        Args:
            fIbetcen (float): 말뚝 중심 간의 거리
            fIdispil (float): 말뚝 직경
            fIwidsta (float): 말뚝 폭
            fIFrefou (float): 확대기초의 모서리 면까지의 여유 거리

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.3.1.5 의 건설기준을 통과하는지 여부

        """

        if fIbetcen>max(750,fIdispil,fIwidsta*2.5) and fIFrefou>225:
          return "Pass"
        else:
          return "Fail"


# 

