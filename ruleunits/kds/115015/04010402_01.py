import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010402_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.4.2 (1)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-31'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '기성콘크리트말뚝 허용압축응력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.4.2 기성콘크리트말뚝
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
    A[기성콘크리트말뚝 허용압축응력];
    B["KDS 11 50 15 4.1.4.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 기성콘크리트말뚝 장기 허용압축응력/];
		VarOut2[/출력변수: 기성콘크리트말뚝 단기 허용압축응력/];
    VarIn1[/입력변수: 콘크리트 설계기준강도/] ;
    VarIn2[/입력변수: 장기 허용압축응력/];


		VarOut~~~VarIn1
		VarOut2~~~VarIn2

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C["35Mpa ≤ 콘크리트설계기기준강도"];
    D(["장기 허용압축응력=콘크리트설계기준강도X0.25"]);
    E(["단기 허용압축응력=장기 허용압축응력X1.5"]);
    C--->D-->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def allowable_compressive_stress_of_precast_concrete_pile(fOltacpcp,fOstacpcp,fIfck) -> float:
        """기성콘크리트말뚝 허용압축응력

        Args:
            fOltacpcp (float): 기성콘크리트말뚝의 장기 허용압축응력
            fOstacpcp (float): 기성콘크리트말뚝의 단기 허용압축응력
            fIfck (float): 콘크리트 설계기준강도

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.4.2 기성콘크리트말뚝 (1)의 값
        """


        fOltacpcp = fIfck * 0.25
        fOstacpcp = fOltacpcp * 1.5
        return fOltacpcp, fOstacpcp


# 

