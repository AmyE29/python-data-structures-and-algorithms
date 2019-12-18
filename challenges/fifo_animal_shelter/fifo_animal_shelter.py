from queue import Node, Queue
""""Creates instances for dogs and cats"""
class Dog:
    def __init__(self, name):
        self.name = name
        self.next = None
class Cat:
    def __init__(self, name):
        self.name = name
        self.next =  None

class Animal_Shelter:
  def __init__(self):
    """"Creates one queue for cats and one queue for dogs"""
    self.dog_queue = Queue()
    self.cat_queue = Queue()

  def enqueue(self, pet):
    """Takes in a cat or a dog and adds it to their queue"""
    if isinstance(pet, Dog):
      self.dog_queue.enqueue(pet)
    elif  isinstance(pet, Cat):
      self.cat_queue.enqueue(pet)
    else:
      raise WrongKindofPetError('We dont shelter those animals here')

  def dequeue(self, pet = None):
    """returns either a dog or a cat. If pref is not "dog" or "cat" then return null. """
    if pet.lower() == 'dog':
      return self.dog_queue.dequeue()
    elif pet.lower() == 'cat':
      return self.cat_queue.dequeue()
    return None

class WrongKindofPetError(ValueError):
  """We don't shelter those animals here"""
  pass
