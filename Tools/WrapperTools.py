# 单例函数装饰器
def singleton_func(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


# 单例类装饰器
class Singleton_class(object):
    def __init__(self,cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls]
        return self._instance[self._cls]
