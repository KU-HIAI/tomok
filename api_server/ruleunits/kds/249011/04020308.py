import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020308(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.8'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '압축하중에 의한 설계변형률'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.8 압축하중에 의한 설계변형률
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 압축하중에 의한 설계변형률];
    B["KDS 24 90 11 4.2.3.8"];
    A ~~~ B
    end

      Variable_def


		subgraph Variable_def;
		VarIn1[/입력변수: 수직설계하중/];
		VarIn2[/입력변수: 내부강판과 접촉하는 받침의 유효 면적/];
		VarIn3[/입력변수: 설계하중에 의한 받침의 a 방향으로의 최대 수평 상대변위/];
	  VarIn4[/입력변수: 설계하중에 의한 받침의 b 방향으로의 최대 수평 상대변위/];
    VarIn5[/입력변수: 형상계수/];
    VarIn6[/입력변수: 전단탄성계수/];
	  VarIn7[/입력변수: a 방향 유효길이/];
	  VarIn8[/입력변수: b 방향 유효길이/];

		VarOut1[/출력변수: 압축하중에 의한 설계변형률/];
    VarOut2[/출력변수: 압축하중에 의한 유효 평면적/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6

		end
         Python_Class ~~~ B1(["KDS 24 90 11 4.2.3.8"]) --> Variable_def;
          Variable_def-->F-->H--->I

    F["<img src='https://latex.codecogs.com/svg.image?\;A_{r}=A_{1}(1-\frac{v_{x,d}}{a^{\prime}}-\frac{v_{y,d}}{b^{\prime}}))'>--------------------------------------------------------"];
    H["<img src='https://latex.codecogs.com/svg.image?\epsilon&space;_{c,d}=\frac{1.5\cdot&space;F_{z,d}}{G\cdot&space;A_{r}\cdot&space;S}'>--------------------------------------------------------"];
    I(["압축하중에 의한 설계변형률"])

    """

    @rule_method
    def Design_Strain_Due_To_Compressive_Load(fIFzd, fIvxd, fIvyd, fIA1, fIS, fIG, fIa, fIb) -> RuleUnitResult:
        """압축하중에 의한 설계변형률

        Args:
            fIFzd (float): 수직설계하중
            fIvxd (float): 설계하중에 의한 받침의 a 방향으로의 최대 수평 상대변위
            fIvyd (float): 설계하중에 의한 받침의 b 방향으로의 최대 수평 상대변위
            fIA1 (float): 내부강판과 접촉하는 받침의 유효 면적
            fIS (float): 형상계수
            fIG (float): 전단탄성계수
            fIa (float): a 방향 유효길이
            fIb (float): b 방향 유효길이

        Returns:
            fOepsiloncd (float): 압축하중에 의한 설계변형률  4.2.3.8 압축하중에 의한 설계변형률의 값
            fOAr (float) : 하중효과로 감소된 유효 평면적 4.2.3.8 압축하중에 의한 유효 평면적의 값
        """
        assert isinstance(fOepsiloncd, float)
        assert isinstance(fOAr, float)
        assert isinstance(fIFzd, float)
        assert isinstance(fIvxd, float)
        assert isinstance(fIvyd, float)
        assert isinstance(fIA1, float)
        assert isinstance(fIS, float)
        assert fIG != 0
        assert isinstance(fIG, float)
        assert fIG != 0
        assert isinstance(fIa, float)
        assert fIa != 0
        assert isinstance(fIb, float)
        assert fIb != 0

        temp = (fIA1*(1-fIvxd/fIa-fIvyd/fIb))
        fOepsiloncd = (1.5*fIFzd)/(fIG*fIS*temp)
        fOAr = temp

        return RuleUnitResult(
            result_variables={
                "fOepsiloncd": fOepsiloncd,
                "fOAr": fOAr,
            }
        )