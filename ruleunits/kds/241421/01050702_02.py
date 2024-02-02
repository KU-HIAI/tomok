import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_01050702_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 1.5.7.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '프리스트레스  힘과 기타 하중에 의한 구조물 내의 콘크리트 압축응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    1. 일반사항
    1.5 구조해석
    1.5.7 프리스트레스트 구조물
    1.5.7.2 긴장할 때 프리스트레스 힘의 제한
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
    A[압축부재의 비지지길이];
    B["KDS 24 14 21 1.5.7.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;

		VarIn2[/입력변수: 콘크리트압축응력/];
    VarIn1[/입력변수: 프리스트레스 힘을 받게 되는 시간 t에서의 콘크리트의 설계기준압축강도/];



		end
		Python_Class ~~~ Variable_def;

		C{"실험이나 경험에 의해 입증될 수 있는 경우"}
		D["압축부재를 횡방향으로 지지할 수 있는 부재의 순간격 "]

		Variable_def --> C
		C --yes--> D
		C --No--> F
	 D["<img src='https://latex.codecogs.com/svg.image?f_{c}\leq&space;0.7f_{ck(t)}'>--------------------------------------------------------"];
     F ~~~~~|"KDS 24 14 21 1.4.2.3"|F
		F["<img src='https://latex.codecogs.com/svg.image?f_{c}\leq&space;0.6f_{ck(t)}'>--------------------------------------------------------"];
		G(["Pass or Fail"])
    F & D---->G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_Compressive_Stress(fIfc,fIfckt,fIuserdefined) -> bool:
        """프리스트레스  힘과 기타 하중에 의한 구조물 내의 콘크리트 압축응력

        Args:
            fIfc (float) : 콘크리트 압축응력
            fIfckt (float) : 프리스트레스 힘을 받게 되는 시간 t에서의 콘크리트의 설계기준압축강도
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 1.5.7.2 긴장할 때 프리스트레스 힘의 제한 (2)의 통과여부
        """
        #default: fIuserdefined = 1
        #프리텐션 부재의 경우, 실험이나 경험에 의해 입증될 수 있다면 프리스트레스 전달시의 응력: fIuserdefined = 2

        if fIuserdefined == 1:
          if fIfc <= 0.6*fIfckt:
            return "Pass"
          else:
            return "Fail"

        if fIuserdefined == 2:
          if fIfc <= 0.7*fIfckt:
            return "Pass"
          else:
            return "Fail"


# 

