from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():

    print("hello world")
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()

    assert t_dict == {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }


def test_replace():
    t_before = Task('finish book', 'brain', False)
    t_after = t_before._replace(id=10, done=True)
    assert t_after == Task('finish book', 'brain', True, 10)
