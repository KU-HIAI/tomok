from functools import wraps
import traceback

# python


def rule_method(fn):
    """
    주어진 룰 함수를 외부에서 호출 가능하도록하는 데코레이터입니다.

    Parameters:
    fn (function): 룰 함수
    """

    class RuleMethod:
        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args, **kwargs):
            if "body" in kwargs:
                try:
                    result = self.fn(**kwargs["body"])
                except Exception as ex:
                    response = {
                        "success": False,
                        "error": {
                            "type": type(ex).__name__,  # exception class name
                            "message": str(ex),  # exception message
                        },
                    }

                    return response, 500
                return result.result_variables
            return self.fn(*args, **kwargs)

    return RuleMethod(fn)


def table_function(fn):
    """
    주어진 테이블 함수를 외부에서 호출 가능하도록하는 데코레이터입니다.

    Parameters:
    fn (function): 테이블 함수
    """
    class TableFunction:
        def __init__(self, fn):
            self.fn = fn
            wraps(fn)(self)

        def __get__(self, instance, owner):
            # 바운드(bound) 메서드를 반환합니다.
            if instance is None:
                return self
            # 원본 함수를 인스턴스에 바인딩합니다.
            bound_fn = self.fn.__get__(instance, owner)
            return self.__class__(bound_fn)

        def __call__(self, *args, **kwargs):
            if "body" in kwargs:
                try:
                    result = self.fn(*args, **kwargs["body"])
                except Exception as ex:
                    response = {
                        "success": False,
                        "error": {
                            "type": type(ex).__name__,  # exception class name
                            "message": str(ex),  # exception message
                        },
                    }
                    return response, 500
                return result.result_variables
            else:
                return self.fn(*args, **kwargs)

        # 추가로 타입 식별을 위해 클래스 이름을 지정합니다.
        def __repr__(self):
            return f"<TableFunction {self.fn.__name__}>"

    return TableFunction(fn)
