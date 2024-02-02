import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040303011101_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.3.3.1.11.1 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-11'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '보강재 돌출폭'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.3 교량용 거더
    4.3.3.1 플레이트거더
    4.3.3.1.11 보강재
    4.3.3.1.11.1 중간수직보강재
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
		A[Title: 중간수직보강재] ;
		B["KDS 14 31 10 4.3.3.1.11.1 (2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarIn1[/입력변수: 돌출폭/] ;
    VarIn2[/입력변수: 웨브의 전체높이/] ;
    VarIn3[/입력변수: 가장 넓은 압축플랜지의 전폭/] ;
    VarIn4[/입력변수: 수직보강재의 두께/] ;
		end

		VarIn1 & VarIn2 ~~~ VarIn3 & VarIn4
		Python_Class ~~~ Variable_def

		C["<img src=https://latex.codecogs.com/svg.image?b_{t}\geq&space;50&plus;\frac{D}{30}>---------------------"]
		D["<img src=https://latex.codecogs.com/svg.image?16t_{p}\geq&space;b_{t}\geq\frac{b_{f}}{4}>------------------------"]

		Variable_def --> C --> D --> E(["PASS or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def entrapment_width(fIbt,fID,fIbf,fItp) -> bool:
        """보강재 돌출폭
        Args:
            fIbt (float): 돌출폭
            fID (float): 웨브의 전체높이
            fIbf (float): 가장 넓은 압축플랜지의 전폭
            fItp (float): 수직보강재의 두께

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.3.3.1.11.1 중간수직보강재 (2)의 통과여부
        """

        if fIbt >= 50 + fID / 30 and 16 * fItp >= fIbt >= fIbf / 4:
            return "Pass"
        else:
            return "Fail"


# 

