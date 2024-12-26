import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010701_05(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.7.1 (5)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '스트럿의 최대 유효강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
    (5)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 스트럿의 최대 유효강도];
    B["KDS 24 14 21 4.1.7.1 (5)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 항복강도/];
		VarIn2[/입력변수: 콘크리트 압축강도 유효계수/];
		VarIn3[/입력변수: 콘크리트 기준압축강도/];
		VarIn4[/입력변수: 종방향과 횡방향 철근 응력 중에서 큰 값/];
		VarIn5[/입력변수: 철근의 재료계수/];
		VarIn6[/입력변수: 철근의 기준항복강도/];

		VarOut1[/출력변수: 스트럿의 최대 유효강도/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~VarIn4 & VarIn5 & VarIn6

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.7.1 (5)"])
		C --> Variable_def

		Variable_def--->F--->D--->E
		F["<img src='https://latex.codecogs.com/svg.image?f_{c2,max}=[0.85-\frac{f_s}{\phi&space;_sf_y}(0.85-v)]f_{ck}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?vf_{ck}<f_{c2,max}<0.85f_{ck}'>---------------------------------"]
    E(["콘크리트 스트럿의 최대 유효강도"])
    """

    @rule_method
    def Maximum_effective_strength_of_strut(fIyiestr,fInu,fIfck,fIfs,fIphis,fIfy) -> RuleUnitResult:
        """스트럿의 최대 유효강도

        Args:
            fIyiestr (float): 항복강도
            fInu (float): 콘크리트 압축강도 유효계수
            fIfck (float): 콘크리트 기준압축강도
            fIfs (float): 종방향과 횡방향 철근 응력 중에서 큰 값
            fIphis (float): 철근의 재료계수
            fIfy (float): 철근의 기준항복강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (5)의 판단 결과
            fOc2max (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (5)의 값
        """

        assert isinstance(fIyiestr, float)
        assert isinstance(fInu, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIfs, float)
        assert isinstance(fIphis, float)
        assert fIphis != 0
        assert isinstance(fIfy, float)
        assert fIfy != 0

        fOc2max = (0.85 - fIfs / (fIphis * fIfy) * (0.85 - fInu)) * fIfck

        if fInu * fIfck < fOc2max < 0.85 * fIfck:
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