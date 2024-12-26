import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_040302020201_01(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 10 4.3.2.2.2.1 (1)'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '휨부재 콘크리트 슬래브의 유효폭'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.3. 휨부재
    4.3.2 형강 및 강관
    4.3.2.2 합성부재
    4.3.2.2.2 휨부재
    4.3.2.2.2.1 일반사항
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
	  subgraph Python_Class
	  A[휨부재 콘크리트 슬래브의 유효폭]
	  B["KDS 14 31 10 4.3.2.2.2.1(1)"]
	  A ~~~ B
	  end

	  subgraph Variable_def
	  VarOut[/출력변수: 콘크리트 슬래브의 유효폭/]
	  VarIn1[/입력변수: 보경간/]
	  VarIn2[/입력변수: 보중심선에서 인접보 중심선까지 거리/]
	  VarIn3[/입력변수: 보중심선에서 슬래브 가장자리/]
	  VarOut ~~~ VarIn1 & VarIn2 & VarIn3
	  end
	  Python_Class ~~~ C1(["KDS 14 31 10 4.3.2.2.2.1(1)"]) -->Variable_def --> D --> E --보중심을 기준으로 좌우 각방향에 대한 유효폭의 합--> F
	  D["min(보경간의1/8, 보중심선에서 인접보 중심선까지의 거리 1/2, 보중심선에서 슬래브 가장자리까지의 거리)"]
	  E["각 방향에 대한 유효폭"]
	  F(["콘크리트 슬래브의 유효폭"])
    """

    @rule_method
    def Effective_width_of_concrete_slab(fIbeaspa,fIDisbeacen,fISlaEdfbea) -> RuleUnitResult:
        """휨부재 콘크리트 슬래브의 유효폭

        Args:
            fIbeaspa (float): 보경간
            fIDisbeacen (float): 보중심선에서 인접보 중심선까지 거리
            fISlaEdfbea (float): 보중심선에서 슬래브 가장자리


        Returns:
            fOEffwidcon (float): 강구조부재설계기준(하중저항계수설계법) 4.3.2.2.2.1 일반사항 (1)의 값
        """

        assert isinstance(fIbeaspa, float)
        assert isinstance(fIDisbeacen, float)
        assert isinstance(fISlaEdfbea, float)


        fOEffwidcon = min(fIbeaspa / 8, fIDisbeacen / 2, fISlaEdfbea)
        return RuleUnitResult(
          result_variables = {
            "fOEffwidcon": fOEffwidcon,
             }
        )