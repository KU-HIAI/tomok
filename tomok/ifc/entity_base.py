# framework
from .util import *
from .property_set import PropertySet


class SupertypeIfcEntityOfPsetAndProp:
    """
    Variables:
        property_set_names: PropertySet 또는 Properties의 이름을 모은 집합
    """
    property_set_names = []

    def __getattr__(self, key):
        raise AttributeError("{0} property_set is not in {1}. {2}".format(
            key, self, self.property_set_names))

    def __repr__(self):
        return repr(self.entity.wrapped_data)

    def get_psets(self):
        return [
            self.__getattribute__(name) for name in self.property_set_names
        ]

    def get_props(
        self,
        names_only: bool = True
    ):
        def get_key(pset: PropertySet):
            if(names_only):
                return pset.entity.Name
            else:
                return pset
        return {get_key(pset): pset.get_properties() for pset in self.get_psets()}

    def get_descriptions(
        self
    ):
        return sum([list(pset.descriptions.values()) for pset in self.get_psets() if len(pset.descriptions.values()) > 0], [])

    def set_psets(self, psets: dict):
        self.property_set_names = list(psets.keys())
        for key, value in psets.items():
            self.__setattr__(key, value)
