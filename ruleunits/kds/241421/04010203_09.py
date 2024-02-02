import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_09 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (9)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '중립축 깊이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (9)
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
    A["중립축 깊이"];
    B["KDS 24 14 21 4.1.2.3 (9)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn9[/입력변수: 중립축 깊이/];
		VarIn1[/입력변수: 작용하는 계수하중에 의한 단면전단력/];
		VarIn2[/입력변수: 단면의 복부폭/];
		VarIn3[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn4[/입력변수: 콘크리트의 재료저항계수/];
		VarIn5[/입력변수: 전단 철근량/];
		VarIn6[/입력변수: 전단철근 간격/];
		VarIn7[/입력변수: 철근의 재료저항계수/];
		VarIn8[/입력변수: 전단철근의 항복강도/];

			VarIn1 & VarIn2 & VarIn3
    	VarIn1 & VarIn2 & VarIn3  ~~~ VarIn4 & VarIn5 & VarIn6
	    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9


		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D--->E--->K
		C["<img src='https://quicklatex.com/cache3/1a/ql_35a66acf9302f3aba5300845677d671a_l3.png'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\frac{A_v}{s}=\frac{V_u}{c\phi&space;_sf_{vy}cot\theta}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?s<c/tan\theta&space;'>------------------------------"]


		K(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def neutral_axis_depth(fIc,fIVu,fIbw,fInu,fIphic,fIfck,fItheta,fIAv,fIs,fIphis,fIfvy) -> bool:
        """중립축 깊이

        Args:
             fIc (float): 중립축 깊이
             fIVu (float): 작용하는 계수하중에 의한 단면 전단력
             fIbw (float): 단면의 복부폭
             fInu (float): 콘크리트 압축강도 유효계수
             fIphic (float): 콘크리트의 재료저항계수
             fIfck (float): 28일 콘크리트 공시체의 기준압축강도
             fItheta (float): 부재 복부에 형성된 스트럿의 경사각
             fIAv (float): 전단 철근량
             fIs (float): 전단철근 간격
             fIphis (float): 철근의 재료저항계수
             fIfvy (float): 전단철근의 항복강도



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (9)의 통과 여부
        """

        import math
        fIc = fIVu / ( fIbw * fInu * fIphic * fIfck) * ( 1/math.tan(math.radians(fItheta)) + math.tan(math.radians(fItheta)) )
        fIAv = fIVu * fIs / ( fIc * fIphis * fIfvy * (1/math.tan(math.radians(fItheta))) )
        if fIs <= fIc / math.tan(math.radians(fItheta)):
          return "Pass"
        else:
          return "Fail"


# 

