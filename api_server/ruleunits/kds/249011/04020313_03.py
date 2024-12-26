import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020313_03(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.13 (3)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '회전저항에 의한 복원모멘트'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.13 구조물에 가해지는 힘, 모멘트, 변형
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
    A[Title: 회전저항에 의한 복원모멘트];
    B["KDS 24 90 11 4.2.3.13 (3)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 전단탄성계수/];
		VarIn2[/입력변수: 회전각/];
		VarIn3[/입력변수: a 방향 유효길이/];
		VarIn4[/입력변수: b 방향 유효길이/];
		VarIn5[/입력변수: 받침개수/];
		VarIn6[/입력변수: 두께/];
		VarIn7[/입력변수: 탄성받침에서 복원모멘트 계수/];
		VarIn8[/입력변수: 원형 받침의 직경/];
    VarOut1[/출력변수: 탄성받침에서 복원모멘트 설계값/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 & VarIn2 & VarIn3 & VarIn4~~~VarIn6 & VarIn7 & VarIn8 & VarIn5 & VarOut1

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.13 (3)"]) -->Variable_def;
		Variable_def--->G
		G{받침의 종류}
		G--직사각형 받침--->K
		G--원형 받침--->L
        K["\n <img src='https://latex.codecogs.com/svg.image? M_{d}=G\frac{\alpha a^{\prime5} b^{\prime}}{n t_i^3K_{s}}'>---------------------------"];
		L["<img src='https://latex.codecogs.com/svg.image? M_{d}=G\frac{\alpha \pi D^{\prime6}}{512n t_i^3}'>--------------------------------"];
    K & L--->I

    I(["탄성받침에서 복원모멘트 설계값"])
    """

    @rule_method
    def Design_values_for_restoring_moments_due_to_rotational_resistance(fIG, fIalpha, fIa, fIb, fIn, fIti, fIKs, fID) -> RuleUnitResult:
        """회전저항에 의한 복원모멘트 설계값

        Args:
            fIG (float): 전단탄성계수
            fIalpha (float): 회전각
            fIa (float): a 방향 유효길이
            fIb (float): b 방향 유효길이
            fIn (float): 받침개수
            fIti (float): 두께
            fIKs (float): 탄성받침에서 복원모멘트 계수
            fID (float): 원형 받침의 직경

        Returns:
           fOMd (float):  KDS 24 90 11 4.2.3.13 (3) 의 회전저항에 의한 복원모멘트 설계값
        """

        assert isinstance(fIG, float)
        assert isinstance(fIalpha, float)
        assert isinstance(fIa, float)
        assert isinstance(fIb, float)
        assert isinstance(fIn, float)
        assert fIn != 0
        assert isinstance(fIti, float)
        assert fIti > 0
        assert isinstance(fIKs, float)
        assert fIKs != 0
        assert isinstance(fID, float)


        if fID == 0 and fIa != 0:
          fOMd = (fIG*fIalpha*(fIa**5)*fIb)/(fIn*(fIti**3)*fIKs)
          return RuleUnitResult(
                 result_variables = {
                     "fOMd": fOMd,
                 }
            )
        else:
          fOMd = (fIG*fIalpha*math.pi*(fID**6))/(512*fIn*(fIti**3))
          return RuleUnitResult(
                 result_variables = {
                     "fOMd": fOMd,
                 }
            )