import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_040206_03(RuleUnit): # KDS241712_040206_03

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.2.6 (3)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '거더의 이동변위'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계에 대한 규정
    4.2.6 설계변위
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
    A[거더의 이동변위];
    B["KDS 24 17 12 4.2.6 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 행정구역에 의해 결정한 값/];
		VarIn1[/입력변수: 설계지진 발생시 지반에 대한 거더의 총 변위/];
    VarIn2[/입력변수: 설계지진 발생 시 거더의 응답변위/];
		VarIn3[/입력변수: 설계지진 발생 시 하부구조의 변위/];
		VarIn4[/입력변수: 콘크리트의 건조숙축에 의한 거더의 이동량/];
    VarIn5[/입력변수: 콘크리트의 크리프에 의한 거더의 이동량/];
		VarIn6[/입력변수: 온도변화로 인한 거더의 이동량/];

		VarOut ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2~~~~  VarIn4 &  VarIn5 &  VarIn6
		end
		Python_Class ~~~ Variable_def;



		D{"<img src='https://latex.codecogs.com/svg.image?d=d_{i}+d_{sub}'>--------------------------------------------------------"};
		Variable_def --> D---->E["KDS 24 17 12 4 6"]--->	F["<img src='https://latex.codecogs.com/svg.image?Delta \l_{i}=d+Delta \l_{s}+Delta \l_{c}+Delta \l_{t}'>--------------------------------------------------------"];

		F--->G(["헹정구역에 의해 결정한 값"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def displacement_of_girder(fOdeltali,fId,fIdi,fIdsub,fIdeltats,fIdeltalc,fIdeltalt) -> float:
        """거더의 이동변위

        Args:
            fOdeltali (float): 행정구역에 의해 결정한 값
            fId (float): 설계지진 발생 시 지반에 대한 거더의 총 변위
            fIdi (float): 설계지진 발생 시 거더의 응답변위
            fIdsub (float): 설계지진 발생 시 하부 구조의 변위
            fIdeltats (float): 콘크리트의 건조수축에 의한 거더의 이동량
            fIdeltalc (float): 콘크리트의 크리프에 의한 거더의 이동량
            fIdeltalt (float): 온도변화로 인한 거더의 이동량
        Returns:
            float: 교량내진 설계기준(케이블교량) 4.2.6 (3) 행정구역에 의해 결정한 값
        """
        fId = fIdi + fIdsub
        fOdeltali = fId + fIdeltats + fIdeltalc + 0.4*fIdeltalt

        return(fOdeltali)


