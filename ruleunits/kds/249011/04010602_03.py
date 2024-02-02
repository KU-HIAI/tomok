import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04010602_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.1.6.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '캔틸레버 시점'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.6 핑거형 신축이음(Finger Expansion Joint)
    4.1.6.2 요구 성능
    (3)
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
    B["KDS 24 90 11 4.1.6.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 캔틸레버 시점/];
		VarIn2[/입력변수: 단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면 사이의 거리/];

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C

		C{"20mm≤단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면 사이의 거리"}
		C--NO---->D

		D["단부 앵글 전면으로부터 캔틸레버 방향으로 10mm ≤ 캔틸레버 시점"];

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Cantilever_Start_Point(fIcantsp, fIdisbtp) -> bool:
        """캔틸레버 시점

        Args:
            fIcantsp (float): 캔틸레버 시점
            fIdisbtp (float): 단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면사이의 거리

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법) 4.1.6.2 요구 성능 (3)의 통과 여부
        """

        if fIdisbtp < 20 :
            if fIcantsp >= 10 :
                return "Pass"
            else :
                return "Fail"
        else :
            return "Pass"


# 

