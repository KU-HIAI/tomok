import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_0405040203 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.2.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-15'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '아치형 파형강판 구조물의 설계압축력'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
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
		A[Title: 설계압축력] ;
		B["KDS 14 31 10 4.5.4.2.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 설계압축력/] ;
      VarIn1[/입력변수: 고정하중에 의한 압축력/] ;
      VarIn2[/입력변수: 활하중에 의한 압축력/] ;
      VarIn3[/입력변수: 지진하중에 의한 압축력/] ;
      VarIn4[/입력변수: 고정하중 하중계수/] ;
      VarIn5[/입력변수: 활하중 하중계수/] ;
      VarIn6[/입력변수: 지진하중 하중계수/] ;
      VarIn7[/입력변수: 충격계수/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{f}=\alpha&space;_{D}T_{D}&plus;max\left\{\alpha&space;_{L}T_{L}(1&plus;i),\alpha&space;_{E}T_{E}\right\}>---------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?T_{f}>------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_compression_force(fOTf,fITD,fITL,fITE,fIalphaD,fIalphaL,fIalphag,fIi) -> bool:
        """아치형 파형강판 구조물의 설계압축력
        Args:
            fOTf (float): 설계압축력
            fITD (float): 고정하중에 의한 압축력
            fITL (float): 활하중에 의한 압축력
            fITE (float): 지진하중에 의한 압축력
            fIalphaD (float): 고정하중 하중계수
            fIalphaL (float): 활하중 하중계수
            fIalphag (float): 지진하중 하중계수
            fIi (float): 충격계수


        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3 설계압축력의 값
        """


        fOTf = fIalphaD * fITD + max(fIalphaL * fITL* (1 + fIi), fIalphag * fITE)
        return fOTf


# 

