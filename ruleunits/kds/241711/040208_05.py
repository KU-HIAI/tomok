import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241711_040208_05(RuleUnit): # KDS241711_040208_05

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 11 4.2.8 (5)' # 건설기준문서
    ref_date = '2022-02-25'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-22'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '교량의 여유간격'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.2 해석 및 설계
    4.2.8 설계변위
    (5)
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
		A[설계변위];
		B["KDS 24 17 11 4.2.8 (5)"];
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 교량의 여유간격/];
		VarIn2[/입력변수: 가동받침의 이동량/];
		VarIn3[/입력변수: 지반에 대한 상부구조의 총 변위/];
		VarIn4[/입력변수: 콘크리트의 건조수축에 의한 이동량/];
		VarIn5[/입력변수: 콘크리트의 크리프에 의한 이동량/];
		VarIn6[/입력변수: 온도변화로 인한 이동량/];
		VarIn1 ~~~ VarIn4
		VarIn2 ~~~ VarIn5
		VarIn3 ~~~ VarIn6
		end

		Python_Class ~~~ Variable_def

		C["<img src='https://latex.codecogs.com/png.image?\dpi{2000}\Delta&space;l_{i}\geq&space;d&plus;\Delta&space;l_{s}&plus;\Delta&space;l_{c}&plus;0.4\Delta&space;l_{t}'>----------------------------------------------------"];

		D["<img src='https://latex.codecogs.com/png.image?\dpi{1000}\Delta&space;l_{i}>'>가동받침의 이동량"];

		E([PASS or Fail]);

		Variable_def --> C -- and --> D --> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def bridge_clearance(fIdeltali,fImoamos,fId,fIdeltals,fIdeltalc,fIdeltalt) -> bool:
        """교량의 여유간격

        Args:
            fIdeltali (float): 교량의 여유간격
            fImoamos (float): 가동받침의 이동량
            fId (float): 지반에 대한 상부구조의 총 변위
            fIdeltals (float): 콘크리트의 건조수축에 의한 이동량
            fIdeltalc (float): 콘크리트의 크리프에 의한 이동량
            fIdeltalt (float): 온도변화로 인한 이동량

        Returns:
            bool: 교량내진설계기준(한계상태설계법) 4.2.8 설계변위 (5) 교량의 여유간격 ②의 통과 여부
        """
        if fIdeltali >= fId + fIdeltals + fIdeltalc + 0.4*fIdeltalt and fIdeltali > fImoamos:
          return 'Pass'
        else:
          return 'Fail'