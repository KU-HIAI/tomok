import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS115015_04010403_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 11 50 15 4.1.4.3 (1)'
    ref_date = '2021-05-12'
    doc_date = '2024-02-07'
    title = '현장타설 콘크리트말뚝의 장기 허용압축응력'

    description = """
    깊은기초 설계기준(일반설계법)
    4. 설계
    4.1 말뚝기초
    4.1.4 말뚝재료의 허용응력
    4.1.4.3 현장타설 콘크리트말뚝
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 현장타설 콘크리트말뚝 장기 허용압축응력];
    B["KDS 11 50 15 4.1.4.3 (1)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarOut[/출력변수: 현장타설 콘크리트말뚝 장기 허용압축응력/];
    VarIn1[/입력변수: 콘크리트설계기준강도/] ;

		VarOut~~~VarIn1

		end
		Python_Class ~~~ C(["KDS 11 50 15 4.1.4.3 (1)"])
		C --> Variable_def;
		Variable_def-->G
		G{"말뚝본체의 전부 또는 일부의 콘크리트가\n 물 또는 흙탕물 중에 타설될 경우 OR 수중타설콘크리트에 대한 조치가 없는경우"};
    G--YES---> D
    D["장기허용압축응력=콘크리트 설계기준강도X20%"];

    G--NO---->E
    E["장기허용압축응력=콘크리트 설계기준강도X25% \n or ≤ 8.5MPa"];
    F(["장기허용압축응력"]);
    E & D---->F
    """

    @rule_method
    def long_term_allowable_compressive_stress_of_cast_in_place_concrete_pile(fIlacscA,fIlacscB,fIfck) -> RuleUnitResult:
        """현장타설 콘크리트말뚝의 장기 허용압축응력

        Args:
            fIlacscA (float): 현장타설 콘크리트말뚝의 장기 허용압축응력 (말뚝본체의 전부 또는 일부의 콘크리트가 물 또는 흙탕물 중에 타설될 경우)
            fIlacscB (float): 현장타설 콘크리트말뚝의 장기 허용압축응력 (말뚝본체 콘크리트 타설을 위한 굴착구멍에 물 또는 흙탕물이 없는 상태에서 콘크리트가 타설될 경우 또는 수중타설콘크리트에 대한 조치가 있는 경우)
            fIfck (float): 설계기준 압축강도

        Returns:
            pass_fail (bool): 깊은기초 설계기준(일반설계법)  4.1.4.3 현장타설 콘크리트말뚝 (1)의 판단 결과
        """

        assert isinstance(fIlacscA, float)
        assert isinstance(fIlacscB, float)
        assert isinstance(fIfck, float)

        if fIlacscA != 0 and fIlacscB == 0 :
          if fIlacscA <= fIfck * 0.2:
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

        elif fIlacscA == 0 and fIlacscB != 0 :
          if fIlacscB <= min(fIfck * 0.25, 8.5):
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

        elif fIlacscA != 0 and fIlacscB != 0 :
          if fIlacscA <= fIfck * 0.2 and fIlacscB <= min(fIfck * 0.25, 8.5):
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

        else :
          return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                }
          )