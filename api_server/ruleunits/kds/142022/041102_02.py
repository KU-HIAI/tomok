import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS142022_041102_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 20 22 4.11.2 (2)'
    ref_date = '2022-01-11'
    doc_date = '2024-10-07'
    title = '철근콘크리트 슬래브와 기초판에 대한 공칭전단강도'

    description = """
    콘크리트구조 전단 및 비틀림 설계기준
    4. 설계
    4.11 슬래브와 기초판에 대한 전단 설계
    4.11.2 2방향 거동에 대한 전단강도
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근콘크리트 슬래브와 기초판에 대한 공칭전단강도];
    B["KDS 14 20 22 4.11.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
    VarOut1[/출력변수: 철근콘크리트 슬래브와 기초판에 대한 공칭전단강도/];
    VarOut2[/출력변수: 콘크리트 재료의 공칭전단응력강도/];
    VarOut3[/출력변수: 슬래브의 두께계수/];
    VarOut4[/출력변수: 위험단면 둘레길이의 영향계수/];
    VarOut5[/출력변수: 압축대 콘크리트의 인장강도/];
    VarOut6[/출력변수: 슬래브 휨 압축대의 균열각도/];
    VarOut7[/출력변수: 압축철근의 영향을 무시하고 계산된 슬래브 위험단면의 압축대 깊이의 평균값/];
    VarOut8[/출력변수: 위험단면의 압축대에 작용하는 평균 압축응력/];
    VarOut9[/출력변수: 설계위험단면에서 양방향으로 각각 h만큼 떨어진 폭의 슬래브에 대한 평균주인장철근비/];
    VarOut10[/출력변수: 설계위험단면에서 연장하여 슬래브에 정착해야하는 주인장철근의 길이/];
    VarIn1[/입력변수: 슬래브와 기초판에서 2방향 전단에 대한 위험단면의 둘레/];
    VarIn2[/입력변수: 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리/];
    VarIn3[/입력변수: 경량콘크리트계수/];
    VarIn4[/입력변수: 설계위험단면에서 양방향으로 각각 h만큼 떨어진 폭의 슬래브에 대한 평균주인장철근비/];
    VarIn5[/입력변수: 부재의 전체 두께/];
    VarIn6[/입력변수: 인장이형철근의 정착길이/];
    VarIn7[/입력변수: 슬래브 또는 기초판에서 Vc를 계산할 때의 계수/];
    VarIn8[/입력변수: 설계기준 압축강도/];

    VarOut1 & VarOut2 & VarOut3 & VarOut4 & VarOut5 ~~~ VarOut6 & VarOut7 & VarOut8 & VarOut9 & VarOut10
    VarOut6 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
    VarIn1 ~~~ VarIn5 & VarIn6 & VarIn7 & VarIn8

    end

    Python_Class ~~~ C(["KDS 14 20 22 4.11.2 (2)"])
		C --> Variable_def

		Variable_def --> D --YES--> E
		D --NO--> F
		E & F --> G --> H

		Variable_def --> I & J --> K
		Variable_def --> L & M

		H & I & K & L & M --> N --> O --> P

    D{"<img src='https://latex.codecogs.com/svg.image? \rho \leq 0.005'>------------------"};
    E["<img src='https://latex.codecogs.com/svg.image? \rho =0.005'>------------------"];
    F["<img src='https://latex.codecogs.com/svg.image? \rho'>----"];
    G["<img src='https://latex.codecogs.com/svg.image? \rho \leq 0.03'>------------------"];
    H["<img src='https://latex.codecogs.com/svg.image? c_{u}=d\left [ 25\sqrt{\rho /f_{ck}}-300\left ( \rho/f_{ck} \right ) \right ]'>------------------"];

	  I["<img src='https://latex.codecogs.com/svg.image? f_{te}=0.2\sqrt{f_{ck}}'>------------------"];
	  J["<img src='https://latex.codecogs.com/svg.image? f_{cc}=(2/3)f_{ck}'>------------------"];
	  K["<img src='https://latex.codecogs.com/svg.image? cot\psi=\sqrt{f_{te}(f_{te}+f_{cc})}/f_{te}'>------------------"];

    L["<img src='https://latex.codecogs.com/svg.image? 0.75\leq k_{s}=(300/d)^{0.25}\leq 1.1'>------------------"];
    M["<img src='https://latex.codecogs.com/svg.image? k_{bo}=4/\sqrt{\alpha_{s}(b_{o}/d)}\leq1.25'>------------------"];

    N["<img src='https://latex.codecogs.com/svg.image? v_{c}=\lambda k_{s}k_{bo}f_{te}cot\psi(c_{u}/d)'>------------------"];

    O["<img src='https://latex.codecogs.com/svg.image? V_{c}=v_{c}b_{o}d'>------------------"];

		P(["철근콘크리트 슬래브와 기초판에 대한 공칭전단강도"]);

		Q["<img src='https://latex.codecogs.com/svg.image? (h+l_{d})'>------------------"];
		R(["설계위험단면에서 연장하여 슬래브에 정착해야하는 주인장철근의 길이"])

		Variable_def --> Q --> R
    """

    @rule_method
    def Nominal_shear_strength_for_reinforced_concrete_slabs_and_foundation_plates(fIbo,fId,fIlambda,fIrho,fIh,fIld,fIalphas,fIfck) -> RuleUnitResult:
        """철근콘크리트 슬래브와 기초판에 대한 공칭전단강도

        Args:
            fIbo (float): 슬래브와 기초판에서 2방향 전단에 대한 위험단면의 둘레
            fId (float): 종방향 인장철근의 중심에서 압축콘크리트 연단까지 거리
            fIlambda (float): 경량콘크리트계수
            fIrho (float): 설계위험단면에서 양방향으로 각각 h만큼 떨어진 폭의 슬래브에 대한 평균주인장철근비
            fIh (float): 부재의 전체 두께
            fIld (float): 인장이형철근의 정착길이
            fIalphas (float): 슬래브 또는 기초판에서 Vc를 계산할 때의 계수
            fIfck (float): 설계기준 압축강도

        Returns:
            fOVc (float): 철근콘크리트 슬래브와 기초판에 대한 공칭전단강도
            fOsmalvc (float): 콘크리트 재료의 공칭전단응력강도
            fOks (float): 슬래브의 두께계수
            fOkbo (float): 위험단면 둘레길이의 영향계수
            fOfte (float): 압축대 콘크리트의 인장강도
            fOcotpsi (float): 압축대 콘크리트의 인장강도
            fOcu (float): 압축철근의 영향을 무시하고 계산된 슬래브 위험단면의 압축대 깊이의 평균값
            fOfcc (float): 위험단면의 압축대에 작용하는 평균 압축응력
            fOrho (float): 설계위험단면에서 양방향으로 각각 h만큼 떨어진 폭의 슬래브에 대한 평균주인장철근비
            fOlemate (float): 설계위험단면에서 연장하여 슬래브에 정착해야하는 주인장철근의 길이
            pass_fail (bool): 콘크리트구조 전단 및 비틀림 설계기준  4.11.2 2방향 거동에 대한 전단강도 (2)의 판단 결과
        """

        assert isinstance(fIbo, float)
        assert fIbo > 0
        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIlambda, float)
        assert fIlambda > 0
        assert isinstance(fIrho, float)
        assert fIrho > 0
        assert isinstance(fIh, float)
        assert fIh > 0
        assert isinstance(fIld, float)
        assert fIld > 0
        assert isinstance(fIalphas, float)
        assert fIalphas == 1.0 or 1.33 or 2.0
        assert isinstance(fIfck, float)
        assert fIfck > 0

        if fIrho <= 0.005:
          fOrho = 0.005
        else:
          fOrho = fIrho

        if (300 / fId) ** 0.25 <= 0.75:
          fOks = 0.75
        elif (300 / fId) ** 0.25 >= 1.1:
          fOks = 1.1
        else:
          fOks = (300 / fId) ** 0.25


        fOlemate = fIh + fIld
        fOfcc = 2 / 3 * fIfck
        fOfte = 0.2 * (fIfck ** 0.5)
        fOcu = fId * (25 * ((fOrho / fIfck) ** 0.5) - 300 * (fOrho / fIfck))
        fOcotpsi = ((fOfte * (fOfte + fOfcc))**0.5) / fOfte
        fOkbo = min(4 / (fIalphas * (fIbo / fId)) ** 0.5, 1.25)
        fOsmalvc = fIlambda * fOks * fOkbo * fOfte * fOcotpsi * (fOcu / fId)
        fOVc = fOsmalvc * fIbo * fId

        if fOrho <= 0.03 :
          return RuleUnitResult(
              result_variables = {
                  "fOVc": fOVc,
                  "fOlemate": fOlemate,
                  "fOcu": fOcu,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )