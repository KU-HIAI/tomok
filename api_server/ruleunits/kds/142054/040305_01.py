import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040305_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.5 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '단일 부착식 앵커의 공칭부착강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.5 인장력을 받는 부착식 앵커의 부착강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 단일 부착식 앵커의 공칭부착강도];
    B["KDS 14 20 54 4.3.5 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/출력변수 : 단일 부착식 앵커의 공칭부착강도/];
    VarIn2[/출력변수 : 부착식 앵커 그룹의 공칭부착강도/];
    VarIn3[/입력변수 : 앵커그룹의 투영영향면적/];
    VarIn4[/입력변수 : 단일 앵커의 투영영향면적/];
    VarIn5[/입력변수 : 부착식 앵커에서 연단거리 영향에 따른 인장강도에대한수정계수/];
    VarIn6[/입력변수 :비균열 콘크리트에 사용되는 부착식앵커의수정계수/];
    VarIn7[/입력변수 :인장을 받는 단일부착식 앵커의 기본부착강도/];
    VarIn8[/입력변수 : 부착식 앵커가 편심하중을 받는 경우의 인장강도에대한수정계수/];
    VarIn9[/입력변수 : 부착식 앵커의 수/];
    VarIn10[/입력변수 : 최대 부착강도를 발현하기 위해 필요한 앵커중심부터 투영영향면적 가장자리까지의 거리/];
    VarIn1~~~ VarIn5~~~VarIn8
    VarIn2 ~~~ VarIn6~~~VarIn9
    VarIn3 ~~~ VarIn7~~~VarIn10
    VarIn4~~~VarIn5

    end

    Python_Class ~~~ C(["KDS 14 20 54 4.3.5 (1)"])
		C --> Variable_def

    D{"<img src='https://latex.codecogs.com/svg.image?A_{Na}\leq&space;nA_{Nao}'>----------------------------"};
    E["<img src='https://latex.codecogs.com/svg.image?A_{Nao}=(2\times&space;10d_{a}(\frac{\tau&space;_{uncr}}{7.6})^{0.5})^{2}'>-------------------------------------------------"];
		F{"단일 부착식 앵커"};
    G{"부착식 앵커 그룹"};
    H{"<img src='https://latex.codecogs.com/svg.image?N_{a} \leq \frac{A_{Na}}{A_{Nao}}\psi_{ed,Na}\psi_{cp,Na}N_{ba}'>---------------------------------------------------"};
    I{"<img src='https://latex.codecogs.com/svg.image?N_{ag} \leq \frac{A_{Na}}{A_{Nao}}\psi_{ec,Na}\psi&space;_{ed,Na}\psi_{cp,Na}N_{ba}'>--------------------------------------------------------------"};
    J(["Pass or Fail"]);

    Variable_def--->D--->E--->F & G
    F--->H--->J
		G--->I--->J
    """

    @rule_method
    def nominal_bond_strength_of_a_single_bonded_anchor(fINa,fINag,fIANa,fIpsedNa,fIpscpNa,fINba,fIpsecNa,fIn,fIda,fItauncr) -> RuleUnitResult:
        """단일 부착식 앵커의 공칭부착강도

        Args:
            fINa (float): 단일 부착식 앵커의 공칭부착강도
            fINag (float): 부착식 앵커 그룹의 공칭부착강도
            fIANa (float): 앵커그룹의 투영영향면적
            fIpsedNa (float): 부착식 앵커에서 연단거리 영향에 따른 인장강도에 대한 수정계수
            fIpscpNa (float): 비균열 콘크리트에 사용되는 부착식앵커의 수정계수
            fINba (float): 인장을 받는 단일부착식 앵커의 기본부착강도
            fIpsecNa (float): 부착식 앵커가 편심하중을 받는 경우의 인장강도에 대한 수정계수
            fIn (float): 부착식 앵커의 수
            fIda (float): 앵커의 외경, 혹은 헤드스터드, 헤드볼트, 갈고리형 볼트의 샤프트 지름
            fItauncr (float): 비균열 콘크리트에 사용된 부착식 앵커의 특성 부착강도

        Returns:
            fOcNa (float): 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (1)의 값 1
            fOANao (float): 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (1)의 값 2
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.5 인장력을 받는 부착식 앵커의 부착강도 (1)의 판단 결과
        """

        assert isinstance(fINa, float)
        assert isinstance(fINag, float)
        assert isinstance(fIANa, float)
        assert isinstance(fIpsedNa, float)
        assert isinstance(fIpscpNa, float)
        assert isinstance(fINba, float)
        assert isinstance(fIpsecNa, float)
        assert 0 < fIpsecNa <= 1.0
        assert isinstance(fIn, float)
        assert isinstance(fIda, float)
        assert isinstance(fItauncr, float)
        assert 0 < fItauncr

        fOcNa = 10 * fIda * ((fItauncr / 7.6)**0.5)
        fOANao = (2 * fOcNa)**2

        if fIANa <= fIn * fOANao :
          if fINa != 0 and fINag == 0 :
            if fINa <= (fIANa / fOANao) * fIpsedNa * fIpscpNa * fINba :
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
          if fINa == 0 and fINag != 0 :
            if fINag <= (fIANa / fOANao) * fIpsecNa * fIpsedNa * fIpscpNa * fINba :
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

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )