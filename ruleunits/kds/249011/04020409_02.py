import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020409_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.9 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '피스톤과 포트 접촉부 검토'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.9 피스톤과 포트 접촉부 검토
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
    A[피스톤과 포트 접촉부 검토];
    B["KDS 24 90 11 4.2.4.9 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 포트의 내부 직경/];
		VarIn2[/입력변수: 재료의 항복 강도/];
		VarIn3[/입력변수: 피스톤 면의 폭/];
		VarIn4[/입력변수: 접촉면의 반경/];
		VarIn5[/입력변수: 재료의 항복 강도/];
		VarIn6[/입력변수: 포트의 탄성계수/];
		VarIn7[/입력변수: 포트의 내부 직경/];
		VarIn8[/입력변수: 수평력/];
		VarIn9[/입력변수: 포트의 설계강도/];
		VarIn10[/입력변수: 포트의 설계강도/];
		VarIn1 ~~~ VarIn2 & VarIn3 & VarIn4
    VarIn4 ~~~ VarIn5 & VarIn6 & VarIn7
		VarIn5 ~~~ VarIn8 & VarIn9 & VarIn10


		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K
		Variable_def--->L

		K["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{f_{y}Dw}{1.95}'>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?&space;V_{Rd}=\frac{8.8f_{y}^{2}RD}{E_{d}}'>--------------------------------------------------------"];
		K & L--->M--->N
		M["<img src='https://latex.codecogs.com/svg.image?V_{Sd}\leq V_{Rd}'>---------------"]
    N(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Strength_Of_Pot(fIVRd, fIVSd, fIDprime, fIyldstm, fIwidsop, fIR, fIfy, fIEd, fIindipt,fIuserdefined) -> bool:
        """피스톤과 포트 접촉부 검토

        Args:
            fIVRd (float): 포트의 설계강도
            fIVSd (float): 수평력
            fIDprime (float): 포트의 내부 직경
            fIyldstm (float): 재료의 항복 강도
            fIwidsop (float): 피스톤 면의 폭
            fIR (float): 접촉면의 반경
            fIfy (float): 재료의 항복 강도
            fIEd (float): 포트의 탄성계수
            fIindipt (float): 포트의 내부 직경
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (2)의 값
        """

        #평면 접촉면 > fIuserdefined == 1
        #곡면 접촉면 > fIuserdefined == 2

        if fIuserdefined == 1:
          fIVRd = fIfy*fIDprime*fIwidsop/1.95
          if fIVSd <= fIVRd :
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          fIVRd = 8.8*fIfy*fIfy*fIR*fIindipt/fIEd
          if fIVSd <= fIVRd :
            return "Pass"
          else:
            return "Fail"


# 

