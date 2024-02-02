import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04060205_04(RuleUnit): # KDS241711_04060205_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.6.2.5 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '최대 소성힌지력'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.6 콘크리트교 설계
    4.6.2 교각의 해석 및 설계 강도
    4.6.2.5 교각의 최대 소성힌지력
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
	A([교각의 최대 소성힌지력])
	B["KDS 24 17 11 4.6.2.5(4)"]
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: 최대 소성힌지력/]
	VarIn1[/입력변수: 휨 초과강도/]
	VarIn2[/입력변수: 교각의 길이/]
	VarOut ~~~ VarIn1 & VarIn2
	end
	Python_Class ~~~ Variable_def --> U
	U --"캔틸레버로 거동하는 교각"--> F
  U --"다주가구에서 골조로 거동하는 방향의 교각"--> G
	F & G --> H

	F["최대소성힌지력 = 교각하단의 휨초과강도 ÷ 교각의길이"]
	G["최대소성힌지력 = 기둥상단과 하단의 휨초과강도 ÷ 교각의길이"]
	H([최대 소성힌지력])
	U{"교각의 거동"}
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def plastic_hinge_force(fIflexst,fIpielen) -> float:
        """최대 소성힌지력

        Args:
            fOplhifo (float): 최대 소성힌지력
            fIflexst (float): 휨 초과강도
            fIpielen (float): 교각의 길이

        Returns:
            float: fOplhifo, 최대 소성힌지
        """
        fOplhifo = fIflexst / fIpielen
        return fOplhifo