temprature=int(input('what is the todays temprature: '))
if(temprature >= 30):
    print('it is a hot day!!')
elif(temprature <=10):
    print('it is a cold day!!!')
else:
    print('it is normal day!!!')
print('\n')
name=input('please type your name : ')
size=len(name)
if size<3:
    print('name must be atleast 3 characters!!')
elif size>50:
    print('name can be maximum of 50 charater')
else:
    print('you enter correct name!!')
print('\n')

weight=float(input('enter the weight?'))
unit=input('(L)bs or (K)g:')
if unit.upper()=='L':
    lbs=weight*0.45
    print(f"thr converted weight {lbs} in kg")
elif unit.upper()=='K':
    kg=weight/0.45
    print(f"thr converted weight {kg} in lbs")
else:
    print('you entered wrong unit!!')