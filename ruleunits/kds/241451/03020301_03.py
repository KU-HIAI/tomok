import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03020301_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 14 51 3.2.3.1 (3)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-18'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '??'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.1 지지력
    (3)
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
    A[사질토 공칭 지지력];
    B["KDS 24 14 51 3.2.3.1 (3)"];
    A ~~~ B
    end

      subgraph Variable_def;
      VarOut1[/출력변수: 공칭지지/];
			VarIn1[/입력변수: 보정된 SPT타격수의 평균값/];
			VarIn2[/입력변수: 기초폭/];
			VarIn3[/입력변수: 지하수 영향 보정계수1/];
			VarIn4[/입력변수: 지하수 영향 보정계수2/];
			VarIn5[/입력변수: 기초의 근입깊이/];
			VarIn6[/입력변수: 하중경사 보정계수/];
			VarIn7[/입력변수: 실제 수평하중/];
			VarIn8[/입력변수: 실제 수직하중/];
			VarIn9[/입력변수: 기초저면에서 깊이 B까지의 평균 콘관입 저항력/];
			VarIn10[/입력변수: 기초저면 위치의 총연직압력/];
			VarIn11[/입력변수: 경험적 지지력계수/];
			VarIn12[/입력변수: 한계압력의 평균값/];
			VarIn13[/입력변수: 기초저면 위치의 총수평압력/];

			VarOut1
			VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4
			VarIn5 ~~~ VarIn6 ~~~ VarIn7 ~~~ VarIn8
			VarIn9 ~~~ VarIn10 ~~~ VarIn11 ~~~ VarIn12 ~~~ VarIn13

      end
      Python_Class ~~~ Variable_def;
      Variable_def

			C[표준관입시험]
			D[콘관입시험]
			E[공내재하시험]

			Variable_def ---> C
			Variable_def ---> D
			Variable_def ---> E

			F{"<img src='	https://latex.codecogs.com/svg.image?q_{ult}=3.2\times&space;10^{-5}\overline{N_{coor}}B(C_{w1}&plus;C_{w2}\frac{D_{f}}{B})R_{i}'>---------------------------------"}
			G{"<img src='	https://latex.codecogs.com/svg.image?q_{ult}=8.2\times&space;10^{-5}q_{c}B(C_{w1}&plus;C_{w2}\frac{D_{f}}{B})R_{i}'>---------------------------------"}
			H{"<img src='	https://latex.codecogs.com/svg.image?q_{ult}=[r_{o}&plus;k(p_{L}-p_{o})]R_{i}'>---------------------------------"}

			C ---> F
			D ---> G
			E ---> H

			F & G & H ---> I[사질토 공칭 지지력]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_Support (fOQult,fIAvgspt,fIB,fICwfist,fICwscnd,fIDf,fIRi,fIH,fIV,fIQc,fIRo,fIK,fIPl,fIPo) -> bool:
        """??
        Args:
            fOQult (float): 공칭지지력
            fIAvgspt (float): 보정된 SPT타격수의 평균값
            fIB (float): 기초폭
            fICwfist (float): 지하수 영향 보정계수
            fICwscnd (float): 지하수 영향 보정계수
            fIDf (float): 기초의 근입깊이
            fIRi (float): 하중경사 보정계수
            fIH (float): 실제 수평하중
            fIV (float): 실제 수직하중
            fIQc (float): 기초저면에서 깊이 B까지의 평균 콘관입 저항력
            fIRo (float): 기초저면 위치의 총연직압력
            fIK (float): 경험적 지지력계수
            fIPl (float): 한계압력의 평균값
            fIPo (float): 기초저면 위치의 총수평압력

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.1 지지력 (3)의 값
        """

        fOQult = 3.2*0.00001*fIAvgspt*fIB*(fICwfist+fICwscnd*fIDf/fIB)*fIRi
        return fOQult

        fOQult = 8.2*0.00001*fIQc*fIB*(fICwfist+fICwscnd*fIDf/fIB)*fIRi
        return fOQult

        fOQult = (fIRo+fIK*(fIPl-fIPo))*fIRi
        return fOQult


# 

