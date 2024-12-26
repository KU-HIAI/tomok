import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS249011_04010602_03(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 90 11 4.1.6.2 (3)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-14'
    title = '캔틸레버 시점'

    description = """
    교량 기타시설설계기준 (한계상태설계법)
    4. 설계
    4.1 신축이음
    4.1.6 핑거형 신축이음(Finger Expansion Joint)
    4.1.6.2 요구 성능
    (3)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 캔틸레버 시점];
    B["KDS 24 90 11 4.1.6.2 (3)"];
    A ~~~ B
    end

		subgraph Variable_def;
		VarIn1[/입력변수: 캔틸레버 시점/];
		VarIn2[/입력변수: 단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면 사이의 거리/];

		end
		Python_Class ~~~ C(["KDS 24 90 11 4.1.6.2 (3)"])
		C --> Variable_def;
		Variable_def--->E

		E{"20mm≤단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면 사이의 거리"}
		E--NO---->D

		D{"단부 앵글 전면으로부터 캔틸레버 방향으로 10mm ≤ 캔틸레버 시점"};
    F(["Pass or Fail"])
    D ---> F
    """

    @rule_method
    def Cantilever_Start_Point(fIcantsp, fIdisbtp) -> RuleUnitResult:
        """캔틸레버 시점
        Args:
            fIcantsp (float): 캔틸레버 시점
            fIdisbtp (float): 단부 앵글의 상면과 상대편 핑거 캔틸레버의 하면사이의 거리

        Returns:
            pass_fail (bool): 교량 기타시설설계기준 (한계상태설계법) 4.1.6.2 요구 성능 (3)의 판단 결과 1
            sOfilwel (string): 교량 기타시설설계기준 (한계상태설계법) 4.1.6.2 요구 성능 (3)의 판단 결과 2
        """

        if fIdisbtp < 20 :
          if fIcantsp >= 10 :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": True,
                    }
                )
          else :
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                    }
                )
        else :
          return RuleUnitResult(
              result_variables = {
                  "sOfilwel": "본 규정을 적용하지 않아도 좋음",
                  "pass_fail": True,
                  }
              )