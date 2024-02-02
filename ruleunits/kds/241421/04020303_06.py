import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04020303_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.2.3.3 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근지름'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.3 간접 균열 제어
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
    A["철근 지름"];
    B["KDS 24 14 21 4.2.3.3 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 평균 지름/];
		VarIn2[/입력변수: 철근 i의 지름/];
		VarIn3[/입력변수: 등가지름/];
		VarOut1[/출력변수: 철근지름/];
    VarOut1~~~VarIn1 & VarIn2  & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--상이한 철근 지름 혼합하여 사용한 단면-->D--->F
		Variable_def--다발철근을 사용할 경우-->C--->F
		D["<img src='https://latex.codecogs.com/svg.image?d_{b,m}=\sum&space;d^2_{b,i}/d_{b,i}'>---------------------------------"]
		C["철근지름=등가지름"]
		F(["철근지름"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def rebar_diameter(fOrebdia,fIdbm,fIsumdbs,fIsumdb,fIequdia,fIuserdefined) -> float:
        """2축 응력 상태의 거더 복부의 유효인장강도

        Args:
             fOrebdia (float): 철근지름
             fIdbm (float): 평균 지름
             fIsumdbs (float): 철근 i 지름의 제곱의 합
             fIsumdb (float): 철근 i 지름의 합
             fIequdia (float): 등가지름
             fIuserdefined (float): 사용자 선택


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.2.3.3 간접 균열 제어 (6)의 값
        """

        #상이한 철근 지름 혼합하여 사용한 단면 > fIuserdefined == 1
        #다발철근을 사용할 경우 > fIuserdefined == 2


        if fIuserdefined == 1:
          fIdbm = fIsumdbs / fIsumdb
          fOrebdia = fIdbm

        if fIuserdefined == 2:
          fOrebdia = fIequdia

        return fOrebdia


# 

