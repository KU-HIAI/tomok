import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.4.3 (1)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-18'
    title = '슬래브의 설계뚫림전단강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.4 뚫림
    4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 슬래브의 설계뚫림전단강도];
    B["KDS 24 14 21 4.1.4.3 (1)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 콘크리트의 재료계수/];
		VarIn2[/입력변수: 유효깊이 변화에 따른 전단강도 보정계수/];
		VarIn3[/입력변수: 인장철근비/];
		VarIn4[/입력변수: 콘크리트 기준압축강도/];
		VarIn5[/입력변수: 축력에 의한 단면의 직각응력/];
		VarIn6[/입력변수: 콘크리트 인장강도/];
		VarIn7[/입력변수: 단면의 유효깊이/];
		VarIn8[/입력변수: y-방향의 인장철근비/];
		VarIn9[/입력변수: z-방향의 인장철근비/];
		VarIn10[/입력변수: 법선응력/];
		VarIn11[/입력변수: 내부 기둥인 경우 기둥 사이의 지간의 종방향 힘이고, 가장자리 외측 기둥인경우 위험단면에 작용하는 계수 종방향력/];
		VarIn12[/입력변수: 내부 기둥인 경우 기둥 사이의 지간의 종방향 힘이고, 가장자리 외측 기둥인경우 위험단면에 작용하는 계수 종방향력/];
	  VarOut1[/출력변수: 슬래브의 설계뚫림전단강도/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4
		VarIn1 & VarIn2 & VarIn3 & VarIn4~~~VarIn5 & VarIn6 & VarIn7 & VarIn8
		VarIn5 & VarIn6 & VarIn7 & VarIn8~~~VarIn9 & VarIn10 & VarIn11 & VarIn12

		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.4.3 (1)"])
		C --> Variable_def

		Variable_def---> D & E & F & G
		D["<img src='https://latex.codecogs.com/svg.image?\kappa=1&plus;\sqrt{200/d}\leq&space;2.0'>---------------------------------"];
		E["<img src='https://latex.codecogs.com/svg.image?\rho&space;_l=\sqrt{\rho&space;_{ly}\rho&space;_{lz}}\leq&space;0.02'>---------------------------------"];
		F["<img src='https://latex.codecogs.com/svg.image?f_{ny}=\frac{N_uy}{A_{cy}}'>---------------------------------"];
		G["<img src='https://latex.codecogs.com/svg.image?f_{ny}=\frac{N_uz}{A_{cz}}'>---------------------------------"];
		F & G--->H
		H["<img src='https://latex.codecogs.com/svg.image?f_n=(f_{ny}&plus;f_{nz})/2'>---------------------------------"];
		D & E & H--->J-->k
		J["<img src='https://latex.codecogs.com/svg.image?v_{cd}=0.85\phi&space;_c\kappa(100\rho&space;_lf_{ck})^{1/3}&plus;0.1f_n\geq(0.4\phi&space;_cf_{ctk}&plus;0.1f_n)'>---------------------------------"];
		k(["슬래브의 설계뚫림전단강도"]);
    """

    @rule_method
    def Design_puncture_shear_strength_of_slab(fIphic,fIfck,fIfctk,fId,fIrhoIy,fIrhoIz,fINuy,fINuz,fIAcy,fIAcz) -> RuleUnitResult:
        """슬래브의 설계뚫림전단강도

        Args:
            fIphic (float): 콘크리트 재료계수
            fIfck (float): 콘크리트 기준압축강도
            fIfctk (float): 콘크리트 인장강도
            fId (float): 단면의 유효깊이
            fIrhoIy (float): y-방향의 인장철근비
            fIrhoIz (float): z-방향의 인장철근비
            fINuy (float): 내부 기둥인 경우 기둥 사이의 지간의 종방향 힘이고, 가장자리 외측 기둥인 경우 위험단면에 작용하는 계수 종방향력
            fINuz (float): 내부 기둥인 경우 기둥 사이의 지간의 종방향 힘이고, 가장자리 외측 기둥인 경우 위험단면에 작용하는 계수 종방향력
            fIAcy (float): y축 콘크리트 단면적
            fIAcz (float): z축 콘크리트 단면적

        Returns:
            fOvd (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 1
            fOk (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 2
            fOrhol (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 3
            fOfn (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 4
            fOfny (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 5
            fOfnz (float): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 값 6
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법) 4.1.4.3 전단철근이 없는 슬래브 또는 기둥 기초판의 뚫림전단강도 (1)의 판단 결과
        """

        assert isinstance(fIphic, float)
        assert isinstance(fIfck, float)
        assert isinstance(fIfctk, float)
        assert isinstance(fId, float)
        assert fId > 0
        assert isinstance(fIrhoIy, float)
        assert fIrhoIy >= 0
        assert isinstance(fIrhoIz, float)
        assert fIrhoIz >= 0
        assert isinstance(fINuy, float)
        assert isinstance(fINuz, float)
        assert isinstance(fIAcy, float)
        assert fIAcy != 0
        assert isinstance(fIAcz, float)
        assert fIAcz != 0

        fOfny = fINuy / fIAcy
        fOfnz = fINuz / fIAcz
        fOfn = (fOfny + fOfnz)/2
        fOk = 1 + (200 / fId)**0.5
        fOrhol = (fIrhoIy * fIrhoIz)**0.5
        fOVcd = 0.85 * fIphic * fOk * (100 * fOrhol * fIfck)**(1/3) + 0.1 * fOfn

        if fOk <= 2.0 and fOrhol <= 0.02 and fOVcd >= 0.4 * fIphic * fIfctk + 0.1 * fOfn :
          return RuleUnitResult(
              result_variables = {
                  "fOVcd": fOVcd,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )