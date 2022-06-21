




#List 
# Hvorfor List? ordered, changeable
#Meget funktionalitet 
studentNames = ["Peter", "Bob", "Hans", "Lauge", "Freja", "Sigurd"]
studentNames2 = ["Signe", "Mathilde"]
differntDataTypes = ["letters", 50, True, 12, "male"]


print(len(studentNames))
#print(studentNames[0])
#print(studentNames[-1])
#print(studentNames[0:2])
studentNames.append("Poul")
studentNames.insert(0,"Anders")
#studentNames.insert(0,studentNames2) - no go
studentNames.extend(studentNames2) 
studentNames.remove("Poul")
studentNames.pop()
popped = studentNames.pop()
print(popped) 
print(studentNames)
studentNames.reverse()
#studentNames.sort() #- hvad hvis det var en collection af ints?
print(studentNames)
#print(studentNames.index("Lauge"))

#for name in studentNames:
    #print(name)



#Tuple
#Hvorfor tuple? ordered and unchangeable 

numbers1= (1, 2, 55, 20, 78, 99, 3, 88 )
sortedT = sorted(numbers1)
result = tuple(sortedT)

print(numbers1)
print(result)


#Set 
#Hvorfor Set? unordered! man kan tilføje og adde nye "items " til et set. duplicates?

fruits= {"Apple", " Mango", "Peach"}
fruits.add("Kiwi")
print(fruits)
fruits.remove("Apple")
print(fruits)


# Dict comprehension 
#Pris i $
itemPriceInDollars = {"milk": 1.9,"coffee": 3.1,"bread": 2.9}

dollarToDkk = 7.07

newPrice = {item: value*dollarToDkk for (item, value) in itemPriceInDollars.items()}
print(newPrice)


# Tuple comprehension - hvorfor er det ikke en ting? 
# (i for i in (1, 2, 3)) virker ikke
numbers2 = tuple((i for i in numbers1 if i < 20))
print(numbers2)


