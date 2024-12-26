import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142024_040301_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 24 4.3.1 (1)'
    ref_date = '2021-02-18'
    doc_date = '2024-02-07'
    title = '타이의 공칭강도'

    description = """
    콘크리트구조 스트럿-타이모델 기준
    4. 설계
    4.3 타이의 인장강도
    4.3.1 강도 산정
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 타이의 공칭강도];
    B["KDS 14 20 24 4.3.1 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def
    VarOut[/출력변수 : 타이의 공칭강도/];
    VarIn1[/입력변수 : 계수축력에 의한 긴장재의 응력 증가분/];
    VarIn2[/입력변수 : 긴장재의 유효 프리스트레스 응력/];
    VarIn3[/입력변수 : 긴장재 타이의 단면적/];
    VarIn4[/입력변수 : 철근의 설계기준항복강도/];
    VarIn5[/입력변수 : 철근타이의 단면력/];
    VarIn6[/입력변수 : 긴장재의 설계기준항복강도/];
    VarOut~~~VarIn3
    VarIn1~~~VarIn4
    VarIn2~~~VarIn5
    end

	  Python_Class ~~~ C(["KDS 14 20 24 4.3.1 (1)"])
		C --> Variable_def

    D{"긴장재가 부착된 경우"};
    E["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}=420MPa'>----------------------"];
    F{"해석에 의해 증명된 경우"};
    G["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}=70MPa'>----------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?\Delta&space;f_{p}'>해석으로 증명된 값 사용"];
    I["<img src='https://latex.codecogs.com/svg.image?f_{pe}&plus;\Delta&space;f_{p}<f_{py}'>----------------------"];
    J["<img src='https://latex.codecogs.com/svg.image?F_{nt}=A_{st}f_{y}&plus;A_{ps}(f_{pe}&plus;\Delta&space;f_{p})'>---------------------------------"];
    K(["타이의 공칭강도"]);
    Variable_def--->D--Yes--->E--->I--->J--->K
    D--No --->F--Yes--->H--->I
    F--No --->G--->I
    """

    @rule_method
    def nominal_strength_of_tie(fIfpe,fIdelfp,fIfy,fIfpy,fIAst,fIAps) -> RuleUnitResult:
        """타이의 공칭강도

        Args:
            fIfpe (float): 긴장재의 유효프리스트레스 응력
            fIdelfp (float): 계수축력에 의한 긴장재의 응력 증가분
            fIfy (float): 철근의 설계기준항복강도
            fIfpy (float): 긴장재의 설계기준항복강도
            fIAst (float): 철근타이의 단면적
            fIAps (float): 긴장재타이의 단면력

        Returns:
            fOFnt (float): 콘크리트구조 스트럿-타이모델 기준  4.3.1 강도 산정 (1)의 값
        """

        assert isinstance(fIfpe, float)
        assert isinstance(fIdelfp, float)
        assert isinstance(fIfy, float)
        assert isinstance(fIfpy, float)
        assert isinstance(fIAst, float)
        assert isinstance(fIAps, float)

        fOFnt = fIAst * fIfy + fIAps * (min(fIfpe + fIdelfp , fIfpy))

        return RuleUnitResult(
              result_variables = {
                  "fOFnt": fOFnt,
              }
          )