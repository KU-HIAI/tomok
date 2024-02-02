import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010201_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.1 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-24'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '무근콘크리트와 보통의 철근량을 포함하고 있는 철근콘크리트의 밀도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.1 강도
    (5)
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
    A[평균인장강도];
    B["KDS 24 14 21 3.1.2.1 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 무근 콘크리트 밀도/];
  	VarOut2[/출력변수: 철근 콘크리트 밀도/];



		end
		Python_Class ~~~ Variable_def;
		Variable_def---->E & F
		E(["철근 콘크리트 밀도"]);
		F(["무근 콘크리트 밀도"]);
		E~~~ |"KDS 24 14 21 Table 3.1-1"| E
		F~~~ |"KDS 24 14 21 Table 3.1-1"| F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_density(fOunrcon,fOdencon,fIgammag,fIuserdefined) -> float:
        """무근콘크리트와 보통의 철근량을 포함하고 있는 철근콘크리트의 밀도

        Args:
             fOunrcon (float): 무근콘크리트 밀도
             fOdencon (float): 철근콘크리트 밀도
             fIgammag (float): 절대건조 밀도
             fIuserdefined (float): 사용자 선택


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.1 강도 (5)의 값
        """

        if 1001 <= round(fIgammag) <= 1200:
          fOunrcon = 1250
          fOdencon = 1350
        elif 1201 <= round(fIgammag) <= 1400:
          fOunrcon = 1450
          fOdencon = 1550
        elif 1401 <= round(fIgammag) <= 1600:
          fOunrcon = 1650
          fOdencon = 1750
        elif 1601 <= round(fIgammag) <= 1800:
          fOunrcon = 1850
          fOdencon = 1950
        elif 1801 <= round(fIgammag) <= 2000:
          fOunrcon = 2050
          fOdencon = 2150

        # 무근콘크리트의 설계 단위 질량을 구할 경우: fIuserdefined = 1
        # 철근콘크리트의 설계 단위 질량을 구할 경우: fIuserdefined = 2
        if fIuserdefined == 1:
          return fOunrcon
        elif fIuserdefined == 2:
          return fOdencon


# 

