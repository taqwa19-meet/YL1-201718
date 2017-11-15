#class Animal(object):
    #def __init__(self,sound,name,age,favorite_color):
        #self.sound= sound
        #self.name= name
        #self.age= age
        #self.favorite_color=favorite_color
    #def eat(self,food):
        #print("yummy!!"+self.name+"is eating"+food)
    #def description(self):
       # print(self.name+"is"+str(self.age)+"years old and loves the color"+self.favorite_color)
    #def make_sound(self):
        #print(self.sound *3)
              
#jeffchimp = Animal("meow","jeffchimp",13,"rainbow")
#jeffchimp.description()

#jeffchimp.make_sound()

class Person(object):
    def __init__(self,name,age,city,gender):
        self.name= name
        self.age= age
        self.city= city
        self.gender= gender
    def eat (self,food):
        print(self.name , "is eating",food)
        
taqwa=Person("taqwa",15,"nazareth","female")
taqwa.eat("sushi")
        
