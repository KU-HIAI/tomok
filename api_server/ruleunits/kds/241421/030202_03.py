import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_030202_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 3.2.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '철근의 기준항복강도와 인장강도'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    3. 재료
    3.2 철근
    3.2.2 재료특성
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 철근의 기준항복강도와 인장강도];
    B["KDS 24 14 21 3.2.2. (3)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수: 항복하중의 기준값/];
		VarIn2[/입력변수: 직접 1축 인장의 최대하중/];
    VarIn3[/입력변수: 공칭단면적/] ;
    VarIn4[/입력변수: 실제 시험을 통하여 얻어지는 항복응력/] ;
		VarOut1[/출력변수: 철근의 기준항복강도/];
		VarOut2[/출력변수: 인장강도/];
		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2 & VarIn3 & VarIn4

		end

	  Python_Class ~~~ C(["KDS 24 14 21 3.2.2. (3)"])
		C --> Variable_def

		Variable_def--->H & D
		H--->E
		H["철근의 기준항복강도=항복하중의 기준값/공칭단면적"]
		D["인장강도=직접 1축 인장의 최대하중/공칭단면적"]
		E["실제 시험을 통하여 얻어지는 항복응력≤기준항복강도x1.3"]
		F(["철근의 기준항복강도"])
		G(["인장강도"])
		E--->F
		D--->G
    """

    @rule_method
    def standard_yield_strength_and_tensile_strength_of_rebar(fIstavay,fImaxlot,fInomcsn,fIyisota) -> RuleUnitResult:
        """철근의 기준항복강도와 인장강도

        Args:
            fIstavay (float): 항복하중의 기준값
            fImaxlot (float): 직접 1축 인장의 최대하중
            fInomcsn (float): 공칭단면적
            fIyisota (float): 실제 시험을 통하여 얻어지는 항복 응력

        Returns:
            fOfy (float): 콘크리트교 설계기준(한계상태설계법)  3.2.2 재료특성 (3)의 값 1
            fOfu (float): 콘크리트교 설계기준(한계상태설계법)  3.2.2 재료특성 (3)의 값 2
            pass_fail (bool): 콘크리트교 설계기준(한계상태설계법)  3.2.2 재료특성 (3)의 판단 결과
        """

        assert isinstance(fIstavay, float)
        assert isinstance(fImaxlot, float)
        assert isinstance(fInomcsn, float)
        assert fInomcsn != 0
        assert isinstance(fIyisota, float)

        fOfy = fIstavay/fInomcsn
        fOfu = fImaxlot/fInomcsn

        if fIyisota <= 1.3 * fOfy :
          return RuleUnitResult(
              result_variables = {
                  "fOfy": fOfy,
                  "fOfu": fOfu,
                  "pass_fail": True,
              }
          )
        else:
          return RuleUnitResult(
              result_variables = {
                  "fOfy": fOfy,
                  "fOfu": fOfu,
                  "pass_fail": False,
              }
          )