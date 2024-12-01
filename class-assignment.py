class Animal :

  def eat(self):
    print('Animal is eating')
  
  def sleep(self):
    print('Animal is eating')

class dog(Animal) :

  def bark(self):
    print('dog is barking')

  def eat (self):
    print('dog is eating')

class cat(Animal) :

  def meow(self):
    print('cat is meowing')

  def sleep (self):
    print('cat is sleeping')


tobias = dog()
tobias.eat() #polymorphism
tobias.sleep()
tobias.bark()

emily = cat()
emily.eat()
emily.sleep() #polymorphism
emily.meow()


    