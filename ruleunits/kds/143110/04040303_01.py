import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04040303_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.4.3.3 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비강관 부재들의 설계비틀림강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.4. 조합력과 비틀림부재
    4.4.3 비틀림 또는 비틀림, 휨, 전단력 또는/과 축력 등을 동시에 받는 부재
    4.4.3.3 비틀림과 조합응력을 받는 비강관 부재
    (1)
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
		A[Title: 비틀림과 조합응력을 받는 비강관 부재] ;
		B["KDS 14 31 10 4.4.3.3 (1)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 설계비틀림강도/] ;
      VarIn1[/입력변수: 수직응력항복 한계상태/] ;
      VarIn2[/입력변수: 전단응력항복 한계상태/] ;
      VarIn3[/입력변수: 좌굴한계상태/] ;
      VarIn4[/입력변수: 강재의 항복강도/] ;
      VarIn5[/입력변수: 단면의 좌굴응력/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ Variable_def

		C["수직응력항복 한계상태"]
		D["전단응력항복 한계상태"]
		R["좌굴 한계상태"]

		E["<img src=https://latex.codecogs.com/svg.image?F_{n}=F_{y}>-----------------"]
		F["<img src=https://latex.codecogs.com/svg.image?F_{n}=0.6F_{y}>-----------------------"]
		G["<img src=https://latex.codecogs.com/svg.image?F_{n}=F_{cr}>-------------------"]
		T["<img src=https://latex.codecogs.com/svg.image?Min(F_{n}=F_{y}or&space;0.6F_{y}or&space;F_{cr})>----------------------------------------"]



		Variable_def --> C & D & R

		C --> E
		D --> F
		R --> G
		E & F & G --> T --> Q(["<img src=https://latex.codecogs.com/svg.image?F_{n}>---------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_torsional_strength(fOFn,fInosyls,fIshsyls,fIbulist,fIFy,fIFcr) -> bool:
        """비강관 부재들의 설계비틀림강도
        Args:
            fOFn (float): 설계비틀림강도
            fInosyls (float): 수직응력항복 한계상태
            fIshsyls (float): 전단응력항복 한계상태
            fIbulist (float): 좌굴한계상태
            fIFy (float): 강재의 항복강도
            fIFcr (float): 단면의 좌굴응력



        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.4.3.3 비틀림과 조합응력을 받는 비강관 부재 (1)의 값
        """

        # 수직응력항복 한계상태
        fInosyls = fIFy

        # 전단응력항복 한계상태
        fIshsyls = 0.6 * fIFy

        # 좌굴 한계상태
        fIbulist = fIFcr


        fOFn = min(fInosyls,fIshsyls,fIbulist)
        return fOFn


# 

