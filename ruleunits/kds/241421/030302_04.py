import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_030302_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.3.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-01'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '프리스트레싱 강재의 기준항복강도 및 기준인장강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.3 프리스트레싱 강재
    3.3.2 재료특성
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
    A["열팽창계수"];
    B["KDS 24 14 21 3.3.3 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 열팽창계수/];
		VarOut1

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D

		C["열팽창계수=12x10-6/°C"]

		D(["열팽창계수"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def specefied_yield_stength_and_specified_tensile_strength_of_prestressing_rebar(fOfpy,fOfpu,fIloawhi,fIvalmal,fInomcse,fIuserdefined) -> float:
        """프리스트레싱 강재의 기준항복강도 및 기준인장강도

        Args:
             fOfpy (float): 기준항복강도
             fOfpu (float): 기준인장강도
             fIloawhi (float): 0.2% 영구연신율이 일어나는 하중
             fIvalmal (float): 인장파단이 일어나는 최대하중의 값
             fInomcse (float): 공칭단면적
             fIuserdefined (float): 사용자 선택




        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.3.2 재료특성 (4) 강도의 값
        """

        # 기준항복강도 계산시: fIuserdefined = 1
        # 기준인장강도 계산시: fIuserdefined = 2
        if fIuserdefined == 1:
          fOfpy = fIloawhi/fInomcse
          return fOfpy
        elif fIuserdefined == 2:
          fOfpu = fIvalmal/fInomcse
          return fOfpu


# 

