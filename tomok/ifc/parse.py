# python
from concurrent.futures import process
from typing import List, Union
from copy import deepcopy
# 3rd-party
from ifcopenshell.entity_instance import entity_instance
from ifcopenshell.file import file
# framework
from .util import iter_inverse
from .property_set import PropertySet
from .parsed_entity import ParsedEntity
from .rule_info import RuleInfo, RuleProcessType


def get_tree(
    ifc: file,
    from_entity: entity_instance,
    filter_is_a: Union[None, str] = None
) -> dict:
    """IFC의 entity_instance를 트리 형태의 dict로 만들어 반환.

    예)
    ```python
    pprint.pprint(parse.get_tree(reader.ifc, beams[0].entity))
    ```
    실행결과)
    ```python
    {'IfcStructuralCurveAction': {'entity_instances': [#213000=IfcRelConnectsStructuralActivity('3gfVO40P5EfQyKZ_bF2102',#42,$,$,#318,#213001),
                                                    #213003=IfcRelDefinesByProperties('3gfVO40P5EfQyKZ_bF2104',#42,$,$,(#213001),#213004),
                                                    #213103=IfcRelDefinesByProperties('3gfVO40P5EfQyKZ_bF2106',#42,$,$,(#213001),#213104),
                                                    #213203=IfcRelDefinesByProperties('3gfVO40P5EfQyKZ_bF2108',#42,$,$,(#213001),#213204)]},
    'entity_instances': [#328=IfcRelDefinesByProperties('2VmbC9Tiz4fvUVpvsbkbTE',#20,$,$,(#318),#324),
                        #329=IfcRelDefinesByProperties('2eHXdToC141v1H2KibUqui',#20,$,$,(#318),#325),
                        #330=IfcRelDefinesByProperties('1DGkgjJfX3KBfqKwuCkrFZ',#20,$,$,(#318),#327),
                        #339=IfcRelDefinesByProperties('04LY4ZNer0lPBmegut9Eb_',#20,$,$,(#318),#338),
                        #571=IfcRelContainedInSpatialStructure('3Zu5Bv0LOHrPC10066FoQQ',#20,$,$,(#135,#174,#207,#240,#273,#318,#366,#411,#456,#501,#547),#103),
                        #592=IfcRelDefinesByType('2XZDT40UTB7gzG1IKOsOmy',#20,$,$,(#318),#308),
                        #105503=IfcRelAssociatesClassification('2wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318,#366,#411,#456,#501),#105502),
                        #210000=IfcRelAssociatesMaterial('3gfVO40P5EfQyKZ_bF2101',#42,$,$,(#318),#210001),
                        #213000=IfcRelConnectsStructuralActivity('3gfVO40P5EfQyKZ_bF2102',#42,$,$,#318,#213001),
                        #213001=IfcStructuralCurveAction('3gfVO40P5EfQyKZ_bF2103',#42,$,$,(#318),$,$,$,$,$,$,$),
                        #214503=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214502),
                        #214505=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214504),
                        #214507=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214506),
                        #214509=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214508),
                        #214603=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214602),
                        #214605=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214604),
                        #214607=IfcRelAssociatesClassification('0wo0TtC7r0hA67SDJ1e9VZ',#20,'Default Classification Classification','',(#318),#214606),
                        #214300=IfcRelDefinesByProperties('4gfVO40P5EfQyKZ_bF2114',#42,$,$,(#318),#214301),
                        #214400=IfcRelDefinesByProperties('4gfVO40P5EfQyKZ_bF2116',#42,$,$,(#318),#214401)]}
    ```

    Args:
        ifc (file): IFC 파일
        from_entity (entity_instance): 탐색을 시작하는 entity
        filter_is_a (Union[None, str], optional): 엔터티 타입 필터 문자열. is_a 로 검사해서 true인 entity만 반환합니다.
        parse (bool): True로 설정할 경우, entity instance를 ParsedEntity로 변한합니다.
        pack (bool): True로 설정할 경우, entity instance들의 pset, material, profile 들을 리스트 형태로 묶습니다.

    Returns:
        dict: from_entity를 참조하는 entity_instances의 트리
    """
    try:
        node_template = {'entity_instances': []}
        tree = deepcopy(node_template)
        tree[from_entity.is_a()] = deepcopy(node_template)
        _pack(tree, from_entity)
        _pack_rule_info(tree, from_entity)
        identifications = []
        for entity, parents in iter_inverse(ifc=ifc, from_entity=from_entity, filter_is_a=filter_is_a):
            parsed_entity = ParsedEntity(ifc, entity)
            cur_node = tree
            for parent_entity in parents:
                if parent_entity.is_a() not in cur_node.keys():
                    cur_node[parent_entity.is_a()] = deepcopy(node_template)
                cur_node = cur_node[parent_entity.is_a()]
            cur_node['entity_instances'].append(parsed_entity)
            _pack(cur_node, parsed_entity)
            _pack_rule_info(cur_node, parsed_entity)
            if parsed_entity.identifications is not None:
                identifications.append(parsed_entity.identifications)
        identifications = sum(identifications, [])
        tree[from_entity.is_a()]['identification'] = identifications
    except Exception as ex:
        print(tree)
        print(ex)
        print(list(iter_inverse(ifc=ifc, from_entity=from_entity, filter_is_a=filter_is_a)))
        raise Exception()
    return tree[from_entity.is_a()]


def _pack(node: dict, parsed_entity: ParsedEntity):
    """Entity의 pset, material, profile이 여러개 있을 경우, 이를 dictionary 형태로 묶음

    Args:
        node (_type_): _description_
        parsed_entity (_type_): _description_
    """
    packing_keys = ['pset', 'material', 'profile', 'id2rel_class']
    for key in parsed_entity.__dict__.keys():
        if key not in packing_keys:
            continue
        if key not in node.keys():
            node[key] = {}
        pack_entity = parsed_entity.__dict__[key]
        if pack_entity is None:
            pass
        if type(pack_entity) is PropertySet:
            node[key][pack_entity.Name] = parsed_entity.__dict__[key]
        elif type(pack_entity) is list:
            for pack_element in pack_entity:
                node[key][pack_element.Name] = pack_element
        elif type(pack_entity) is dict:
            for pack_key, pack_value in pack_entity.items():
                node[key][pack_key] = pack_value


def _pack_rule_info(node: dict, parsed_entity: ParsedEntity):
    if hasattr(parsed_entity, 'rule_info'):
        packing_process_types = {RuleProcessType.Decision: 'rule_decision',
                                RuleProcessType.Indirect: 'rule_indirect'}
        for key in packing_process_types.values():
            if key not in node.keys():
                node[key] = []
        rule_info: RuleInfo = parsed_entity.rule_info
        if rule_info is None:
            return
        if rule_info.process_type in packing_process_types.keys():
            key = packing_process_types[rule_info.process_type]
            node[key].append(rule_info)
            node[key] = sorted(node[key], key=lambda r: r.priority)
