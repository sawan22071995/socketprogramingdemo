def fib(n):
        a = 0
        b = 1
        if n<0:
            print("you entered the wrong or invalid value!!")
        elif n==1:
            print(a)
        else:
            print(a, end=" ")
            print(b, end=" ")
            for i in range(2, n):

                c = a + b
                a = b
                b = c
                print(c ,end=" ")

n = int(input("how many terms do you want:"))
fib(n)
print()


class Comp:
    def config(self):
        print("hello world")


com1 = Comp()
com2 = Comp()
com1.config()
Comp.config(com2)