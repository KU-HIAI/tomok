import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040302010110_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.2.1.1.10 (1)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단일 ㄱ형강 항복강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.1 단일부재
    4.3.2.1.1 휨강도
    4.3.2.1.1.10 단일ㄱ형강
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
	  A[단일ㄱ형강]
	  B["KDS 14 31 10 4.3.2.1.1.10(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수:항복강도/]
	  VarIn1[/입력변수: 압축플랜지 항복강도/]
	  VarIn2[/입력변수: 휨축에 대한 항복모멘트/]
	  VarOut ~~~ VarIn1 & VarIn2
	  end
	  Python_Class ~~~ Variable_def --> D --> E
	  D["<img src='https://latex.codecogs.com/svg.image?&space;M_n=1.5M_y'>--------------------------"]
	  E(["<img src='https://latex.codecogs.com/svg.image?&space;M_n'>--------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def yield_strength(fOMn,fIMy) -> bool:
        """단일 ㄱ형강 항복강도
        Args:
            fOMn (float): 압축플랜지 항복강도
            fIMy (float): 휨축에 대한 항복모멘트

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.2.1.1.10 단일ㄱ형강 (1)의 값
        """


        fOMn = 1.5 * fIMy
        return fOMn


# 

