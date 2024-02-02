import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_01040501_04(RuleUnit): # KDS241711_01040501_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 1.4.5.1 (4)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-19'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '하중조합'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    1. 일반사항
    1.4 내진설계의 기본방침
    1.4.5 철도 중요구조물의 내진설계 검토사항
    1.4.5.1 열차 주행의 안전성 검증
    (4)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    #### 1.4.5.1 열차 주행의 안전성 검증
    \n (4) 열차 주행의 안전성 검증에는 다음의 하중조합을 적용한다.
    \n $$U=1.0\\left ( DW+L/2+EH+\\left ( WA+BP \\right ) +EQ\\right ) \quad(1.4(철)-1)$$
    \n 여기서,
    \n DW : 고정하중
    \n L/2 : 단선활하중
    \n EH : 수평토압
    \n WA : 정수압과 유수압
    \n BP : 부력 또는 양압력
    \n EQ : 기초의 설계지진력
    """

    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[하중조합];
		B["KDS 24 17 11 1.4.5.1 (4)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarOut[/출력변수: 전단지연에 의한 감소계수/];
		VarIn1[/입력변수: 고정하중/];
		VarIn2[/입력변수: 단선활하중/];
		VarIn3[/입력변수: 수평토압/];
		VarIn4[/입력변수: 정수압과 유수압/];
		VarIn5[/입력변수: 부력 또는 양압력/];
		VarIn6[/입력변수: 기초의 설계지진력/];

		VarOut ~~~ VarIn1
		VarOut ~~~ VarIn2
		VarOut ~~~ VarIn3
		VarIn2 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn2 ~~~ VarIn6
		end

		Python_Class ~~~ Variable_def

		C["<img src='https://latex.codecogs.com/svg.image?U=1.0(DW&plus;L/2&plus;EH&plus;(WA&plus;BP)&plus;EQ)'>--------------------------------------------------------------------------------"];

		D(["<img src='https://latex.codecogs.com/svg.image?U'>"])

		Variable_def --> C --> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def load_combination(fOU, fIDW, fILover2, fIEH, fIWA, fIBP, fIEQ) -> float:
        """하중조합

        Args:
            fOU (float): 하중조합
            fIDW (float): 고정하중
            fILover2 (float): 단선활하중
            fIEH (float): 수평토압
            fIWA (float): 정수압과 유수압
            fIBP (float): 부력 또는 양압력
            fIEQ (float): 기초의 설계지진력

        Returns:
            float: 교량내진설계기준(한계상태설계법) 1.4.5.1 열차 주행의 안전성 검증 (4)의 값
        """
        fOU = 1.0 * (fIDW + fILover2 + fIEH + (fIWA + fIBP) + fIEQ)
        return fOU


# ## 룰 유닛 작성해보기
# 지금까지의 내용을 바탕으로 룰 유닛을 작성해봅시다.
# 
# 새로운 룰 유닛을 작성하기 위해서는, 아래 코드 블럭에서 클래스 이름, 메타정보에 해당하는 변수, 실행 함수의 이름과 내용을 수정하면 됩니다.

