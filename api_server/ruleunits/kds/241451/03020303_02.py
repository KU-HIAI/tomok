import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03020303_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.2.3.3 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '설계저항력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.3 활동 파괴
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 활동파괴];
    B["KDS 24 14 51 3.2.3.3 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수: 설계저항력/];
		VarOut2[/출력변수: 설계저항력/];
		VarIn1[/입력변수: 흙과 기초 사이의 전단저항에 대한 저항계수/];
		VarIn2[/입력변수: 흙과 기초 사이의 공칭전단/];
		VarIn3[/입력변수: 수동저항에 대한 저항계수/];
		VarIn4[/입력변수: 구조무의 총 설계 수명에 대한 흙의 공칭수동저항력/];
		VarIn5[/입력변수: 흙의 내부마찰각/];
		VarIn6[/입력변수: 총연직력/];

		VarOut1 ~~~ VarOut2
		VarIn1 ~~~ VarIn2 ~~~ VarIn3
		VarIn4 ~~~ VarIn5 ~~~ VarIn6

    end
    Python_Class ~~~ C(["KDS 24 14 51 3.2.3.3 (2)"])
		C --> Variable_def;

		K[기초 아래 흙이 사질토]
		D["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{\tau}Q_{\tau}&plus;\phi&space;_{ep}Q_{ep}'>---------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?Q_{\tau}=Vtan\delta'>---------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?tan\delta=tan\phi&space;_{f}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?tan\delta=0.8tan\phi&space;_{f}'>---------------------------------"]
		H[현장타설 콘크리트 기초]
		I[프리캐스트 콘크리트 기초]
		J([활동파괴에 대한 설계저항력])

		Variable_def ---> K ---> H & I
		H ---> F
		I ---> G
		F & G ---> E
		E ---> D ---> J
    """

    @rule_method
    def Design_Resistance(fICoeres,fISQtau,fIResman,fIResstr,fIAngsoi,fIV,fIlacscA,fIlacscB,fIlacscC) -> RuleUnitResult:
        """설계저항력

        Args:
            fICoeres (float): 흙과 기초 사이의 전단저항에 대한 저항계수
            fISQtau (float): 흙과 기초 사이의 공칭 전단저항력
            fIResman (float): 수동저항에 대한 저항계수
            fIResstr (float): 구조물의 총 설계 수명에 대한 흙의 공칭수동저항력
            fIAngsoi (float): 흙의 내부마찰각
            fIV (float): 총연직력
            fIlacscA (float): 흙과 기초 사이의 공칭 전단저항력 (기초 아래 흙이 사질토, 현장타설 콘크리트 기초)
            fIlacscB (float): 흙과 기초 사이의 공칭 전단저항력 (기초 아래 흙이 사질토, 프리캐스트 콘크리트 기초)
            fIlacscC (float): 흙과 기초 사이의 공칭 전단저항력 (기초 아래 흙이 사질토가 아닌 경우)

        Returns:
            fOQr (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 (2)의 값 1
            fOSQtau (float): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 (2)의 값 2
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 (2)의 판단 결과
        """

        assert isinstance(fICoeres, float)
        assert isinstance(fISQtau, float)
        assert isinstance(fIResman, float)
        assert isinstance(fIResstr, float)
        assert isinstance(fIAngsoi, float)
        assert isinstance(fIV, float)
        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)
        assert isinstance(fIlacscC, float)

        import math

        if fIlacscA != 0 and fIlacscB == 0 and fIlacscC == 0 :
          fOSQtau = fIV * math.tan(math.radians(fIAngsoi))
          fOQr = fICoeres * fOSQtau + fIResman * fIResstr
          return RuleUnitResult(
              result_variables = {
                  "fOQr": fOQr,
                  }
              )
        elif fIlacscA == 0 and fIlacscB != 0 and fIlacscC == 0 :
          fOSQtau = fIV * 0.8 * math.tan(math.radians(fIAngsoi))
          fOQr = fICoeres * fOSQtau + fIResman * fIResstr
          return RuleUnitResult(
              result_variables = {
                  "fOQr": fOQr,
                  }
              )
        elif fIlacscA != 0 and fIlacscB == 0 and fIlacscC != 0 :
          fOQr = fICoeres * fISQtau + fIResman * fIResstr
          return RuleUnitResult(
              result_variables = {
                  "fOQr": fOQr,
                  }
              )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )