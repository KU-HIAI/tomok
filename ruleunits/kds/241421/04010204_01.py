import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04010204_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 4.1.2.4 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-05'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '플랜지 내민부와 복부 사이 계면 전단에서 종방향 전단응력'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.2 전단
    4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단
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
    A["종방향 전단응력"];
    B["KDS 24 14 21 4.1.2.4 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 구간 Δx에서 플랜지 단면에 작용하는 종방향력의차이/];
		VarIn2[/입력변수: 계면에서 플랜지의 두께/];
		VarIn3[/입력변수: 검토하는 구간 길이/];
		VarOut1[/출력변수: 종방향 전단응력/];
		VarOut1~~~~VarIn1 & VarIn2 & VarIn3

		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->D
		C["<img src='https://latex.codecogs.com/svg.image?v&space;_{uf}=\frac{\Delta&space;C}{t_{f}\Delta&space;x}'>---------------------------------"]
		D(["종방향 전단응력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Longitudinal_shear_stress(fOvuf,fIdeltaC,fIdeltax,fItf) -> float:
        """플랜지 내민부와 복부 사이 계면 전단에서 종방향 전단응력

        Args:
             fOvuf (float): 종방향 전단응력
             fIdeltaC (float): 구간 Δx에서 플랜지 단면에 작용하는 종방향력의차이
             fIdeltax (float): 계면에서 플랜지의 두께
             fItf (float): 검토하는 구간 길이



        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.1.2.4 T형 단면 부재의 플랜지와 복부 사이 계면 전단 (1)의 값
        """

        fOvuf = fIdeltaC/fItf/fIdeltax*1000
        return fOvuf


# 

