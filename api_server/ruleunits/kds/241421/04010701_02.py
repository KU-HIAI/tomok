import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010701_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.7.1 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-21'
    title = '계수하중에 의해 유발된 철근과 콘크리트의 응력'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.7 겹판요소 모델
    4.1.7.1 판요소 설계
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 계수하중에 의해 유발된 철근과 콘크리트의 응력];
    B["KDS 24 14 21 4.1.7.1 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarOut1[/출력변수: 횡방향 콘크리트의 응력/];
		VarOut2[/출력변수: 종방향 콘크리트의 응력/];
    VarOut3[/출력변수: 콘크리트 스트럿에 유발된 압축응력/];
		VarIn1[/입력변수: 철근 재료계수/];
		VarIn2[/입력변수: 종방향 축에 일치하게 직교 2방향으로 배치한 철근의 콘크리트 단면적에 대한 비/];
		VarIn3[/입력변수: 횡방향 축에 일치하게 직교 2방향으로 배치한 철근의 콘크리트 단면적에 대한 비/];
		VarIn4[/입력변수: 요소의 종방향으로 작용하는 법선응력/];
		VarIn5[/입력변수: 요소의 횡방향으로 작용하는 법선응력/];
		VarIn6[/입력변수: 요소에 작용하는 전단응력/];
		VarIn7[/입력변수: 스트럿의 최대 유효 압축강도/];
		VarIn8[/입력변수: 균열면에서 종방향으로 유발된 철근 응력/];
		VarIn9[/입력변수: 균열면에서 횡방향으로 유발된 철근 응력/];
		VarIn10[/입력변수: 종방향 철근의 항복응력/];
		VarIn11[/입력변수: 횡방향 철근의 항복응력/];
		VarIn12[/입력변수: 종방향 축에 대한 스트럿의 경사각/];
		VarIn13[/입력변수: 콘크리트 재료계수/];

		VarIn1 & VarIn2 & VarIn3
    ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9
		VarIn8 ~~~ VarIn10 & VarIn11 & VarIn12 & VarIn13
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.7.1 (2)"])
		C --> Variable_def

		Variable_def-->G & D & E--->F

		G["<img src='https://latex.codecogs.com/svg.image?\rho&space;_lf_{sl}=f_{nl}&plus;v&space;cot\theta\leq\phi&space;_s\rho&space;_lf_{yl}'>---------------------------------"]
		D["<img src='https://latex.codecogs.com/svg.image?\rho&space;_lf_{st}=f_{nt}&plus;v&space;cot\theta\leq\phi&space;_s\rho&space;_tf_{yt}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?f_{c2}=v(tan\theta&plus;cot\theta)\leq\phi&space;_cf_{c2,max}'>---------------------------------"]
		F(["콘크리트의 응력"])
    """

    @rule_method
    def stress_of_concrete_and_rebar(fIrhol,fIfnl,fIv,fItheta,fIphis,fIfyl,fIrhot,fIfnt,fIfyt,fIphic,fIfc2max) -> RuleUnitResult:
        """계수하중에 의해 유발된 철근과 콘크리트의 응력

        Args:
            fIrhol (float): 종방향 축에 일치하게 직교 2방향으로 배치한 철근의 콘크리트 단면적에 대한 비
            fIfnl (float): 요소의 종방향으로 작용하는 법선응력
            fIv (float): 요소에 작용하는 전단응력
            fItheta (float): 종방향 축에 대한 스트럿의 경사각
            fIphis (float): 철근 재료계수
            fIfyl (float): 종방향 철근의 항복응력
            fIrhot (float): 횡방향 축에 일치하게 배치한 철근의 콘크리트 단면적에 대한 비
            fIfnt (float): 요소의 횡방향으로 작용하는 법선응력
            fIfyt (float): 횡방향 철근의 항복응력
            fIphic (float): 콘크리트 재료계수
            fIfc2max (float): 스트럿의 최대 유효 압축강도

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (2)의 판단 결과
            fOfsl (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (2)의 값
            fOfst (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (2)의 값
            fOfc2 (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.7.1 판요소 설계 (2)의 값
        """

        assert isinstance(fIrhol, float)
        assert fIrhol != 0
        assert isinstance(fIfnl, float)
        assert isinstance(fIv, float)
        assert isinstance(fItheta, float)
        assert fItheta != 0
        assert isinstance(fIphis, float)
        assert isinstance(fIfyl, float)
        assert isinstance(fIrhot, float)
        assert fIrhot != 0
        assert isinstance(fIfnt, float)
        assert isinstance(fIfyt, float)
        assert isinstance(fIphic, float)
        assert isinstance(fIfc2max, float)

        import math

        fOfsl = (fIfnl + fIv/math.tan(math.radians(fItheta)))/fIrhol
        fOfst = (fIfnt + fIv*math.tan(math.radians(fItheta)))/fIrhot
        fOfc2 = fIv*(math.tan(math.radians(fItheta)) + 1/math.tan(math.radians(fItheta)))

        if fOfsl <= fIphis*fIfyl and fOfst <= fIphis*fIfyt and fOfc2 <= fIphic*fIfc2max:
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