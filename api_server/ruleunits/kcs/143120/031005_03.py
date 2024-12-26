import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_031005_03(RuleUnit):

    priority = 1
    acc_able = False
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.10.5 (3)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '스터드의 필릿용접'

    description = """
    용접
    3. 시공
    3.10 스터드의 용접
    3.10.5 스터드필릿용접
    """

    content = """
    #### 3.10.5 스터드필릿용접
    (3) 스터드의 필릿용접은 다음 규정에 준하여 시행한다.
    ④ 스터드의 마무리 높이는 설계 치수에 대해 ±2 mm 이내 이어야 한다.
    ⑤ 스터드의 기울기는 5° 이내 이어야 한다.
    ⑦ 모재의 최소 예열온도는 표 3.4-1에 의한다.
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 스터드의 필릿용접"];
    B["KCS 14 31 20 3.10.5 (3)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.10.5 (3)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/"출력변수: 스터드의 마무리 높이"/];
    VarIn1[/입력변수: 스터드의 마무리 높이/];
    VarIn2[/입력변수: 설계치수/];
		end
		subgraph V2
    VarOut2[/"출력변수: 스터드의 기울기"/];
    VarIn3[/입력변수: 스터드의 기울기/];
		end
		subgraph V3
    VarOut3[/"출력변수: 최소 예열온도"/];
    VarIn4[/입력변수: 강종/];
    VarIn5[/입력변수: 용접방법/];
    VarIn6[/입력변수: 판두께/];
		end
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"스터드의 마무리 높이\n 스터드의 기울기\n 최소 예열온도 \n."}
    C --> |"스터드의 마무리 높이"|D{"설계치수-2mm \n <스터드의 마무리 높이 \n< 설계치수+2mm \n."}
		D --> |True|Pass1([Pass])
		D --> |False|Fail1([Fail])
    C --> |"스터드의 기울기"|E{"<5°"}
		E --> |True|Pass2([Pass])
		E --> |False|Fail2([Fail])
    C --> |"최소 예열온도"|F{강종, 용접 방법, 판두께}
		F --> |표 3.4-1|G[최소 예열온도]
		G  --> End([스터드의 필릿용접])
    """

    @rule_method
    def Finishing_Height_of_Stud(fIFinHei, fIDesSiz, fISloStu, sIWelMet, sISteGra, fIThiPla) -> str:
        """ 스터드의 필릿용접
        Args:
        fIFinHei (float): 스터드의 마무리 높이
        fIDesSiz (float): 설계치수
        fISloStu (float): 스터드의 기울기
        sIWelMet (str): 용접방법
        sISteGra (str): 강종
        fIThiPla (float): 판두께

        Returns:
        pass_fail (bool): 용접 3.10.5 스터드필릿용접 (3)의 판단 결과
        sOMinPre (str): 최소 예열온도
        """
        assert isinstance(fIFinHei, float)
        assert isinstance(fIDesSiz, float)
        assert isinstance(fISloStu, float)
        assert isinstance(sIWelMet, str)
        assert sIWelMet in["저수소계 이외의 용접봉에 의한 피복아크용접(SMAW)", "저수소계 용접봉에 의한 피복아크용접", "SAW, 가스실드아크용접(GMAW 또는 FCAW)"]
        assert isinstance(sISteGra, str)
        assert sISteGra in["SM275", "SMA275", "SM355", "SM420", "SM460", "SN355", "SMA355W", "SMA460W", "HSB380", "HSB380L", "HSB380W", "HSB460", "HSB460L", "HSB460W", "HSB690", "HSB690L", "HSB690W"]
        assert isinstance(fIThiPla, float)


        if fIDesSiz - 2 <= fIFinHei <= fIDesSiz + 2 and fISloStu <= 5:
          pass_fail = True
        else:
          pass_fail = False

        if sIWelMet == "저수소계 이외의 용접봉에 의한 피복아크용접(SMAW)":
          if sISteGra == "SM275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOPreInt = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "-"
            elif fIThiPla > 50:
              sOMinPre = "-"
        elif sIWelMet == "저수소계 용접봉에 의한 피복아크용접":
          if sISteGra == "SM275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOPreInt = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SMA275":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SM355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "SM420" or "SM460" or "SN355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "100"
          elif sISteGra == "SMA355W" or "SMA460W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "100"
          elif sISteGra == "HSB380" or "HSB380L" or "HSB380W" or "HSB460" or "HSB460L" or "HSB460W":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "HSB690" or "HSB690L":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "HSB690W":
            if fIThiPla <= 25:
              sOMinPre = "50"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "80"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "80"
            elif fIThiPla > 50:
              sOMinPre = "80"
        elif sIWelMet == "SAW, 가스실드아크용접(GMAW 또는 FCAW)":
          if sISteGra == "SM275":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "SMA275":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "SM355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "SM420" or "SM460" or "SN355":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "SMA355W" or "SMA460W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "80"
          elif sISteGra == "HSB380" or "HSB380L" or "HSB380W" or "HSB460" or "HSB460L" or "HSB460W":
            sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
          elif sISteGra == "HSB690" or "HSB690L":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"
          elif sISteGra == "HSB690W":
            if fIThiPla <= 25:
              sOMinPre = "예열없음(모재의 표면온도가 0 ℃ 이하일 경우에는 20 ℃ 정도로 가열한다는 것)"
            elif 25 < fIThiPla <= 40:
              sOMinPre = "50"
            elif 40 < fIThiPla <= 50:
              sOMinPre = "50"
            elif fIThiPla > 50:
              sOMinPre = "50"

        return RuleUnitResult(
                result_variables = {
                    "pass_fail": pass_fail,
                    "sOMinPre": sOMinPre,
                }
            )