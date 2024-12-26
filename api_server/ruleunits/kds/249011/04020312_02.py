import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020312_02(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.12 (2)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '버클링 안전성'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
    (2)
    """
    content = """
    """
    flowchart = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
    (2)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트d
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 버클링 안전성];
    B["KDS 24 90 11 4.2.3.12 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 탄성받침의 수직설계하중: 직각사각형 받침인 경우/];
		VarIn2[/입력변수: 탄성받침의 수직설계하중: 원형 받침인 경우/];
		VarIn3[/입력변수: 하중효과로 감소된 유효 평면적/];
		VarIn4[/입력변수: a 방향 유효길이/];
		VarIn5[/입력변수: 전단탄성계수/];
		VarIn6[/입력변수: 최소두께의 탄성중합체 내부 층에 대한 형상계수/];
		VarIn7[/입력변수: 전단에 유효한 받침 탄성중합체의 총 두께/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn6 & VarIn7 & VarIn5
    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.12 (2)"]) -->Variable_def;
		Variable_def--->G
		G{받침의 종류}
		G--직사각형 받침--->K
		G--원형 받침--->L
    K["\n <img src='https://latex.codecogs.com/svg.image? \frac{F_{z,d}}{A_{r}} < \frac{2a^{\prime}GS_{1}}{3T_{e}}'>-----------------------"];
		L["\n <img src='https://latex.codecogs.com/svg.image? \frac{F_{z,d}}{A_{r}} < \frac{2D^{\prime}GS_{1}}{3T_{e}}'>-----------------------"];
    K & L--->I

    I(["Pass or Fail"])
    """

    @rule_method
    def Buckling_safety(fIFzdA, fIFzdB, fIAr, fIa, fIG, fIS1,fITe) -> RuleUnitResult:
        """버클링 안전성

        Args:
            fIFzdA (float): 탄성받침의 수직설계하중 (직각사각형 받침인 경우)
            fIFzdB (float): 탄성받침의 수직설계하중 (원형 받침인 경우)
            fIAr (float): 하중효과로 감소된 유효 평면적
            fIa (float): a 방향 유효길이
            fIG (float): 전단탄성계수
            fIS1 (float): 최소두께의 탄성중합체 내부 층에 대한 형상계수
            fITe (float): 전단에 유효한 받침 탄성중합체의 총 두께

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.3.12 안정성 (3)의 통과 여부
        """
        assert isinstance(fIFzdA, float)
        assert isinstance(fIFzdB, float)
        assert isinstance(fIAr, float)
        assert fIAr > 0
        assert isinstance(fIa, float)
        assert isinstance(fIG, float)
        assert isinstance(fIS1, float)
        assert isinstance(fITe, float)
        assert fITe > 0

        if fIFzdA != 0 and fIFzdB ==0:
          temp_L = fIFzdA/fIAr
          temp_R = 2*fIa*fIG*fIS1/(3*fITe)
          if temp_L < temp_R:
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
          temp_L = fIFzdB/fIAr
          temp_R = 2*fIa*fIG*fIS1/(3*fITe)
          if temp_L < temp_R:
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