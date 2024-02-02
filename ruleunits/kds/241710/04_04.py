import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_부록_04_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 17 10 부록 4.4' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '콘크리트에 의한 공칭전단강도'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    부록. 철근콘크리트 기둥의 연성도 내진설계
		4. 전단 설계
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
    A["콘크리트에 의한 공칭전단강도"];
    B["KDS 24 17 10 부록.4.(4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:소요 변위연성도/];
		VarIn2[/입력변수:전단 유효단면적/];
		VarIn3[/입력변수:기둥 총단면적/];
		VarIn4[/입력변수:복부 폭/];
		VarIn5[/입력변수:유효깊이/];


		VarOut1[/출력변수:콘크리트에 의한 전단강도/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3 & VarIn4 & VarIn5

		end

		Python_Class ~~~ Variable_def

		D["<img src='https://latex.codecogs.com/svg.image?&space;V_{c}=k\sqrt{f_{ck}}A_{e}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?k=0.3-0.1(\mu&space;_{\Delta}-2)'>---------------------------------"]
		C{소요변위 연성도 > 2}
		F{소요변위 연성도 ≤ 2}
		G([콘크리트에 의한 공칭전단강도])
		H[k = 0.3]

		Variable_def ---> C & F
		C ---> E  --->D
		F ---> H ---> D ---> G

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_shear_strength_of_concrete(fOshcon,fIdisduc,fIshcrose,fIcolcros,fIabdwid,fIdepth,flk,flck,fIuserdefined) -> float:
        """콘크리트에 의한 공칭전단강도

        Args:
            fOshcon (float): 콘크리트에 의한 전단강도
            fIdisduc (float): 소요 변위연성도
            fIshcrose (float): 전단 유효단면적
            fIcolcros (float): 기둥 총단면적
            fIabdwid (float): 복부폭
            fIdepth (float): 유효깊이
            flk (float): 계수
            flck (float): 콘크리트의 설계기준압축강도
            fIuserdefined (float): 사용자 선택


        Returns:
            float: 교량 내진설계기준(일반설계법) 부록 4. 전단 설계 (4)의 값
        """

        # 원형단면과 사각형단면
        fIshcrose = fIcolcros * 0.8

        # I형 단면이나 사각형 중공단면
        fIshcrose = fIabdwid * fIdepth


        # fIuserdefined == 1 : 원형단면과 사각형단면
        # fIuserdefined == 2 : I형 단면이나 사각형 중공단면


        if fIdisduc <= 2.0:
          flk = 0.3
          if fIuserdefined == 1:
            fOshcon = flk * flck ** 0.5 * fIshcrose
            return fOshcon
          elif fIuserdefined == 2:
            fIshcrose = fIabdwid * fIdepth
            return fIshcrose
        else:
          flk = 0.3 - 0.1 * (fIdisduc - 2)
          if fIuserdefined == 1:
            fOshcon = flk * flck ** 0.5 * fIshcrose
            return fOshcon
          elif fIuserdefined == 2:
            fIshcrose = fIabdwid * fIdepth
            return fIshcrose




# 

