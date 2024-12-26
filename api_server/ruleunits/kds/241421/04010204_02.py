import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010204_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.2.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-17'
    title = '횡방향 소요 철근량'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 소요 철근량];
    B["KDS 24 14 21 4.1.2.4 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 플랜지에 배치되는 종방향 전단철근 면적/];
		VarIn2[/입력변수: 플랜지 내의 횡방향 철근 간격/];
		VarIn3[/입력변수: 플랜지와 복부 계면에 작용하는 계수전단응력/];
		VarIn4[/입력변수: 플랜지 두께/];
		VarIn5[/입력변수: 철근 또는 프리스트레싱 강재의 재료계수/];
		VarIn6[/입력변수: 철근의 기준항복강도/];
		VarIn7[/입력변수: 거더 플랜지에 형성된 스트럿의 경사각/];
		VarIn1~~~~VarIn2 & VarIn3 & VarIn4
		VarIn3~~~~VarIn5 & VarIn6 & VarIn7

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.2.4 (2)"])
		C --> Variable_def

		Variable_def--->D--->E
		D{"<img src='https://latex.codecogs.com/svg.image?\frac{A_{vf}}{s_{f}}\geq\frac{v_{uf}t_{f}}{\phi_{s}f_{y}cot\theta&space;_{f}}'>---------------------------------"}
		E(["Pass or Fail"])
    """

    @rule_method
    def transverse_required_amount_of_reinforcement(fIAvf,fIsf,fIvuf,fItf,fIphis,fIfy,fIthetaf) -> RuleUnitResult:
        """횡방향 소요 철근량

        Args:
            fIAvf (float): 플랜지에 배치되는 종방향 전단철근 면적
            fIsf (float): 플랜지 내의 횡방향 철근 간격
            fIvuf (float): 플랜지와 복부 계면에 작용하는 계수전단응력
            fItf (float): 플랜지 두께
            fIphis (float): 철근 또는 프리스트레싱 강재의 재료계수
            fIfy (float): 철근의 기준항복강도
            fIthetaf (float): 거더 플랜지에 형성된 스트럿의 경사각

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (2)의 판단결과
        """

        assert isinstance(fIAvf, float)
        assert isinstance(fIsf, float)
        assert fIsf != 0
        assert isinstance(fIvuf, float)
        assert isinstance(fItf, float)
        assert isinstance(fIphis, float)
        assert fIphis != 0
        assert isinstance(fIfy, float)
        assert fIfy != 0
        assert isinstance(fIthetaf, float)

        import math

        if fIAvf / fIsf >= fIvuf * fItf * math.tan(math.radians(fIthetaf)) / (fIphis * fIfy):
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