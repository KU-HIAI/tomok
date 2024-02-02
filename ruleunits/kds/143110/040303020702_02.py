import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303020702_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.2.7.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '폐단면 박스의 압축플랜지 공칭휨강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.2 박스거더
    4.3.3.2.7 휨강도-정모멘트부
    4.3.3.2.7.2 비조밀단면
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
		A[Title: 비조밀단면] ;
		B["KDS 14 31 10 4.3.3.2.7.2 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
			VarOut1[/출력변수: 압축플랜지 공칭휨강도/] ;
      VarOut2[/출력변수: 인장플랜지 공칭휨강도/] ;
      VarIn1[/입력변수: 웨브 응력감소계수/] ;
      VarIn2[/입력변수: 하이브리드 단면의 응력감소계수/] ;
      VarIn3[/입력변수: 압축플랜지의 최소항복강도/] ;
      VarIn4[/입력변수: 하중조합으로 구해진 1차 층간변위/] ;
      VarIn5[/입력변수: 계수하중에 의한 플랜지의 순수비틀림 전단응력/] ;
      VarIn6[/입력변수: 박스거더 단면의 폐합단면적/] ;
      VarIn7[/입력변수: 계수하중에 의한 내부 비틀림모멘트/] ;
      VarIn8[/입력변수: 인장플랜지의 최소항복강도/] ;
      VarIn9[/입력변수: 계수하중에 의한 플랜지의 순수비틀림 전단응력/] ;
			end
			Python_Class ~~~ Variable_def
			VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3
			VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
			VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

			C["<img src=https://latex.codecogs.com/svg.image?F_{nc}=R_{b}R_{h}F_{yc}>--------------------------"]
			D["<img src=https://latex.codecogs.com/svg.image?F_{nc}=R_{b}R_{h}F_{yc}\Delta&space;>--------------------------"]
			E["<img src=https://latex.codecogs.com/svg.image?\Delta=\sqrt{1-3(\frac{f_{v}}{F_{yc}})^{2}}>--------------------------"]
			H["<img src=https://latex.codecogs.com/svg.image?F_{nt}=R_{h}F_{yt}\Delta&space;>--------------------------"]
			I["<img src=https://latex.codecogs.com/svg.image?\Delta=\sqrt{1-3(\frac{f_{v}}{F_{yt}})^{2}}>--------------------------"]

			Variable_def --"U형단면 박스"--> C --> F(["<img src=https://latex.codecogs.com/svg.image?F_{nc}>---------"])
			Variable_def --"폐단면 박스"--> E --> D --> F
			Variable_def --> I --> H -->U(["<img src=https://latex.codecogs.com/svg.image?F_{nt}>---------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Compression_Flange_Nominal_Flexural_Strength(fOFnc,fIRb,fIRh,fIFyc,fIdelta,fIFv,fIAo,fIT,fOFnt,fIFyt,fIuserdefined,fItfc,fItft) -> bool:
        """폐단면 박스의 압축플랜지 공칭휨강도
        Args:
            fOFnc (float): 압축플랜지 공칭휨강도
            fIRb (float): 웨브응력감소계수
            fIRh (float): 하이브리드 단면의 응력감소계수
            fIFyc (float): 압축플랜지의 최소항복강도
            fIdelta (float): 하중조합으로 구해진 1차 층간변위
            fIFv (float): 계수하중에 의한 플랜지의 순수비틀림 전단응력
            fIAo (float): 박스거더 단면의 폐합단면적
            fIT (float): 계수하중에 의한 내부 비틀림모멘트
            fOFnt (float): 인장플랜지 공칭휨강도
            fIFyt (float): 인장플랜지의 최소항복강도
            fIuserdefined (float): 사용자 선택
            fItfc (float):
            fItft (float):

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.2.7.2 비조밀단면 (2)의 통과여부
        """

        # 공칭휨강도
        # fIuserdefined == 1 : U형단면 박스의 압축플랜지 공칭휨강도
        # fIuserdefined == 2 : 폐단면 박스의 압축플랜지 공칭휨강도
        # fIuserdefined == 3 : 폐단면과 U형단면 박스의 인장플랜지 공칭휨강도


        if fIuserdefined == 1:
          fOFnc = fIRb * fIRh * fIFyc
          return fOFnc
        elif fIuserdefined == 2:
          fIFv = fIT / (2 * fIAo * fItfc)
          fIdelta = (1 - 3 * (fIFv / fIFyc) ** 2) ** 0.5
          fOFnc = fIRb * fIRh * fIFyc * fIdelta
          return fOFnc
        elif fIuserdefined == 3:
          fIFv = fIT / (2 * fIAo * fItft)
          fIdelta = (1 - 3 * (fIFv / fIFyc) ** 2) ** 0.5
          fOFnt = fIRh * fIFyt * fIdelta
          return fOFnt


# 

