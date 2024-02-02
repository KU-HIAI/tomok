import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010103_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.1.3 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '축력과 2축 휨이 작용하는 부재의 휨강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도
    (3)
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
    A["축력과 2축 휨이 작용하는 부재의 휨강도"];
    B["KDS 24 14 21 4.1.1.3 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트/];
		VarIn2[/입력변수: 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트/];
    VarIn3[/입력변수: y축에 대한 설계휨강도/] ;
		VarIn4[/입력변수: z축에 대한 설계휨강도/] ;
		VarIn5[/입력변수: 단면 형상과 축력비에 따른 지수/];
		VarIn6[/입력변수: 계수하중에 의한 축력/];
		VarIn7[/입력변수: 단면의 설계중심축압축강도/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn2 & VarIn3 & VarIn4~~~VarIn5 & VarIn6 & VarIn7
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->D
		D{"단면 형상과 축력비에 따른 지수"}
		D--직사각형 단면인 경우-->

		C{"<img src='https://latex.codecogs.com/svg.image?N_{u}/N_{od}'>---------------------------------"}

		C--0.7-->E[α=1.5]
		C--1.0-->F[α=2.0]
		C--0.1보다 작거나 같을때-->G[α=1.0]
		D--원형단면과 타원형 단면인 경우--> H[α=2.0]
		E & F & G & H--->I--->K
		I{"<img src='https://latex.codecogs.com/svg.image?(\frac{M_{uy}}{M_{dy}})^{\alpha}&plus;(\frac{M_{uz}}{M_{dz}})^{\alpha}\leq&space;1.0'>---------------------------------"}
		K(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def bending_strength_of_member_subject_to_axial_force_and_biaxial_bending(fIMuy,fIMuz,fIMdy,fIMdz,fIalpha,fINu,fINod,fIuserdefined) -> bool:
        """축력과 2축 휨이 작용하는 부재의 휨강도

        Args:
             fIMuy (float): 2차 모멘트를 포함하는 y축에 대한 계수휨모멘트
             fIMuz (float): 2차 모멘트를 포함하는 z축에 대한 계수휨모멘트
             fIMdy (float): y축에 대한 설계휨강도
             fIMdz (float): z축에 대한 설계휨강도
             fIalpha (float): 단면 형상과 축력비에 따른 지수
             fINu (float): 계수하중에 의한 축력
             fINod (float): 단면의 설계중심축압축강도
             fIuserdefined (float): 사용자 선택


        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.1.1.3 축력과 2축 휨이 작용하는 부재의 휨강도 (3)의 통과 여부
        """

        #원형 단면과 타원형 단면의 경우: fIuserdefined = 1
        #직사각형 단면의 경우: fIuserdefined = 2
        if fIuserdefined == 1:
          fIalpha = 2.0
        elif fIuserdefined == 2:
          fIvariable = fINu / fINod
          if fIvariable <= 0.1:
            fIalpha = 1.0
          elif fIvariable > 0.1 and fIvariable < 0.7:
            fIalpha = (0.5 / 0.6) * (fIvariable - 0.7) + 1.5
          elif fIvariable == 0.7:
            fIalpha = 1.5
          elif fIvariable > 0.7 and fIvariable < 1.0:
            fIalpha = (0.5 / 0.3) * (fIvariable - 0.7) + 1.5
          elif fIvariable == 1.0:
            fIalpha = 2.0
        if (fIMuy/fIMdy)**fIalpha + (fIMuz/fIMdz)**fIalpha <= 1.0:
          return "Pass"
        else:
          return "Fail"


# 

# 

