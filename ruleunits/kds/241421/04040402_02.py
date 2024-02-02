import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04040402_02 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Sunjae Lee'  # 작성자명
    ref_code = 'KDS 24 14 21 4.4.4.2 (2)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-11-14'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '최소피복두께'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.4 내구성 및 피복두께
    4.4.4 콘크리트 피복두께
    4.4.4.2 최소피복두께
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
    A["최소피복두께"];
    B["KDS 24 14 21 4.4.4.2 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 부착에 대한 요구사항을 만족하는 최소피복두께/];
		VarIn2[/입력변수: 환경조건에 대한 요구사항을 만족하는 최소피복두께/];
		VarIn3[/입력변수: 고부식성 노출환경에서 피복두께 증가값/];
		VarIn4[/입력변수: 스테인레스 철근을 사용할 때 피복두께 감소값/];
		VarIn5[/입력변수: 코팅과 같은 추가 보호 조치를 취한 경우 피복두께 감소값/];

		VarOut1[/출력변수: 최소피복두께/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3
		 VarIn2~~~VarIn4 & VarIn5

		end
		Python_Class ~~~ Variable_def--->C--->F
		C["<img src='https://latex.codecogs.com/svg.image?t_{c,min}=max[{t_{c,min,b},t_{c,min,dur}&plus;\Delta&space;t_{c,dur.\gamma}-\Delta&space;t_{c,dur,st}-\Delta&space;t_{c,dur,add},10mm}]'>---------------------------------"]

		F(["최소피복두께"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def minimum_cover_thickness(fOtcmin,fItcminb,fItcmidu,fIdtcdug,fIdtcdus,fIdtcdua) -> float:
        """최소피복두께

        Args:
             fOtcmin (float): 최소피복두께
             fItcminb (float): 부착에 대한 요구사항을 만족하는 최소피복두께
             fItcmidu (float): 환경조건에 대한 요구사항을 만족하는 최소피복두께
             fIdtcdug (float): 고부식성 노출환경에서 피복두께 증가값
             fIdtcdus (float): 스테인레스 철근을 사용할 때 피복두께 감소값
             fIdtcdua (float): 코팅과 같은 추가 보호 조치를 취한 경우 피복두께 감소값


        Returns:
            float: 콘크리트교 설계기준 (한계상태설계법) 4.4.4.2 일반 사항 (2)의 값
        """

        fOtcmin = max(fItcminb, fItcmidu+fIdtcdug-fIdtcdus-fIdtcdua, 10)
        return fOtcmin


# 

