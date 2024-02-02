import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050703_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.7.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘 '    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.7 프리스트레스트 구조물
    1.5.7.3 긴장한 뒤 프리스트레스 힘의 계산
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
    A["시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘"];
    B["KDS 24 14 21 1.5.7.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 긴장 도입 직후의 프리스트레싱 강재의 응력/];
    VarIn2[/입력변수: 프리스트레스 강재의 기준항복강도/] ;
	 	VarOut1[/출력변수: 시간 t_0에서 콘크리트에 전달되는 프리스트레스 힘/];


	  VarOut1~~~~VarIn1
		VarOut1~~~~VarIn2
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C
		C["<img src='https://latex.codecogs.com/svg.image?f_{pmo}=min(0.75f_{py},0.85f_{py})'>--------------------------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?P_{mo}=A_{p}f_{pmo}'>--------------------------------------------------------"]
		C--->D

		D--->E
		E(["시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘"]);

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Prestress_Force_Transmitted_To_The_Concrete_At_Time_t0(fIPmo,fIfpmo,fIfpy,fIAp) -> bool:
        """시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘

        Args:
             fIPmo (float) : 시간 t_{0}에서 콘크리트에 전달되는 프리스트레스 힘
             fIfpmo (float) : 긴장 도입 직후의 프리스트레싱 강재의 응력
             fIfpy (float) : 프리스트레스 강재의 기준항복강도
             fIAp (float) : 프리스트레싱 강재의 단면적



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 1.5.7.3 긴장한 뒤 프리스트레스 힘의 계산 (1)의 통과여부
        """

        if fIPmo == min(0.75 * fIfpy, 0.85 * fIfpy) and fIPmo <= fIAp * fIfpmo:
            return True
        else:
            return False


# 

