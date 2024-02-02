import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040305_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.3.5 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '주면마찰력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.3 극한한계상태의 지지력
    3.4.3.5 암반에 설치한 현장타설말뚝의 지지력 산정
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
    A[암반에 설치한 현장타설말뚝의 지지력 산정];
    B["KDS 24 14 51 3.4.3.5 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarOut1[/출력변수:주면마찰력/]
			VarIn1[/입력변수:암의 일축압축강도/]
			VarIn2[/입력변수:대기압/]
			VarIn3[/입력변수:암반절리를 고려한 감소계수/]
			VarIn4[/입력변수:콘크리트 압축강도/]

			VarOut1
			VarIn1 ~~~ VarIn2
			VarIn3 ~~~ VarIn4

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C{"<img src='https://latex.codecogs.com/svg.image?0.65\alpha&space;_{E}p_{a}(\frac{q_{u}}{p_{a}})^{0.5}<7.8p_{a}(\frac{f_{c}^{\prime}}{P_{a}})^{0.5}'>---------------------------------"}
			D([주면 마찰력])

			Variable_def ---> C ---> D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def skin_friction(fIqs,fIqu,fIPa,fIredjoi,fIfc) -> float:
        """주면마찰력
        Args:
            fIqs (float): 주면마찰력
            fIqu (float): 암의 일축압축강도
            fIPa (float): 대기압
            fIredjoi (float): 암반절리를 고려한 감소계수
            fIfc (float): 콘크리트 압축강도

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.3.5 암반에 설치한 현장타설말뚝의 지지력 산정 (2)의 값

        """

        fIqs = 0.65*fIredjoi*fIPa*(fIqu/fIPa)**0.5
        if fIqs < 7.8*fIPa*(fIfc/fIPa)**0.5:
          return fIqs
        else:
          return "Fail"


# 

