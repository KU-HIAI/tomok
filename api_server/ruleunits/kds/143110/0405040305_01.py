import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040305_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.5.4.3.5 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '이음부 강도'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5. 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.3 박스형 파형강판 구조물
    4.5.4.3.5 이음부 강도
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 이음부 강도] ;
		B["KDS 14 31 10 4.5.4.3.5 (1)"] ;
		A ~~~ B
		end

    subgraph Variable_def
    VarOut1[/출력변수: 이음부 강도/] ;
    VarIn1[/입력변수: 압축 및 휨에 의한 이음부 공칭강도/] ;
    VarIn2[/입력변수: 휨에 의한 이음부 공칭강도/] ;
    VarIn3[/입력변수: 파형강판의 소성모멘트강도/] ;
    VarIn4[/입력변수: 계수/] ;
    VarIn5[/입력변수: 설계압축력/] ;
		end

		VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
		VarIn2 ~~~ VarIn4 & VarIn5

		Python_Class ~~~ C(["KDS 14 31 10 4.5.4.3.5 (1)"])
		C --> Variable_def

		F["휨에 대해서만 설계하는 경우"]
		D["압축력과 휨을 동시에 고려하는 경우"]

		Q["<img src=https://latex.codecogs.com/svg.image?\phi&space;_{j}S_{m}\geq&space;M_{pf}>-----------------------------------"]
		W["<img src=https://latex.codecogs.com/svg.image?\phi&space;_{j}S_{s}\geq&space;T_{f}>--------------------------------"]
		Variable_def --> F & D
		F --> Q
		D --> W

		Q & W --> S(["PASS or Fail"])
    """


    @rule_method
    def joint_strength(fISs,fISm,fIMpf,fIphij,fITf) -> RuleUnitResult:
        """이음부 강도

        Args:
            fISs (float): 압축 및 휨에 의한 이음부 공칭강도
            fISm (float): 휨에 의한 이음부 공칭강도
            fIMpf (float): 파형강판의 소성모멘트강도
            fIphij (float): 계수
            fITf (float): 설계압축력

        Returns:
            pass_fail (bool): 강구조부재설계기준(하중저항계수설계법)  4.5.4.3.5 이음부 강도 (1)의 판단 결과
        """

        assert isinstance(fISs, float)
        assert isinstance(fISm, float)
        assert isinstance(fIMpf, float)
        assert isinstance(fIphij, float)
        assert isinstance(fITf, float)

        if fISs != 0 and fISm == 0 :
          if fIphij * fISs >= fIMpf:
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

        elif fISs == 0 and fISm != 0 :
          if fIphij * fISm >= fITf:
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