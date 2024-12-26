import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040402_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.2 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '기본 콘크리트 브레이크아웃 강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력을 받는 앵커의 기본 콘크리트 브레이크아웃강도];
    B["KDS 14 20 54 4.4.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarIn1[/입력변수 : 기본 콘크리트 브레이크아웃 강도/];
    VarIn2[/입력변수 : 전단력에 대해 앵커가 지압을 받는 길이/];
    VarIn3[/입력변수 : 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형 볼트의 샤프트 지름/];
    VarIn4[/입력변수 : 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수/];
    VarIn5[/입력변수 : 콘크리트의 설계기준압축강도/];
    VarIn6[/입력변수 : 앵커 샤프트 중심부터 콘크리트 단부까지의 거리/];
    VarIn7[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    VarIn3~~~VarIn6
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.2 (2)"])
		C --> Variable_def

    D{"앵커 구분"};
    E["헤드스터드 및 전체 묻힘깊이에 걸쳐 단일 관을 가지는 후설치앵커인 경우"];
    F["간격 슬리브가 확장슬리브와 분리된 비틀림제어 확장앵커인 경우"];
    G["<img src='https://latex.codecogs.com/svg.image?l_{e}=h_{ef}(\leq&space;8d_{a})'>----------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?l_{e}=2d_{a}'>"];
    I{"<img src='https://latex.codecogs.com/svg.image?V_{b}\leq&space;Min\left(\left(0.6\left(\frac{l_{e}}{d_{a}}\right)^ {0.2}\sqrt{d_{a}}\right)\lambda_{a}\sqrt{f_{ck}}(c_{a1})^{1.5},3.7\lambda_{a}\sqrt{f_{ck }}(c_{a1})^{1.5}\right)'>---------------------------------------------------------------------------------"};
    J(["Pass or Fail"]);
    Variable_def--->D--->E--->G--->I--->J
    D--->F--->H--->I
    """

    @rule_method
    def Basic_Concrete_Breakout_Strength(fIVb,fIle,fIda,fIlamda,fIfck,fIcaone,fIhef) -> RuleUnitResult:
        """기본 콘크리트 브레이크아웃 강도

        Args:
            fIVb (float): 기본 콘크리트 브레이크아웃 강도
            fIle (float): 전단력에 대해 앵커가 지압을 받는 길이
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형볼트의 샤프트지름
            fIlamda (float): 앵커 강도 설계에서 경량콘크리트의 저감된 물성을 고려한 수정계수
            fIfck (float): 콘크리트의 설계기준압축강도
            fIcaone (float): 앵커 샤프트 중심부터 콘크리트 단부까지의거리
            fIhef (float): 앵커의 유효묻힘깊이

        Returns:
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.4.2 전단력을 받는 앵커의 콘크리트 브레이크아웃강도 (2)의 판단 결과
        """

        assert isinstance(fIVb, float)
        assert isinstance(fIle, float)
        assert fIle > 0
        assert isinstance(fIda, float)
        assert fIda > 0
        assert isinstance(fIlamda, float)
        assert isinstance(fIfck, float)
        assert fIfck > 0
        assert isinstance(fIcaone, float)
        assert fIcaone > 0
        assert isinstance(fIhef, float)

        if fIhef != 0 :
          if fIVb <= min((0.6 * ((fIle / fIda)**0.2) * (fIda**0.5)) * fIlamda * (fIfck**0.5) * (fIcaone**1.5), 3.7 * fIlamda * (fIfck**0.5) * (fIcaone**1.5)) and fIle <= 8 * fIda :
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

        if fIhef == 0 :
          if fIVb <= min((0.6 * ((fIle / fIda)**0.2) * (fIda**0.5)) * fIlamda * (fIfck**0.5) * (fIcaone**1.5), 3.7 * fIlamda * (fIfck**0.5) * (fIcaone**1.5)) and fIle <= 8 * fIda :
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