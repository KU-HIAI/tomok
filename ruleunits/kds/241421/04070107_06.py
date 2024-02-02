import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04070107_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.7.1.7 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-21'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '단순 받침부의 공칭길이'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.1 프리캐스트 콘크리트 구조물의 일반사항
    4.7.1.7 프리캐스트 요소의 받침부 지압판
    (6)
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
    A["단순 받침부의 공칭길이"];
    B["KDS 24 14 21 4.7.1.7 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:지압응력을 고려한 순 지압판 길이/];
		VarIn2[/입력변수:받침점 반력/];
		VarIn3[/입력변수:받침부의 순 폭/];
		VarIn4[/입력변수:설계지압강도/];
		VarIn5[/입력변수:지지하는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리/];
		VarIn6[/입력변수:지지되는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리/];
		VarIn7[/입력변수: 지지하는 부재사이의 간격에 대한 오차의 허용값/];
		VarIn8[/입력변수:지지되는 부재의 길이에 대한 오차 허용값/];
		VarIn9[/입력변수:부재길이/];


		VarOut1[/출력변수:단순 받침부의 공칭길이/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		 VarIn2~~~~VarIn4 & VarIn5 & VarIn6
		VarIn5~~~~VarIn7 & VarIn8 & VarIn9
		end

		Python_Class ~~~ Variable_def
		Variable_def--->E & D

		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;a_1=F_u/(b_1f_d)'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;\Delta&space;a_3=l_n/2500'>---------------------------------"]
		D & E--->F--->G
		F["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;a=a_1&plus;a_2&plus;a_3&plus;\sqrt{\Delta&space;a_2^2&plus;\Delta&space;a_3^2}'>---------------------------------"]
		G(["단순 받침부의 공칭길이"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Nominal_Length_of_Simple_Support(fOa, fIa1, fIFu, fIb1, fIfd, fIa2, fIa3, fIdeltaa2, fIdeltaa3, fIln) ->float:
        """단순 받침부의 공칭길이
        Args:
             fOa (float): 단순 받침부의 공칭길이
             fIa1 (float): 지압응력을 고려한 순 지압판 길이
             fIFu (float): 받침점 반력
             fIb1 (float): 받침부의 순 폭
             fIfd (float): 설계지압강도
             fIa2 (float): 지지하는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리
             fIa3 (float): 지지되는 부재의 바깥쪽 끝에서 받침부 외측까지의 거리
             fIdeltaa2 (float): 지지하는 부재사이의 간격에 대한 오차의 허용값
             fIdeltaa3 (float): 지지되는 부재의 길이에 대한 오차 허용값
             fIln (float): 부재길이
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.7.1.7 (6) 설계기준에 따른 단순 받침부의 공칭길이 적합여부
        """
        fIa1 = fIFu/(fIb1*fIfd)

        fIdeltaa3 = fIln/2500

        fOa = fIa1+fIa2+fIa3+math.sqrt(math.pow(fIdeltaa2,2)+math.pow(fIdeltaa3,2))

        return fOa


# 

