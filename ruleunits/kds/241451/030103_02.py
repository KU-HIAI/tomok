import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_030103_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 51 3.1.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '저항계수'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.1 한계상태와 저항계수
    3.1.3 극한한계상태
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
    A[극한한계상태];
    B["KDS 24 14 51 3.1.3 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
      VarIn1[/입력변수: 저항계수/];
			VarIn2[/입력변수: 지지력/];
			VarIn3[/입력변수: 하중계수/];
			VarIn4[/입력변수: 하중/];


      end
      Python_Class ~~~ Variable_def;
      Variable_def---->E--->F
			E["저항계수X지지력 ≥ 하중계수X하중 "];

      F(["Pass or Fail"]);
      E~~~ |"KDS 24 12 11"| E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Resistance_Factor (fIresifa,fIbearca,fIlodfac,fIloadlo) -> bool:
        """저항계수
        Args:
            fIresifa (float): 저항계수
            fIbearca (float): 지지력
            fIlodfac (float): 하중계수
            fIloadlo (float): 하중


        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.1.3 극한한계상태 (2)의 통과 여부
        """

        if fIresifa*fIbearca >= fIlodfac*fIloadlo:
            return "Pass"
        else:
            return "Fail"


# 

