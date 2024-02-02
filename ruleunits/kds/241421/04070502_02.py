import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070502_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.5.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장타설 원형 중공 슬래브교의 치수'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.2 현장타설 속빈 슬래브교
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
    A["현장타설 속빈 슬래브교"];
    B["KDS 24 14 21 4.7.5.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:중공의 중심간 간격/];
		VarIn2[/입력변수:슬래브의 전체 높이/];
		VarIn3[/입력변수:콘크리트의 최소두께/];
		VarIn4[/입력변수:중공의 횡방향 폭/];
		VarIn5[/입력변수:중공 높이/];
		VarIn6[/입력변수:중공 사이의 복부 두께/];
		VarIn7[/입력변수:바닥판 전체 높이/];
		VarIn8[/입력변수:중공 위의 콘크리트 최소두께/];


		VarIn1 & VarIn2 & VarIn3 & VarIn4
		~~~VarIn5 & VarIn6 & VarIn7 & VarIn8
		end
		Python_Class ~~~ Variable_def
		Variable_def--->C--yes-->D & E
		C{속빈 부위가 원형 중공일 경우}
		D["중공의 중심간 간격≥슬래브의 전체 높이"]
		E["콘크리트의 최소두께≥140mm"]
		C--NO-->F & G & H

		F["중공의 횡방향 폭≤중공 높이X1.5"]

		G["중공 사이의 복부 두께≥바닥판 전체 높이X20%"]
		H["중공 위의 콘크리트 최소두께≥175mm"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Center_to_center_spacing_of_hollows(fIcensph, fIovehsl, fImithco, fItrwiho, fIholhei, fIabdthi, fIovhebp, fImicoth, fIuserdefined) ->bool:
        """현장타설 원형 중공 슬래브교의 치수
        Args:
             fIcensph (float): 중공의 중심간 간격
             fIovehsl (float): 슬래브의 전체 높이
             fImithco (float): 콘크리트의 최소두께
             fItrwiho (float): 중공의 횡방향 폭
             fIholhei (float): 중공 높이
             fIabdthi (float): 중공 사이의 복부 두께
             fIovhebp (float): 바닥판 전체 높이
             fImicoth (float): 중공 위의 콘크리트 최소두께
             fIuserdefined (float): 사용자 선택
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.5.2 (2) 설계기준에 따른 현장타설 원형 중공 슬래브교의 치수 적합여부
        """
        #속빈 부위가 원형 중공일 경우: fIuserdefined = 1
        #중공이 사각형일 경우: fIuserdefined = 2

        if fIuserdefined == 1:
          if fIcensph >= fIovehsl and fImithco >= 140:
            return "Pass"
          else:
            return "Fail"
        elif fIuserdefined == 2:
          if fItrwiho <= 1.5*fIholhei and fIabdthi >= fIovhebp/5 and fImicoth >= 175:
            return "Pass"
          else:
            return "Fail"
        else:
          return "Fail"


# 

