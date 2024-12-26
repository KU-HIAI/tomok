import sys
import os

from tomok import RuleUnit, rule_method, RuleUnitResult

import math
from typing import List

class KCS143120_030502_01(RuleUnit):

    priority = 1
    acc_able = True
    author = '국가건설기준센터'
    ref_code = 'KCS 14 31 20 3.5.2 (1)'
    ref_date = '2019-05-20'
    doc_date = '2023-11-13'
    title = '용접봉의 최대지름'

    description = """
    용접
    3. 시공
    3.5 피복아크용접(SMAW)
    3.5.2 용접절차
    """

    content = """
    #### 3.5.2 용접절차
    (1) 용접봉의 최대지름은 다음을 기본으로 한다.
    ① 루트패스를 제외한 아래보기자세의 모든 용접: 6 mm
    ② 수평 필릿용접부: 6 mm
    ③ 아래보기자세로 수행한 필릿용접부의 루트패스와 루트간격이 6 mm 이상의 그루브용접:6 mm
    ④ 수직자세 및 위보기자세 용접 : 4 mm
    ⑤ 그루브용접부의 루트용접 및 위에서 언급한 경우를 제외한 기타 용접: 5 mm
    """

    flowchart = """
    flowchart TD
    subgraph Python_Class
    A["Title: 용접봉의 최대지름"];
    B["KCS 14 31 20 3.5.2 (1)"];
    B ~~~ A
    end

    KCS(["KCS 14 31 20 3.5.2 (1)"])

    subgraph Variable_def
		subgraph V1
    VarOut1[/"출력변수: 용접봉의 최대지름"/];
    VarIn1[/입력변수: 루트 패스를 제외한 아래보기 자세의 모든 용접/];
		end
		subgraph V2
    VarOut2[/"출력변수: 용접봉의 최대지름"/];
    VarIn2[/입력변수: 수평 필릿용접부/];
		end
		subgraph V3
    VarOut3[/"출력변수: 용접봉의 최대지름"/];
    VarIn3[/입력변수: 아래보기자세로 수행한 필릿용접부의 루트패스/];
    VarIn4[/입력변수: 루트간격이 6mm 이상의 그루브 용접/];
		end
		subgraph V4
    VarOut4[/"출력변수: 용접봉의 최대지름"/];
    VarIn5[/입력변수: 수직자세 용접/];
    VarIn6[/입력변수: 위보기자세 용접/];
		end
		subgraph V5
    VarOut5[/"출력변수: 용접봉의 최대지름"/];
    VarIn7[/입력변수: 그루브용접부의 루트용접/];
		end
		V1 & V2 ~~~ V3 & V4 & V5
		end

    Python_Class ~~~ KCS
    KCS --> Variable_def
    Variable_def --> C{"루트 패스를 제외한 아래보기 자세의 모든 용접 \n 수평 필릿용접부 \n 아래보기자세로 수행한 필릿용접부의 루트패스 \n루트간격이 6mm 이상의 그루브 용접\n 수직자세 용접\n 위보기자세 용접\n 그루브용접부의 루트용접\n."}
    C --> |"루트 패스를 제외한 아래보기 자세의 모든 용접"|D[6 mm]
    C --> |"수평 필릿용접부"|E[6 mm]
    C --> |"아래보기자세로 수행한 필릿용접부의 루트패스 \n 루트간격이 6mm 이상의 그루브 용접"|F[6 mm]
    C --> |"수직자세 용접\n위보기자세 용접"|G[4 mm]
    C --> |"그루브용접부의 루트용접 \n False"|H[5 mm]
		D & E & F & G & H --> End([용접봉의 최대지름])
    """

    @rule_method
    def Flat_Position_Except_for_Root_Pass(bIFlaPos, bIHorFil, bIRooFla, bIGroSpa, bIVerPos, bIOvePos, bIRooGro) -> RuleUnitResult:
        """ 용접봉의 최대지름
        Args:
        bIFlaPos (bool): 루트 패스를 제외한 아래보기 자세의 모든 용접
        bIHorFil (bool): 수평 필릿용접부
        bIRooFla (bool): 아래보기자세로 수행한 필릿용접부의 루트패스
        bIGroSpa (bool): 루트간격이 6mm 이상의 그루브 용접
        bIVerPos (bool): 수직자세 용접
        bIOvePos (bool): 위보기자세 용접
        bIRooGro (bool): 그루브용접부의 루트용접 및 기타 용접

        Returns:
        fOMaxWel (float): 용접봉의 최대지름
        """
        assert isinstance(bIFlaPos, bool)
        assert isinstance(bIHorFil, bool)
        assert isinstance(bIRooFla, bool)
        assert isinstance(bIGroSpa, bool)
        assert isinstance(bIVerPos, bool)
        assert isinstance(bIOvePos, bool)
        assert isinstance(bIRooGro, bool)
        assert (bIFlaPos + bIHorFil + bIRooFla + bIGroSpa + bIVerPos + bIOvePos + bIRooGro) == 1

        if bIVerPos == True or bIOvePos == True:
          fOMaxWel = 4
        elif bIRooGro == True:
          fOMaxWel = 5
        elif bIFlaPos == True or bIHorFil == True or bIRooFla == True or bIGroSpa == True:
            fOMaxWel = 6

        return RuleUnitResult(
                result_variables = {
                    "fOMaxWel": fOMaxWel
                }
            )