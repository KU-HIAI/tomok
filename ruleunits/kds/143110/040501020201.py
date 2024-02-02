import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040501020201 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.1.2.2.1 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '절점구속 가새 소요강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.2 기둥 안정용 가새
    4.5.1.2.2 절점구속 가새
    4.5.1.2.2.1 소요강도
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
		A[Title: 소요강도] ;
		B["KDS 14 31 10 4.5.1.2.2.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 소요강도/] ;
      VarIn1[/입력변수: 하중조합으로 구해진 소요인장강도/] ;

			end
		VarOut1 ~~~ VarIn1

		Python_Class ~~~ Variable_def


		E["<img src=https://latex.codecogs.com/svg.image?P_{bu}=0.01P_{u}>--------------------"]



		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?P_{bu}>------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def required_strength(fOPbu,fIPu) -> bool:
        """절점구속 가새 소요강도
        Args:
            fOPbu (float): 소요강도
            fIPu (float): 하중조합으로 구해진 소요인장강도


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.1.2.2.1 소요강도의 통과여부
        """


        fOPbu = 0.01 * fIPu
        return fOPbu


# 

