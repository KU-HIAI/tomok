import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_04010202_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 14 31 10 4.1.2.2 (2)' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '순단면적'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.1 인장부재
    4.1.2 단면적의 산정
    4.1.2.2 순단면적
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
		A[순단면적] ;
		B["KDS 14 31 10 4.1.2.2(2)"] ;
		A ~~~ B
		end

		subgraph Variable_def
    VarOut1[/출력변수: 순단면적/]
    VarIn1[/입력변수: 부재의 총단면적/]
    VarIn2[/입력변수: 인장력에 의한 파단선상에 있는 구멍의 수/]
    VarIn3[/입력변수: 연결재 구멍의 직경/]
    VarIn4[/입력변수: 연결재 게이지선 사이의 응력 수직 방향 중심간격/]
    VarIn5[/입력변수: 응접한 2개 구멍의 응력 방향 중심간/]
		end

		Python_Class ~~~ Variable_def
  	C["불규칙배치(엇모배치)인 경우"] ;
    D(["<img src='https://latex.codecogs.com/svg.image?&space;A_{n}=A_{g}-ndt&plus;\Sigma\frac{s^{2}}{4g}t&space;'>------------------------------------------------------"])
    Variable_def --> C -->D
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def net_area(fOAn,fIAg,fIn,fId,fIt,fIsumstg) -> float:
        """순단면적

        Args:
            fOAn (float): 순단면적
            fIAg (float): 부재의 총단면적
            fIn (float): 인장력에 의한 파단선상에 있는 구멍의 수
            fId (float): 연결재 구멍의 직경
            fIt (float): 연결재 게이지선 사이의 응력 수직방향 중심간격
            fIsumstg (float): 식 4.1-2의 시그마 값


        Returns:
            float: 강구조부재설계기준(하중저항계수설계법)  4.1.2.2 순단면적 (2)의 값
        """

        fOAn = fIAg - fIn*fId*fIt + fIsumstg
        return fOAn


# 

