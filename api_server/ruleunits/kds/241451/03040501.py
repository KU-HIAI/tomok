import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03040501(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.4.5.1'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '말뚝지름 및 상부기둥의 지름'

    description = """
    3. 설계
    3.4 현장타설말뚝
    3.4.5 현장타설말뚝의 구조세목
    3.4.5.1 일반사항
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝지름 및 상부기둥의 지름];
    B["KDS 24 14 51 3.4.5.1"];
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

		Python_Class ~~~ C(["KDS 24 14 51 3.4.5.1"])
		C --> Variable_def

		F["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{s}Q_{s,bell}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?Q_{s,bell}=q_{s,bell}A_{u}'>---------------------------------"]
		E{Average of MIN,저면 바닥으로부터 상향으로 확대선단부의 지름, 지지층에 근입된 말뚝길이}
		H{Db/Dp = 0.75이경우 Nu = 0.0, Db/Dp = 2.5인경우 Nu = 8.0까지 선형적으로 변함}

		Variable_def -- 저면위로 확대선단부 지름의 2배거리 내 평균 비배수 전단강도 ---> E ---> F ---> I([감가된 인발저항력])
		Variable_def -- 인발부착계수 ---> H ---> D ---> F
    """

    @rule_method
    def Pile_diameter_and_upper_column_diameter(fIdiasta,fIdiacol,fIdiapil) -> RuleUnitResult:
        """말뚝지름 및 상부기둥의 지름

        Args:
            fIdiasta (float): 말뚝지름
            fIdiacol (float): 상부기둥의 지름
            fIdiapil (float): 현장타설말뚝의 지름

        Returns:
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.4.5.1 일반사항의 판단 결과
        """

        assert isinstance(fIdiasta, float)
        assert isinstance(fIdiacol, float)
        assert isinstance(fIdiapil, float)

        if fIdiasta >= 750 and fIdiacol <= fIdiapil:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
                  }
              )
        else :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
                  }
              )