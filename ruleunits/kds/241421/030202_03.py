import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_030202_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 21 3.2.2 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '철근의 기준항복강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.2 재료특성
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
    A["철근의 기준항복강도, 인장강도"];
    B["KDS 24 14 21 3.2.2. (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 항복하중의 기준값/];
		VarIn2[/입력변수: 직접 1축 인장의 최대하중/];
    VarIn3[/입력변수: 공칭단면적/] ;
    VarIn4[/입력변수: 실제 시험을 통하여 얻어지는 항복응력/] ;
		VarOut1[/출력변수: 철근의 기준항복강도/];
		VarOut2[/출력변수: 인장강도/];
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C & D
		C--->E
		C["철근의 기준항복강도=항복하중의 기준값/공칭단면적"]
		D["인장강도=직접 1축 인장의 최대하중/공칭단면적"]
		E["실제 시험을 통하여 얻어지는 항복응력≤기준항복강도x1.3"]
		F(["철근의 기준항복강도"])
		G(["인장강도"])
		E--->F
		D--->G

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Standard_Yield_Strength_Of_Rebar(fOfy,fOfu,fIstavay,fImaxlot,fInomcsn,fIyisota,fIuserdefined) -> float:
        """철근의 기준항복강도

        Args:
             fOfy (float): 철근의 기준항복강도
             fOfu (float): 인장강도
             fIstavay (float): 항복하중의 기준값
             fImaxlot (float): 직접 1축 인장의 최대하중
             fInomcsn (float): 공칭단면적
             fIyisota (float): 실제 시험을 통하여 얻어지는 항복 응력
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.2.2 재료특성 (3)의 값과 통과 여부
        """

        # 철근의 기준항복강도 계산시: fIuserdefined = 1
        # 철근의 인장강도 계산시: fIuserdefined = 2
        if fIuserdefined == 1:
          fOfy = fIstavay/fInomcsn
          if fIyisota <= 1.3 * fOfy:
            return fOfy, "Pass"
          else:
            return fOfy, "Fail"
        elif fIuserdefined == 2:
          fOfu = fImaxlot/fInomcsn
          return fOfu


# 

