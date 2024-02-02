import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020304_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '균열 발생 후의 모든 하중 단계에서의 설계 균열폭'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
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
    A["설계 균열폭"];
    B["KDS 24 14 21 4.2.3.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 최대 균열 간격/];
		VarIn2[/입력변수: 적합한 하중조합에 의해 발생된 철근 평균변형률/];
		VarIn3[/입력변수: 인접된 균열 사이 콘크리트의 평균 변형률/];
		VarOut1[/출력변수: 설계 균열폭/];
    VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end
		Python_Class ~~~ Variable_def--->D--->F
		D["<img src='https://latex.codecogs.com/svg.image?\omega&space;_k=l_{r,max}(\varepsilon&space;_{sm}-\varepsilon&space;_{cm})'>---------------------------------"]
		F(["설계 균열폭"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_crack_width(fOwk,fIlrmax,fIepsilonsm,fIepsiloncm) -> float:
        """2축 응력 상태의 거더 복부의 유효인장강도

        Args:
             fOwk (float): 설계 균열폭
             fIlrmax (float): 최대 균열 간격
             fIepsilonsm (float): 적합한 하중조합에 의해 발생된 철근평균변형률
             fIepsiloncm (float): 인접된 균열 사이 콘크리트의 평균 변형률


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 값
        """

        fOwk = fIlrmax * (fIepsilonsm-fIepsiloncm)
        return fOwk


# 

