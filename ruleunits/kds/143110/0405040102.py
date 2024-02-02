import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040102 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.1.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '구조용 파형강판의 최소두께'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.1 일반사항
    4.5.4.1.2 최소두께
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
		A[Title: 최소두께] ;
		B["KDS 14 31 10 4.5.4.1.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 구조용 파형강판의 최소두께/] ;
			end

		Python_Class ~~~ Variable_def

		E["구조용 파형강판의 최소두께 = 3.0mm"]

		Variable_def --> E --> D(["구조용 파형강판의 최소두께"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Minimum_thickness_of_structural_corrugated_steel_plate(fOmtscss) -> bool:
        """구조용 파형강판의 최소두께
        Args:
            fOmtscss (float): 구조용 파형강판의 최소두께



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.1.2 최소두께의 값
        """



        fOmtscss = 3.0
        return fOmtscss


# 

