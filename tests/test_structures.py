import pytest

from src.structures.queue_on_stacks import QueueOnStacks


def test_queue_on_stacks_basic():
    q = QueueOnStacks()
    assert q.is_empty() and len(q) == 0

    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1
    assert len(q) == 2

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty()


def test_queue_on_stacks_empty_errors():
    q = QueueOnStacks()
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.front()


def test_queue_on_stacks_operations():
    q = QueueOnStacks()
    for i in range(5):
        q.enqueue(i)
    # Добавили 0,1,2,3,4 -> должны выйти в том же порядке
    for i in range(5):
        assert q.dequeue() == i
    assert q.is_empty()
