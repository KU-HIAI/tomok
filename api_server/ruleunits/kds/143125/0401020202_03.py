import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143125_0401020202_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 25 4.1.2.2.2 (3)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-23'
    title = '필릿용접의 최소길이 및 유효용접치수'

    description = """
    강구조 연결 설계기준(하중저항계수설계법)
    4. 설계
    4.1 공통사항
    4.1.2 용접
    4.1.2.2 필릿용접
    4.1.2.2.2 제한사항
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
    A[Title: 필릿용접의 최소길이 및 유효용접치수]
    B["KDS 14 31 25 4.1.2.2.2 (3)"]
  	A ~~~ B
  	end

	  subgraph Variable_def
	  VarOut1[/출력변수: 필릿용접의 최소길이/]
  	VarOut2[/출력변수: 유효용접치수/]
	  VarIn1[/입력변수: 공칭용접치수/]
  	VarIn2[/입력변수: 유효길이/]
	  VarOut1 ~~~ VarIn1
  	VarOut2 ~~~ VarIn2
  	end

		Python_Class ~~~ C(["KDS 14 31 25 4.1.2.2.2 (3)"])
		C --> Variable_def

	  Variable_def --> D & E
  	D-->F
	  E-->G
  	D["필릿용접의 최소길이≥ 공칭용접치수x4"]
	  E["유효용접치수≤ 유효길이 x 1/4"]
	  F([필릿용접의 최소길이])
    G([유효용접치수])
    """

    @rule_method
    def minumium_length_of_fillet_weld_nd_effective_welding_dimension(fImilefw,fIefwedi,fInowedi,fIefflen) -> RuleUnitResult:
        """필릿용접의 최소길이 및 유효용접치수

        Args:
            fImilefw (float): 필릿용접의 최소길이
            fIefwedi (float): 유효용접치수
            fInowedi (float): 공칭용접치수
            fIefflen (float): 유효길이

        Returns:
            pass_fail (bool): 강구조 연결 설계기준(하중저항계수설계법)   4.1.2.2.2 제한사항 (3)의 판단 결과
        """

        assert isinstance(fImilefw, float)
        assert isinstance(fIefwedi, float)
        assert isinstance(fInowedi, float)
        assert isinstance(fIefflen, float)


        if fImilefw >= 4*fInowedi and fIefwedi <= fIefflen/4 :
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )