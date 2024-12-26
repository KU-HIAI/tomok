import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241221_041807_01(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 12 21 4.18.7 (1)'
    ref_date = '2021-04-15'
    doc_date = '2024-02-15'
    title = '선박충돌에너지'

    description = """
    강교 설계기준(한계상태설계법)
    4. 설계
    4.18 선박충돌하중: CV
    4.18.5 연간파괴빈도
    4.18.7 선박충돌에너지
    (1)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 선박의 충돌에너지];
    B["KDS 24 12 21 4.18.7 (1)"];
    A ~~~ B
    end
    subgraph Variable_def
    VarOut[/출력변수 : 선박의 충돌에너지/];
    VarIn1[/입력변수 : 선박의 용적톤수/];
    VarIn2[/입력변수 : 수리동적질량계수/];
    VarIn3[/입력변수 : 선박충돌속도/];
    end

    Python_Class ~~~ C(["KDS 24 12 21 4.18.7 (1)"])
		C --> Variable_def

    D{"적재선박의 경우"};
    E["선박의 용적톤수 = 비적재선박질량 + 화물질량"];
    F["선박의 용적톤수 = 비적재선박질량 + 선박의 수송을 위한 water ballast의 질량"];
    G{"견인되는 바지선의 경우"};
    H["선박의 용적 = 예인선의 질량 + 예인되는 바지선들의 질량"];
    I["<img src ='https://latex.codecogs.com/svg.image?KE=500C_{H}MV^2'>---------------------------------"];
    J(["선박의 충돌에너지"]);

    Variable_def--->D--Yes--->E--->I--->J
    D--No--->F--->I
    Variable_def--->G--->H--->I
    """

    @rule_method
    def the_collision_energy_of_a_ship(fIM,fICH,fIV) -> RuleUnitResult:
        """선박충돌에너지

        Args:
            fIM (float): 선박의 용적 톤수
            fICH (float): 수리동적질량계수
            fIV (float): 선박충돌속도

        Returns:
            fOKE (float): 강교 설계기준(한계상태설계법)  4.18.7 선박충돌에너지 (1)의 값
        """

        assert isinstance(fIM, float)
        assert isinstance(fICH, float)
        assert isinstance(fIV, float)

        fOKE = 500 * fICH * fIM * (fIV**2)

        return RuleUnitResult(
            result_variables = {
                "fOKE": fOKE,
            }
        )