import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241421_04010102_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 21 4.1.1.2 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '압축연단의 한계변형률'

    description = """
    콘크리트교 설계기준 (한계상태설계법)
    4. 설계
    4.1 극한한계상태
    4.1.1 휨과 축력
    4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 압축연단의 한계변형률];
    B["KDS 24 14 21 4.1.1.2 (2)"];
    A ~~~ B
    end
	  subgraph Variable_def;
		VarIn1[/입력변수: 압축연단의 한계변형률/];
		VarIn2[/입력변수: 최대 압축응력에서의 압축 변형률/];
    VarIn3[/입력변수: 강재의 극한한계변형률/] ;

		VarIn1 & VarIn2 & VarIn3
		end

	  Python_Class ~~~ C(["KDS 24 14 21 4.1.1.2 (2)"])
		C --> Variable_def

		Variable_def--->E--->D

		E{"최대 압축응력에서의 압축 변형률≤압축연단의 한계변형률≤강재의 극한한계변형률"};
		D(["Pass or Fail"])
    """

    @rule_method
    def Limitting_Strain_of_Compression_Edge(fIepscud,fIepsco,fIepscu) -> RuleUnitResult:
        """압축연단의 한계변형률

        Args:
            fIepscud (float): 압축연단의 한계변형률
            fIepsco (float): 최대 압축응력에서의 압축 변형률
            fIepscu (float): 강재의 극한한계변형률

        Returns:
            pass_fail (bool): 콘크리트교 설계기준 (한계상태설계법)  4.1.1.2 휨 및 축력이 작용하는 부재의 극한한계상태 검증 (2)의 판단 결과
        """

        assert isinstance(fIepscud, float)
        assert isinstance(fIepsco, float)
        assert isinstance(fIepscu, float)

        if fIepsco <= fIepscud <= fIepscu:
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