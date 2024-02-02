import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010104_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.1.4 (2)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-31'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '재하시험에 의한 축방향 허용압축지지력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.1.4 재하시험에 의한 축방향 허용압축지지력 결정
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
    A[허용압축지지력];
    B["KDS 11 50 15 4.1.1.4 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarOut1[/출력변수: 허용압축지지력/]
    VarIn1[/입력변수: 항복하중/] ;
    VarIn2[/입력변수: 극한하중/];
    VarIn3[/입력변수: 지지력 산정식에 의해 구해진 극한지지력/];

		VarOut1~~~VarIn1
		VarOut1~~~VarIn2
		VarOut1~~~VarIn3
		end
		Python_Class ~~~ Variable_def;

		C["지지력 산정식에 의해 구해진 극한지지력중 작은값"]
		D["min(극한하중*1/3,항복하중*0.5)"]
		E{"재하시험"}
		Variable_def --> E
		E --yes--> D
		E --No--> C

    C & D ------>H
    H(["허용압축 지지력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def allowable_compressive_bearing_capacity(fOacombc,fIforcey,fIforceu,fIultbcf,fIuserdefined) -> float:
        """재하시험에 의한 축방향 허용압축지지력

        Args:
            fOacombc (float): 허용압축지지력
            fIforcey (float): 항복하중
            fIforceu (float): 극한하중
            fIultbcf (float): 지지력 산정식에 의해 구해지는 극한지지력중 작은 값
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.1.4 재하시험에 의한 축방향 허용압축지지력 결정 (2)의 값
        """
        #재하시험 없을때 = fIuserdefined == 1
        #재하시험 시 = fIuserdefined == 2

        if fIuserdefined == 1 :
          fOacombc = fIultbcf/3
          return fOacombc

        if fIuserdefined == 2 :
          fOacombc = min(fIforceu/3,fIforcey*0.5)
          return fOacombc


# 

