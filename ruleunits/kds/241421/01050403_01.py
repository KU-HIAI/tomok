import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050403_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.4.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '소성힌지영역에서 계산된 회전각'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.4 소성해석
    1.5.4.3 회전 능력
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
    A[소성회전 조건];
    B["KDS 24 14 21 1.5.4.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 단면의 압축 연단에서 중립축까지 깊이/];
    VarIn2[/입력변수: 단면의 유효깊이/] ;
    VarIn3[/입력변수: 28일 콘크리트 공시체의 기준압축강도/] ;
		VarIn4[/입력변수: 회전각/] ;
		VarIn5[/입력변수: 허용 소성회전각/] ;



		VarIn1~~~VarIn4
   	VarIn2~~~VarIn4
		VarIn3~~~VarIn4


   	VarIn2~~~VarIn5
		VarIn3~~~VarIn5

		end
		Python_Class ~~~ Variable_def;
		Variable_def---->C
		Variable_def---->F
		C--->D
		C["<img src='https://latex.codecogs.com/svg.image?c/d\leq&space;0.3(f_{ck}\leq40MPa)\:\:\:or\;\:c/d\leq&space;0.23(f_{ck}>40MPa)'>--------------------------------------------------------"];
		D([Pass or Fail]) ;
		F["<img src='https://latex.codecogs.com/svg.image?\Theta_{s}\leq\Theta_{PI,d}'>--------------------------------------------------------"];
		E([Pass or Fail]) ;
		F---->E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Rotation_Angle(fId,fIfck,fIc) -> bool:
        """소성힌지영역에서 계산된 회전각

        Args:
            fIdepfrc (float) : 단면의 압축 연단에서 중립축까지 깊이
            fId (float) : 단면의 유효깊이
            fIfck (float) : 28일 콘크리트 공시체의 기준압축강도
            fIc (float) : 단면의 압축 연단에서 중립축까지 깊이



        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 1.5.4.3 회전 능력 (1)의 값
        """

        if fIfck <= 40 :
            if fIc/fId <= 0.30 :
                return "Pass"
            else:
                return "Fail"
        else:
            if fIc/fId <= 0.23 :
                return "Pass"
            else:
                return "Fail"

        if fOThetas <= fIThetapld :
          return "Pass"
        else:
          return "Fail"


# 

