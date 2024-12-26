import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020403_04(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.4.3 (4)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '건조수축에 의한 곡률'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.4 처짐
    4.2.4.3 직접 처짐 계산에 의한 검증
    (4)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 건조수축에 의한 곡률];
    B["KDS 24 14 21 4.2.4.3 (4)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 건조수축에 의해 유발된 곡률/];
		VarIn2[/입력변수: 콘크리트 유효탄성계수를 적용한 탄성계수비/];
		VarIn3[/입력변수: 건조수축 변형률/];
		VarIn4[/입력변수: 단면 도심에 대한 철근 면적의 1차모멘트/];
		VarIn5[/입력변수: 단면 2차모멘트/];
		VarIn6[/입력변수: 콘크리트 유효탄성계수를 적용한 탄성계수비/];
		VarIn7[/입력변수: 건조수축 변형률/];
    VarIn8[/입력변수: 단면 도심에 대한 철근 면적의 1차모멘트/];
		VarIn9[/입력변수: 단면 2차모멘트/];
		VarOut1[/출력변수: 건조수축에 의해 유발된 곡률/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3
		VarIn2~~~VarIn4 & VarIn5  & VarIn6
		VarIn5~~~VarIn7 & VarIn8  & VarIn9
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.4.3 (4)"])
		C --> Variable_def

		Variable_def--->C--->F
		C["<img src='https://latex.codecogs.com/svg.image?\frac{1}{r_{sh}}=n\varepsilon&space;_{sh}\frac{S}{I}'>---------------------------------"]

		F(["건조수축에 의해 유발된 곡률"])
    """

    @rule_method
    def dry_shrinkage_curvature(fIn,fIepsish,fIS,fII) -> RuleUnitResult:
        """건조수축에 의한 곡률

        Args:
            fIn (float): 콘크리트 유효탄성계수를 적용한 탄성계수비
            fIepsish (float): 건조수축 변형률
            fIS (float): 단면 도심에 대한 철근 면적의 1차모멘트
            fII (float): 단면 2차모멘트


        Returns:
            fOrsh (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.4.3 직접 처짐 계산에 의한 검증 (4)의 값
        """

        assert isinstance(fIn, float)
        assert isinstance(fIepsish, float)
        assert isinstance(fIS, float)
        assert isinstance(fII, float)
        assert fII != 0

        fOrsh = fIn * fIepsish * fIS / fII

        return RuleUnitResult(
            result_variables = {
                "fOrsh": fOrsh,
            }
        )