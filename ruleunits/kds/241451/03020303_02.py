import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03020303_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.2.3.3 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-10'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계저항력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.2 확대기초
    3.2.3 극한한계상태의 지지력
    3.2.3.3 활동 파괴
    (2)
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
    A[활동파괴];
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
      Python_Class ~~~ Variable_def;
      Variable_def

			C[기초 아래 흙이 사질토]
			D["<img src='https://latex.codecogs.com/svg.image?&space;Q_{R}=\phi&space;Q_{n}=\phi&space;_{\tau}Q_{\tau}&plus;\phi&space;_{ep}Q_{ep}'>---------------------------------"]
			E["<img src='https://latex.codecogs.com/svg.image?Q_{\tau}=Vtan\delta'>---------------------------------"]
			F["<img src='https://latex.codecogs.com/svg.image?tan\delta=tan\phi&space;_{f}'>---------------------------------"]
			G["<img src='https://latex.codecogs.com/svg.image?tan\delta=0.8tan\phi&space;_{f}'>---------------------------------"]
			H[현장타설 콘크리트 기초]
			I[프리캐스트 콘크리트 기초]
			J([활동파괴에 대한 설계저항력])

			Variable_def ---> C ---> H & I
			H ---> F
			I ---> G
			F & G ---> E
			E ---> D ---> J
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_Resistance(fICoeres,fISQtau,fIResman,fIResstr,fIAngsoi,fIV,fIuserdefined) -> float:
        """설계저항력
        Args:
            fOQr (float): 설계저항력
            fICoeres (float): 흙과 기초 사이의 전단저항에 대한 저항계수
            fISQtau (float): 흙과 기초 사이의 공칭 전단저항력
            fIResman (float): 수동저항에 대한 저항계수
            fIResstr (float): 구조물의 총 설계 수명에 대한 흙의 공칭수동저항력
            fIAngsoi (float): 흙의 내부마찰각
            fIV (float): 총연직력
            fIuserdefined (float): 사용자 선택


        Returns:
            float: 교량 하부구조 설계기준 (한계상태설계법) 3.2.3.3 (2)의 설계저항력 값
        """
        import math
        if  fIuserdefined == 1: #기초 아래 흙이 사질토, 현장타설 콘크리트 기초
          fISQtau = fIV * math.tan(math.radians(fIAngsoi))
          fOQr = fICoeres * fISQtau + fIResman * fIResstr
          return fOQr
        elif  fIuserdefined == 2: #기초 아래 흙이 사질토, 프리캐스트 콘크리트 기초
          fISQtau = fIV * 0.8 * math.tan(math.radians(fIAngsoi))
          fOQr = fICoeres * fISQtau + fIResman * fIResstr
          return fOQr
        elif  fIuserdefined == 3: #기초 아래 흙이 사질토가 아닌 경우
          fOQr = fICoeres * fISQtau + fIResman * fIResstr
          return fOQr


# 

