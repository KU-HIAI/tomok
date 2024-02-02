import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030112 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.1.12' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.12 성토체를 관통하는 말뚝
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
    A[성토체를 관통하는 말뚝];
    B["KDS 24 14 51 3.3.1.12"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarIn1[/입력변수: 말뚝/];
			VarIn2[/입력변수: 성토재의 입자크기/];

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C["관입깊이 ≥ 3000mm"]
			D["성토재의 입자크기 ≤ 150mm"]

			Variable_def ---> C & D --->E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def stake(fIstake,fIparcla) -> bool:
        """말뚝
        Args:
            fIstake (float): 말뚝
            fIparcla (float): 성토재의 입자크기

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.3.1.12 의 건설기준을 통과하는지 여부

        """

        if fIstake>=3000 and fIparcla<=150:
          return "Pass"
        else:
          return "Fail"


# 

