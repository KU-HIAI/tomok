import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04050201_02(RuleUnit): # KDS241712_04050201_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.5.2.1 (2)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '철근콘크리트 주탑 및 교각의 축방향철근'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.1 일반사항
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
    A[일반사항];
    B["KDS 24 17 12 4.5.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 철근콘크리트 주탑 및 교각의 축방향철근/];
    VarIn2[/입력변수: 철근콘크리트 교각의 횡방향철근/];
		VarIn3[/입력변수: 인장강도/];
		VarIn4[/입력변수: 항복강도/];
		VarIn5[/입력변수: 설계기준항복강도/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5

		end
		Python_Class ~~~ Variable_def;


	Variable_def--->D---> E & F
		D["철근콘크리트 주탑 및 교각의 축방향 철근"];
		E["설계기준항복 강도≤500MPa"];
		F["인장강도≥항복강도 X 1.25"]
		G["철근콘크리트 교각의 횡방향철근"];
		H["설계기준항복 강도≤500MPa"];
		Variable_def--->G--->H
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def steel_for_reinforced_concrete_pylons_and_piers(fItstaxrb,fIystaxrb,fItsthorb) -> bool:
        """철근콘크리트 주탑 및 교각의 축방향철근

        Args:
            fItstaxrb (float): 축방향철근의 설계기준항복강도
            fIystaxrb (float): 축방향철근의 인장강도
            fItsthorb (float): 횡방향철근의 설계기준항복강도

        Returns:
            bool: 교량내진 설계기준(케이블교량) 4.5.2.1 일반사항 (2)의 통과여부
        """
        if fItstaxrb <= 500 and fIystaxrb >= 1.25 * fItstaxrb and fItsthorb <= 500:
          return "Pass"
        else:
          return "Fail"


