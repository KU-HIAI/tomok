import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060501_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.5.1 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '바닥판 설계'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.5 교량의 콘크리트 바닥슬래브
    4.6.5.1 일반 사항
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
    A["일반 사항"];
    B["KDS 24 14 21 4.6.5.1 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:콘크리트 바닥판 두께/];
		VarIn2[/입력변수:홈 또는 마모 방지 층의 두께/];
		VarIn3[/입력변수:판 최소 두께/];
		VarIn4[/입력변수:프리스트레스트 콘크리트 바닥판의 최소두께/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4


		end

		Python_Class ~~~ Variable_def--->F & E
		F["판 최소두께=콘크리트 바닥판 두께-흠또는 마모방지 층의 두께≥220mm"]
		E["프리스트레스트 콘크리트 바닥판의 최소두께≥200mm"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def thickness_of_plate(fIthigwp,fIplamth,fImintpc) ->float:
        """바닥판 설계
        Args:
             fIthigwp (float): 홈 또는 마모 방지 층의 두께
             fIplamth (float): 판 최소 두께
             fImintpc (float): 프리스트레스트 콘크리트 바닥판의 최소 두께

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.6.5.1(5) 바닥판 설계
        """
        #사람의 통행이 없는 바닥판인 경우: fIuserdefined = 1
        #제한된 수의 사람이 통행하는 바닥판인 경우: fIuserdefined = 2
        #많은 사람이 통행하는 바닥판인 경우: fIuserdefined = 3

        if fIplamth-fIthigwp>=220 and fImintpc>=200:
          return "Pass"
        else:
          return "Fail"


# 
