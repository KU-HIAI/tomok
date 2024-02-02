import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010403_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.4.3 (1)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장타설 콘크리트말뚝의 장기 허용압축응력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.4.3 현장타설 콘크리트말뚝
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
    A[현장타설 콘크리트말뚝 장기 허용압축응력];
    B["KDS 11 50 15 4.1.4.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 현장타설 콘크리트말뚝 장기 허용압축응력/];
    VarIn1[/입력변수: 콘크리트설계기준강도/] ;

		VarOut~~~VarIn1

		end
		Python_Class ~~~ Variable_def;
		Variable_def-->C
		C{"말뚝본체의 전부 또는 일부의 콘크리트가\n 물 또는 흙탕물 중에 타설될 경우 OR 수중타설콘크리트에 대한 조치가 없는경우"};
    C--YES---> D
    D["장기허용압축응력=콘크리트 설계기준강도X20%"];

    C--NO---->E
    E["장기허용압축응력=콘크리트 설계기준강도X25% \n or ≤ 8.5MPa"];
    F(["장기허용압축응력"]);
    E & D---->F
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def longterm_allowable_compressive_stress_of_cast_in_place_concretepile(fOlacccp,fIfck,fIuserdefined) -> float:
        """현장타설 콘크리트말뚝의 장기 허용압축응력

        Args:
            fOlacccp (float): 현장타설 콘크리트말뚝의 장기 허용압축응력
            fIfck (float): 콘크리트 설계기준강도
            fIuserdefined (float): 사용자 선택

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.4.3 현장타설 콘크리트말뚝 (1)의 값
        """
        #말뚝본체의 전부 또는 일부의 콘크리트가 물 또는 흙탕물 중에 타설될 경우 = fIuserdefined == 1
        #말뚝본체 콘크리트 타설을 위한 굴착구멍에 물 또는 흙탕물이 없는 상태에서 콘크리트가 타설될 경우 또는 수중타설콘크리트에 대한 조치가 있는 경우 = fIuserdefined == 2

        if fIuserdefined == 1:
          fOlacccp = fIfck * 0.2
          return fOlacccp

        if fIuserdefined == 2:
          fOlacccp = min(fIfck * 0.25, 8.5)
          return fOlacccp


# 

