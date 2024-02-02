import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020406_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.6 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '탄성패드 설계'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.6 탄성패드 설계
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
    A[탄성패드의 설계];
    B["KDS 24 90 11 4.2.4.6 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 탄성패드의 설계강도/];
		VarIn2[/입력변수: 탄성중합체의 허용압축응력/];
		VarIn3[/입력변수: 직경/];
		VarIn4[/입력변수: 수평력/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K--->L--->M

		K["<img src='https://latex.codecogs.com/svg.image?N_{Rd}=\frac{1}{1.3}\times\frac{\pi}{4}\times&space;d^{2}\times&space;f_{e,k}'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?N_{Sd}\leq&space;N_{Rd}'>--------------------------------------------------------"];
		M(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Strength_Of_Elastic_Pads(fONRd, fId, fINsd, fIfek) -> bool:
        """탄성패드 설계

        Args:
           fONRd (float): 탄성패드의 설계강도
            fId (float): 직경
            fINsd (float): 수평력
            fIfek (float): 탄성중합체의 허용압축응력

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.4.6 탄성패드 설계 (2)의 통과 여부
        """
        import math
        fONRd = ((math.pi)*(fId**2)*fIfek)/(1.3*4)

        if fINsd <= fONRd :
          return "Pass"
        else :
          return "Fail"


# 

