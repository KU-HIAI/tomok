import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04050203_04(RuleUnit): # KDS241712_04050203_04

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.5.2.3 (4)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-18'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '골조 교각의 상하단 2차모멘트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.3 주탑 및 교각의 P-Δ효과
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
    A[주탑 및 교각의 P-Δ효과];
    B["KDS 24 17 12 4.5.2.3 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 상단의 횡방향 상대변위/];
    VarIn2[/입력변수: 하단의 횡방향 상대변위/];
		VarIn3[/입력변수: 상단의 2차모멘트/];
			VarIn4[/입력변수: 하단의 2차모멘트/];


	 VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def;




		E["상단의 2차 모멘트=상단의 횡방향 상대변위x1.5x축력"]
		F["하단의 2차 모멘트=하단의 횡방향 상대변위x1.5x축력"]
	Variable_def----> E & F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def P_delta_Effects_of_pylons_and_frmae_piers(fItrdiot,fItrdobm,fOsemotp,fOsemabm,fIaxifor,fIuserdefined) -> float:
        """골조 교각의 2차모멘트

        Args:
            fItrdiot (float): 상단의 횡방향 상대변위
            fItrdobm (float): 하단의 횡방향 상대변위
            fOsemotp (float): 상단의 2차모멘트
            fOsemabm (float): 하단의 2차모멘트
            fIaxifor (float): 축력
            fIuserdefined (float): 사용자선택

        Returns:
            float: 교량내진 설계기준(케이블교량) 4.5.2.3 주탑 및 교각의 P-Δ효과 (4)의 상,하단 2차모멘트
        """

        #상단의 2차모멘트: fIuserdefined = 1
        #하단의 2차모멘트: fIuserdefined = 2

        if fIuserdefined == 1:
          fOsemotp = fItrdiot * 1.5 * fIaxifor
          return fOsemotp
        elif fIuserdefined == 2:
          fOsemabm = fItrdobm * 1.5 * fIaxifor
          return fOsemabm


