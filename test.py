from ruleifc_kds142054_040305_01 import RuleIFC_KDS124054_040305_01
from tomok.ifc import IFCReader

if __name__ == '__main__':
    ruleifc = RuleIFC_KDS124054_040305_01(
        reader=IFCReader(ifc_filepath="대성요청확장파일_v4.ifc")
    )
    
    entities = ruleifc.retrieve_entities("0ZCqvdQhLE28JaY93BNupT")
    
    ruleifc.process(entities)