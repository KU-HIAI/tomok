import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04050407_05 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.5.4.7 (5)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최대 지름 12mm의 용접된 횡철근의 정착력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.5 철근 상세
    4.5.4 철근의 정착
    4.5.4.7 용접철근에 의한 정착
    (5)
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
    A["용접의 설계전단강도"];
    B["KDS 24 14 21 4.5.4.7 (5)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 공칭지름/];
		VarIn2[/입력변수: 철근의 설계항복강도/];
		VarIn3[/입력변수: 최대 지름/];
		VarIn4[/입력변수: 횡방향 철근의 지름/];
		VarIn5[/입력변수: 정착철근의 지름/];


		VarOut1[/출력변수: 용접의 설계전단강도/];

		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		VarIn2~~~VarIn4 & VarIn5

		end
		Python_Class ~~~ Variable_def--->C--->D--->E--->F

		C{"<img src='https://latex.codecogs.com/svg.image?f_{yd}=500MPa'>---------------------------------"}
		D{"최대 지름=12mm"}

		E["<img src='https://latex.codecogs.com/svg.image?F_{btd}=F_{wd}\leq&space;12A_sf_{cd}d_{b,t}/d_b'>---------------------------------"]
		F(["용접의 설계전단강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Anchorage_capacity_of_welded_transverse_bars_up_to_12mm_in_diameter(fInomdia,fIfcd,fImaxdia,fIAs,fOFwd,fIdbt,fIdb) -> float:
        """최대 지름 12mm의 용접된 횡철근의 정착력

        Args:
            fInomdia (float): 공칭지름
            fIfcd (float): 콘크리트 설계압축강도
            fImaxdia (float): 최대 지름
            fIAs (float): 철근 단면적
            fOFwd (float): 용접의 설계전단강도
            fIdbt (float): 횡방향 철근의 지름
            fIdb (float): 정착철근의 지름

        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.5.4.7 용접철근에 의한 정착 (5)의 값
        """

        if fIdbt <= 12 and fIdb <= 12:
          fOFwd = min(fOFwd, 12*fIAs*fIfcd*fIdbt/fIdb)
          return fOFwd
        else:
          return "Fail"


# 

