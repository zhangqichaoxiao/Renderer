# -*- coding:utf-8 -*-


class Singleton(object):
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            # print('Creating the object')
            cls._instance = super(Singleton, cls).__new__(cls)
            # Put any initialization here.
            if getattr(cls._instance, "_initialize"):
                cls._instance._initialize(*args)
        return cls._instance

