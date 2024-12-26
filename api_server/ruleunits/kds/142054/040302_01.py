import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040302_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.3.2 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '단일 앵커 또는 앵커 그룹 공칭콘크리트 브레이크아웃강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.3 인장하중에 대한 설계 조건
    4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 인장력을 받는 단일 앵커 또는 앵커 그룹의 공칭콘크리트 브레이크아웃강도];
    B["KDS 14 20 54 4.3.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 단일앵커의 공칭콘크리트 브레이크아웃강도/];
    VarIn2[/입력변수 : 앵커그룹의 공칭콘크리트 브레이크아웃강도/];
    VarIn3[/입력변수 : 앵커가 편심하중을 받는 경우의 인장강도에대한 수정계수/];
    VarIn4[/입력변수 : 연단거리 영향에 따른 인장강도에대한 수정계수/];
    VarIn5[/입력변수 : 균열 유무에 따른 인장강도에대한 수정계수/];
    VarIn6[/입력변수 : 설치 시 쪼갬인장응력을 고려하여, 후설치앵커를 보조철근없이 비균열 콘크리트에 사용하기위한 인장강도에대한 수정계수/];
    VarIn7[/입력변수 : 앵커의 유효묻힘깊이/];
    VarIn8[/입력변수 : 단일 앵커 또는 앵커 그룹 브레이크아웃 파괴면의 투영면적/];
    VarIn9[/입력변수 : 단일 앵커에 대한 콘크리트 브레이크아웃 파괴면의 투영면적/];
    VarIn10[/입력변수 : 그룹에서 인장을 받는 앵커의 수/];
    VarIn1~~~VarIn5~~~VarIn9
    VarIn2~~~VarIn6~~~VarIn8
    VarIn3~~~VarIn6
    VarIn4~~~VarIn7~~~VarIn10
    end
    Python_Class ~~~ C(["KDS 14 20 54 4.3.2 (1)"])
		C --> Variable_def

    D["<img src='https://latex.codecogs.com/svg.image?A_{Nco}=9h_{ef}^{2}'>---------------"];
    E{"<img src='https://latex.codecogs.com/svg.image?A_{Nc}\leq&space;nA_{Nco}'>----------------"};
    F{"앵커 구분"};
    G{"<img src='https://latex.codecogs.com/svg.image?N_{cb}\leq\frac{A_{Nc}}{A_{Nco}}\psi&space;_{ed,N}\psi&space;_{c,N}\psi&space;_{cp,N}N_{b}'>--------------------------------------------"};
    H{"<img src='https://latex.codecogs.com/svg.image?N_{cbg}\leq\frac{A_{Nc}}{A_{Nco}}\psi&space;_{ec,N}\psi&space;_{ed,N}\psi&space;_{c,N}\psi&space;_{cp,N}N_{b}'>--------------------------------------------"};
    I(["Pass or Fail"]);
    Variable_def--->D--->E--->F--단일 앵커--->G--->I
    F--앵커 그룹--->H--->I
    """

    @rule_method
    def Nominal_concrete_breakout_strength_of_single_anchor_or_anchor_group(fINcb,fINcbg,fIpsiecN,fIpsiedN,fIpsicN,fIpsicpN,fIhef,fIANc,fINb,fIn) -> RuleUnitResult:
        """단일 앵커 또는 앵커 그룹 공칭콘크리트 브레이크아웃강도

        Args:
            fOANco (float): 단일 앵커에 대한 콘크리트 브레이크아웃 파괴면의 투영면적
            fINcb (float): 단일 앵커의 공칭콘크리트 브레이크아웃강도
            fINcbg (float): 앵커 그룹의 공칭콘크리트 브레이크아웃강도
            fIpsiecN (float): 앵커가 편심하중을 받는 경우의 인장강도에 대한 수정계수
            fIpsiedN (float): 연단거리 영향에 따른 인장강도에 대한 수정계수
            fIpsicN (float): 균열 유무에 따른 인장강도에 대한 수정계수
            fIpsicpN (float): 설치 시 쪼갬인장응력을 고려하여, 후설치앵커를 보조철근 없이 비균열 콘크리트에 사용하기 위한 인장강도에 대한 수정계수
            fIhef (float): 앵커의 유효묻힘깊이
            fIANc (float): 단일 앵커 또는 앵커 그룹 브레이크아웃 파괴면의 투영면적
            fINb (float): 균열 콘크리트에서 인장을 받는 단일앵커의 기본 콘크리트 브레이크아웃강도
            fIn (float): 그룹에서 인장을 받는 앵커의 수

        Returns:
            fOANco (float): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (1)의 값
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.3.2 인장력을 받는 앵커의 콘크리트 브레이크아웃강도 (1)의 판단 결과
        """

        assert isinstance(fINcb, float)
        assert isinstance(fINcbg, float)
        assert isinstance(fIpsiecN, float)
        assert 0 < fIpsiecN <= 1.0
        assert isinstance(fIpsiedN, float)
        assert isinstance(fIpsicN, float)
        assert isinstance(fIpsicpN, float)
        assert isinstance(fIhef, float)
        assert isinstance(fIANc, float)
        assert isinstance(fINb, float)
        assert isinstance(fIn, float)

        fOANco = 9 * (fIhef**2)

        if fIANc <= fIn * fOANco :
          if fINcb != 0 and fINcbg == 0 :
            if fINcb <= (fIANc / fOANco) * fIpsiedN * fIpsicN * fIpsicpN * fINb :
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
          if fINcb == 0 and fINcbg != 0 :
            if fINcbg <= (fIANc / fOANco) * fIpsiecN * fIpsiedN * fIpsicN * fIpsicpN * fINb :
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