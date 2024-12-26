import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143110_0405040202_02(RuleUnit):
    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '최소토피고'

    description = """
    강구조부재설계기준(하중저항계수설계법)
    4. 설계
    4.5 기타 부재
    4.5.4 파형강판 구조물
    4.5.4.2 아치형 파형강판 구조물
    4.5.4.2.2 최소토피고
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
		subgraph Python_Class
		A[Title: 최소토피고] ;
		B["KDS 14 31 10 4.5.4.2.2 (2)"] ;
		A ~~~ B
		end

      subgraph Variable_def
      VarOut1[/출력변수: 최소토피고/] ;
      VarOut2[/출력변수: 대골형 파형간판의 최소토피고/] ;
      VarIn1[/입력변수: 구조물 스프링라인 사이 거리/] ;
      VarIn2[/입력변수: 구조물 단면 점검부에서 스프링라인까지 연직거리의 2배/] ;
			end

		VarOut1 & VarOut2 ~~~ VarIn1 & VarIn2
		Python_Class ~~~ Variable_def

		Q["<img src=https://latex.codecogs.com/svg.image?H_{min}=Max(0.6,\frac{D_{h}}{6}\left(\frac{D_{h}}{D_{v}}\right)^{0.5},0.4\left(\frac{D_{h}}{D_{v}}\right)^{2})>---------------------------------------------------------"]
		R["<img src=https://latex.codecogs.com/svg.image?H_{min}=Min(Max(0.6,\frac{D_{h}}{6}\left(\frac{D_{h}}{D_{v}}\right)^{0.5},0.4\left(\frac{D_{h}}{D_{v}}\right)^{2})or&space;1.5)>------------------------------------------------------------------"]
		Variable_def --> Q --> D(["<img src=https://latex.codecogs.com/svg.image?H_{min}>-----------"])
		Variable_def --> R --> F(["<img src=https://latex.codecogs.com/svg.image?H_{min}>-----------"])
    """


    @rule_method
    def minimum_cover(fIDh,fIDv) -> RuleUnitResult:
        """최소토피고

        Args:
            fIDh (float): 구조물 스프링라인 사이 거리
            fIDv (float): 구조물 단면 정점부에서 스프링라인까지 연직거리의 2배

        Returns:
            fOHmin (float): 강구조부재설계기준(하중저항계수설계법) 4.5.4.2.2 최소토피고 (2)의 값
        """

        assert isinstance(fIDh, float) and fIDh > 0
        assert isinstance(fIDv, float) and fIDv > 0

        fOHmin = min(max(0.6, (fIDh / 6) * (fIDh / fIDv) ** 0.5, 0.4 * (fIDh / fIDv) ** 2),1.5)

        return RuleUnitResult(
            result_variables = {
              "fOHmin": fOHmin,
            }
         )