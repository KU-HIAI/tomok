import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_04090202_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.9.2.2 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '횡방향 등분포 압력'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.9 정수압, 유수압, 부력, 파압: WA, BP, WP
    4.9.2 유수압
    4.9.2.2 횡방향
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 횡방향 등분포 압력];
    B["KDS 24 12 21 4.9.2.2 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 횡방향 등분포 압력/];
    VarIn1[/입력변수 : 표 4.9-2로 주어지는 횡방향 항력계수/];
    VarIn2[/입력변수 : 속력/];
    VarOut ~~~ VarIn1
    VarOut ~~~ VarIn2
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.9.2.2 (1)"])
		C --> Variable_def

    D{"교각의 중축과 흐름 접근방향의 각도"};
    E["CL=0.0"];
    F["CL=0.5"];
    G["CL=0.7"];
    H["CL=0.9"];
    I["CL=1.0"];
    J["<img src='https://latex.codecogs.com/svg.image?p=0.514C_{D}V^{2}'>-----------------"];
    K(["횡방향 등분포 압력"]);
    Variable_def--->D;
    D--->N["0"]--->E--->J--->K;
    D--->M["5"]--->F--->J;
    D--->O["10"]--->G--->J;
    D--->P["20"]--->H--->J;
    D--->Q["&ge; 30"]--->I--->J
    """

    @rule_method
    def lateral_equal_distribution_pressure(fICL,fIangle,fIV) -> RuleUnitResult:
        """횡방향 등분포 압력

        Args:
            fICL (float): 표 4.9-2로 주어지는 횡방향 항력계수
            fIangle (float): 흐름과 교각의 종축이 이루는 각도
            fIV (float): 속력

        Returns:
            fOp (float): 강교 설계기준(한계상태설계법)  4.9.2.2 횡방향 (1)의 값
        """

        assert isinstance(fICL, float)
        assert isinstance(fIangle, float)
        assert isinstance(fIV, float)

        fOp = 0.514 * fICL * (fIV**2)

        return RuleUnitResult(
            result_variables = {
                "fOp": fOp,
            }
        )