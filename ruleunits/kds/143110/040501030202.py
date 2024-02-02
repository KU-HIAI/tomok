import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143110_040501030202 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 14 31 10 4.5.1.3.2.2' # 건설기준문서
    ref_date = '2017-12-20'  # 디지털 건설문서 작성일
    doc_date = '2023-12-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '비보강 웨브의 뒤틀림강성도'    # 건설기준명

    #
    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.1 기둥과 보의 가새
    4.5.1.3 보 안정용 가새
    4.5.1.3.2 비틀림좌굴 가새
    4.5.1.3.2.2 연속 비틀림좌굴 가새
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
		A[Title: 연속 비틀림좌굴 가새] ;
		B["KDS 14 31 10 4.5.1.3.2.2"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 비보강 웨브의 뒤틀림강성도/] ;
      VarIn1[/입력변수: 강재의 탄성계수/] ;
      VarIn2[/입력변수: 플랜지 도심간의 거리/] ;
      VarIn3[/입력변수: 보 웨브의 두께/] ;

			end
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3

		Python_Class ~~~ Variable_def

		E["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{sec}=\frac{3.3Et_{w}^{3}}{12h_{o}}>--------------------------------"]

		Variable_def --> E --> D(["<img src=https://latex.codecogs.com/svg.image?\beta&space;_{sec}>----------"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Torsional_stiffness_of_unreinforced_web(fObetasec,fIE,fIho,fItw) -> bool:
        """비보강 웨브의 뒤틀림강성도
        Args:
            fObetasec (float): 비보강 웨브의 뒤틀림강성도
            fIE (float): 강재의 탄성계수
            fIho (float): 플랜지 도심간의 거리
            fItw (float): 보 웨브의 두께




        Returns:
            bool: 강구조부재설계기준(하중저항계수설계법) 4.5.1.3.2.2 연속 비틀림좌굴 가새의 값
        """




        fObetasec = (3.3 * fIE * fItw ** 3) / (12 * fIho)
        return fObetasec


# 

