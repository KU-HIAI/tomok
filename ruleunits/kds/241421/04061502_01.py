import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04061502_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Seonghan Yoon'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.15.2 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '건조수축 및 온도변화에 대한 보강'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.15 건조수축 및 온도 철근
    4.6.15.2 두께 1200mm 이하인 부재
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
    A["기둥 또는 벽체에 연결된 수평타이"];
    B["KDS 24 14 21 4.6.14.2 (4)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:타이의 작용인장력/];
		VarIn2[/입력변수:부재의 총 단면적/];
		VarIn3[/입력변수:철근의 설계기준항복강도/];

		VarIn1 & VarIn2 & VarIn3

		end

		Python_Class ~~~ Variable_def
		Variable_def--->E

		E["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;A_s\geq&space;0.75A_g/f_{yd}'>---------------------------------"]
		E ---> G(["Pass or Fail"])

    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def cross_sectional_area(fIAs,fIAg,fIfyd) -> bool:
        """건조수축 및 온도변화에 대한 보강

        Args:
             fIAs (float): 단면적
             fIAg (float): 부재의 총 단면적
             fIfyd (float): 철근의 설계기준항복강도

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.15.2 두께 1200mm 이하인 부재 (1)의 통과여부
        """

        if fIAs >= 0.75*fIAg/fIfyd:
          return 'Pass'

        else:
          return 'Fail'


# 

# 

