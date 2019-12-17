from queue_with_stacks import Node, Stack, PseudoQueue
import pytest

@pytest.fixture
def my_stack():
    new_stack = Stack()
    values = ['a', 'b','c', 10]
    for el in values:
       new_stack.push(el)

    return new_stack


def test_stack1_stack2_exists(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    assert pseudo_q.stack1.peek() == 10
    assert pseudo_q.stack2.peek() == None

def test_enqueue(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    pseudo_q.enqueue('cat')
    assert pseudo_q.stack1.peek() == 'cat'

def test_enqueue_empty_stack():
    pseudo_q = PseudoQueue(Stack())
    pseudo_q.enqueue('cat')
    assert pseudo_q.stack1.peek() == 'cat'

def test_dequeue(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    assert pseudo_q.dequeue() == 'a'


def test_enqueue_dequeue(my_stack):
    pseudo_q = PseudoQueue(my_stack)
    assert pseudo_q.stack1.peek() == 10
    pseudo_q.enqueue('cat')
    assert pseudo_q.stack1.peek() == 'cat'
    pseudo_q.enqueue('dog')
    assert pseudo_q.stack1.peek() == 'dog'
    assert pseudo_q.dequeue() == 'a'
    assert pseudo_q.stack1.peek() == 'dog'
    assert pseudo_q.dequeue() == 'b'
    assert pseudo_q.stack1.peek() == 'dog'
    assert pseudo_q.dequeue() == 'c'
    assert pseudo_q.dequeue() == 10
    assert pseudo_q.dequeue() == 'cat'
    assert pseudo_q.dequeue() == 'dog'

def test_dequeue_empty():
    pseudo_q = PseudoQueue(Stack())
    with pytest.raises(Exception):  
        result = pseudo_q.dequeue()