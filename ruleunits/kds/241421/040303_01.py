import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_040303_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.3.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '프리스트레싱 긴장재의 피로영역범위'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.3 피로한계상태
    4.3.3 프리스트레싱 긴장재
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
    A["프리스트레싱 긴장재"];
    B["KDS 24 14 21 4.3.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 피로응력/];
		VarIn2[/입력변수: 곡률 반경/];
		VarIn1 & VarIn2
		end
		Python_Class ~~~ Variable_def--->C
		C{"곡률반경"}
		C--곡률 반경≥9000mm--->D
		D["피로응력=125MPa"]
		C--곡률 반경<3600mm--->E
		E["피로응력=70MPa"]

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Fatigue_area_range_of_prestressing_tendons(fIfatstr,fIradcuv) -> float:
        """프리스트레싱 긴장재의 피로영역범위

        Args:
             fIfatstr (float): 피로응력
             fIradcuv (float): 곡률 반경

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.3.3 프리스트레싱 긴장재 (1)의 값
        """

        if fIradcuv >= 9000:
          if fIfatstr <= 125:
            return "Pass"
          else:
            return "Fail"

        if fIradcuv <= 3600:
          if fIfatstr <= 70:
            return "Pass"
          else:
            return "Fail"


# 

