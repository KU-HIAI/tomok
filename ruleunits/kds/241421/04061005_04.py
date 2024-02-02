import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from tomok.core.rule_unit import RuleUnit
from tomok.core.decorator import rule_method

import math
from typing import List

class KDS241421_04061005_04 (RuleUnit):

    # 아래 클래스 멤버 변수에 할당되는 값들을 작성하는 룰에 맞게 수정
    priority = 1   # 건설기준 우선순위
    author = 'Jiwoo Won'  # 작성자명
    ref_code = 'KDS 24 14 21 4.6.10.5 (4)' # 건설기준문서
    ref_date = '2021-04-12'  # 디지털 건설문서 작성일
    doc_date = '2023-12-20'  # 건설기준문서->디지털 건설기준 변환 기준일
    title = '현장 타설 말뚝의 축방향 철근 배치'    # 건설기준명

    #
    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.6 부재 상세
    4.6.10 기초판
    4.6.10.5 현장 타설 말뚝
    (4)
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
    A["쪼갬력"];
    B["KDS 24 14 21 4.6.10.4 (2)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수:쪼갬력/];
		VarIn2[/입력변수:단면의 압축 연단에서 중립축까지 깊이/];
		VarIn3[/입력변수:부재의 전체 깊이/];
		VarIn4[/입력변수:계수하중에 의한 축력값/];

		VarOut1[/출력변수:쪼갬력/];
		VarOut1~~~VarIn1 & VarIn2 & VarIn3 & VarIn4


		end

		Python_Class ~~~ Variable_def
		Variable_def--->E--->D--->F


		E["h=min(b,H)"]
		D["<img src='https://latex.codecogs.com/svg.image?\inline&space;\LARGE&space;F_s=0.25(1-c/h)N_u'>---------------------------------"]



		F(["쪼갬력"])
    """

    # 작성하는 룰에 맞게 함수 이름과 내용을 수정,
    @rule_method
    def rebar_arrange(fImindaxr,fIaxireb,fIinsgbr,fIAc,fIAs) ->bool:
        """현장 타설 말뚝의 축방향 철근 배치
        Args:
             fImindaxr (float): 축방향 철근의 최소 지름
             fIaxireb (float): 축방향 철근
             fIinsgbr (float): 철근 사이의 순간격
             fIAc (float): 콘크리트 단면적
             fIAs (float): 인장 철근 단면적

        Returns:
            bool: 콘크리트교 설계기준 (한계상태설계법) 4.6.10.5 (4)의 현장 타설 말뚝의 축방향 철근 배치
        """
        if fIAc<=0.5:
          if fImindaxr>=16 and fIaxireb>=6 and fIinsgbr<=200 and fIAs>=0.005*fIAc:
            return "Pass"
          else:
            return "Fail"
        elif 0.5<fIAc<=1.0:
          if fImindaxr>=16 and fIaxireb>=6 and fIinsgbr<=200 and fIAs>=25:
            return "Pass"
          else:
            return "Fail"
        elif fIAc>1.0:
          if fImindaxr>=16 and fIaxireb>=6 and fIinsgbr<=200 and fIAs>=0.0025*fIAc:
            return "Pass"
          else:
            return "Fail"


# 

