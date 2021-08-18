""" tutorial """
# import ipdb


def nombre(param: str) -> str:
    """ okay types??? """
    # ipdb.set_trace()
    print(param)


def argsmethod(*args):
    print(args)


def kargumentos(**kwargs):
    """ karguments """
    print(kwargs)


def test_nombre():
    nombre("test")
    nombre(1)


def test_karg():
    kargumentos(a='foo', b='bar', c=312)


def test_args():
    argsmethod(1, 2, 3, 4, 5)
