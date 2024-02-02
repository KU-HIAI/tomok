import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241451_03030116_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 51 3.3.1.16 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-30'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '설계지지력'    # 건설기준명

    #
    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.1 일반사항
    3.3.1.16 최대 허용항타하중
    (1)
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
    A[최대허용항타하중];
    B["KDS 24 14 51 3.3.1.16 (1)"];
    A ~~~ B
    end

      subgraph Variable_def;
			VarOut1[/출변수: 설계지지력/];
			VarIn1[/입력변수: 강도 저항계수/];
			VarIn2[/입력변수: 강재의 항복강도/];
			VarIn3[/입력변수: 부재의 총단면적/];
			VarIn4[/입력변수: 강도 저항계수/];
			VarIn5[/입력변수: 강재의 항복강도/];
			VarIn6[/입력변수: 부재의 순단면적/];

			VarOut1
			VarIn1 ~~~ VarIn2 ~~~	VarIn3
			VarIn4 ~~~ VarIn5 ~~~	VarIn6

      end
      Python_Class ~~~ Variable_def;
      Variable_def
			C[강재말뚝]
			D[압축]
			E[인장]
			F["<img src='https://latex.codecogs.com/svg.image?0.90\phi&space;F_{y}A_{g}'>---------------------------------"]
			G["<img src='https://latex.codecogs.com/svg.image?0.90\phi&space;F_{y}A_{n}'>---------------------------------"]
			I([Pass or Fail])

			Variable_def ---> C ---> D & E
			D ---> F
			E ---> G
			F & G ---> H(설계지지력) ---> I
			G~~~ |"KDS 24 14 21"| G
			G~~~ |"KDS 24 14 31"| G
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Design_load(fODeslodc,fODeslodt,fItyplod,fIcoefic,fIFyc,fIAg,fIFyt,fIAn) -> bool:
        """설계지지력
        Args:
            fODeslodc (float): 설계지지력
            fODeslodt (float): 설계지지력
            fItyplod (float): 말뚝 상부의 최대 타입하중
            fIcoefic (float): 강도 저항계수
            fIFyc (float): 강재의 항복강도
            fIAg (float): 부재의 총단면적
            fIFyt (float): 강재의 항복강도
            fIAn (float): 부재의 순단면적

        Returns:
            bool: 교량 하부구조 설계기준 (한계상태설계법) 3.3.1.16(1)의 말뚝 상부의 최대 타입하중이 건설기준을 만족하는지 여부

        """

        fODeslodc=0.90*fIcoefic*fIFyc*fIAg
        fODeslodt=0.90*fIcoefic*fIFyt*fIAn
        if fItyplod<=fODeslodc and fItyplod<=fODeslodt:
          return "Pass"
        else:
          return "Fail"


# 

