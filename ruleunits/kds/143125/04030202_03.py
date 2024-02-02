import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04030202_03 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.3.2.2 (3)' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '간격 K형 접합에서 주강관이 압축인 경우 주강관 응력상관계수'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.3 강관구조접합
    4.3.2 강관 간의 트러스접합
    4.3.2.2 각형강관
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
		A[Title: 각형강관] ;
		B["KDS 14 31 25 4.3.2.2 (3)"] ;
		A ~~~ B
		end

		subgraph Variable_def
		VarOut1[/출력변수: 주강관 응력상관계수/] ;
		VarIn1[/입력변수: 유요성 비/] ;
		VarIn2[/입력변수: 유효폭 비/] ;
	  VarIn3[/입력변수: 주강관의 소요압축강도/]
		VarIn4[/입력변수: 주강관의 소요휨강도/]
		VarIn5[/입력변수: 주강관의 총단면적/]
		VarIn6[/입력변수: 설계응력/]
		VarIn7[/입력변수: 주강관의 탄성단면계수/]
		VarIn8[/입력변수: 주강관의 항복강도/]
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		VarIn5 ~~~ VarIn7 & VarIn8
		end

		Python_Class ~~~ Variable_def

		C(["<img src='https://latex.codecogs.com/svg.image?Q_{f}=1.3-0.4U/\beta_{eff}\leq&space;1'>----------------------------------------------------------"]) ;
    D[K형 접합에서 주장관이 압축인 경우]
	  E["<img src='https://latex.codecogs.com/svg.image?U=\left|P_{u}/A_{g}F_{c}&plus;M_{u}/SF_{c}\right|'>----------------------------------------------------------"] ;
		Variable_def --> D --> E -->C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Cast_steel_pipe_stress_correlation_coefficient(fOQf,fIU,fIbetaeff,fIPu,fIMu,fIAg,fIFc,fIS,fIFy) -> bool:
        """간격 K형 접합에서 주강관이 압축인 경우 주강관 응력상관계수
        Args:
            fOQf (float): 주강관 응력상관계수
            fIU (float): 유요성비
            fIbetaeff (float): 유효폭 비
            fIPu (float): 주강관의 소요압축강도
            fIMu (float): 주강관의 소요휨강도
            fIAg (float): 주강관의 총단면적
            fIFc (float): 설계응력
            fIS (float): 주강관의 탄성단면계수
            fIFy (float): 주강관의 항복강도

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법) 4.3.2.2 각형강관 (3)의 통과여부
        """

        fIU = abs(fIPu / (fIAg * fIFc) + fIMu / (fIS * fIFc))
        fOQf = min(1.3 - 0.4 * fIU / fIbetaeff, 1)
        return fOQf


# 

