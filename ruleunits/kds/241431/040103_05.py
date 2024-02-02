import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_040103_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.1.3 (5)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-08-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '인장피로를 받는 볼트의 응력범위'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.1 한계상태
    4.1.3 피로 및 파괴한계상태
    (5)
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
		A[피로 및 파괴한계];
		B["KDS 24 14 31 4.1.39(05)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarOut1[/출력변수: 응력범위/]
		VarOut2[/출력변수: 설계하중으로 인한 볼트 1개당 프라임인장력/]

		VarIn1[/입력변수: 피로설계 활하중/]
		VarIn2[/입력변수: 프라잉력/]
		VarIn3[/입력변수: 외부하중으로 인한 작용력/]
		VarIn4[/입력변수: 설계하중에 의한 볼트 1개당 인장력/]
		VarIn5[/입력변수: 볼트의 중심에서 연단까지 거리/]
		VarIn6[/입력변수: 볼트의 중심에서 연결부의 필릿용접단까지거리/]
		VarIn7[/입력변수: 가장 얇은 연결부의 두께/]

		VarOut1 ~~~ VarIn1 & VarIn2
		VarOut2 ~~~ VarIn4 & VarIn5
		VarIn4 & VarIn5 ~~~ VarIn6 & VarIn7
		end

		Python_Class ~~~ Variable_def



		D(["응력범위=피로설계 활하중+프라잉력"])
		E["Qu ≤ 외부하중으로 인한 작용력X0.6"]
		F["<img src='https://latex.codecogs.com/svg.image?Q_u=\left(\frac{3b}{8a}-\frac{t^3}{328000}\right)P_u'>------------------------------------------------------------------------------------------------"]
		J([Pass or Fail])
		K([Qu])

		Variable_def --> D
		Variable_def --> E
		Variable_def --> F



		E--> J
		F--> K
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Stress_range_of_bolts_subject_to_tensile_fatigue(fOdeltaf, fIdefall, fIfrapow, fIforexl, fIQu, fIPu, fIa, fIb, fIt) -> bool:
        """인장피로를 받는 볼트의 응력범위

        Args:
            fOdeltaf (float): 응력범위
            fIdefall (float): 피로설계 활하중
            fIfrapow (float): 프라잉력
            fIforexl (float): 외부하중으로 인한 작용력
            fIQu (float): 설계하중으로 인한 볼트 1개당 프라잉 인장력
            fIPu (float): 설계하중에 의한 볼트 1개당 인장력
            fIa (float): 볼트의 중심에서 연단까지 거리
            fIb (float): 볼트의 중심에서 연결부의 필릿용접단까지 거리
            fIt (float): 가장 얇은 연결부의 두께

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.1.3 피로 및 파괴한계상태 (5)의 값
        """
        fIQu = ((3*fIb)/(8*fIa)-(fIt^3)/328000)*fIPu

        if fIPu <= 0 :
          fOdeltaf = fIdefall + 0
          return fOdeltaf
        else:
          fOdeltaf = fIdefall + fIQu
          return fOdeltaf

        if fOQu <= fIforexl*0.6 :
          return fOdeltaf, "Pass"
        else:
          return fOdeltaf, "Fail"


# 

