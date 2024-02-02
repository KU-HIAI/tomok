import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405020202 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.2.2.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '핀의 지압강도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.2 강도
    4.5.2.2.2 지압
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
		A[Title: 지압] ;
		B["KDS 14 31 10 4.5.2.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
			VarOut1[/출력변수: 핀의 지압강도/] ;
      VarIn1[/입력변수: 판의 두께/] ;
      VarIn2[/입력변수: 핀의 직경/] ;
      VarIn3[/입력변수: 지압에 댓한 강도저항계수/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{n}=1.5tDF_{y}>------------------------------------------"]
		F["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{r}=\phi&space;_{b}(R_{pB})_{n}>------------------------------------------"]

		Variable_def --> E --> F --> D(["<img src=https://latex.codecogs.com/svg.image?(R_{pB})_{r}>-----------------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Pin_bearing_strength(fORpBr,fIRpBn,fIt,fID,fIphib,fIFy) -> bool:
        """핀의 지압강도
        Args:
            fORpBr (float): 핀의 지압강도
            fIRpBn (float): 핀의 공칭지압강도
            fIt (float): 판의 두께
            fID (float): 핀의 직경
            fIphib (float): 지압에 대한 강도저항계수
            fIFy (float): 핀의 항복강도

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.2.2.2 지압의 값
        """

        fIRpBn = 1.5 * fID * fIFy
        fORpBr = fIphib * fIRpBn
        return fORpBr


# 

