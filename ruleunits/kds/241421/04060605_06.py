import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04060605_06 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanhyuk Kim'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.6.5 (6)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '압축부재의 띠철근'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.6 기둥
    4.6.6.5 띠철근 상세
    (6)
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
    A["띠철근 상세"];
    B["KDS 24 14 21 4.6.6.5 (6)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:최하단 띠철근/];
		VarIn2[/입력변수:상부로부터 띠철근 간격/];
		VarIn3[/입력변수:최상단 띠철근/];
		VarIn4[/입력변수:최하단 수평철근으로부터 띠철근 간격/];



		VarIn1 & VarIn2 & VarIn3 & VarIn4
		end

		Python_Class ~~~ Variable_def
		Variable_def--->C & F

		C["최하단 띠철근<상부로부터 띠철근 간격X1/2"]
		F["최상단 띠철근<최하단 수평철근으로부터 띠철근 간격X1/2"]
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def bottom_tie(fIbottie, fIstspto, fItopreb, fIstbsbh) ->bool:
        """나선철근의 순간격
        Args:
             fIbottie (float): 최하단 띠철근
             fIstspto (float): 상부로부터 띠철근 간격
             fItopreb (float): 최상단 띠철근
             fIstbsbh (float): 최하단 수평철근으로부터 띠철근 간격
        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.6.5 (6) 설계기준에 따른 압축부재의 띠철근 적합여부
        """
        if fIbottie < fIstspto/2 and fItopreb < fIstbsbh/2:
          return "Pass"
        else:
          return "Fail"


# 

