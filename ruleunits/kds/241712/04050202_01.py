import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04050202_01(RuleUnit): # KDS241712_04050202_01

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.5.2.2 (1)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '축력을 고려한 교각의 항복강성'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.5 콘크리트교의 설계
    4.5.2 주탑 및 교각의 해석 및 설계강도
    4.5.2.2 주탑 및 교각의 휨강성
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
    A[축력을 고려한 교각의 항복강성];
    B["KDS 24 17 12 4.5.2.2 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut1[/출력변수: 축력을 고려한 교각의 항복강성/];
    VarIn1[/입력변수: 축력을 고려한 교각의 항복모멘트/];
		VarIn2[/입력변수: 축력을 고려한 교각의 항복곡률/];


		VarOut1~~~~ VarIn1 & VarIn2

		end
		Python_Class ~~~ Variable_def;


		D["<img src='https://latex.codecogs.com/svg.image?EI_{y}=\frac{M_{y}}{\phi&space;_{y}}'>--------------------------------------------------------"];



	Variable_def--->D---> E

		E(["축력을 고려한 교각의 항복강성"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def Flexural_Strength_of_Pylon_and_Piers(fOEIy,fIMy,fIphiy) -> float:
        """축력을 고려한 교각의 항복강성

        Args:
            fOEIy (float): 축력을 고려한 교각의 항복강성
            fIMy (float): 축력을 고려한 교각의 항복모멘트
            fIphiy (float): 축력을 고려한 교각의 항복곡률

        Returns:
            교량내진 설계기준(케이블교량) 4.5.2.2 (1) 주탑 및 교각의 휨강성
        """
        fOEIy = fIMy/fIphiy
        return(fOEIy)


