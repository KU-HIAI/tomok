import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241712_04040201_02(RuleUnit): # KDS241712_04040201_02

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jonghyeok Lee'  # 작성자명
    ref_code = 'KDS 24 17 12 4.4.2.1 (2)' # 건설기준문서
    ref_date = '2023-09-12'  # 디지털 건설문서 작성일  (고시일)
    doc_date = '2023-09-14'  # 건설기준문서->디지털 건설기준 변환 기준일 (작성 년월)
    title = '최대지반가속도'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    교량내진설계기준(한계상태설계법)
    4. 설계
    4.4 기초 및 교대의 내진설계
    4.4.2 기초
    4.4.2.1 조사
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
    A[최대지반가속도];
    B["KDS 24 17 12 4.4.2.1 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 최대지반가속도/];
    VarIn2[/입력변수: 유효수평지반가속도/];
		VarIn3[/입력변수: 단주기 지반증폭계수/];
		VarIn4[/입력변수: 부지고유의 지반응답해석결과/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4

		end
		Python_Class ~~~ Variable_def;



		D{"최대지반가속도"};
		Variable_def --> D--암반지반---->E["유효수평지반가속도"]
		D--토사지반---->F["최대지반가속도=유효수평지반가속도 X 단주기 지반증폭계수 or 부지고유의 지반응답해석결과"]
		F & E---->G(["최대지반가속도"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def maximum_ground_acceleration(fOmaxgra,fIS,fIFa,fIssgrar,fIuserdefined) -> float:
        """최대지반가속도

        Args:
            fOmaxgra (float): 최대지반가속도
            fIS (float): 유효수평지반가속도
            fIFs (float): 단주기 지반증폭 계수
            fIssgrar (float): 부지고유의 지반응답해석결과
            fIuserdefined (float): 사용자 선택

        Returns:
        float: 교량내진 설계기준(케이블교량) 4.4.2.1 (2) 최대지반가속도
        """

      #암반지반: fIuserdefined = 1
      #토사지반: fIuserdefined = 2
        if fIuserdefined == 1:
          fOmaxgra = fIS
        elif fIuserdefined == 2:
          if fIssgrar == None:
            fOmaxgra = fIS * fIFa
          else:
            fOmaxgra = max(fIS * fIFa, fIssgrar)
        return fOmaxgra


