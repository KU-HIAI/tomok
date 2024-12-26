import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030401_01_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.4.1 (1) ①'
    ref_date = '2019-05-20'
    doc_date = '2023-11-10'
    title = '예열에 관한 일반사항'

    description = """
    용접
    3. 시공
    3.4 예열
    3.4.1 예열에 관한 일반사항
    """

    content = """
    #### 3.4.1 예열에 관한 일반사항
    (1) 다음의 경우는 예열을 해야 한다.
    ① 강재의 밀시트에서 다음 식 (3.4-1)에 따라서 계산한 탄소당량, C_{e q}가 0.44%를 초과 할 때
    C_{e q}=\mathrm{C}+\frac{\mathrm{Mn}}{6}+\frac{\mathrm{Si}}{24}+\frac{\mathrm{Ni}}{40}+\frac{\mathrm{Cr}}{5}+\frac{\mathrm{Mo}}{4}+\frac{\mathrm{V}}{14}+\left(\frac{\mathrm{Cu}}{13}\right)(\%) (3.4-1)
    다만, ()항은 Cu >= 0.5%일 때에 더한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예열에 관한 일반사항];
    B["KCS 14 31 20 3.4.1 (1) ①"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.4.1 (1) ①"])

    subgraph Variable_def
    VarIn1[/입력변수: 탄소/];
    VarIn2[/입력변수: 망간/];
    VarIn3[/입력변수: 규소/];
    VarIn4[/입력변수: 니켈/];
    VarIn5[/입력변수: 크로뮴/];
    VarIn6[/입력변수: 몰리브덴/];
    VarIn7[/입력변수: 바나듐/];
    VarIn8[/입력변수: 구리/];
    VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~ VarIn5
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"구리 ≥ 0.5 % "}
		C --> |True|E["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{eq} = C+\frac{Mn}{6}+\frac{Si}{24}+\frac{Ni}{40}+\frac{Cr}{5}+\frac{Mo}{4}+\frac{V}{14}+\frac{Cu}{13}'>---------------------------------------------------------------------"]
		C --> |False|F["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{eq} = C+\frac{Mn}{6}+\frac{Si}{24}+\frac{Ni}{40}+\frac{Cr}{5}+\frac{Mo}{4}+\frac{V}{14}'>--------------------------------------------------------------"]
		E & F --> |"> 0.44%"|G([Pass or Fail])
    """

    @rule_method
    def General_About_Preheating(fICarbon, fIMangan, fISilico, fINickel, fIChromi, fIMolybd, fIVanadi, fICopper) -> RuleUnitResult:
        """ 예열에 관한 일반사항
        Args:
        fICarbon (float): 카본
        fIMangan (float): 망간
        fISilico (float): 규소
        fINickel (float): 니켈
        fIChromi (float): 크로뮴
        fIMolybd (float): 몰리브덴
        fIVanadi (float): 바나듐
        fICopper (float): 구리

        Returns:
        pass_fail (bool): 용접 3.4.1 예열에 관한 일반사항 (1) ①의 판단 결과
        """
        assert isinstance(fICarbon, float)
        assert isinstance(fIMangan, float)
        assert isinstance(fISilico, float)
        assert isinstance(fINickel, float)
        assert isinstance(fIChromi, float)
        assert isinstance(fIMolybd, float)
        assert isinstance(fIVanadi, float)
        assert isinstance(fICopper, float)

        if fICopper >= 0.05 :
          if fICarbon + (fIMangan / 6) + (fISilico / 24) + (fINickel /40) + (fIChromi / 5) + (fIMolybd / 4) + (fIVanadi / 14) + (fICopper / 13) > 0.0044:
            pass_fail = True
          else:
            pass_fail = False
        else:
          if fICarbon + (fIMangan / 6) + (fISilico / 24) + (fINickel /40) + (fIChromi / 5) + (fIMolybd / 4) + (fIVanadi / 14) > 0.0044:
            pass_fail = True
          else:
            pass_fail = False

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail
                }
            )