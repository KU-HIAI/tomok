import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04060402_01(RuleUnit): # KDS241712_04060402_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.6.4.2 (1)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-20'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '지진해석에 의한 단면의 전단력'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.6 붕괴방지수준의 내진성능 검증
    4.6.4 주탑 및 교각의 내진성능검증
    4.6.4.2 전단성능 검증
    (1)
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
    A[전단성능 검증];
    B["KDS 24 17 12 4.6.4.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 지진해석에 의한 단면의 전단력/];
		VarIn2[/입력변수: 전단강도/];




	  VarIn1

		end
		Python_Class ~~~ Variable_def--->E




		E["지진해석에 의한 단면의 전단력≤전단강도"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Verification_of_shear_performance(fIsecsfs,fIshestr) -> bool:
        """지진해석에 의한 단면의 전단력
        Args:
            fIsecsfs (float): 지진해석에 의한 단면의 전단력
            fIshestr (float): 전단강도

        Returns:
            float: 교량내진 설계기준(케이블교량) 4.6.4.2 (1) 의 통과여부
        """
        if fIsecsfs <= fIshestr:
          return("Pass")
        else:
          return("Fail")


