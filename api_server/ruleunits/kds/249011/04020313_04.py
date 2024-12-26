import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04020313_04(RuleUnit):
    priority = 1
    acc_able = False #기준맵에 존재하면 True, 존재하지 않으면 False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.2.3.13 (4)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-12'
    title = '수직처짐'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.2 받침
    4.2.3 강재보강 탄성받침
    4.2.3.13 구조물에 가해지는 힘, 모멘트, 변형
    (4)
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
    A[Title: 수직처짐];
    B["KDS 24 90 11 4.2.3.13 (4)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarIn1[/입력변수: 수직설계하중/];
		VarIn2[/입력변수: 탄성중합체 층 두께/];
		VarIn3[/입력변수: 내부강판과 접촉하는 받침의 유효 면적/];
		VarIn4[/입력변수: 전단탄성계수/];
		VarIn5[/입력변수: 최소두께의 탄성중합체 내부 층에 대한 형상계수/];
		VarIn6[/입력변수: 탄성중합체의 체적탄성계수/];

    VarOut1[/출력변수: 총 수직처짐/];

    VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 & VarIn2 & VarIn3 ~~~ VarIn6 & VarIn4

    end

    Python_Class ~~~ C(["KDS 24 90 11 4.2.3.13 (4)"]) -->Variable_def;
		Variable_def--->G

        G["\n <img src='https://latex.codecogs.com/svg.image? v_{z,d} = \sum \frac{F_{z,d}t_{i}}{A_{1}}(\frac{1}{5GS_{1}}-\frac{1}{E_{b}})'>------------------------------------------"];
        G--->I

    I(["수직처짐 값"])
    """

    @rule_method
    def Total_Vertical_Deflection (fIzd, fIti, fIA1, fIG, fIS1, fIEb) -> RuleUnitResult:
        """수직처짐

        Args:
            fIzd (float): 수직설계하중
            fIti (float): 탄성중합체 층 두께
            fIA1 (float): 내부강판과 접촉하는 받침의 유효 면적
            fIG (float): 전단탄성계수
            fIS1 (float): 최소두께의 탄성중합체 내부 층에 대한 형상계수
            fIEb (float): 탄성중합체의 체적탄성계수

        Returns:
           fOMd (float):  KDS 24 90 11 4.2.3.13 (4) 의 수직처짐의 값
        """

        assert isinstance(fIzd, float)
        assert isinstance(fIti, float)
        assert isinstance(fIA1, float)
        assert fIA1 != 0
        assert isinstance(fIG, float)
        assert fIG != 0
        assert isinstance(fIS1, float)
        assert fIS1 != 0
        assert isinstance(fIEb, float)
        assert fIEb != 0


        fOvzd = sum((fIzd*fIti[j]/fIA1)*(1/(5*fIG*(fIS1**2)) + 1/fIEb) for j in range(i))

        return RuleUnitResult(
              result_variables = {
                 "fOvzd": fOvzd,
              }
        )