import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040504020503 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.4.5.3' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '파형강판 지중구조물 설계압축력'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.5 휨모멘트와 압축력에 의한 소성힌지
    4.5.4.2.5.3 완공 후 검토
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
		A[Title: 완공 후 검토] ;
		B["KDS 14 31 10 4.5.4.2.5.3"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarIn1[/입력변수: 설계압축력/] ;
      VarIn2[/입력변수: 파형강판의 소성압축강도/] ;
      VarIn3[/입력변수: 완공 후 소성힌지 저항계수/] ;
      VarIn4[/입력변수: 파형강판의 단면적/] ;
      VarIn5[/입력변수: 파형강판의 항복강도/] ;
      VarIn6[/입력변수: 완공 후 작용하는 휨모멘트/] ;
      VarIn7[/입력변수: 상부 아치 정점부까지 고정하중에 의한 휨모멘트/] ;
      VarIn8[/입력변수: 상부 아치 정점부위의 고정하중에 의한 휨모멘트/] ;
      VarIn9[/입력변수: 완공 후 활하중에 의한 휨모멘트/] ;
      VarIn10[/입력변수: 토피고 H와 Dh/2 중 작은 값/] ;
      VarIn11[/입력변수: 지간 및 토피고에 따른 하중감소계수/] ;
      VarIn12[/입력변수: 차량축하중/] ;
      VarIn13[/입력변수: 등가선하중 환산계수/] ;
      VarIn14[/입력변수: 파형강판의 소성모멘트 강도/] ;
      VarIn15[/입력변수: 파형강판의 소성단면계수/] ;
		end

		VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12
		VarIn11 ~~~ VarIn13 & VarIn14 & VarIn15


		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?\left(\frac{T_{f}}{P_{pf}}\right)^{2}&plus;\left|\frac{M}{M_{pf}}\right|\leq&space;1>------------------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?M_{f}=\alpha&space;_{D}\left|M_{1}&plus;M_{D}\right|&plus;\alpha&space;_{L}M_{L}(1&plus;i)=K_{m1}R_{B}\gamma&space;D_{h}^{3}-K_{m2}R_{B}\gamma&space;D_{h}^{2}H_{e}&plus;K_{m3}R_{U}D_{h}A_{L}/k_{4}>-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?P_{pf}=\phi&space;_{h}AF_{y}>------------------------------------------"]
		S["<img src=https://latex.codecogs.com/svg.image?M_{pf}=\phi&space;_{h}ZF_{y}>------------------------------------------"]
		Z["<img src=https://latex.codecogs.com/svg.image?H_{e}=Min(H,D_{h}/2)>------------------------------------------------"]

		Variable_def --> R --> Z --> W --> S --> Q --> X(["PASS or Fail"])


    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def design_compression_force(fITf,fIPpf,fIphih,fIA,fIFy,fIMf,fIM1,fIMD,fIML,fIHe,fIKm1,fIKm2,fIKm3,fIRB,fIRU,fIAL,fIk4,fIMpf,fIZ) -> bool:
        """파형강판 지중구조물 설계압축력
        Args:
            fITf (float): 설계압축력
            fIPpf (float): 파형강판의 소성압축강도
            fIphih (float): 완공 후 소성힌지저항계수
            fIA (float): 파형강판의 단면적
            fIFy (float): 파형강판의 항복강도
            fIMf (float): 완공 후 작용하는 휨모멘트
            fIM1 (float): 상부 아치 정점부까지 고정하중에 의한 휨모멘트
            fIMD (float): 상부 아치 정점부 위의 고정하중에 의한 휨모멘트
            fIML (float): 완공 후 활하중에 의한 휨모멘트
            fIHe (float): 토피고 H와 Dh/2 중 작은 값
            fIKm1 (float): 시공 중 검토식 참조
            fIKm2 (float): 시공 중 검토식 참조
            fIKm3 (float): 시공 중 검토식 참조
            fIRB (float): 시공 중 검토식 참조
            fIRU (float): 지간 및 토피고에 따른 하중감소계수
            fIAL (float): 차량축하중
            fIk4 (float): 등가선하중 환산계수
            fIMpf (float): 파형강판의 소성모멘트강도
            fIZ (float): 파형강판의 소성단면계수

        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.5.3 완공 후 검토의 통과여부
        """

        if (fITf / fIPpf) ** 2 + abs(fIMf / fIMpf) <= 1:
          return "Pass"
        else:
          return "Fail"


# 

