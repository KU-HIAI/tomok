import traceback
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
                try:
                    result = self.fn(**kwargs['body'])
                except Exception as ex:
                    response = {
                        'success': False,
                        'error': {
                            'type': type(ex).__name__,  # exception class name
                            'message': str(ex),  # exception message
                        }
                    }

                    return response, 500
                return result.result_variables
            return self.fn(*args, **kwargs)
    
    return RuleMethod(fn)
