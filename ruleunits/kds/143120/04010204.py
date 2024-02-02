import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143120_04010204 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 14 31 20 4.1.2.4' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-08-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '용접지단 사이의 간격 검토'    # 건설기준명

    #
    description = """
    강구조 피로 및 파단 설계기준(하중저항계수설계법)
    4. 설계(피로 및 파단)
    4.1 피로
    4.1.2 하중유발피로
    4.1.2.4 구속을 줄이기 위한 상세
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
    A(["하중유발피로"]);
    B["KDS 14 31 20 4.1.2.2"];
    A ~~~ B
    end

    subgraph Variable_def
    VarIn1[/입력변수: 하중조합 규정에 명시된 하중계수/];
    VarIn2[/입력변수: 하중효과/];
    VarIn3[/입력변수: 4.1.2.5에 규정된 공칭피로강도/];

    end
    Python_Class ~~~ Variable_def
		Variable_def --> H

    E([PASS or Fail])

		H{"<img src='https://latex.codecogs.com/svg.image?\gamma(\Delta&space;f)\leq(\Delta&space;F)_{n}';\gamma (\Delta f)\leq (\Delta F)_{n}>-----------------------------"};
	  H-->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Examine_the_spacing_between_the_welded_joints(fIdistan) -> bool:
        """용접지단 사이의 간격 검토

        Args:
            fIdistan (float): 용접지단 사이의 간격

        Returns:
            bool: 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.4 구속을 줄이기 위한 상세의 통과 여부
        """
        if fIdistan >= 25:
          return "Pass"
        else:
          return "Fail"


# 

