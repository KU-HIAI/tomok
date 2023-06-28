import tomok

class SampleRule(tomok.RuleUnit):
    # [TODO] meta 정보

    @tomok.rule_method
    def example_method(self: tomok.RuleUnit, var1: int, var2: int):
        return var1 * var2


SampleRule().example_method(3,4)