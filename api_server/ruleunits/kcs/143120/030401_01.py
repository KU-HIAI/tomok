import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030401_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.4.1 (1)'
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
    ② 경도시험에 있어서 예열하지 않고 최고 경도(H_{v})가 370을 초과 할 때
    ③ 모재의 표면온도가 0℃ 이하일 때
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 예열에 관한 일반사항];
    B["KCS 14 31 20 3.4.1 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.4.1 (1)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/출력변수: 예열에 관한 일반사항/];
    VarOut2[/출력변수: 탄소당량/];
		VarIn1[/입력변수: 강재의 밀시트/]
    VarIn2[/입력변수: 탄소/];
    VarIn3[/입력변수: 망간/];
    VarIn4[/입력변수: 규소/];
    VarIn5[/입력변수: 니켈/];
    VarIn6[/입력변수: 크로뮴/];
    VarIn7[/입력변수: 몰리브덴/];
    VarIn8[/입력변수: 바나듐/];
    VarIn9[/입력변수: 구리/];
		VarOut1 &  VarOut2 & VarIn1 & VarIn2 & VarIn3 & VarIn4 ~~~  VarIn7
		end
		subgraph V2
    VarOut3[/출력변수: 예열에 관한 일반사항/];
		VarIn10[/입력변수: 경도시험/]
    VarIn11[/입력변수: 예열/];
    VarIn12[/입력변수: 최고 경도/];
		end
		subgraph V3
    VarOut4[/출력변수: 예열에 관한 일반사항/];
		VarIn13[/입력변수: 모재의 표면온도/]
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
		Variable_def --> C{"강재의 밀시트 \n 경도시험 \n 모재의 표면온도"}
		C --> |강재의 밀시트|D{"구리 ≥ 0.5 % "}
		D --> |True|E["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{eq} = C+\frac{Mn}{6}+\frac{Si}{24}+\frac{Ni}{40}+\frac{Cr}{5}+\frac{Mo}{4}+\frac{V}{14}+\frac{Cu}{13}'>---------------------------------------------------------------------"]
		D --> |False|F["<img src='https://latex.codecogs.com/png.image?\dpi{500}\ C_{eq} = C+\frac{Mn}{6}+\frac{Si}{24}+\frac{Ni}{40}+\frac{Cr}{5}+\frac{Mo}{4}+\frac{V}{14}'>--------------------------------------------------------------"]
		E & F --> |"> 0.44%"|G[예열을 해야 한다.]
		C --> |경도시험|H{"예열 \n 최고경도 ≤ 370"}
		H --> |False|I[예열을 해야 한다.]
		C --> |모재의 표면온도|J{"모재의 표면온도 ≤ 0℃"}
		J --> |True|K[예열을 해야 한다.]
		G & I & K --> End([ 예열에 관한 일반사항])
    """

    @rule_method
    def Mill_Sheet_of_Steel(bIMilShi, fICarbon, fIMangan, fISilico, fINickel, fIChromi, fIMolybd, fIVanadi, fICopper, bIHarTes, bIPre, fIMaxHar, fISurMet) -> RuleUnitResult:
        """ 플럭스 건조
        Args:
        bIMilShi (bool): 강재의 밀시트
        bIHarTes (bool): 경도시험
        fICarbon (float): 카본
        fIMangan (float): 망간
        fISilico (float): 규소
        fINickel (float): 니켈
        fIChromi (float): 크로뮴
        fIMolybd (float): 몰리브덴
        fIVanadi (float): 바나듐
        fICopper (float): 구리
        bIPre (bool): 예열
        fIMaxHar (float): 최고 경도
        fISurMet (float): 모재의 표면온도

        Returns:
        sOGenPre (str): 예열에 관한 일반사항
        fOCarEqu (float): 탄소당량
        """
        assert isinstance(bIMilShi, bool)
        assert isinstance(bIHarTes, bool)
        assert isinstance(fICarbon, float)
        assert isinstance(fIMangan, float)
        assert isinstance(fISilico, float)
        assert isinstance(fINickel, float)
        assert isinstance(fIChromi, float)
        assert isinstance(fIMolybd, float)
        assert isinstance(fIVanadi, float)
        assert isinstance(fICopper, float)
        assert isinstance(bIPre, bool)
        assert isinstance(fIMaxHar, float)
        assert isinstance(fISurMet, float)

        if bIMilShi == True and bIHarTes == False:
          if fICarbon + (fIMangan / 6) + (fISilico / 24) + (fINickel /40) + (fIChromi / 5) + (fIMolybd / 4) + (fIVanadi / 14) + (fICopper / 13) > 0.0044:
            sOGenPre = "예열을 해야한다"
            fOCarEqu = fICarbon + (fIMangan / 6) + (fISilico / 24) + (fINickel /40) + (fIChromi / 5) + (fIMolybd / 4) + (fIVanadi / 14) + (fICopper / 13)
          else:
            sOGenPre = "예열을 하지 않아도 된다"
            fOCarEqu = None
        elif bIMilShi == False and bIHarTes == True:
          if bIPre == False:
            if fIMaxHar > 370:
              sOGenPre = "예열을 해야한다"
              fOCarEqu = None
            else:
              sOGenPre = "예열을 하지 않아도 된다"
              fOCarEqu = None
        elif bIMilShi == False and bIHarTes == False:
          if fISurMet <= 0:
            sOGenPre = "예열을 해야한다"
            fOCarEqu = None
          else:
            sOGenPre = "예열을 하지 않아도 된다"
            fOCarEqu = None
        else:
          sOGenPre = "예열을 하지 않아도 된다"
          fOCarEqu = None

        return RuleUnitResult(
                result_variables = {
                    "sOGenPre": sOGenPre,
                    "fOCarEqu": fOCarEqu,
                }
            )