import pytest

from stacks_and_queues import Node, Stack, Queue


#########################################################
# Can successfully push onto a stack
# Can successfully push multiple values onto a stack
#########################################################
def test_one_push():
    new_stack = Stack()
    new_stack.push('Penny')
    assert new_stack.top.value == 'Penny'

def test_many_push():
    new_stack = Stack()
    new_stack.push('Penny')
    new_stack.push('Honey')
    new_stack.push('Lacey')
    new_stack.push('Pickles')
    assert new_stack.top.value == 'Pickles'


#########################################################
# Can successfully pop off the stack
#########################################################
def test_none_pop():
    new_stack = Stack()
    assert new_stack.pop() == None

def test_one_pop(stack_of_one):
    assert stack_of_one.pop() == 'Penny'

def test_many_pop(stack_of_four):
    assert stack_of_four.pop() == 'Pickles'

#########################################################
# Can successfully empty a stack after multiple pops
#########################################################
def test_empty_the_stack(stack_of_four):
    stack_of_four.pop() # 4 pop
    stack_of_four.pop() # 3 pop
    stack_of_four.pop() # 2 pop
    stack_of_four.pop() # 1 pop
    assert stack_of_four.is_empty() == True

#########################################################
# Can successfully peek the next item on the stack
#########################################################
def test_none_peek():
    new_stack = Stack()
    assert new_stack.peek() == None

def test_one_peek(stack_of_one):
    assert stack_of_one.peek() == 'Penny'

def test_many_peek(stack_of_four):
    assert stack_of_four.peek() == 'Pickles'

#########################################################
# Can successfully instantiate an empty stack
#########################################################
def test_empty_stack():
    new_stack = Stack()
    assert new_stack.top == None

#########################################################
# Can successfully enqueue into a queue
#########################################################
def test_enqueue_one():
    new_queue = Queue()
    new_queue.enqueue('Penny')
    assert new_queue.front.value == 'Penny'
#########################################################
# Can successfully enqueue multiple values into a queue
#########################################################
def test_add_four():
    new_queue = Queue()
    new_queue.enqueue('Penny')
    new_queue.enqueue('Honey')
    new_queue.enqueue('Lacey')
    new_queue.enqueue('Pickles')
    assert new_queue.front.value == 'Penny'
    assert new_queue.end.value == 'Pickles'


#########################################################
# Can successfully dequeue out of a queue the expected value
#########################################################
def test_dequeue_one(queue_of_one):
    assert queue_of_one.dequeue() == 'Penny'

def test_dequeue_four(queue_of_four):
    queue_of_four.dequeue()
    queue_of_four.dequeue()
    queue_of_four.dequeue()
    assert queue_of_four.dequeue() == 'Pickles'


#########################################################
# Can successfully peek into a queue, seeing the expected value
#########################################################
def test_peek_none():
    new_queue = Queue()
    assert new_queue.peek() == None

def test_peek_first(queue_of_four):
    assert queue_of_four.peek() == 'Penny'

def test_peek_second(queue_of_four):
    queue_of_four.dequeue()
    assert queue_of_four.peek() == 'Honey'


#########################################################
# Can successfully empty a queue after multiple dequeues
#########################################################
def test_is_empty_dequeue_none():
    new_queue = Queue()
    new_queue.dequeue()
    assert new_queue.is_empty() == True

def test_is_empty_dequeue_one(queue_of_one):
    assert queue_of_one.is_empty() == False
    queue_of_one.dequeue() # One
    assert queue_of_one.is_empty() == True

def test_is_empty_dequeue_four(queue_of_four):
    assert queue_of_four.is_empty() == False
    queue_of_four.dequeue()
    queue_of_four.dequeue()
    queue_of_four.dequeue()
    queue_of_four.dequeue()
    assert queue_of_four.is_empty() == True

#########################################################
# Can successfully instantiate an empty queue
#########################################################
def test_none():
    new_queue = Queue()
    assert isinstance(new_queue, Queue)


@pytest.fixture()
def stack_of_one():
    new_stack = Stack()
    new_stack.push('Penny')
    return new_stack

@pytest.fixture()
def stack_of_four():
    new_stack = Stack()
    new_stack.push('Penny')
    new_stack.push('Honey')
    new_stack.push('Lacey')
    new_stack.push('Pickles')
    return new_stack

@pytest.fixture()
def queue_of_one():
    new_queue = Queue()
    new_queue.enqueue('Penny')
    return new_queue

@pytest.fixture()
def queue_of_four():
    new_queue = Queue()
    new_queue.enqueue('Penny')
    new_queue.enqueue('Honey')
    new_queue.enqueue('Lacey')
    new_queue.enqueue('Pickles')
    return new_queue
