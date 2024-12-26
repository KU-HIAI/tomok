import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040504020301(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.2.3.1'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '상부 토피하중에 의한 압축력'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.3 설계압축력
    4.5.4.2.3.1 고정하중에 의한 압축력
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 상부 토피하중에 의한 압축력] ;
		B["KDS 14 31 10 4.5.4.2.3.1"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 상부 토피하중에 의한 압축력/] ;
      VarIn1[/입력변수: 뒤채움 흙과 구조물의 상대 축강성 매개변수/] ;
      VarIn2[/입력변수: 뒤채움 흙의 할선탄성계수/] ;
      VarIn3[/입력변수: 구조물 단면의 정점부에서 스프링라인까지 연직거리의 2배/] ;
      VarIn4[/입력변수: 파형강판의 탄성계수/] ;
      VarIn5[/입력변수: 파형강판의 단면적/] ;
      VarIn6[/입력변수: 단면형상과 토피고에 따른 무차원 아칭계수/] ;
      VarIn7[/입력변수: 상부아치 위 뒤채움 흙과 포장의 자중/] ;
			end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6 & VarIn7

		Python_Class ~~~ C1(["KDS 14 31 10 4.5.4.2.3.1"]) -->Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?T_{D}=0.5(1.0-0.1C_{s})A_{f}W>---------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?T_{D}>------"])
    """


    @rule_method
    def Compressive_force_due_to_top_cover_load(fICs,fIEs,fIDv,fIE,fIA,fIAf,fIW) -> RuleUnitResult:
        """상부 토피하중에 의한 압축력

        Args:
            fICs (float): 뒤채움 흙과 구조물의 상대 축강성 매개변수
            fIEs (float): 뒤채움 흙의 할선탄성계수
            fIDv (float): 구조물 단면의 정점부에서 스프링라인까지 연직거리의 2배
            fIE (float): 파형강판의 탄성계수
            fIA (float): 파형강판의 단면적
            fIAf (float): 단면형상과 토피고에 따른 무차원 아칭계수
            fIW (float): 상부아치 위 뒤채움 흙과 포장의 자중

        Returns:
            fOTD (float): 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.3.1 고정하중에 의한 압축력의 값
        """

        assert isinstance(fICs, float)
        assert isinstance(fIEs, float)
        assert isinstance(fIDv, float)
        assert isinstance(fIE, float) and fIE != 0
        assert isinstance(fIA, float) and fIA != 0
        assert isinstance(fIAf, float)
        assert isinstance(fIW, float)


        if fICs != 0:
          fICs = (1000 * fIEs * fIDv) / (fIE * fIA)
        else:
          fICs = fICs

        fOTD = 0.5 * (1.0 - 0.1 * fICs) * fIAf * fIW

        return RuleUnitResult(
            result_variables = {
              "fOTD": fOTD,
            }
         )