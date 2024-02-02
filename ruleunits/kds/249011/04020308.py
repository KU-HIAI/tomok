import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020308 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.8' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축하중에 의한 설계병형물'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.8 압축하중에 의한 설계변형률
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
    A[압축하중에 의한 설계변형률];
    B["KDS 24 90 11 4.2.3.8"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 수직설계하중/];
		VarIn2[/입력변수: 하중효과로 감소된 유효 평면적/];
		VarIn3[/입력변수: 설계하중에 의한 받침의 a 방향으로의 최대 수평 상대  변위/];
	  VarIn4[/입력변수: 설계하중에 의한 받침의 b 방향으로의 최대 수평 상대변위/];
	  VarIn5[/입력변수: a 방향 유효길이/];
	  VarIn6[/입력변수: b 방향 유효길이/];

		VarOut1[/출력변수: 압축하중에 의한 설계변형률/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

		end
    Python_Class ~~~ Variable_def;
    Variable_def-->F-->H--->I
    F["<img src='https://latex.codecogs.com/svg.image?A_{r}=A_{1}\left(1-\frac{\nu&space;_{x,d}}{a^{'}}-\frac{\nu&space;_{y,d}}{b^{'}}\right)'>--------------------------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?\epsilon&space;_{c,d}=\frac{1.5\cdot&space;F_{z,d}}{G\cdot&space;A_{r}\cdot&space;S}'>--------------------------------------------------------"];
    I(["압축하중에 의한 설계변형률"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Strain_Due_To_Compressive_Load(fOepsiloncd, fIFzd, fIAr, fIvxd, fIvyd, fIA1, fIS, fIG, fIa, fIb) -> float:
        """압축하중에 의한 설계병형물

        Args:
            fOepsiloncd (float): 압축하중에 의한 설계변형률
            fIFzd (float): 수직설계하중
            fIAr (float): 하중효과로 감소된 유효 평면적
            fIvxd (float): 설계하중에 의한 받침의 a 방향으로의 최대 수평 상대변위
            fIvyd (float): 설계하중에 의한 받침의 b 방향으로의 최대 수평 상대변위
            fIA1 (float): 내부강판과 접촉하는 받침의 유효 면적
            fIS (float): 형상계수
            fIG (float): 전단탄성계수
            fIa (float): a 방향 유효길이
            fIb (float): b 방향 유효길이

        Returns:
            float: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.8 압축하중에 의한 설계변형률의 값
        """

        fOepsiloncd = (1.5*fIFzd)/(fIG*fIS*(fIA1*(1-fIvxd/fIa-fIvyd/fIb)))
        return fOepsiloncd


# 

