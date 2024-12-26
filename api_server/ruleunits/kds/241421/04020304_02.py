import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04020304_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.2.3.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '변형률 차이'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.2 사용한계상태
    4.2.3 균열
    4.2.3.4 균열폭 계산
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 변형률 차이];
    B["KDS 24 14 21 4.2.3.4 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 균열면에서 계산한 철근 인장응력/];
		VarIn2[/입력변수: 철근의 평균 탄성계수/];
		VarIn3[/입력변수: 콘크리트 탄성계수/];
		VarIn4[/입력변수: 첫 균열이 발생할 때 유효한 콘크리트 인장강도/];
		VarIn5[/입력변수: 하중작용 기간에 따른 계수/];
		VarIn6[/입력변수: 탄성계수비/];
		VarIn7[/입력변수: 유효 철근비/];
		VarIn8[/입력변수: 콘크리트 유효 인장면적/];
		VarIn9[/입력변수: 콘크리트 유효 인장면적 내에 있는 철근의 단면적/];
		VarIn10[/입력변수: 콘크리트 유효 인장면적 내에 있는 프리스트레싱강재의단면적/];
		VarIn11[/입력변수: 콘크리트 유효 인장깊이/];
		VarIn12[/입력변수: 철근과 긴장재의 부착특성 및 지름의 차이에 따른영향을반영하기위한계수/];
		VarIn13[/입력변수: 단면의 깊이/];
		VarIn14[/입력변수: 단면의 유효깊이/];
		VarIn15[/입력변수: 중립축 깊이/];
		VarOut1[/출력변수: 변형률 차이/];
		VarOut1~~~VarIn1 & VarIn2  & VarIn3 & VarIn4
		VarIn2~~~VarIn5  & VarIn6 & VarIn7 & VarIn8
		VarIn6~~~VarIn9 & VarIn10 & VarIn11 & VarIn12
		VarIn10~~~VarIn13 & VarIn14 & VarIn15
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.2.3.4 (2)"])
		C --> Variable_def

		Variable_def--->D & E --->F--->G
		D["<img src='https://quicklatex.com/cache3/1d/ql_83d716ec9ddf5a1ff56c2f0450c5ef1d_l3.png'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?d_{cte}=min[2.5(h-d),(h-c)/3,h/2]'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?\varepsilon&space;_{sm}-\varepsilon&space;_{cm}=\frac{f_{so}}{E_s}-0.4\frac{f_{cte}}{E_s\rho&space;_e}(1&plus;n\rho&space;_e)\geq&space;0.6\frac{f_{so}}{E_s}'>---------------------------------"]
		G(["변형률 차이"])
    """

    @rule_method
    def strain_difference(fIEs,fIEc,fIfso,fIfcte,fIActe,fIAs,fIAp,fIxi1) -> RuleUnitResult:
        """설계 균열폭

        Args:
            fIEs (float): 철근의 평균 탄성계수
            fIEc (float): 콘크리트 탄성계수
            fIfso (float): 균열면에서 계산한 철근 인장응력
            fIfcte (float): 첫 균열이 발생할 때 유효한 콘크리트인장강도
            fIActe (float): 콘크리트 유효 인장면적
            fIAs (float): 콘크리트 유효 인장면적 내에 있는 철근의 단면적
            fIAp (float): 콘크리트 유효 인장면적 내에 있는 프리스트레싱강재의 단면적
            fIxi1 (float): 철근과 긴장재의 부착특성 및 지름의 차이에 따른 영향을 반영하기 위한  계수

        Returns:
            fOesmecm (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 값 1
            fOn (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 값 2
            fOrhoe (float): 콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 값 3
            pass_fail (bool):  콘크리트교 설계기준 (한계상태설계법) 4.2.3.4 균열폭 계산 (1)의 판단 결과
        """

        assert isinstance(fIEs, float)
        assert isinstance(fIEc, float)
        assert isinstance(fIfso, float)
        assert isinstance(fIfcte, float)
        assert isinstance(fIActe, float)
        assert isinstance(fIAs, float)
        assert isinstance(fIAp, float)
        assert isinstance(fIxi1, float)

        fOn = fIEs / fIEc
        fOrhoe = (fIAs + (fIxi1**2) * fIAp) / fIActe

        fOesmecm = fIfso / fIEs - 0.4 * fIfcte / fIEs / fOrhoe * (1 + fOn * fOrhoe)

        if fOesmecm >= 0.6 * fIfso / fIEs :
          return RuleUnitResult(
              result_variables = {
                  "fOesmecm": fOesmecm,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOesmecm": fOesmecm,
                  "pass_fail": False,
              }
          )