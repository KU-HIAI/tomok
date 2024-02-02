import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04110303_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.11.3.3 (2)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '전체인장을 받는 바닥판 검토'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.11 구조형식
    4.11.3 강바닥판
    4.11.3.3 전체 및 국부적 영향의 중첩
    (2)
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
    A[전체인장, 국부휨 및 전체 전단력을 동시에 받는 바닥판];
    B["KDS 24 14 31 4.11.3.3 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
    VarIn1[/입력변수: 바닥판의 전체 축방향 응력/] ;
    VarIn2[/입력변수: 바닥판의 전체전단응력/];
    VarIn3[/입력변수: 종방향리브를 포함한 바닥판의 유효단면적/];
    VarIn4[/입력변수: 바닥판의 유효폭을 고려한 바닥강판의 설계인장강도/];
		VarIn5[/입력변수: 설계하중에 의한 종방향리브의 국부 휨모멘트/];
    VarIn6[/입력변수: 연단의 항복 도달을 기준으로 한 종방향 리브의 휨강도/];

		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ Variable_def;

		C["<img src='https://latex.codecogs.com/svg.image?\frac{P_{u}}{P_{r}}&plus;\frac{M_{ur}}{M_{rr}}\leq&space;1.33'>------------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?P_{u}=A_{d,eff}(f_{g}^{2}&plus;3f_{vg}^{2})^{0.5}'>-----------------------------------------------------------"]
		E([Pass or Fail])

		Variable_def --> D --> C

		C --> E

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Examine_the_floor_plate_under_full_tension(fIfg,fIfvg,fIAdeff,fIPr,fIMur,fIMrr) -> bool:
        """전체인장을 받는 바닥판 검토

        Args:
            fIfg (float): 바닥판의 전체 축방향 응력
            fIfvg (float): 바닥판의 전체전단응력
            fIAdeff (float): 종방향리브를 포함한 바닥판의 유효단면적
            fIPr (float): 바닥판의 유효폭을 고려한 바닥강판의 설계인장강도
            fIMur (float): 설계하중에 의한 종방향리브의 국부 휨모멘트
            fIMrr (float): 연단의 항복 도달을 기준으로 한 종방향 리브의 휨강도

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.11.3.3 전체 및 국부적 영향의 중첩 (2)의 통과 여부
        """

        temp = fIAdeff*(((fIfg**2)+3*(fIfvg**2))**0.5)
        if (temp/fIPr)+(fIMur/fIMrr) <= 1.33 :
          return "Pass"
        else:
          return "Fail"


# 

