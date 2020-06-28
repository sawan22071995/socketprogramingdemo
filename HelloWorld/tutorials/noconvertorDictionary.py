number=input("please enter any number: ")
num={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
    
}
x=""
for i in number:
    x+=num.get(i,'@')+" "
print(x)