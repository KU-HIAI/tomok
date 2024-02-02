import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050202_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.2.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '받침점에서의 위험 설계모멘트'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.2 구조물의 이상화
    1.5.2.2 기하학적 자료
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
    A[설계모멘트];
    B["KDS 24 14 21 1.5.2.2 (3)"];
    A ~~~ B
    end

    subgraph Variable_def
	  VarIn1[/입력변수: 설계 모멘트/];
    VarIn2[/입력변수: 고정단모멘트/] ;


    end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["설계 모멘트≥고정단모멘트X0.65"];
		C--->D
		D(["Pass or Fail"]);

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Moment(fIdesmom,fIfixenm) -> bool:
        """받침점에서의 위험 설계모멘트

        Args:
            fIdesmom (float) : 설계모멘트
            fIfixenm (float) : 고정단모멘트




        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 1.5.2.2 기하학적 자료 (3)의 통과여부
        """

        if fIdesmom >= 0.65*fIfixenm :
          return "Pass"
        else :
          return "Fail"


# 

