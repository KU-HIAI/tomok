import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241211_040103_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 12 11 4.1.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계인상력'    # 건설기준명

    #
    description = """
    교량 설계하중조합(한계상태설계법)
    4. 설계
    4.1 하중의 종류와 하중조합
    4.1.3 받침인상과 포스트텐션힘을 위한 하중계수
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
    A[받침인상과 포스트텐션힘을 위한 하중계수];
    B["KDS24 12 11 4.1.3 (1)"];
    A ~~~ B
    end
	subgraph Variable_def
	VarIn1[/입력변수 : 설계인상력/];
	VarIn2[/입력변수 : 받침인상위치에 가장 가까운 지점에 발생하는 고정하중에 의한 반력/];
	VarIn3[/입력변수 : 활하중계수/];
	VarIn4[/입력변수 : 활하중에 의한 반력/];

	end
	Python_Class~~~Variable_def
	D{"발주자가 지정하지 않은 경우"};
	E{"받침인상작업시 교통통제가 이루어지지 않는 경우"};
	F["설계인상력 ≤ 받침인상위치에 가장 가까운 지점에 발생하는 고정하중에 의한 반력 x 1.3"];
	G["설계인상력 ≤ 받침인상위치에 가장 가까운 지점에 발생하는 고정하중에 의한 반력 x 1.3 + 활하중계수 x 활하중에 의한 반력"];
	Variable_def --> D --> E
	E --> F --Yes--->H(["Pass or Fail"])
	E -->G --No--->H(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_powerReaction_force_due_to_load(fIFdjack,fIRldead,fIcoefl,fIRllive,fIuserdefined) -> bool:
        """설계인상력

        Args:
            fIFdjack (float): 설계 인상력
            fIRldead (float): 고정하중에 의한 반력
            fIcoefl (float): 활하중계수
            fIRllive (float): 활하중에 의한 반력
            fIuserdefined (float): 사용자 선택

        Returns:
            bool: 교량 설계하중조합(한계상태설계법)  설계인상력이 건설기준 4.1.3(1)을 통과하는지 여부
        """

        if fIuserdefined==1: #받침인상작업 시 교통통제가 이루어지지 않은 경우
          if fIFdjack>=1.3*fIRldead+fIcoefl*fIRllive:
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined==2: #1의 경우가 아닌 경우
          if fIFdjack>=1.3*fIRldead:
            return "Pass"
          else:
            return "Fail"


# 

# 

