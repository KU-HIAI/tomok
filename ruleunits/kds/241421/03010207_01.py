import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_03010207_01 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Chanwoo Yang'  # 작성자명
    ref_code = 'KDS 24 14 21 3.1.2.7 (1)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-28'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '증기양생한 콘크리트의 강도'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.1 콘크리트
    3.1.2 재료특성
    3.1.2.7 증기양생한 콘크리트 재료
    (1) 강도
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
    A["t일의 콘크리트 압축강도"];
    B["KDS 24 14 21 3.1.2.7 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 강도 보정 계수/];
		VarIn2[/입력변수: 증기양생 후 평균압축강도/];
    VarIn3[/입력변수: 콘크리트 압축강도의 평균값/] ;
    VarIn4[/입력변수: 증기양생을 수행한 시간/] ;
		VarOut1[/출력변수: t일의 콘크리트 압축강도/];
		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4
		end
		Python_Class ~~~ Variable_def;
		Variable_def--->C--->F

		C["<img src='https://latex.codecogs.com/svg.image?f_{cm}(t)=f_{cmp}&plus;\frac{f_{cm}-f{cmp}}{log(28-t_{p}&plus;1)}log(t-t_{p}&plus;1)'>---------------------------------"]
		F(["t일의 콘크리트 압축강도"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def Concrete_compressive_strength_at_day_t(fOfcmt,fIbetacct,fIfcmp,fIfcm,fItp) -> float:
        """증기양생한 콘크리트의 강도

        Args:
             fOfcmt (float): t일의 콘크리트 압축강도
             fIbetacct (float): 강도 보정 계수
             fIfcmp (float): 증기양생 후 평균압축강도
             fIfcm (float): 콘크리트 압축강도의 평균값
             fItp (float): 증기양생을 수행한 시간
             fIt (float): 온도에 따라 조정한 콘크리트 재령


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 3.1.2.7 증기양생한 콘크리트 재료 (1) 강도의 값
        """

        fOfcmt = min(fIfcm*fIbetacct, fIfcmp + (fIfcm-fIfcmp)/(math.log10(28-fItp+1))*math.log10(fIt-fItp+1))
        return fOfcmt


# 

