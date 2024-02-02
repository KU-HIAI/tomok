import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070203_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.2.3 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장타설 거더 교량의 상부 플랜지 두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.2 거더 교량
    4.7.2.3 현장타설 거더 교량
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
    A["현장타설 거더 교량"];
    B["KDS 24 14 21 4.7.2.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:콘크리트 거더의 구성 요소 두께/];
		VarIn2[/입력변수:상부 플랜지/];
		VarIn3[/입력변수:복부, 포스트텐션/];
		VarIn4[/입력변수:복부, 포스트텐션/];
		VarIn5[/입력변수:하부 플랜지/];

		VarIn1 & VarIn2 & VarIn3
	~~~~VarIn4 & VarIn5

		end

		Python_Class ~~~ Variable_def
		Variable_def--->D & E

		D["상부플랜지의 두께>정착과 피복두께에 필요한 두께"]
		E["인접 거더사이의 순간격X1/20≤ 상부플렌지의 두께"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Upper_Flange_Thickness(fIupflth, fIthreft, fIingadg) ->bool:
        """현장타설 거더 교량의 상부 플랜지 두께
        Args:
             fIupflth (float): 상부 플랜지 두께
             fIthreft (float): 정착과 피복두께에 필요한 두께
             fIingadg (float): 인접 거더 사이의 순간격
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.2.3 (1) 설계기준에 따른 현장타설 거더 교량의 상부 플랜지 두께 적합여부
        """
        if fIupflth > fIthreft and fIupflth >= fIingadg/20 :
          return "Pass"
        else:
          return "Fail"


# 

