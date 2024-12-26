import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142012_010603_04_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 20 12 1.6.3 (4) ②'
    ref_date = '2022-09-01'
    doc_date = '2023-09-25'
    title = '일반적인 콘크리트의 측압'

    description = """
    거푸집 및 동바리
    1. 일반사항
    1.6 거푸집 및 동바리 설계
    1.6.3 거푸집 및 동바리 구조계산
    (4)
    """
    content = """
    #### 1.6.3 거푸집 및 동바리 구조계산
    (4) 거푸집 설계에서는 굳지 않은 콘크리트의 측압을 고려하여야 한다.
    ② 일반 콘크리트용 측압은 아래 ③의 경우를 제외하고는 식 (1.6-1)에 의해 산정한다.

	    $$p = WH$$ (1.6-1)
       여기서,  $$p$$:콘크리트의 측압(kN/㎡)
	            $$W$$:굳지 않은 콘크리트의 단위 중량(kN/㎥)
	            $$H$$:콘크리트의 타설 높이(m)
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 일반적인 콘크리트의 측압];
    B["KCS 14 20 12 1.6.3 (4) ②"];
    B ~~~ A
    end

    KCS(["KCS 14 20 12 1.6.3 (4) ②"])

    subgraph Variable_def
    VarOut[/출력변수: 콘크리트 측압/];
    VarIn1[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn2[/입력변수: 콘크리트의 타설 높이/];
    VarIn3[/입력변수: 콘크리트 슬럼프/];
    VarIn4[/입력변수: 타설깊이/];
    VarIn5[/입력변수: 일반적인 내부 진동다짐/];
    VarIn6[/입력변수: 굳지 않은 콘크리트의 단위 중량/];
    VarIn7[/입력변수: 기둥/];
    VarIn8[/입력변수: 벽체/];
    VarOut ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn3  ~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"콘크리트 슬럼프 ≤ 175mm, \n 타설 깊이 ≤ 1.2m \n 일반적인 내부 진동다짐 \n 기둥 or 벽체"}
    C --> |"False"|D["<img src='https://latex.codecogs.com/png.image?\dpi{500} p = WH'>"];
    D --> End([콘크리트의 측압])
    """

    @rule_method

    def general_concrete_pressure(fIConSlu, fIPouDep, bIVibCom, bICol, bIWal, fIW, fIH) -> RuleUnitResult:
        """
        Args:
            fIConSlu (float): 콘크리트 슬럼프
            fIPouDep (float): 타설깊이
            bIVibCom (bool): 일반적인 내부 진동다짐
            bICol (bool): 기둥
            bIWal (bool): 벽체
            fIW (float): 굳지 않은 콘크리트의 단위 중량
            fIH (float): 콘크리트의 타설 높이

        Returns:
            fOConPre (float): 콘크리트 측압
        """
        assert isinstance(fIConSlu, float)
        assert isinstance(fIPouDep, float)
        assert isinstance(bIVibCom, bool)
        assert isinstance(bICol, bool)
        assert isinstance(bIWal, bool)
        assert (bICol+bIWal) !=2
        assert isinstance(fIW, float)
        assert isinstance(fIH, float)


        if fIConSlu > 175 or fIPouDep > 1.2 or bIVibCom == False or bICol == False or bIWal == False:
            fOConPre = fIW * fIH
        else:
            fOConPre = None
        return RuleUnitResult(
            result_variables = {
                "fOConPre": fOConPre,
                })