import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS249011_04030306 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seohyun Jin'  # 작성자명
    ref_code = 'KDS 24 90 11 4.3.3.6' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-10-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '지진격리받침에 작용하는 부반력에 의한 인장응력'    # 건설기준명

    #
    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.3 적층고무형 지진격리받침
    4.3.3 설계 요구조건
    4.3.3.6 부반력으로 인한 안정성 검토
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
    A[최대압축응력];
    B["KDS 24 90 11 4.3.3.5"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 전단력/];
		VarIn2[/입력변수: 자가격리받침면적/];
		VarIn3[/입력변수: 허용인장응력/];
		VarOut1[/출력변수: 지진격리받침에 작용하는 부반력에 의한 인장응력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def;
		Variable_def-->D--->E
		D["<img src='https://latex.codecogs.com/svg.image?\sigma&space;_{t}=\frac{V}{A}\leq\sigma&space;_{te}'>--------------------------------------------------------"];
		D~~~ |"Table 24 90 11 4.3-3"| D
		E(["Pass or Fail"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Tensile_Stresses_Due_To_Negative_Reaction_Forces_Acting_On_Seismic_Isolation_Bracing(fIsigmat,fIV,fIAe,fIsigmate) -> bool:
        """지진격리받침에 작용하는 부반력에 의한 인장응력

        Args:
            fIsigmat (float): 지진격리받침에 작용하는 부반력에 의한 인장응력
            fIV (float): 전단력
            fIAe (float): 자가격리받침면적
            fIsigmate (float): 허용인장응력

        Returns:
            bool: 교량 기타시설설계기준 (한계상태설계법)  4.3.3.6 부반력으로 인한 안정성 검토의 통과 여부
        """

        if fIV/fIAe <= fIsigmate :
           return "Pass"
        else:
           return "Fail"


# 

