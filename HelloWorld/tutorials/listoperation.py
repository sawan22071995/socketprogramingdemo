number=[1,8,6,7,9,3,5]
number.append(0)
print(number)
number.clear()
print(number)
for i in range(10):
    number.append(i)
print(number)
x=number.copy()
print(x)
print(number.count(1))
number.remove(8)
print(number)
number.extend('6')
print(number)
number.insert(3,55)
print(number)
number.pop(10)
print(number)
print(number.__sizeof__())
number.append(6)
number.append(6)
print(number.count(6))
number.sort()
print(number)
number.reverse()
print(number)
#list are mutable...
number[2]=99
print(number)





