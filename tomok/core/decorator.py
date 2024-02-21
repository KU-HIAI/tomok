# python

def rule_method(fn):
    """
    주어진 룰 함수를 외부에서 호출 가능하도록하는 데코레이터입니다.

    Parameters:
    fn (function): 룰 함수
    """
    class RuleMethod():
        def __init__(self, fn):
            self.fn = fn
        
        def __call__(self, *args, **kwargs):
            if 'body' in kwargs:
                result = self.fn(**kwargs['body'])
                return result.result_variables
            return self.fn(*args, **kwargs)
    
    return RuleMethod(fn)
