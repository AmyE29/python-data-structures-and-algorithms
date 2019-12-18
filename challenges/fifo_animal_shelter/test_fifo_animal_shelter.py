import pytest

from fifo_animal_shelter import Dog, Cat, Animal_Shelter,WrongKindofPetError

def test_shelter():
  assert Animal_Shelter()

def test_cat():
  assert Dog('Dog')

def test_dog():
  assert Cat('Cat')

@pytest.fixture()
def shelter():
  return Animal_Shelter()

def test_add_remove_one_dog(shelter):
  shelter.enqueue(Dog('Dog'))
  shelter.enqueue(Cat('Cat'))
  assert shelter.dequeue('dog').name == 'Dog'

def test_add_remove_one_cat(shelter):
  shelter.enqueue(Dog('Dog'))
  shelter.enqueue(Cat('Cat'))
  assert shelter.dequeue('cat').name == 'Cat'

def test_add_remove_multi_cat(shelter):
  shelter.enqueue(Cat('Cat'))
  shelter.enqueue(Cat('Cat2'))
  assert shelter.dequeue('cat').name == 'Cat'
  assert shelter.dequeue('cat').name == 'Cat2'



