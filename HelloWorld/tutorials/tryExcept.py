try:
    age=int(input("age :"))
    print(age)
    x=1000
    y=x/age
    print(y)
except ValueError:
    print('Invalid Value!!')
except ZeroDivisionError:
    print('Dont enter the age as 0')
