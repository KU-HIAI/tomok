import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010701_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.7.1 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '판요소가 2축 압축상태이며 전단응력이 작용할 때의 콘크리트 스트럿 최대 유효강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
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
    A["콘크리트 스트럿의 최대 유효강도"];
    B["KDS 24 14 21 4.1.7.1 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트 기준압축강도/];
		VarIn2[/입력변수: 주응력/];
		VarIn3[/입력변수: 주응력/];
		VarIn4[/입력변수: 콘크리트의 기준강도/];

		VarOut1[/출력변수: 콘크리트 스트럿의 최대 유효강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4



		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D--->E
		C{"콘크리트 기준강도 50MPa이하인경우"}
		D["<img src='https://latex.codecogs.com/svg.image?&space;f_{c2,max}=0.85f_{ck}\frac{1&plus;3.8(f_1/f_2)}{[1&plus;(f_1/f_2)]^2}'>---------------------------------"]
    E(["콘크리트 스트럿의 최대 유효강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_strut_maximum_effective_strength(fOc2max,fIfck,fIf1,fIf2,fIststco) -> float:
        """판요소가 2축 압축상태이며 전단응력이 작용할 때의 콘크리트 스트럿 최대 유효강도

        Args:
             fOc2max (float): 콘크리트 스트럿 최대 유효강도
             fIfck (float): 콘크리트 기준압축강도
             fIf1 (float): 주응력
             fIf2 (float): 주응력
             fIststco (float): 콘크리트의 기준강도

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (6)의 값
        """

        fOc2max = 0.85*fIfck*(1+3.8*fIf1/fIf2)/(1+(fIf1/fIf2))**2
        if fIststco <= 50:
          return fOc2max, "Pass"
        else:
          return fOc2max, "Fail"


# 

