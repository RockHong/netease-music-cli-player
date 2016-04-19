#coding=utf-8

class Singleton(object):
    """Singleton Class
    This is a class to make some class being a Singleton class.
    Such as database class or config class.

    usage:
        class xxx(Singleton):
            def __init__(self):
                if hasattr(self, '_init'):
                    return
                self._init = True
                other init method
    """

    # Hong: __new__(), https://docs.python.org/3/reference/datamodel.html#object.__new__
    # Hong: 关于*args, **kwargs，见https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
    # **xxx，表示参数xxx是一个dictionary
    # *yyy，表示参数yyy是一个tuple
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # Hong: super(), https://docs.python.org/3/library/functions.html#super
            # Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.
            # 用super()可以调用父类的方法
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

