import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405020201 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.2.2.1' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '휨고 전단의 조합에서 설계하중에 의한 휨모멘트'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.2 핀
    4.5.2.2 강도
    4.5.2.2.1 휨과 전단의 조합
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
		A[Title: 휨과 전단의 조합] ;
		B["KDS 14 31 10 4.5.2.2.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 설계하중에 의한 휨모멘트/] ;
      VarIn2[/입력변수: 핀의 직경/] ;
      VarIn3[/입력변수: 핀의 항복강도/] ;
      VarIn4[/입력변수: 휨에 대한 강도저항계수/] ;
      VarIn5[/입력변수: 설계하중에 의한 전단력/] ;
      VarIn6[/입력변수: 전단에 대한 강도저항계수/] ;

			end
		VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6

		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\frac{6.0M_{u}}{\phi&space;_{f}D^{3}F_{y}}&plus;\left(\frac{2.2V_{u}}{\phi&space;_{v}D^{2}F_{y}}\right)^{3}\leq&space;0.95>------------------------------------------"]

		Variable_def --> E --> D(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Bending_moment_due_to_design_load(fIMu,fID,fIFy,fIphif,fIVu,fIphiv) -> bool:
        """휨고 전단의 조합에서 설계하중에 의한 휨모멘트
        Args:
            fIMu (float): 설계하중에 의한 휨모멘트
            fID (float): 핀의 직경
            fIFy (float): 핀의 항복강도
            fIphif (float): 휨에 대한 강도저항계수
            fIVu (float): 설계하중에 의한 전단력
            fIphiv (float): 전단에 대한 강도저항계수


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.2.2.1 휨과 전단의 조합의 통과여부
        """

        if (6.0 * fIMu) / (fIphif * fID ** 3 * fIFy) + ((2.2 * fIVu) / (fIphiv * fID ** 2 * fIFy)) ** 3 <= 0.95:
          return "Pass"
        else:
          return "Fail"


# 

