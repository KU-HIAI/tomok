import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04061301_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.13.1 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '프리텐션 정착영역의 파열저항력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.13 프리텐션 정착부
    4.6.13.1 계수파열저항력
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
    A["프리텐션 정착영역의 파열저항력"];
    B["KDS 24 14 21 4.6.13.1 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:철근의 설계 항복강도/];
		VarIn2[/입력변수:보의 단부에서 h/4 이내에 배치되는 횡방향 철근의 총면적/];
		VarIn3[/입력변수:프리캐스트 보의 높이/];

		VarOut1[/출력변수:프리텐션 정착영역의 파열저항력/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;P_r=f_{yd}A_s'>---------------------------------"]

		F(["프리텐션 정착영역의 파열저항력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Rupture_resistance_of_the_pre_tension_fixing_area(fOPr,fIfyd,fIAs) ->bool:
        """프리텐션 정착영역의 파열저항력
        Args:
             fOPr (float): 프리텐션 정착영역의 파열저항력
             fIfyd (float): 철근의 설계 항복강도
             fIAs (float): 보의 단부에서 h/4 이내에 배치되는 횡방향 철근의 총면적

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.13.1 계수파열저항력 (1)의 값
        """

        fOPr = fIfyd * fIAs
        return fOPr


# 

