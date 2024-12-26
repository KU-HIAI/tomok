import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS143120_04010205(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 14 31 20 4.1.2.5'
    ref_date = '2017-12-20'
    doc_date = '2024-02-13'
    title = '공칭피로강도'

    description = """
    강구조 피로 및 파단 설계기준(하중저항계수설계법)
    4. 설계(피로 및 파단)
    4.1 피로
    4.1.2 하중유발피로
    4.1.2.5 피로강도
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["KDS 14 31 20 4.1.2.5"];
    B[Title: 공칭피로강도];
		A ~~~ B
		end

		C(["KDS 14 31 20 4.1.2.5"]);

		Python_Class ~~~ C ;

		subgraph Variable_def;
    VarOut1[/출력변수: 공칭피로강도/];
		VarIn1[/입력변수: 대상 구조상세가 설계수명 동안 받을 것으로 예상되는 활하중에 의한 응력범위 반복횟수/] ;
    VarIn2[/입력변수: 일정진폭 피로한계값/];
    VarIn3[/입력변수: 무한수명 공칭피로강도/];
    VarIn4[/입력변수: 일정진폭 피로한계값에 해당하는 응력범위 반복횟수/];
    VarIn5[/입력변수: 무한수명 응력범위에 해당하는 응력 범위 반복횟수/];
    VarIn6[/입력변수: 상세범주 C에 대한 공칭피로강도/];
		VarIn7[/입력변수: 하중 전달판의 두께방향으로의 용접루트 사이 간격/];
    VarIn8[/입력변수: 하중을 받는 판의 두께/];
    VarIn9[/입력변수: 하중 전달판 두께 방향의 필릿용접의 각장/];

    VarOut1 ~~~ VarIn1 & VarIn2 & VarIn3
    VarIn2 ~~~ VarIn4 & VarIn5 & VarIn6
    VarIn5 ~~~ VarIn7 & VarIn8 & VarIn9

		end

		D["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{3}}(\Delta&space;)_{TH}'>------------------------------------------------------------------"]
		E["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\frac{N_{TH}}{N})^{\frac{1}{5}}(\Delta&space;F)_{TH}'>--------------------------------------------------------------------"]
		F["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}=(\Delta&space;F)_{n}^{c}(\frac{1.12-(\frac{2a}{t_{p}})&plus;1.24(\frac{\omega}{t_{p}})}{t_{p}^{0.167}})\leq(\Delta&space;F)_{n}^{c}'>-----------------------------------------------------------------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?N_{TH}\leq&space;N\leq&space;N_{CL}'>-------------------------------------"]
		U["<img src='https://latex.codecogs.com/svg.image?N\leq&space;N_{TH}'>-------------------------"]

		C --> Variable_def ;
		Variable_def --> I;
    Variable_def --> J;
		Variable_def --> K;

		I{일정진폭응력}
		J{다양한 진폭응력}
		K{불연속된 판에 의해 하중을 받고 응력방향과 수직한 방향으로 \n 필릿 용접 또는 부분용입 그루브용접 연결된 상세부 모재}

		I-->G-->D;
		J-->H & U
		H-->E --> R
		U-->D --> Q
		K-->F --> S

		Q(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		R(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
		S(["<img src='https://latex.codecogs.com/svg.image?(\Delta&space;F)_{n}'>-----------------"])
    """

    @rule_method
    def nominal_fatigue_strength(fIdelFnA,fIdelFnB,fIdelFnC,fIdelFth,fIdelFcl,iIN,iINth,iINcl,fIdelFcn,fItwoa,fItp,fIw) -> RuleUnitResult:
        """공칭피로강도

        Args:
            fIdelFnA (float): 공칭피로강도 (일정진폭응력)
            fIdelFnB (float): 공칭피로강도 (다양한 진폭응력)
            fIdelFnC (float): 공칭피로강도 (불연속된 판에 의해 하중을 받고 응력방향과 수직한 방향으로 필릿용접 또는 부분용입 그루브용접 연결된 상세부 모재)
            fIdelFth (float): 일정진폭 피로한계값
            fIdelFcl (float): 무한수명 공칭피로강도
            iIN (int): 대상 구조상세가 설계수명 동안 받을 것으로 예상되는 활하중에 의한 응력범위 반복횟수
            iINth (int): 일정진폭 피로한계값에 해당하는 응력범위 반복횟수
            iINcl (int): 무한수명 응력범위(cut-off limit)에 해당하는 응력범위 반복횟수
            fIdelFcn (float): 상세범주 C에 대한 공칭피로강도
            fItwoa (float): 하중 전달판의 두께방향으로의 용접루트 사이 간격
            fItp (float): 하중을 받는 판의 두께
            fIw (float): 하중 전달판 두께방향의 필릿용접의 각장

        Returns:
            fOdelFn (float): 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.5 피로강도의 값
            pass_fail (bool): 강구조 피로 및 파단 설계기준(하중저항계수설계법)  4.1.2.5 피로강도의 판단 결과
        """

        assert isinstance(fIdelFth, float)
        assert isinstance(fIdelFcl, float)
        assert isinstance(iIN, int)
        assert iIN > 0
        assert isinstance(iINth, int)
        assert iINth > 0
        assert isinstance(iINcl, int)
        assert isinstance(fIdelFcn, float)
        assert isinstance(fItwoa, float)
        assert isinstance(fItp, float)
        assert fItp > 0
        assert isinstance(fIw, float)

        if fIdelFnA != 0 and fIdelFnB == 0 and fIdelFnC == 0 :
          if iIN <= iINth :
            fOdelFn = (iINth/iIN)**(1/3)*fIdelFth
            return RuleUnitResult(
                result_variables = {
                    "fOdelFn": fOdelFn,
                    "pass_fail": True,
                }
            )
          else:
            return RuleUnitResult(
                result_variables = {
                    "pass_fail": False,
                }
            )

        elif fIdelFnA == 0 and fIdelFnB != 0 and fIdelFnC == 0 :
          if iIN <= iINth :
            fOdelFn = (iINth/iIN)**(1/3) * fIdelFth
          elif iINth <= iIN <= iINcl:
            fOdelFn = (iINth/iIN)**(1/5) * fIdelFth
          elif iINcl <= iIN:
            fOdelFn = fIdelFcl
            return RuleUnitResult(
                result_variables = {
                    "fOdelFn": fOdelFn,
                }
            )

        elif fIdelFnA == 0 and fIdelFnB == 0 and fIdelFnC != 0 :
          fOdelFn = fIdelFcn * (1.12 - (fItwoa / fItp) + 1.24 * (fIw / fItp)) / (fItp**1.167)
          if fOdelFn <= fIdelFcn :
            return RuleUnitResult(
                result_variables = {
                    "fOdelFn": fOdelFn,
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