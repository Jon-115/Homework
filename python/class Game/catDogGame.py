
# Create a Cat/Dog game, create a class for both the cat and dog. Both animals should have the following properties:
#breed, weight, fur color, name
# Each animal will make their own unique sound
# Cat/Dog class which can do everything that both animals can do, but in its unique twist

class Cat:
    def __init__(self, breed: str, weight: int, furColor:str, name:str):
        self.breed = breed
        self.weight = weight
        self.furColor = furColor
        self.name = name

    def meow(self):
        print('Meow')    

    def scratch(self):
        print('scratch')


class Dog: 
    def __init__(self, breed: str, weight: int, furColor:str, name:str):
        self.breed = breed
        self.weight = weight
        self.furColor = furColor
        self.name = name
        

    def bark(self):
        print("bark")

    def dig(self):
        print("dig")


class CatDog(Cat,Dog):
    def meoark(self):
        print("meoark")



catDog = CatDog("siamese sheparp",90,"brendall","Steven")
catDog.bark()
catDog.meow()
catDog.meoark()

cat = Cat("black",15,"black","white")
cat.meow()

dog = Dog("Husky",50,("white","black"),"Charles")
dog.bark()

print(catDog.name)
print(dog.name)
print(cat.name)



































