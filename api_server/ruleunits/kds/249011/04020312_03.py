import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020312_03(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.12 (3)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '미끄럼 안전성'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
    (3)
    """
    content = """
    """
    flowchart = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.12 안정성
    (3)
    """
    # https://dillinger.io/ 표와 이미지 랜더링 확인 사이트
    # 이미지 링크 변환 사이트 https://www.somanet.xyz/2017/06/blog-post_21.html
    # 건설기준문서내용(text)
    content = """
    """
    # 플로우차트(mermaid)
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 미끄럼 안정성];
    B["KDS 24 90 11 4.2.3.12 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 모든 수평력의 합/];
		VarIn2[/입력변수: Fxy,d가 적용될 때 최소 수직설계하중/];
		VarIn3[/입력변수: 총 수직변형/];
		VarIn4[/입력변수: 하중효과로 감소된 유효 평면적/];
		VarIn5[/입력변수: 마찰계수/];
		VarIn6[/입력변수: 고정되지 않는 탄성받침의 마찰계수 계산을 위한 계수/];
		VarIn7[/입력변수: 최소수직하중에 의한 압축응력/];
		VarIn8[/입력변수: 평균압축응력/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn6 & VarIn7 & VarIn8 & VarIn5
    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.12 (3)"]) -->Variable_def;
		Variable_def--->G
		G{받침의 종류}
		G--고정되지 않은 받침--->K

		G--고정된 받침-->L0

        K["\n <img src='https://latex.codecogs.com/svg.image? F_{xy,d} \leq \mu_{e}F_{z,dmin}'>---------------------------"];
		L0["\n <img src='https://latex.codecogs.com/svg.image? \mu_{e} = 0.1 + \frac{1.5K_{f}}{\sigma_{m}}'>---------------------------"];
        L1["\n <img src='https://latex.codecogs.com/svg.image? F_{xy,d} \leq \mu_{e}F_{z,dmin}'>---------------------------"];
        L2["\n <img src='https://latex.codecogs.com/svg.image? \sigma_{cdmin}= \frac{F_{z,dmin}}{Ar} \geq 3'>----------------------------"];
    K -->I
    L0-->L1-->L2--->I

    I(["Pass or Fail"])
    """

    @rule_method
    def Skid_stability(fIFxyd, fIFzdminA, fIFzdminB, fIAr, fImue, fIKf, fIsigmac,fIsigmam) -> RuleUnitResult:
        """미끄럼 안정성

        Args:
            fIFxyd (float): 모든 수평력의 합
            fIFzdminA (float): Fxy,d가 적용될 때 최소 수직설계하중 (고정이 되지 않은 받침의 경우)
            fIFzdminB (float): Fxy,d가 적용될 때 최소 수직설계하중 (고정이 된 받침의 경우)
            fIAr (float): 하중효과로 감소된 유효 평면적
            fImue (float): 마찰계수
            fIKf (float): 고정되지 않는 탄성받침의 마찰계수 계산을 위한 계수
            fIsigmac (float): 최소수직하중에 의한 압축응력
            fIsigmam (float): 평균압축응력

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법)  4.2.3.12 안정성 (3)의 통과 여부
        """
        assert isinstance(fIFxyd, float)
        assert isinstance(fIFzdminA, float)
        assert isinstance(fIFzdminB, float)
        assert isinstance(fIAr, float)
        assert fIAr != 0
        assert isinstance(fImue, float)
        assert isinstance(fIKf, float)
        assert isinstance(fIsigmac, float)
        assert isinstance(fIsigmam, float)
        assert fIsigmam != 0

        if fIFzdminA != 0 and fIFzdminB == 0:
          if fIFxyd <= fImue * fIFzdminA:
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
          if fIKf != 0:
            fImue = 0.1 + (1.5 * fIKf)/fIsigmam

          if fIFzdminB/fIAr >= 3 or fIsigmac >= 3:
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