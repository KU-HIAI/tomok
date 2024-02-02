import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241710_0202_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 17 10 2.2 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-16'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계지진력'    # 건설기준명

    #
    description = """
    교량 내진설계기준(일반설계법)
    2. 설계
    2.2 해석 및 설계
    (4) 직교 지진력의 조합
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
    A[해석 및 설계];
    B["KDS 24 17 10 2.2 (4)"];
    A ~~~ B
    end



      subgraph Variable_def;
			VarOut1[/출력변수:설계지진력/]
			VarIn1[/입력변수:종방향축의 탄성 지진력/]
			VarIn2[/입력변수:횡방향축의 탄성 지진력/]


			VarOut1 ~~~
			VarIn1 & VarIn2

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C[종방향축의 탄성지진력 + 횡방향 축의 탄성 지진력 X 30%]
			D[횡방향축의 탄성지진력 + 종방향축의 해석으로부터 구한 탄성지진력 X 30%]
			E([설계지진력])

			Variable_def ---> C & D ---> E
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_seismic_force(fOdeforc,fIElalng,fIElatrn,fIuserdefined) -> float:
        """설계지진력

        Args:
             fOdeforc (float): 설계지진력
             fIElalng (float): 종방향축의 탄성지지력
             fIElatrn (float): 횡방향축의 탄성 지지력
             fIuserdefined (float): 사용자 선택



        Returns:
            float: 교량 내진설계기준(일반설계법) 2.2 해석 및 설계 (4)의 값
        """

        # 하중경우 1: fIuserdefined = 1
        # 하중경우 2: fIuserdefined = 2
        if fIuserdefined == 1:
          fOdeforc = fIElalng + 0.3 * fIElatrn
        elif fIuserdefined == 2:
          fOdeforc = fIElatrn + 0.3 * fIElalng
        return fOdeforc


# 

