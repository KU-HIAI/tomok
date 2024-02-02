import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302020201_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.2.2.1 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '휨부재 콘크리트 슬래브의 유효폭'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.2 합성부재
    4.3.2.2.2 휨부재
    4.3.2.2.2.1 일반사항
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
	  A[일반사항]
	  B["KDS 14 31 10 4.3.2.2.2.1(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 콘크리트 슬래브의 유효폭/]
	  VarIn1[/입력변수: 보경간/]
	  VarIn2[/입력변수: 보중심선에서 인접보 중심선까지 거리/]
	  VarIn3[/입력변수: 보중심선에서 슬래브 가장자리/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end
	  Python_Class ~~~ Variable_def --> D --> E --보중심을 기준으로 좌우 각방향에 대한 유효폭의 합--> F
	  D["min(보경간의1/8, 보중심선에서 인접보 중심선까지의 거리 1/2, 보중심선에서 슬래브 가장자리까지의 거리)"]
	  E["각 방향에 대한 유효폭"]
	  F(["콘크리트 슬래브의 유효폭"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Effective_width_of_concrete_slab(fOEffwidcon,fIbeaspa,fIDisbeacen,fISlaEdfbea) -> bool:
        """휨부재 콘크리트 슬래브의 유효폭

        Args:
            fOEffwidcon (float): 콘크리트 슬래브의 유효폭
            fIbeaspa (float): 보경간
            fIDisbeacen (float): 보중심선에서 인접보 중심선까지 거리
            fISlaEdfbea (float): 보중심선에서 슬래브 가장자리

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법)  4.3.2.2.2.1 일반사항 (1)의 값
        """

        fOEffwidcon = min(fIbeaspa / 8, fIDisbeacen / 2, fISlaEdfbea)
        return fOEffwidcon


# 

