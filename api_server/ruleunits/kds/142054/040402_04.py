import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040402_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.2 (4)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '앵커 샤프트 중심부터 콘크리트 단부까지의거리'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 앵커 샤프트 중심부터 콘크리트단부까지의 거리 산정];
    B["KDS 14 20 54 4.4.2 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 앵커 샤프트 중심부터 콘크리트단부까지의 거리/];
    VarIn2[/입력변수 : 앵커가 정착되는 부재 두께/];
    VarIn3[/입력변수 : 전단력 직각방향으로 가장 큰 앵커사이 간격/];
    VarIn4[/입력변수 : 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트 단부까지 거리/];
    VarIn1~~~VarIn3
    VarIn2~~~VarIn4
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.2 (4)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?c_{a2}<1.5c_{a1},h_{a}<1.5c_{a1}'>를 모두 만족하는 경우"};
    E{"<img src='https://latex.codecogs.com/svg.image?c_{a1}\leq&space;Max(c_{a2}/1.5,h_{a}/1.5,s/3)'>------------------------------------"};
    F(["Pass or Fail"]);
    Variable_def--->D--->E--->F
    """

    @rule_method
    def Distance_from_anchor_shaft_center_to_concrete_end(fIha,fIcaone,fIcatwo,fIs) -> RuleUnitResult:
        """앵커 샤프트 중심부터 콘크리트단부까지의 거리

        Args:
            fIha (float): 앵커가 정착되는 부재 두께 (앵커축과 평행한 방향)
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트단부까지의 거리
            fIcatwo (float): 앵커 샤프트 중심부터 ca1과 직각방향에 있는 콘크리트단부까지 거리
            fIs (float): 앵커의 중심 간격

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (4)의 판단 결과
        """

        assert isinstance(fIha, float)
        assert isinstance(fIcaone, float)
        assert isinstance(fIcatwo, float)
        assert isinstance(fIs, float)

        if fIcaone <= max(fIcatwo / 1.5 , fIha / 1.5 , fIs / 3) :
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
            )
        else:
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )