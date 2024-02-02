from kds142054_040305_01 import KDS142054_040305_01
from kds142054_040305_03 import KDS142054_040305_03
from kds142054_040305_04 import KDS142054_040305_04
from tomok.core.util import *

fOpsecNa = None
fOpsedNa = None
fIeprimN = 50
fIcNa = 90
fIcamin = 100


ruleunit03 = KDS142054_040305_03()
kds142054_040305_03_result = ruleunit03.correction_factor_for_attached_anchor_groups_with_eccentricity_of_tensile_force(
    fOpsecNa, fIeprimN, fIcNa
)
logging_clear("KDS142054_040305_03 Result: {}".format(kds142054_040305_03_result))

ruleunit04 = KDS142054_040305_04()
kds142054_040305_04_result = (
    ruleunit04.correction_factor_for_edge_influence_of_single_or_group_of_anchor(
        fOpsedNa, fIcamin, fIcNa
    )
)
logging_clear("KDS142054_040305_04 Result: {}".format(kds142054_040305_04_result))

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

ruleunit01 = KDS142054_040305_01()
Rule_Review_Result = ruleunit01.nominal_bond_strength_of_a_single_bonded_anchor(
    fINa, fINag, fIANa, fIANao, fIpsedNa, fIpscpNa, fINba, fIpsecNa, iIn, fIcNa
)
# 해당건설기준 항목 의 결과는?

logging_clear("RuleUnit KDS142054 040305_01 실행 결과: {}".format(Rule_Review_Result))
