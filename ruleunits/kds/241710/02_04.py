import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_02_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 2.4' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '소위 변위연성도'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		2. 소요연성도
		(4)
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
    A["소요 연성도"];
    B["KDS 24 17 10 부록 2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:교량의 주축방향 1차모드 주기/];
		VarIn2[/입력변수:통제주기/];
		VarIn3[/입력변수:소요 응답수정계수/];

		VarOut1[/출력변수:소위 변위연성도/];
		VarOut2[/출력변수:변위연성도-응답수정계수 상관계수/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def ---> F
		F -- Yes ---> E ---> D
		F -- No ---> G ---> D ---> C

		C([소요 변위연성도])
		D["<img src='https://latex.codecogs.com/svg.image?\mu_{\Delta}=\lambda_{DR}R_{req}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\lambda_{DR}=(1-\frac{1}{R_{req}}\frac{1.25T_{s}}{T}&plus;\frac{1}{R_{req}})'>---------------------------------"]
		F{T ≤ 1.25T_s}
		G["<img src='https://latex.codecogs.com/svg.image?\lambda_{DR}=1'>---------------------------------"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def so_called_displacement_ductility(fOdisduc,fIdiscoe,fIt,fIts,fIrrea) -> float:
        """소위 변위연성도

        Args:
            fOdisduc (float): 소위 변위연성도
            fIdiscoe (float): 변위연성도-응답수정계수 상관계수
            fIt (float): 교량의 주축방향 1차모드 주기
            fIts (float): 통제주기
            fIrrea (float): 소요 응답수정계수

        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 2. 소요연성도 (4)의 값
        """

        if fIt < fIts * 1.25:
          fIdiscoe = (1 - 1 / fIrrea) * 1.25 * fIts / fIt + 1 / fIrrea
          fOdisduc = fIdiscoe * fIrrea
          return fOdisduc
        else:
          fOdisduc = 1.0 * fIrrea
          return fOdisduc


# 

