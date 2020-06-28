Number=9
chance=1
while chance<=3:
    x=int(input('guess the number :'))
    if  x == Number:
        print('you win!!')
        break
    else:
        print('try gain!!!')
        print(f"your {3-chance} only left")
    chance+=1

