from kds142054_040305_01 import KDS142054_040305_01
from kds142054_040305_03 import KDS142054_040305_03
from kds142054_040305_04 import KDS142054_040305_04
from tomok.core.util import *
import time


if __name__ == "__main__":
    fOpsecNa = None
    fOpsedNa = None
    fIeprimN = 50
    fIcNa = 90
    fIcamin = 100
    logging_normal("CHECKING... KDS 14 20 54 4.3.5(3)")
    time.sleep(2)
    logging_info("args01(fOpsecNa) - {}".format(fOpsecNa))
    time.sleep(1)
    logging_info("args02(fIeprimN) - {}".format(fIeprimN))
    time.sleep(1)
    logging_info("args03(fIcNa) - {}".format(fIcNa))
    ruleunit03 = KDS142054_040305_03()
    kds142054_040305_03_result = ruleunit03.correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(fOpsecNa,fIeprimN,fIcNa)
    time.sleep(4)
    logging_clear("KDS 14 20 54 4.3.5(3) Result: {}".format(kds142054_040305_03_result))

    time.sleep(3)
    logging_normal("CHECKING... KDS 14 20 54 4.3.5(4)")
    time.sleep(2)
    logging_info("args01(fOpsedNa) - {}".format(fOpsedNa))
    time.sleep(1)
    logging_info("args02(fIcamin) - {}".format(fIcamin))
    time.sleep(1)
    logging_info("args03(fIcNa) - {}".format(fIcNa))
    time.sleep(4)
    ruleunit04 = KDS142054_040305_04()
    kds142054_040305_04_result = ruleunit04.correction_factor_for_edge_influence_of_single_or_group_of_anchor(fOpsedNa,fIcamin,fIcNa)
    logging_clear("KDS 14 20 54 4.3.5(4) Result: {}".format(kds142054_040305_04_result))
    
    

    fINa = 80
    fINag = 80
    fIANa = 500000
    fIANao = 88947.4
    fIpsedNa = kds142054_040305_03_result
    fIpscpNa = 1.0
    fINba = 15
    fIpsecNa = kds142054_040305_04_result
    iIn = 6
    fIcNa = 90

    time.sleep(3)
    logging_normal("CHECKING... KDS 14 20 54 4.3.5(1)")
    time.sleep(2)
    logging_info("args01(fINa) - {}".format(fINa))
    time.sleep(1)
    logging_info("args02(fINag) - {}".format(fINag))
    time.sleep(1)
    logging_info("args03(fIANa) - {}".format(fIANa))
    time.sleep(1)
    logging_info("args04(fIANao) - {}".format(fIANao))
    time.sleep(1)
    logging_system("args05 fIpsedNA - {} | Refers To: KDS 14 20 54 4.3.5(3) >>> KDS 14 20 54 4.3.5(1)".format(fIpsedNa))
    time.sleep(1)
    logging_info("args06(fIpscpNa) - {}".format(fIpscpNa))
    time.sleep(1)
    logging_info("args07(fINba) - {}".format(fINba))
    time.sleep(1)
    logging_system("args08 fIpsecNA - {} | Refers To: KDS 14 20 54 4.3.5(4) >>> KDS 14 20 54 4.3.5(1)".format(fIpsecNa))
    time.sleep(1)
    logging_info("args09(iIn) - {}".format(iIn))
    time.sleep(1)
    logging_info("args10(fIcNa) - {}".format(fIcNa))
    time.sleep(4)
    
    ruleunit01 = KDS142054_040305_01()
    Rule_Review_Result = ruleunit01.nominal_bond_strength_of_a_single_bonded_anchor(
        fINa, fINag, fIANa, fIANao, fIpsedNa, fIpscpNa, fINba, fIpsecNa, iIn, fIcNa)
    # 해당건설기준 항목 의 결과는?

    logging_clear("KDS 14 20 54 4.3.5(1) Result: {}".format(Rule_Review_Result))