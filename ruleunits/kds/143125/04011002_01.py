import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS143125_04011002_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Hyunjong Shin'  # 작성자명
    ref_code = 'KDS 14 31 25 4.1.10.2' # 건설기준문서
    ref_date = '2017-12-20'  # 고시일
    doc_date = '2023-11-17'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '웨브 국부공칭강도'    # 건설기준명

    #
    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.10 집중하중을 받는 플랜지와 웨브
    4.1.10.2 웨브 국부항복강도
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
	A([웨브 국부공칭강도])
	B["KDS 14 31 25 4.1.10.2"]
	A ~~~ B
	end

	subgraph Variable_def
  VarOut[/출력변수: 웨브 국부공칭강도/]
	VarIn1[/입력변수: 압축 집중하중의 작용점에서 재단까지의 거리/]
	VarIn2[/입력변수: 부재깊이/]
	VarIn3[/입력변수: 플랜지의 바깥쪽면으로부터 웨브 필릿선단까지의 거리/]
	VarIn4[/입력변수: 집중하중이 작용하는폭/]
	VarIn5[/입력변수: 웨브의 항복응력/]
	VarIn6[/입력변수: 웨브두께/]

	VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	VarIn1 & VarIn2 & VarIn3 ~~~ VarIn4 & VarIn5 & VarIn6
	end

	Python_Class ~~~ Variable_def --> C --> D --Pass--> E --> F


	C["인장 또는 압축 집중하중의 작용점에서 재단까지의 거리 > 부재깊이 d"]
	D["Pass or Fail"]
	E["<img src='https://latex.codecogs.com/svg.image?R_n=(5k&plus;N)F_{yw}t_w'>------------------------------"]
	F(["<img src='https://latex.codecogs.com/svg.image?R_n'>"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def web_local_nominal_strength(fORn,fIdfaccl,fId,fIk,fIN,fIFyw,fItw) -> bool:
        """웨브 국부공칭강도
        Args:
            fORn (float): 웨브 국부공칭강도
            fIdfaccl (float): 압축 집중하중의 작용점에서 재단까지의 거리
            fId (float): 부재깊이
            fIk (float): 플랜지의 바깥쪽 면으로부터 웨브 필릿선단까지의 거리
            fIN (float): 집중하중이 작용하는폭
            fIFyw (float): 웨브의 항복응력
            fItw (float): 웨브두께

        Returns:
            bool: 강구조 연결 설계기준(하중저항계수설계법)  4.1.10.2 인장 또는 압축 집중하중의 작용점에서 재단까지의 거리가 부재깊이를 초과할 경우의 웨브 국부공칭강도 (1)의 값
        """
        fORn = ((5*fIk)+fIN)*fIFyw*fItw

        if fIdfaccl > fId :
          return fORn


# 
