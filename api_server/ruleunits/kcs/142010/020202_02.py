import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS142010_020202_02(RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    acc_able = True # ACC 가능 여부
    author = '국가건설기준센터'  # 작성자명
    ref_code = 'KCS 14 20 10 2.2.2 (2)' # 건설기준문서
    ref_date = '2022-09-01'  # 디지털 건설문서 작성일
    doc_date = '2024-02-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '일반콘크리트'   # 건설기준명

    # 건설기준문서항목 (분류체계정보)
    description = """
    일반콘크리트
    2. 자재
    2.2 배합
    2.2.2 배합강도
    (2)
    """

    # 건설기준문서내용(text)
    content = """
    #### 2.2.2 배합강도
    (2) 품질기준강도(f_{cq})는 식 (2.2-1)과 같이 구조계산에서 정해진 설계기준압축강도(f_{ck})와 내구성 설계를 반영한 내구성기준압축강도(f_{cd})중에서 큰 값으로 정한다.

f_{cq} = max(f_{ck}, f_{cd}) (MPa)   (2.2-1)
    """

    # 플로우차트(mermaid)
    flowchart = """
flowchart TD
    subgraph Python_Class
    A["Title: 콘크리트 품질기준강도"];
    B["KCS 14 31 30 2.2.2 (2)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 30 2.2.2 (2)"])

    subgraph Variable_def
		VarIn1[/"입력변수: 설계기준압축강도"/];
		VarIn2[/"입력변수: 콘크리트 내구성기준압축강도"/];
    end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> D["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cq}=max(f{ck},f{cd})']'>--------------------------------------------------------"]

		D --> E(["<img src='https://latex.codecogs.com/png.image?\dpi{110}f{cq}']'>-------"]);
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정
    @rule_method
    def concrete_strength_quality_critera(fISpeCom, fIConDur) -> RuleUnitResult:
        """콘크리트 품질기준강도

        Args:
            fISpeCom (float): 설계기준압축강도
            fIConDur (float): 콘크리트 내구성기준압축강도

        Returns:
            fOConQua (float):콘크리트 품질기준 강도
        """
        assert isinstance(fISpeCom, float)
        assert isinstance(fIConDur, float)

        fOConQua = max(fISpeCom, fIConDur)
        return RuleUnitResult(
            result_variables = {
                "fOConQua": fOConQua
            }
        )