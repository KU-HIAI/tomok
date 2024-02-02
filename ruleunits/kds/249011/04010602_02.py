import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04010602_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.1.6.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인접 핑거들 사이의 틈'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.6 핑거형 신축이음(Finger Expansion Joint)
    4.1.6.2 요구 성능
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
    A[요구성능];
    B["KDS 24 90 11 4.1.6.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 교축방향으로 열린 길이/];
		VarIn2[/입력변수: 핑거의 겹침/];

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C

		C{"가장 벌어진 상태(계수 극한이동상태)"}
		C--교축방향으로 열린길이 200mm이하---->D

		D["인접 핑거들 사이의 틈≤75mm"];
		C--교축방향으로 열린길이 200mm초과---->E
		E["인접 핑거들 사이의 틈≤50mm"];
		F{"계수 극한이동 상태에서"}
		Variable_def--->F--->G
		G["38mm≤핑거의 겹침,20mm≤인접 핑거들 사이의 틈"];
		G & D & E---->H
		H(["Pass OR Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Length_Open_In_Axial_Direction (fIlenoad,fIfingla,fIfinglw,fIwidth) -> bool:
        """인접 핑거들 사이의 틈
        Args:
            fIlenoad (float): 교축방향으로 열린 길이
            fIfingla (float): 핑거의 겹침
            fIfinglw (float): 핑거들 사이의 틈
            fIwidth (float): 폭

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.1.6.2 요구 성능 (2)의 통과 여부
        """

        if fIlenoad <= 200 and fIwidth <= 75:
          return "Pass"
        elif fIlenoad >= 200 and  fIwidth <= 50:
          if fIfingla >= 38:
            return "Pass"
          elif fIfingla == 0 and fIfinglw >= 20:
            return "Pass"
          else:
            return "Fail"
        else:
          return "Fail"


# 

