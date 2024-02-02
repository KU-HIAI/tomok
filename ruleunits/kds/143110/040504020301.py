import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040504020301 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.3.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '상부 토피하중에 의한 압축력'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    4.5.4.2.3.1 고정하중에 의한 압축력
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
		A[Title: 고정하중에 의한 압축력] ;
		B["KDS 14 31 10 4.5.4.2.3.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 상부 토피하중에 의한 압축력/] ;
      VarIn1[/입력변수: 뒤채움 흙과 구조물의 상대 축강성 매개변수/] ;
      VarIn2[/입력변수: 뒤채움 흙의 할선탄성계수/] ;
      VarIn3[/입력변수: 구조물 단면의 정검부에서 스프링 라인까지 연직거리의 2배/] ;
      VarIn4[/입력변수: 파형강판의 탄성계수/] ;
      VarIn5[/입력변수: 파형간판의 단면적/] ;
      VarIn6[/입력변수: 단면형상과 토피고에 따른 무차원 아칭계수/] ;
      VarIn7[/입력변수: 상부아치 위 뒤채움 흙과 포장의 자중/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{D}=0.5(1.0-0.1C_{s})A_{f}W>---------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?T_{D}>------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Compressive_force_due_to_top_cover_load(fOTD,fICs,fIEs,fIDv,fIE,fIA,fIAf,fIW) -> bool:
        """상부 토피하중에 의한 압축력
        Args:
            fOTD (float): 상부 토피하중에 의한 압축력
            fICs (float): 뒤채움 흙과 구조물의 상대 축강성 매개변수
            fIEs (float): 뒤채움 흙의 할선탄성계수
            fIDv (float): 구조물 단면의 정점부에서 스프링라인까지 연직거리의 2배
            fIE (float): 파형강판의 탄성계수
            fIA (float): 파형강판의 단면적
            fIAf (float): 단면형상과 토피고에 따른 무차원 아칭계수
            fIW (float): 상부아치 위 뒤채움 흙과 포장의 자중

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3.1 고정하중에 의한 압축력의 값
        """




        fICs = (1000 * fIEs * fIDv) / (fIE * fIA)
        fOTD = 0.5 * (1.0 - 0.1 * fICs) * fIAf * fIW
        return fOTD


# 

