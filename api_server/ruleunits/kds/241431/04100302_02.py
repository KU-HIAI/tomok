import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241431_04100302_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 31 4.10.3.2 (2)'
    ref_date = '2018-08-30'
    doc_date = '2024-02-20'
    title = '바닥판의 허용처짐량'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.10 바닥판과 바닥틀
    4.10.3 한계상태
    4.10.3.2 사용한계상태
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 바닥판의 허용처짐량];
    B["KDS 24 14 31 4.10.3.2 (2)"];
    A ~~~ B
    end

    subgraph Variable_def
	  VarOut1[/출력변수: 바닥판의 허용처짐량/];
    VarIn1[/입력변수: 바닥판 지지부재의 중심간 거리/] ;
	  end

		Python_Class ~~~ C(["KDS 24 14 31 4.10.3.2 (2)"])
		C --> Variable_def

		D[L/1200] ;
		E{보도부} ;
    G[L/1000];
    H[L/800];
    Variable_def --> E
		D & G & H --> I([바닥판의 허용처짐량])

    E--매우중요-->D;
    E--Yes-->G;
    E--No-->H;
    """

    @rule_method
    def floor_plate_allowable_deflection(fIflpadA,fIflpadB,fIflpadC,fIL) -> RuleUnitResult:
        """바닥판의 허용처짐량

        Args:
            fIflpadA (float): 바닥판의 허용처짐량 (보도부가 없는 바닥판)
            fIflpadB (float): 바닥판의 허용처짐량 (보도부가 있는 바닥판)
            fIflpadC (float): 바닥판의 허용처짐량 (보도부가 매우 중요한 바닥판)
            fIL (float): 바닥판 지지부재의 중심간 거리

        Returns:
            fOflpad (float): 강교 설계기준(한계상태설계법)  4.10.3.2 사용한계상태 (2)의 값
            pass_fail (bool): 강교 설계기준(한계상태설계법)  4.10.3.2 사용한계상태 (2)의 판단 결과
        """

        assert isinstance(fIL, float)

        if fIflpadA != 1 and fIflpadB == 0 and fIflpadC == 0 :
          fOflpad = fIL / 800
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        elif fIflpadA == 0 and fIflpadB != 1 and fIflpadC == 0 :
          fOflpad = fIL / 1000
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        elif fIflpadA == 0 and fIflpadB == 0 and fIflpadC != 1 :
          fOflpad = fIL / 1200
          return RuleUnitResult(
              result_variables = {
                  "fOflpad": fOflpad,
              }
          )

        else:
          return RuleUnitResult(
              result_variables = {
                  "pass_fail": False,
              }
          )