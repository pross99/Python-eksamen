class NameGenerator:
    
    
    def __init__(self,color,animal):
        self.color = color
        self.animal = animal

  


    @property
    def gamerName(self):
        return '{}.{}xx'.format(self.color, self.animal)


    @gamerName.setter
    def gamerName(self,name):
        color, animal = name.split(" ")
        self.color = color
        self.animal = animal

    @gamerName.deleter
    def gamerName(self):
        print("Delete GamerTag!")
        self.color= None
        self.last = None
     



tag_1 = NameGenerator("Grey", "Panda")


#tag_1.color = "blue"

#tag_1.gamerName = "Blue Hippo"

print(tag_1.color)
print(tag_1.animal)
print(tag_1.gamerName)



## OOP i Python vs Java 