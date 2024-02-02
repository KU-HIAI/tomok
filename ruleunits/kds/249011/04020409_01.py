import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020409_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.4.9 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-12'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '피스톤과 포트 접촉부 검토'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.4 포트받침
    4.2.4.9 피스톤과 포트 접촉부 검토
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
    A[피스톤과 포트 접촉부 검토];
    B["KDS 24 90 11 4.2.4.9 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 피스톤의 폭/];
		VarIn2[/입력변수: 접촉면의 반경/];
		VarIn3[/입력변수: 직경/];


    VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def;
		Variable_def--->K--평면--->L--->N
		K--곡면--->M--->N
		K{"접촉면의 상태"}
		L["W<15mm"];
		M["접촉면의 반경 <img src='https://latex.codecogs.com/svg.image?\leq Max(0.5D, 100mm)'>---------------"]
    N(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Width_Of_Piston(fIw, fID, fIr,fIuserdefiend) -> bool:
        """피스톤과 포트 접촉부 검토

        Args:
            fIw (float): 피스톤의 폭
            fID (float): 직경
            fIr (float): 접촉면의 반경
            fIuserdefiend (float): 사용자 선택


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.4.9 피스톤과 포트 접촉부 검토 (1)의 통과여부
        """

        #접촉면이 평면인 경우 > fIuserdefiend == 1
        #접촉면이 곡면인 경우 > fIuserdefiend == 2

        if fIuserdefiend == 1:
          if fIw < 15 :
            return "Pass"
          else :
            return "Fail"

        if fIuserdefiend == 2:
          if fIr >= max(0.5*fID, 100):
            return 'Pass'
          else:
            return 'Fail'


# 

