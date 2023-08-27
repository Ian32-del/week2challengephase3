class Restuarant :
    def __init__(self , name):
        self._name = name

    def name (self):
        return self._name
    
recipe = Restuarant("Eat Here")
print(recipe.name())

cook = Restuarant("Best Food Here")
print(cook.name())