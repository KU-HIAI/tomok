import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010203_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.3 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '공칭복부폭'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.3 전단보강철근이 배치된 부재
    (6)
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
    A["공칭복부폭"];
    B["KDS 24 14 21 4.1.2.3 (6)"];
    A ~~~ B
    end
    subgraph Variable_def;
    VarOut1[/출력변수: 공칭복부폭/];
    VarIn1[/입력변수: 프리스트레싱 덕트의 지름/];
    VarIn2[/입력변수: 단면의 복부폭/];
    VarIn3[/입력변수: 덕트의 외측 지름/];
    VarIn4[/입력변수: 가장 불리한 위치에서의 덕트의 외측 지름/];
    VarIn5[/입력변수: 콘크리트의 재료저항계수/];
    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4 & VarIn5
    end
    Python_Class ~~~ Variable_def;
    Variable_def--->H--yes-->I
    I--yes-->L
    I--No-->J
    L & J--->K
    H["프리스트레싱 덕트의 지름 <img src='https://latex.codecogs.com/svg.image?\dpi{10}\leq\;\frac{b_{w}}{8}'>---------------"]
    I{"그라우트 된 덕트"}
    L["<img src='https://latex.codecogs.com/svg.image?b_{w,nom}=b_w-0.5\sum\phi&space;'>---------------------------------"]
    J["<img src='https://latex.codecogs.com/svg.image?b_{w,nom}=b_w-1.2\sum\phi&space;'>---------------------------------"]
    K(["공칭복부폭"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_Abdomen_Width(fIdiprdu,fObwnom,fIbw,fIphi,fIsumphi,fIuserdefined) -> float:
        """공칭복부폭

        Args:
             fIdiprdu (float): 프리스트레싱 덕트의 지름
             fObwnom (float): 공칭복부폭
             fIbw (float): 단면의 복부폭
             fIphi (float): 덕트의 외측 지름
             fIsumphi (float): 가장 불리한 위치에서의 덕트의 외측 지름 합계
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.3 전단보강철근이 배치된 부재 (6)의 값
        """

        if fIdiprdu >= fIbw / 8:
          if fIuserdefined == 1:
            fObwnom = fIbw - 0.5 * fIsumphi
          elif fIuserdefined == 2:
            fObwnom = fIbw - 1.2 * fIsumphi
        return fObwnom


# 

