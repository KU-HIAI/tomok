import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070501_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.5.1 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '채움 토사의 두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.1 현장타설 슬래브 상부구조
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
    A["현장타설 슬래브 상부구조"];
    B["KDS 24 14 21 4.7.5.1 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:채움 토사의 두께/];
		VarIn2[/입력변수:주철근량의 비/];
		VarIn3[/입력변수:경간길이/];
		VarIn4[/입력변수:손실 발생 후 프리스트레스 강재의 유효 프리스트레스/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def
		Variable_def--->D
		D{"채움 토사의 두께≥600mm"}
		D--철근콘크리트 슬래브--->E
		D--프리스트레스트 슬래브--->F

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{1750}{\sqrt{L}}\leq&space;50%'>---------------------------------"]

		F["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\frac{1750}{\sqrt{L}}\frac{f_{pe}}{410}\leq&space;50%'>---------------------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def transverse_reinforcement(fIthifis, fIramasm, fIL, fIfpe) ->bool:
        """채움 토사의 두께
        Args:
             fIthifis (float): 채움 토사의 두께
             fIramasm (float): 주철근량의 비
             fIL (float): 경간길이
             fIfpe (float): 손실 발생 후 프리스트레스 강재의 유효 프리스트레스
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.5.1 (3) 설계기준에 따른 채움 토사의 두께 적합여부
        """
        if fIthifis >= 600:
          if 1750/math.sqrt(fIL)<=50 or 1750/math.sqrt(fIL)*fIfpe/410<=50:
            return "Pass"
          else:
            return "Fail"
        else:
          return "Fail"


# 

