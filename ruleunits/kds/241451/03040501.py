import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03040501 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 51 3.4.5.1' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-19'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '말뚝지름 및 상부기둥의 지름'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.4 현장타설말뚝
    3.4.5 현장타설말뚝의 구조세목
    3.4.5.1 일반사항
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
    A[인발];
    B["KDS 24 14 51 3.4.3.7 (2)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarOut1[/출력변수:감가된 인발저항력/]
			VarIn1[/입력변수:qs,bell/]
			VarIn2[/입력변수:Au/]
			VarIn3[/입력변수:인발 부착계수/]
			VarIn4[/입력변수:확대선단부의 지름/]
			VarIn5[/입력변수:지지층 근입깊이/]
			VarIn6[/입력변수:말뚝지름/]
			VarIn7[/입력변수:저면위로 확대선단부 지름의 2배거리 내 평균 비배수 전단강도/]
			VarIn8[/입력변수:강도감소계수/]

			VarOut1 ~~~
			VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4
			VarIn5 ~~~ VarIn6 ~~~ VarIn7 ~~~ VarIn8

      end
			Python_Class ~~~ Variable_def;
      Variable_def

			C["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{s}Q_{s,bell}'>---------------------------------"]
			D["<img src='https://latex.codecogs.com/svg.image?Q_{s,bell}=q_{s,bell}A_{u}'>---------------------------------"]
			E{Average of MIN,저면 바닥으로부터 상향으로 확대선단부의 지름, 지지층에 근입된 말뚝길이}
			H{Db/Dp = 0.75이경우 Nu = 0.0, Db/Dp = 2.5인경우 Nu = 8.0까지 선형적으로 변함}

			Variable_def -- 저면위로 확대선단부 지름의 2배거리 내 평균 비배수 전단강도 ---> E ---> C ---> I([감가된 인발저항력])
			Variable_def -- 인발부착계수 ---> H ---> D ---> C
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Pile_diameter_and_upper_column_diameter(fIdiasta,fIdiacol,fIdiapil) -> float:
        """말뚝지름 및 상부기둥의 지름
        Args:
            fIdiasta (float): 말뚝지름
            fIdiacol (float): 상부기둥의 지름
            fIdiapil (float): 현장타설말뚝의 지름

        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.1 일반사항의 부합 여부

        """

        if fIdiasta >= 750 and fIdiacol <= fIdiapil:
          return "Pass"
        else:
          return "Fail"


# 

