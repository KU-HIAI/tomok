import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04070502_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.7.5.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-22'
    title = '현장타설 원형 중공 슬래브교의 치수'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.7 구조 형식에 따른 추가 규정
    4.7.5 슬래브교
    4.7.5.2 현장타설 속빈 슬래브교
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 현장타설 원형 중공 슬래브교의 치수];
    B["KDS 24 14 21 4.7.5.2 (2)"];
    A ~~~ B
    end

	  subgraph Variable_def;
		VarIn1[/입력변수:중공의 중심간 간격/];
		VarIn2[/입력변수:슬래브의 전체 높이/];
		VarIn3[/입력변수:콘크리트의 최소두께/];
		VarIn4[/입력변수:중공의 횡방향 폭/];
		VarIn5[/입력변수:중공 높이/];
		VarIn6[/입력변수:중공 사이의 복부 두께/];
		VarIn7[/입력변수:바닥판 전체 높이/];
		VarIn8[/입력변수:중공 위의 콘크리트 최소두께/];

		VarIn1 & VarIn2 & VarIn3 & VarIn4
		~~~VarIn5 & VarIn6 & VarIn7 & VarIn8
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.7.5.2 (2)"])
		C --> Variable_def

		Variable_def--->J--yes-->D & E
		J{속빈 부위가 원형 중공일 경우}
		D{"중공의 중심간 간격≥슬래브의 전체 높이"}
		E{"콘크리트의 최소두께≥140mm"}
		J--NO-->F & G & H

		F{"중공의 횡방향 폭≤중공 높이X1.5"}

		G{"중공 사이의 복부 두께≥바닥판 전체 높이X20%"}
		H{"중공 위의 콘크리트 최소두께≥175mm"}
		D & E & F & G & H ---> I(["Pass or Fail"])
    """

    @rule_method
    def size_of_cast_in_place_circular_hollow_slab_bridge(fIcirhol,fIsquhol,fIcensph, fIovehsl, fImithco, fItrwiho, fIholhei, fIabdthi, fIovhebp, fImicoth) -> RuleUnitResult:
        """현장타설 원형 중공 슬래브교의 치수

        Args:
            fIcirhol (float): 속빈 부위가 원형 중공일 경우
            fIsquhol (float): 중공이 사각형일 경우
            fIcensph (float): 중공의 중심간 간격
            fIovehsl (float): 슬래브의 전체 높이
            fImithco (float): 콘크리트의 최소두께
            fItrwiho (float): 중공의 횡방향 폭
            fIholhei (float): 중공 높이
            fIabdthi (float): 중공 사이의 복부 두께
            fIovhebp (float): 바닥판 전체 높이
            fImicoth (float): 중공 위의 콘크리트 최소두께

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.7.5.2 현장타설 속빈 슬래브교 (2)의 판단 결과
        """

        assert isinstance(fIcirhol, float)
        assert isinstance(fIsquhol, float)
        assert isinstance(fIcensph, float)
        assert isinstance(fIovehsl, float)
        assert isinstance(fImithco, float)
        assert isinstance(fItrwiho, float)
        assert isinstance(fIholhei, float)
        assert isinstance(fIabdthi, float)
        assert isinstance(fIovhebp, float)
        assert isinstance(fImicoth, float)

        if fIcirhol != 0 and fIsquhol == 0 :
          if fIcensph >= fIovehsl and fImithco >= 140:
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

        elif fIcirhol == 0 and fIsquhol != 0 :
          if fItrwiho <= 1.5*fIholhei and fIabdthi >= fIovhebp/5 and fImicoth >= 175:
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

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )