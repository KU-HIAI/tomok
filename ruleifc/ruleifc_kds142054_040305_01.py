import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from ruleunits import (
    kds142054_040305_01,
    kds142054_040305_03,
    kds142054_040305_04,
    kds142054_040305_05
)

print('work')