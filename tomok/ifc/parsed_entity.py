# 3rd-party
from ifcopenshell.entity_instance import entity_instance
from ifcopenshell.file import file
# framework
from .util import _entity_to_list
from .property_set import PropertySet
from .rule_info import RuleProcessType, RuleInfo


class ParsedEntity():
    def __init__(self, ifc: file, entity: entity_instance):
        self.ifc = ifc
        self.entity = entity
        self.pset = self._gather_psets()
        self.material = self._gather_materials()
        self.profile = self._gather_profiles()
        self.id2rel_class, self.identifications = self._gather_identifications()
        self.rule_info = self._gather_rule_info()

    @property
    def Name(self):
        return self.get_name()

    def get_name(self, sub_entity=None):
        if sub_entity is None:
            return self.entity.Name
        if type(sub_entity) is PropertySet:
            return sub_entity.Name
        if type(sub_entity) is list:
            return ", ".join([e.Name for e in sub_entity])
        if type(sub_entity) is entity_instance:
            return sub_entity.Name
        return None

    def __repr__(self) -> str:
        return "\033[95m[{0}/{1}/{2}] \033[94m[pset: {3}] \033[96m[mat: {4}] \033[92m[prof: {5}] \033[93m[rule:{6}]\033[0m".format(
            self.entity.id(),
            self.entity.is_a(),
            ", ".join(
                [id_str for id_str in self.identifications if id_str is not None]),
            self.get_name(self.pset),
            self.get_name(self.material),
            self.get_name(self.profile),
            self.rule_info
        )

    def _get_attr(self, entity: entity_instance, attr_str: str, default_value=None):
        attrs = attr_str.split('.')
        cur_entity = entity
        for attr in attrs:
            if not hasattr(cur_entity, attr):
                return default_value
            cur_entity = cur_entity.__getattr__(attr)
        if type(default_value) is list:
            return _entity_to_list(cur_entity)
        return cur_entity

    def _gather_psets(self):
        pset = self._get_attr(
            self.entity, 'RelatingPropertyDefinition', default_value=None)
        if pset is None or not pset.is_a('IfcPropertySet'):
            return None
        return PropertySet(self.ifc, pset)

    def _gather_materials(self):
        mat_profiles = self._get_attr(
            self.entity, 'RelatingMaterial.MaterialProfiles', default_value=None)
        if mat_profiles is None or len(mat_profiles) == 0:
            return None
        mats = sum([list(self._get_attr(mat_profile, 'Material.HasProperties',
                   default_value=[])) for mat_profile in mat_profiles], [])
        if(len(mats) == 0):
            return None
        mats = [PropertySet(self.ifc, mat, access='Properties')
                for mat in mats]
        return mats

    def _gather_profiles(self):
        mat_profiles = self._get_attr(
            self.entity, 'RelatingMaterial.MaterialProfiles', default_value=None)
        if mat_profiles is None or len(mat_profiles) == 0:
            return None
        profs = sum([list(self._get_attr(mat_profile, 'Profile.HasProperties',
                    default_value=[])) for mat_profile in mat_profiles], [])
        if(len(profs) == 0):
            return None
        profs = [PropertySet(self.ifc, prof, access='Properties')
                 for prof in profs]
        return profs

    def _gather_identifications(self):
        rel_classes = self._get_attr(
            self.entity, 'RelatingClassification', default_value=[])
        id2rel_class = {self._get_attr(
            rel_class, 'Identification', default_value=None): rel_class for rel_class in rel_classes}
        identifications = list(id2rel_class.keys())
        return id2rel_class, identifications

    def _gather_rule_info(self):
        process_type_dict = {
            # key는 소문자로 적을 것
            'decision': RuleProcessType.Decision,
            'indirect': RuleProcessType.Indirect
        }
        rel_classes = self._get_attr(
            self.entity, 'RelatingClassification', default_value=[])
        for rel_class in rel_classes:
            id_str = self._get_attr(
                rel_class, 'Identification', default_value='').strip().lower()
            if id_str in process_type_dict.keys():
                process_type = process_type_dict[id_str]
                priority = self._get_attr(
                    rel_class, 'Description', default_value=9999)
                if type(priority) is str:
                    priority = int(priority) if priority.isdigit() else 9999
                execute_rule_name = self._get_attr(
                    rel_class, 'ReferencedSource.Identification', default_value=None)
                affect_property_name = self._get_attr(
                    rel_class, 'ReferencedSource.Identification.ReferencedSource.Identification', default_value=None)
                return RuleInfo(process_type=process_type, affect_property_name=affect_property_name, execute_rule_name=execute_rule_name, priority=priority)
        return None
