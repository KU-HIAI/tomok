import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241431_04100503_07 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 31 4.10.5.3 (7)' # 건설기준문서
    ref_date = '2018-08-30'  # 고시일
    doc_date = '2023-09-04'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '직교이방성 강바닥판의 세부 요구조건'    # 건설기준명

    #
    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 바닥판과 바닥틀
    4.10.5 강재 바닥판
    4.10.5.3 직교이방성 강바닥판
    (7)
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
	  A[직교이방성 강바닥판]
	  B["KDS 24 14 31 4.10.5.3(7)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
		VarIn1[/입력변수: 바닥강판의 두께/];
		VarIn2[/입력변수: 리브 복부판의 간격/];
		VarIn3[/입력변수: 폐단면 리브의 두께/];
		VarIn4[/입력변수: 리브 복부판의 두께/];
		VarIn5[/입력변수: 표면의 강도효과를 고려한 바닥강판의 유효두께/];
		VarIn6[/입력변수: 리브 복부판 간격 중 큰 것/];
		VarIn7[/입력변수: 리브 복부판의 경사진 길이/]
		end

		Python_Class ~~~ Variable_def

		VarIn1 ~~~ VarIn5
		VarIn2 ~~~ VarIn6
		VarIn3 ~~~ VarIn7
		VarIn4 ~~~ VarIn7

		C["바닥강판의두께 &ge; (max(14mm or 리브 복부판의 간격))x 0.04"]
		D["폐단면 리브의 두께 &ge; 7mm"]
	  I["<img src='https://latex.codecogs.com/svg.image?\frac{t_{r}a^{3}}{t_{d,eff}^{3}h^{}}\leq&space;400'>----------------"]

		Variable_def --> C & D & I
		C --> F([Pass or Fail])
		D --> J([Pass or Fail])
		I --> K([Pass or Fail])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Detailed_requirements_for_orthotropic_steel_bottom_plate(fIflpthi,fIspriwe,fIcrithi,fItr,fItdeff,fIa,fIh) -> bool:
        """직교이방성 강바닥판의 세부 요구조건

        Args:
            fIflpthi (float): 바닥강판의 두께
            fIspriwe (float): 리브 복부판의 간격
            fIcrithi (float): 폐단면 리브의 두께
            fItr (float): 리브 복부판의 두께
            fItdeff (float): 표면의 강도효과를 고려한 바닥강판의 유효두께
            fIa (float): 리브 복부판 간격 중 큰 것
            fIh (float): 리브 복부판의 경사진 길이

        Returns:
            bool: 강교 설계기준(한계상태설계법)  4.10.5.3 직교이방성 강바닥판 (7)의 통과 여부
        """

        if fIflpthi >= 14 and fIflpthi >= fIa*0.04:
          return "Pass"
        else:
          print("판의 최소두께가 NG")
          return "Fail"

        if fIcrithi >= 7:
          return "Pass"
        else:
          print("폐단면 리브의 두께 NG")
          return "Fail"

        temp = (fItr*(fIa**3))/((fItdeff**3)*fIh)

        if temp <= 400:
          return temp, "Pass"
        else:
          return temp, "Fail"


# 

