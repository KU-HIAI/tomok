import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011102_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지압보강재의 돌출폭'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.2 하중집중점 지압보강재
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
		A[Title: 하중집중점 지압보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.2 (2)"] ;
		A ~~~ B
		end

    subgraph Variable_def
			VarIn1[/입력변수: 주강관의 소성화/] ;
      VarIn2[/입력변수: 전단항복'뚫림'의 한계상태/] ;
      VarIn3[/입력변수: 주강관의 항복강도/] ;
      VarIn4[/입력변수: 주강관의 두께/] ;
    end
    VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
    Python_Class ~~~ Variable_def

    C["<img src=https://latex.codecogs.com/svg.image?b_{t}\leq&space;0.48t_{p}\sqrt{\frac{E}{F_{ys}}}>------------------------"]
    Variable_def --> C --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Protruding_width_of_acupressure_stiffener(fIbt,fItp,fIE,fIFys) -> bool:
        """지압보강재의 돌출폭
        Args:
            fIbt (float): 지압보강재의 돌출폭
            fItp (float): 지압보강재의 두께
            fIE (float): 강재의 탄성계수
            fIFys (float): 지압보강재의 최소항복강도

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.11.2 하중집중점 지압보강재 (2)의 통과여부
        """

        if fIbt <= 0.48 * fItp * (fIE / fIFys) ** 0.5 :
            return "Pass"
        else:
            return "Fail"


# 

