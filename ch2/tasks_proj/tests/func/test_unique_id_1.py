import pytest
import tasks
from tasks import Task


@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))

    # grab a unique id
    uid = tasks.unique_id()
    # make sure it isnt in the list of existing ids
    assert uid not in ids


@pytest.mark.xfail(tasks.__version__ < '0.2.0', reason ='not supported until version 0.2.')
def test_unique_id_1():
    """Calling unique_id() twice should return different numbers"""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Demonstrate xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_is_not_a_duck():
    """Demonstrate xpass"""
    uid = tasks.unique_id()
    assert uid != 'a duck'



