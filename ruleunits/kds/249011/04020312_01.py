import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04020312_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.2.3.12 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-09-27'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '직사각형 받침'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
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
    A[회전 안정성];
    B["KDS 24 90 11 4.2.3.12 (1)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 직사각형 받침/];
		VarIn2[/입력변수: 원형 받침/];
		VarIn3[/입력변수: 총 수직변형/];
		VarIn4[/입력변수: 받침의 유효직경/];
		VarIn5[/입력변수: 탄성받침의 너비 a를 가로지르는 회전각/];
		VarIn6[/입력변수: 탄성받침의 길이 b를 가로지르는 회전각/];
		VarIn7[/입력변수: a 방향 유효길이/];
		VarIn8[/입력변수: b 방향 유효길이/];
    VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 & VarIn2 & VarIn3 & VarIn4~~~VarIn6 & VarIn7 & VarIn8 & VarIn5

    end

    Python_Class ~~~ Variable_def;
		Variable_def--->G
		G{받침의 종류}
		G--직사각형 받침--->K
		G--원형 받침--->L
		K["<img src='https://latex.codecogs.com/svg.image?\sum\nu_{z,d}-\frac{(a^{'}\cdot\alpha&space;_{a,d}&plus;b^{'}\cdot\alpha&space;_{b,d})}{3}\geq0>--------------------------------------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image?\sum\nu_{z,d}-\frac{(D^{'}\cdot\alpha&space;_{d})}{3}\geq0&space;
    K & L--->I

    I(["Pass or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Square_Bearings(fItvedef, fIsqubea, fIcirbea, fIeffdia, fIalphaad, fIalphabd, fIa, fIb,fIuserdefined) -> bool:
        """직사각형 받침

        Args:
            fItvedef (float): 총 수직변형
            fIsqubea (float): 직사각형 받침
            fIcirbea (float): 원형 받침
            fIeffdia (float): 받침의 유효직경
            fIalphaad (float): 탄성받침의 너비 a를 가로지르는 회전각
            fIalphabd (float): 탄성받침의 길이 b를 가로지르는 회전각
            fIa (float): a 방향 유효길이
            fIb (float): b 방향 유효길이
            fIuserdefined (float): 사용자 선택


        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.2.3.12 안전성 (1)의 통과 여부
        """
        #직사각형 받침 > fIuserdefined == 1
        #원형 받침 > fIuserdefined == 2

        if fIuserdefined == 1:
          if fItvedef-(fIalphaad*fIa+fIalphabd*fIb)/3 >= 0 :
            return 'Pass'
          else:
            return 'Fail'
        elif fIuserdefined == 2:
          if fItvedef-fIeffdia*fIalphaad/3 >= 0 :
            return 'Pass'
          else:
            return 'Fail'


# 

