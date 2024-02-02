import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020302_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.3.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '주요 시공단계에서 압축을 받는 비합성박스의 압축플랜지'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.3 시공성
    4.3.3.2.3.2 휨
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
		A[Title: 휨] ;
		B["KDS 14 31 10 4.3.3.2.3.2 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 비합성박스의 압축플랜지/] ;
      VarIn2[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn3[/입력변수: 종방향 뒴을 고려하지 않고 계산된 고려중인 단면의 계수하중에 의한 종방향 플랜지 응력/] ;
      VarIn4[/입력변수: 웨브의 공칭휨좌굴강도/] ;
      VarIn5[/입력변수: 압축플랜지의 공칭휨강도/] ;
			end
			Python_Class ~~~ Variable_def
			VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4 & VarIn5

			C["<img src=https://latex.codecogs.com/svg.image?f_{bu}\leq\phi&space;_{f}F_{nc}>-----------------------"]
			D["<img src=https://latex.codecogs.com/svg.image?f_{bu}\leq\phi&space;_{f}F_{crw}>------------------------"]

			Variable_def --> C --> D --> F(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Compression_flange_of_non_composite_box(fIcofncb,fIphif,fIfbu,fIFcrw,fIFnc) -> bool:
        """주요 시공단계에서 압축을 받는 비합성박스의 압축플랜지
        Args:
            fIcofncb (float): 비합성박스의 압축플랜지
            fIphif (float): 휨에 대한 강도저항계수
            fIfbu (float): 종방향 뒴을 고려하지 않고 계산된 고려 중인 단면의 계수하중에 의한 종방향플랜지응력
            fIFcrw (float): 웨브의 공칭휨좌굴강도
            fIFnc (float): 압축플랜지의 공칭휨강도


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.3.2 휨 (2)의 통과여부
        """


        if fIfbu <= fIphif * fIFnc and fIfbu <= fIphif * fIFcrw:
            return "Pass"
        else:
            return "Fail"


# 

