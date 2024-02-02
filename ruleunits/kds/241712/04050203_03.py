import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04050203_03(RuleUnit): # KDS241712_04050203_03

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.5.2.3 (3)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-18'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '캔틸레버 교각의 2차모멘트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진 설계기준(케이블교량)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.3 주탑 및 교각의 P-Δ효과
    (3)
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
    B["KDS 24 17 12 4.5.2.3 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
	  VarOut1[/출력변수: 2차 모멘트/];
    VarIn1[/입력변수: 기둥 상단과 하단의 횡방향 최대상대변위/];
		VarIn2[/입력변수: 축력/];


		VarOut1~~~~ VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def;


		D{"휨강성으로 탄성 지진해석 수행하는 경우"}

		E["2차모멘트=기둥 상단과 하단의 횡방향 최대상대변위X1.5X축력"]
	  Variable_def--->D---> E

    E--->F

		F(["2차모멘트"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def P_delta_Effects_of_pylons_and_cantilever_piers(fImdtdtc,fIaxifor,fOsecmom) -> float:
        """캔틸레버 교각의 2차모멘트

        Args:
            fImdtdtc (float): 기둥 상단과 하단의 횡방향 최대상대변위
            fIaxifor (float): 축력
            fOsecmom (float): 2차모멘트

        Returns:
            float: 교량내진 설계기준(케이블교량) 4.5.2.3 주탑 및 교각의 P-Δ효과 (3)의 값
        """
        fOsecmom = fImdtdtc*1.5*fIaxifor
        return fOsecmom


