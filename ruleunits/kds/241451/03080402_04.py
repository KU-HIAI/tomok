import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03080402_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.8.4.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '앵커의 최소 수평간격'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.8 앵커지지 벽체
    3.8.4 지반 파괴에 대한 안전성
    3.8.4.2 앵커의 인발저항력(pullout capacity)
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
    A[앵커의 인발저항력];
    B["KDS 24 14 51 3.8.4.2 (4)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarOut1[/출력변수:앵커의최소 수평간격/]
			VarIn1[/입력변수:정착부 직/]

			VarOut1 ~~~
			VarIn1

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[Max,정착부 직경의 3배, 1500mm]
			D([앵커의 최소 수평간])

			Variable_def ---> C ---> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_horizontal_spacing_of_anchors(fOminanc,fIsetdia) -> float:
        """앵커의 최소 수평간격
        Args:
            fOminanc (float): 앵커의 최소 수평간격
            fIsetdia (float): 정착부 직경

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.8.4.2 앵커의 인발저항력(pullout capacity) (4)의 값

        """

        fOminanc = max(3*fIsetdia,1500)
        return fOminanc


# 

