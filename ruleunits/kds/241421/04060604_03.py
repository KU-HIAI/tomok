import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060604_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.6.4 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '나선철근의 순간격'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.4 나선철근 상세
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
    A["나선철근 상세"];
    B["KDS 24 14 21 4.6.6.4 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:나선철근의 순간격/];
		VarIn2[/입력변수:굵은골재 최대치수/];
		VarIn3[/입력변수:나선철근 중심간의 간격/];
		VarIn4[/입력변수:축방향 철근 지름/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end
		Python_Class ~~~ Variable_def---> F & D
		Variable_def--->E & G
		F["나선철근의 순간격≥25mm"]
		D["나선철근의 순간격≥굵은골재 최대치수 X1.33"]
		E["나선철근 중심간의 간격≤축방향 철근 지름X6"]
		G["나선철근 중심간의 간격≤150mm"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Instantaneous_gap_of_spiral_rebar(fIIncabe,fIcoaagr,fIspabcs,fIaxibar) ->bool:
        """나선철근의 순간격
        Args:
             fIIncabe (float): 나선철근의 순간격
             fIcoaagr (float): 굵은골재 최대치수
             fIspabcs (float): 나선철근 중심간의 간격
             fIaxibar (float): 축방향 철근 지름
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.6.4 (3) 설계기준에 따른 나선철근의 순간격 적합여부
        """

        if fIIncabe >= 25 and fIIncabe >= fIcoaagr*1.33 and fIspabcs <= fIaxibar*6 and fIspabcs <= 150:
          return "Pass"
        else:
          return "Fail"


# 

