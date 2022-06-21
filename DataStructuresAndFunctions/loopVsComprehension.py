#kvadrattal

lst_a = [1, 2, 3, 4, 5]
lst_b = []
for i in lst_a:
   lst_b.append(i**2)
print(lst_b)
[1, 4, 9, 16, 25]


lst_b = [i**2 for i in lst_a]
print(lst_b)
[1, 4, 9, 16, 25]

#comprehension = stærk "one-liner"