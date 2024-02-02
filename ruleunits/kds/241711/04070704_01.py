import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_04070704_01(RuleUnit): # KDS241711_04070704_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.7.7.4 (1)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-11-16'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = 'i번째 모드의 탄성지진응답계수'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.7 지진격리교량의 설계
    4.7.7 해석방법
    4.7.7.4 다중모드스펙트럼해석법
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
	A[i번째 모드의 탄성지진응답계수];
	B["KDS 24 17 11 4.7.7.4 (1)"];
	A ~~~ B
	end

	subgraph Variable_def
	VarOut[/출력변수: i번째 모드의 탄성지진응답계수/];
	VarIn1[/입력변수: 해당모드주기/];
	VarIn2[/입력변수: 유효주기/];
	VarIn3[/입력변수: 지진격리교량의 감쇠계수/];
	VarIn4[/입력변수: 지진격리교량의 지반계수/];
	VarIn5[/입력변수: 유효수평지반가속도/];
	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn2 ~~~ VarIn4 & VarIn5
	end

	Python_Class ~~~ Variable_def

	C["<img src='https://latex.codecogs.com/svg.image?C_{si}=\frac{SS_i}{T_i}'>"];
	D["<img src='https://latex.codecogs.com/svg.image?C_{si}=\frac{SS_i}{T_iB}'>"];
	E(["<img src='https://latex.codecogs.com/svg.image?C_{si}'>"]);
	F{"<img src='https://latex.codecogs.com/svg.image?T_i\leq&space;0.8T_{eff}'>"};

	Variable_def ---> F

	F -- Yes ---> C

	F -- No ---> D

	C & D ---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Elastic_seismic_response_coefficient_of_the_ith_mode(fOCsi,fITi,fITeff,fIS,fISi,fIB) -> float:
        """i번째 모드의 탄성지진응답계수

        Args:
            fOCsi (float): i번째 모드의 탄성지진응답계수
            fITi (float): 해당모드주기
            fITeff (float): 유효주기
            fIS (float): 유효수평지반가속도
            fISi (float): 지진격리교량의 지반계수
            fIB (float): 지진격리교량의 감쇠계수

        Returns:
            float: 교량내진설계기준(한계상태설계법) 4.7.7.4 다중모드스펙트럼해석법 (1)의 값
        """

        if fITi <= 0.8 * fITeff:
          fOCsi = fIS * fISi / fITi
        else:
          fOCsi = fIS * fISi / fITi / fIB
        return fOCsi