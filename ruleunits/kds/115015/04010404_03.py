import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS115015_04010404_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 11 50 15 4.1.4.4 (3)' # 건설기준문서
    ref_date = '2021-05-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '강말뚝 단기 허용압축응력'    # 건설기준명

    #
    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.1 말뚝의 축방향 지지력과 변위
    4.1.4.4 강말뚝
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
    A[강말뚝 단기 허용압축응력];
    B["KDS 11 50 15 4.1.4.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarOut1[/출력변수: 단기 허용압축응력/]
    VarIn1[/입력변수: 장기 허용압축응력/] ;

		VarOut1~~~VarIn1

		end
		Python_Class ~~~ Variable_def;

		C["단기 허용압축응력=장기 허용압축응력X1.5"]

		Variable_def --> C
	  C--->D
    D(["단기허용압축응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def short_term_allowable_compressivestress(fOstacos,fIltacos) -> float:
        """강말뚝 단기 허용압축응력

        Args:
            fOstacos (float): 단기 허용압축응력
            fIltacos (float): 장기 허용압축응력

        Returns:
            float: 깊은기초 설계기준(일반설계법)  4.1.4.4 강말뚝 (3)의 값
        """
        fOstacos = fIltacos * 1.5
        return fOstacos


# 

