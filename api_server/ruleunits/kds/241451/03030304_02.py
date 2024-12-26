import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KDS241451_03030304_02(RuleUnit):
    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KDS 24 14 51 3.3.3.4 (2)'
    ref_date = '2021-04-12'
    doc_date = '2024-02-13'
    title = '말뚝 선단지지력 및 주면 마찰력'

    description = """
    교량 하부구조 설계기준 (한계상태설계법)
    3. 설계
    3.3 타입말뚝
    3.3.3 극한한계상태의 지지력
    3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가
    (2)
    """
    content = """
    """
    flowchart = """
    flowchart TD
    subgraph Python_Class
    A[Title: 말뚝 선단지지력 및 주면 마찰력];
    B["KDS 24 14 51 3.3.3.4 (2)"];
    A ~~~ B
    end

    subgraph Variable_def;
		VarOut1[/출력변수:말뚝의 공칭 단위선단지지력/]
		VarOut2[/출력변수:타입말뚝에 대한 단위 주면 마찰/]
		VarIn1[/입력변수:사질토에서 깊이/]
		VarIn2[/입력변수:말뚝 선단근처의 대표적인 SPT 타격횟수/]
		VarIn3[/입력변수:SPT 타격횟수/]
		VarIn4[/입력변수:말뚝의 폭 또는 직경/]
		VarIn5[/입력변수:지지층에 관입된 말뚝길이/]
		VarIn6[/입력변수:한계 선단지지력/]
		VarIn7[/입력변수:말뚝 주면을 따라 얻은 보정하지 않은 평균 SPT 타격횟수/]
		VarOut1 ~~~ VarOut2
		VarIn1 ~~~ VarIn2 ~~~ VarIn3 ~~~ VarIn4
		VarIn5 ~~~ VarIn6 ~~~ VarIn7

    end

		Python_Class ~~~ C(["KDS 24 14 51 3.3.3.4 (2)"])
		C --> Variable_def;

		K[표준 관입시험을 이용한 방법]
		D[말뚝 선단지지력]
		E[주면마찰력]
		F["<img src='https://latex.codecogs.com/svg.image?&space;q_{p}=\frac{0.038N_{corr}D_{b}}{D}\leq&space;q_{l}'>---------------------------------"]
		G["<img src='https://latex.codecogs.com/svg.image?N_{corr}=[0.77log_{10}(\frac{1.92}{\sigma&space;_{v}^{'}})]N'>---------------------------------"]
		H["<img src='https://latex.codecogs.com/svg.image?q_{s}=0.0019\overline{N}'>---------------------------------"]
		I["<img src='https://latex.codecogs.com/svg.image?q_{s}=0.00096\overline{N}'>---------------------------------"]
		J([말뚝지지력 평가])

		Variable_def ---> K ---> D & E
		D ---> G ---> F
		E ---> H & I

		H & F & I ---> J
    """

    @rule_method
    def pile_end_bearing_capacity_and_skin_friction(fIqlA,fIqlB,fIqsA,fIqsB,fIN,fID,fIDblaye,fIsigvpr,fIavespt) -> RuleUnitResult:
        """말뚝 선단지지력 및 주면 마찰력

        Args:
            fIqlA (float): 한계 선단지지력(사질토)
            fIqlB (float): 한계 선단지지력(비소성 실트)
            fIqsA (float): 타입말뚝에 대한 단위 주면마찰력 (배토 말뚝)
            fIqsB (float): 타입말뚝에 대한 단위 주면마찰력 (비배토 말뚝)
            fIN (float): SPT 타격횟수
            fID (float): 말뚝의 폭 또는 직경
            fIDblaye (float): 지지층에 관입된 말뚝길이
            fIsigvpr (float): 상재응력 (=log10(1.92/sigma))
            fIavespt (float): 말뚝 주면을 따라 얻은 보정하지 않은 평균 SPT 타격횟수

        Returns:
            fOqp (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가 (2)의 값 1
            fOql (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가 (2)의 값 2
            fOqs (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가 (2)의 값 3
            fONcorr (float): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가 (2)의 값 4
            pass_fail (bool): 교량 하부구조 설계기준 (한계상태설계법) 3.3.3.4 현장 원위치시험을 통한 말뚝지지력의 평가 (2)의 판단 결과 1
            sOnone (string): 건축물 설계하중  3.5.3 제한사항 (2)의 판단 결과 2
        """

        assert isinstance(fIN, float)
        assert isinstance(fID, float)
        assert fID != 0
        assert isinstance(fIDblaye, float)
        assert isinstance(fIsigvpr, float)
        assert fIsigvpr != 0
        assert isinstance(fIavespt, float)


        fONcorr = 0.77 * fIsigvpr * fIN
        fOqp = 0.038 * fONcorr * fIDblaye / fID
        fOqsB = 0.00096 * fIavespt

        if fIqlA != 0 and fIqlB == 0 :
          fOql = 0.4 * fONcorr
          if fIqsA != 0 and fIqsB == 0 :
            fOqs = 0.0019 * fIavespt
            if fOqp <= fOql :
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": True,
                  }
              )
            else:
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": False,
                  }
              )
          if fIqsA == 0 and fIqsB != 0 :
            fOqs = 0.00096 * fIavespt
            if fOqp <= fOql :
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": True,
                  }
              )
            else:
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": False,
                  }
              )

        if fIqlA == 0 and fIqlB != 0 :
          fOql = 0.3 * fONcorr
          if fIqsA != 0 and fIqsB == 0 :
            fOqs = 0.0019 * fIavespt
            if fOqp <= fOql :
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": True,
                  }
              )
            else:
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": False,
                  }
              )
          if fIqlA == 0 and fIqlB != 0 :
            fOqs = 0.00096 * fIavespt
            if fOqp <= fOql :
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": True,
                  }
              )
            else:
              return RuleUnitResult(
                  result_variables = {
                      "fOqp": fOqp,
                      "fOqs": fOqs,
                      "pass_fail": False,
                  }
              )

        else :
          return RuleUnitResult(
              result_variables = {
                  "sOnone": "해당없음",
              }
          )