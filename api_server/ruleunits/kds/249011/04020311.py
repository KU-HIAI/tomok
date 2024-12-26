import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020311(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.11'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '적층탄성받침의 보강판 최소두께'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.11 보강판 규정
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 적층탄성받침의 보강판 최소두께];
    B["KDS 24 90 11 4.2.3.11"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 수직설계하중/];
		VarIn2[/입력변수: 하중효과로 감소된 유효 면적/];
		VarIn3[/입력변수: 내부보강판 양면에서의 탄성중합체의 두께/];
		VarIn4[/입력변수: 내부보강판 양면에서의 탄성중합체의 두께/];
		VarIn5[/입력변수: 보강판의 항복 응력/];
		VarIn6[/입력변수: 보강판의 인장응력을 고려하기 위한 계수/];
    VarOut1[/출력변수: 적층탄성받침의 보강판 최소두께/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
		end

		Python_Class ~~~ C(["KDS 24 90 11 4.2.3.11"]) --> Variable_def;
		Variable_def--->G
		G{구멍이 없는 경우}
		G--yes--->K
		G--NO--->L
		K["<img src='https://latex.codecogs.com/svg.image?K_{h}=1'>---------------"];
		L["<img src='https://latex.codecogs.com/svg.image?K_{h}=2'>----------------"];

    K & L--->F--->I
    F["<img src='https://latex.codecogs.com/svg.image?t_{s}=\frac{1.3F_{z,d}(t_{1}&plus;t_{2})K_{h}}{A_{r}f_{y}},t_{s}\geq&space;2mm'>--------------------------------------------------------"];

		I(["적층탄성받침의 보강판 최소두께"])
    """

    @rule_method
    def Minimum_Thickness_Of_Stiffeners_For_Laminated_Elastic_Supports(fIFzd, fIAr, fIt1, fIt2, fIfy, fIKh) -> RuleUnitResult:
        """적층탄성받침의 보강판 최소두께

        Args:
            fIFzd (float): 수직설계하중
            fIAr (float): 하중효과로 감소된 유효 면적
            fIt1 (float): 내부보강판 양면에서의 탄성중합체의 두께
            fIt2 (float): 내부보강판 양면에서의 탄성중합체의 두께
            fIfy (float): 보강판의 항복 응력
            fIKh (float): 보강판의 인장응력을 고려하기 위한 계수

        Returns:
            fOts (float): 적층탄성받침의 보강판 최소두께 4.2.3.11의 값
        """
        assert isinstance(fOts, float)
        assert isinstance(fIFzd, float)
        assert isinstance(fIAr, float)
        assert fIAr != 0
        assert isinstance(fIt1, float)
        assert isinstance(fIt2, float)
        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert isinstance(fIKh, float)

        fOts = (1.3*fIFzd*(fIt1+fIt2)*fIKh)/(fIAr*fIfy)
        if fOts < 2:
          fOts = 2

        return RuleUnitResult(
            result_variables = {
                "fOts": fOts,

            }
        )