import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142054_040401_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 54 4.4.1 (2)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-19'
    title = '전단력을 받는 앵커의 공칭강도'

    description = """
    콘크리트용 앵커 설계기준
    4. 설계
    4.4 전단하중에 대한 설계 조건
    4.4.1 전단력을 받는 앵커의 강재강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 전단력을 받는 앵커의 공칭강도];
    B["KDS 14 20 54 4.4.1 (2)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarIn1[/입력변수 : 전단력을 받는 앵커의 공칭강도/];
    VarIn2[/입력변수 : 전단에 대한 단일 앵커의 유효단면적/];
    VarIn3[/입력변수 : 앵커 강재의 설계기준인장강도/];
    VarIn4[/입력변수 : 앵커 강재의 설계기준항복강도/];
    VarIn1~~~VarIn3
    VarIn2~~~VarIn4
    end

    Python_Class ~~~ C(["KDS 14 20 54 4.4.1 (2)"])
		C --> Variable_def

    D{"부속물 구분"};
    E["선설치 헤드스터드"];
    F["선설치 헤드볼트와 갈고리볼트 그리고 슬리브가 전단 파괴면까지 연장되어 있지 않은 후설치 앵커"];
    G["슬리브가 전단 파괴면까지 연장되어 있는 후 설치 앵커의 경우"];
    H{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    I{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    J{"그라우트로 채워 높인 부위에 사용되는 앵커인 경우"};
    K{"<img src='https://latex.codecogs.com/svg.image?f_{uta}\leq&space;Min(1.9f_{ya},860MPa)'>---------------------------------------"};
    O{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;A_{se,V}f_{uta}'>-----------------------------"};
    P{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.8A_{se,V}f_{uta}'>---------------------------------"};
    Q{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.6A_{se,V}f_{uta}'>---------------------------------"};
    R{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.48A_{se,V}f_{uta}'>---------------------------------"};
    W{"실험결과가 있는 경우"};
    S["전단력을 받는 앵커의 공칭강도=실험결과에 기초하여 산정"];
    T{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.6A_{se,V}f_{uta}'>---------------------------------"};
    V{"<img src='https://latex.codecogs.com/svg.image?V_{sa}\leq&space;0.48A_{se,V}f_{uta}'>---------------------------------"};
    X(["Pass or Fail"]);
    Variable_def--->K--->D--->E--->H--Yes--->P--->X
    H--No--->O--->X
    D--->F--->I--Yes--->R--->X
    I--No--->Q--->X
    D--->G--->W--Yes--->S--->X
    W--No--->J--Yes--->T--->X
    J--No--->V--->X
    """

    @rule_method
    def Nominal_strength_of_anchor_subjected_to_shear_force(fIVsaA,fIVsaB,fIAseV,fIfuta,fIfya) -> RuleUnitResult:
        """전단력을 받는 앵커의 공칭강도

        Args:
            fIVsaA (float): 전단력을 받는 앵커의 공칭강도 (선설치 헤드스터드)
            fIVsaB (float): 전단력을 받는 앵커의 공칭강도 (선설치 헤드볼트와 갈고리볼트 그리고 슬리브가 전단 파괴면까지 연장되어 있지 않은 후설치앵커)
            fIAseV (float): 전단에 대한 단일 앵커의 유효단면적
            fIfuta (float): 앵커 강재의 설계기준인장강도
            fIfya (float): 앵커 강재의 설계기준항복강도

        Returns:
            sOVsa (string): 콘크리트용 앵커 설계기준  4.4.1 전단력을 받는 앵커의 강재강도 (2)의 판단 결과 1
            pass_fail (bool): 콘크리트용 앵커 설계기준  4.4.1 전단력을 받는 앵커의 강재강도 (2)의 판단 결과 2
        """

        assert isinstance(fIVsaA, float)
        assert isinstance(fIVsaB, float)
        assert isinstance(fIAseV, float)
        assert isinstance(fIfuta, float)
        assert isinstance(fIfya, float)


        if fIVsaA != 0 and fIVsaB == 0 :
          if fIVsaA <= fIAseV * fIfuta and fIfuta <= min(1.9 * fIfya, 860) :
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
        elif fIVsaA == 0 and fIVsaB != 0 :
          if fIVsaB <= 0.6 * fIAseV * fIfuta and fIfuta <= min(1.9 * fIfya, 860) :
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
                  "sOVsa": "슬리브가 전단 파괴면까지 연장되어 있는 후설치 앵커의 경우, 별도의 실험결과에 기초하여 산정",
              }
          )