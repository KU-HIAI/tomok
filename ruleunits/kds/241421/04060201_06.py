import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060201_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.2.1 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트가 일체로 시공되는 경우의 지점부 단면 설계'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.2 보
    4.6.2.1 주철근
    (6)
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
    A["주철근"];
    B["KDS 24 14 21 4.6.2.1 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:휨강도/];
		VarIn2[/입력변수: 최대 휨모멘트/];
		VarIn1 & VarIn2
		end

		Python_Class ~~~ Variable_def--->F--->G

		F["휨모멘트≥ 최대 휨모멘트X0.15"]
		G(["Pass or fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def steel_bending_moment(fIbenmax,fIbenmom) ->bool:
        """콘크리트가 일체로 시공되는 경우의 지점부 단면 설계
        Args:
             fIbenmax (float): 최대 휨모멘트
             fIcrabem (float): 지점부 단면이 저항할 수 있는 휨모멘트

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 지점부 단면 설계가 4.6.2.1(6)의 건설기준을 만족하는지 여부
        """
        if fIbenmom>=0.15*fIbenmax:
          return "Pass"
        else:
          return "Fail"


# 

